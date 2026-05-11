use std::io::{BufReader, ErrorKind};
use std::path::{Path, PathBuf};
use std::time::{Duration, SystemTime, UNIX_EPOCH};

use serde::de::DeserializeOwned;
use serde::{Deserialize, Serialize};
use serde_json::Value;

use crate::call_context::{YaiCallContext, YaiCallContextConfig, DEFAULT_RUST_CLIENT_SUBJECT_REF};
use crate::envelope::YaiEnvelope;
use crate::status::{YaiError, YaiResult};
use crate::transport::YaiTransport;

use super::local_ipc_rpc_endpoint::{resolve_endpoint, LocalIpcRpcEndpoint};
use super::local_ipc_rpc_error::{
    contract_error, discovery_failure, LocalIpcRpcClientErrorKind, LOCAL_IPC_RPC_TRANSPORT,
};
use super::local_ipc_rpc_frame::{
    read_frame_json, write_frame_json, LocalIpcRpcFrame, LocalIpcRpcFrameType,
};
use super::local_ipc_rpc_handshake::{LocalIpcRpcHandshakeRequest, LocalIpcRpcHandshakeResponse};

#[cfg(unix)]
use std::os::unix::net::UnixStream;

const DEFAULT_TIMEOUT_MS: u64 = 750;

#[derive(Debug, Clone)]
pub struct LocalIpcRpcTransportConfig {
    pub endpoint: Option<PathBuf>,
    pub client_ref: String,
    pub timeout_ms: u64,
    pub use_runtime_discovery_file: bool,
    pub use_platform_default: bool,
}

impl Default for LocalIpcRpcTransportConfig {
    fn default() -> Self {
        Self {
            endpoint: None,
            client_ref: "sdk-rust".to_string(),
            timeout_ms: DEFAULT_TIMEOUT_MS,
            use_runtime_discovery_file: false,
            use_platform_default: false,
        }
    }
}

impl LocalIpcRpcTransportConfig {
    pub fn from_env() -> Self {
        let endpoint = std::env::var("YAI_LOCAL_IPC_ENDPOINT")
            .ok()
            .map(|value| value.trim().to_string())
            .filter(|value| !value.is_empty())
            .map(PathBuf::from);

        Self {
            endpoint,
            ..Self::default()
        }
    }

    pub fn with_platform_default(mut self) -> Self {
        self.use_platform_default = true;
        self
    }

    pub fn with_runtime_discovery_file(mut self) -> Self {
        self.use_runtime_discovery_file = true;
        self
    }
}

#[derive(Debug, Clone)]
pub struct LocalIpcRpcTransport {
    config: LocalIpcRpcTransportConfig,
}

#[derive(Debug, Clone, Serialize)]
pub struct LocalIpcRpcClientRef {
    pub client_ref: String,
    pub surface_ref: String,
}

#[derive(Debug, Clone, Serialize)]
pub struct LocalIpcRpcRequestEnvelope {
    pub schema: String,
    pub envelope_id: String,
    pub operation_id: String,
    pub request_id: String,
    pub correlation_id: String,
    pub client_ref: String,
    pub client_subject_ref: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub client_connection_ref: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub client_attachment_ref: Option<String>,
    pub system_root_context_ref: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub work_case_ref: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub system_call_ref: Option<String>,
    pub client: LocalIpcRpcClientRef,
    pub transport: String,
    pub created_at: String,
    pub input: Value,
}

#[derive(Debug, Clone, Deserialize)]
#[serde(bound(deserialize = "TData: DeserializeOwned"))]
struct LocalIpcRpcResponseEnvelope<TData> {
    operation_id: String,
    status: String,
    #[serde(default)]
    message: Option<String>,
    #[serde(default)]
    system_call_ref: Option<String>,
    #[serde(default)]
    client_subject_ref: Option<String>,
    #[serde(default)]
    client_connection_ref: Option<String>,
    #[serde(default)]
    client_attachment_ref: Option<String>,
    #[serde(default)]
    system_root_context_ref: Option<String>,
    #[serde(default)]
    work_case_ref: Option<String>,
    #[serde(default)]
    control_admission_ref: Option<String>,
    #[serde(default)]
    result: Option<TData>,
    #[serde(default)]
    error: Option<Value>,
}

impl LocalIpcRpcTransport {
    pub fn new(config: LocalIpcRpcTransportConfig) -> Self {
        Self { config }
    }

    pub fn config(&self) -> &LocalIpcRpcTransportConfig {
        &self.config
    }

    pub fn is_default_transport() -> bool {
        false
    }

    pub fn supports_provider_transport_boundary() -> bool {
        false
    }

    pub fn transport_name() -> &'static str {
        LOCAL_IPC_RPC_TRANSPORT
    }

    pub fn discover_endpoint(
        &self,
        operation_id: &'static str,
    ) -> Result<LocalIpcRpcEndpoint, YaiError> {
        resolve_endpoint(
            self.config.endpoint.as_deref(),
            self.config.use_runtime_discovery_file,
            self.config.use_platform_default,
        )
        .map_err(|failure| discovery_failure(operation_id, failure))
    }

    pub fn prepare_handshake_request(&self) -> LocalIpcRpcHandshakeRequest {
        LocalIpcRpcHandshakeRequest::new(self.config.client_ref.clone())
    }

    pub fn call_context_config(&self) -> YaiCallContextConfig {
        YaiCallContextConfig {
            client_ref: self.config.client_ref.clone(),
            client_subject_ref: DEFAULT_RUST_CLIENT_SUBJECT_REF.to_string(),
            ..YaiCallContextConfig::default()
        }
    }

    pub fn prepare_handshake_frame(
        &self,
        request_id: &str,
    ) -> YaiResult<LocalIpcRpcFrame<LocalIpcRpcHandshakeRequest>> {
        let handshake = self.prepare_handshake_request();
        handshake.validate().map_err(|message| {
            contract_error(
                "transport.handshake",
                LocalIpcRpcClientErrorKind::VersionMismatch,
                message,
            )
        })?;
        LocalIpcRpcFrame::new(
            self.frame_id("handshake"),
            LocalIpcRpcFrameType::HandshakeRequest,
            "v1",
            Some(request_id.to_string()),
            Some(request_id.to_string()),
            None,
            handshake,
        )
        .map_err(|err| {
            contract_error(
                "transport.handshake",
                LocalIpcRpcClientErrorKind::UnsupportedFrame,
                format!("failed to encode handshake frame: {err}"),
            )
        })
    }

    fn prepare_operation_request_frame(
        &self,
        operation_id: &'static str,
        request: Option<Value>,
        context: YaiCallContext,
    ) -> YaiResult<LocalIpcRpcFrame<LocalIpcRpcRequestEnvelope>> {
        let request_id = context.request_id.clone();
        let correlation_id = context.correlation_id.clone();
        let payload = self.prepare_request_envelope(operation_id, request, context);
        LocalIpcRpcFrame::new(
            self.frame_id(operation_id),
            LocalIpcRpcFrameType::OperationRequest,
            "v1",
            Some(request_id),
            Some(correlation_id),
            None,
            payload,
        )
        .map_err(|err| {
            contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::UnsupportedFrame,
                format!("failed to encode operation.request frame: {err}"),
            )
        })
    }

    pub fn prepare_request_envelope(
        &self,
        operation_id: &'static str,
        request: Option<Value>,
        context: YaiCallContext,
    ) -> LocalIpcRpcRequestEnvelope {
        LocalIpcRpcRequestEnvelope {
            schema: "api.request-envelope.v1".to_string(),
            envelope_id: self.frame_id("envelope"),
            operation_id: operation_id.to_string(),
            request_id: context.request_id,
            correlation_id: context.correlation_id,
            client_ref: context.client_ref.clone(),
            client_subject_ref: context.client_subject_ref,
            client_connection_ref: context.client_connection_ref,
            client_attachment_ref: context.client_attachment_ref,
            system_root_context_ref: context.system_root_context_ref,
            work_case_ref: context.work_case_ref,
            system_call_ref: context.system_call_ref,
            client: LocalIpcRpcClientRef {
                client_ref: self.config.client_ref.clone(),
                surface_ref: "sdk-rust".to_string(),
            },
            transport: context.transport,
            created_at: timestamp_string(),
            input: request.unwrap_or(Value::Null),
        }
    }

    fn frame_id(&self, label: &str) -> String {
        let stamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap_or_default()
            .as_nanos();
        let sanitized = label.replace(['.', '/', ' '], "-");
        format!("sdk01-{sanitized}-{stamp}")
    }

    #[cfg(unix)]
    fn connect_unix(
        &self,
        operation_id: &'static str,
        endpoint: &Path,
    ) -> Result<UnixStream, YaiError> {
        let stream = UnixStream::connect(endpoint).map_err(|err| {
            let kind = match err.kind() {
                ErrorKind::NotFound => LocalIpcRpcClientErrorKind::EndpointMissing,
                ErrorKind::PermissionDenied => LocalIpcRpcClientErrorKind::PermissionDenied,
                _ => LocalIpcRpcClientErrorKind::RuntimeUnavailable,
            };
            contract_error(
                operation_id,
                kind,
                format!(
                    "local_ipc_rpc connection failed for {}: {err}",
                    endpoint.display()
                ),
            )
        })?;

        let timeout = Duration::from_millis(self.config.timeout_ms.max(1));
        stream.set_read_timeout(Some(timeout)).map_err(|err| {
            contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::RuntimeUnavailable,
                format!("failed to set local_ipc_rpc read timeout: {err}"),
            )
        })?;
        stream.set_write_timeout(Some(timeout)).map_err(|err| {
            contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::RuntimeUnavailable,
                format!("failed to set local_ipc_rpc write timeout: {err}"),
            )
        })?;

        Ok(stream)
    }

    #[cfg(not(unix))]
    fn connect_unix(&self, operation_id: &'static str, endpoint: &Path) -> Result<(), YaiError> {
        Err(contract_error(
            operation_id,
            LocalIpcRpcClientErrorKind::PlatformDeferred,
            format!(
                "Windows named pipe support is deferred; endpoint candidate was {}",
                endpoint.display()
            ),
        ))
    }

    #[cfg(unix)]
    fn invoke_over_unix<TData>(
        &self,
        operation_id: &'static str,
        endpoint: &LocalIpcRpcEndpoint,
        request: Option<Value>,
        context: YaiCallContext,
    ) -> YaiResult<YaiEnvelope<TData>>
    where
        TData: DeserializeOwned,
    {
        let request_id = context.request_id.clone();
        let handshake_frame = self.prepare_handshake_frame(&request_id)?;
        let operation_frame =
            self.prepare_operation_request_frame(operation_id, request, context)?;

        let mut stream = self.connect_unix(operation_id, &endpoint.path)?;
        let reader_stream = stream.try_clone().map_err(|err| {
            contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::RuntimeUnavailable,
                format!("failed to clone local_ipc_rpc stream: {err}"),
            )
        })?;
        let mut reader = BufReader::new(reader_stream);

        write_frame_json(&mut stream, &handshake_frame).map_err(|err| {
            contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::RuntimeUnavailable,
                format!("failed to write handshake.request frame: {err}"),
            )
        })?;

        let handshake_response = read_frame_json::<LocalIpcRpcHandshakeResponse, _>(&mut reader)
            .map_err(|err| {
                let kind =
                    if err.kind() == ErrorKind::TimedOut || err.kind() == ErrorKind::WouldBlock {
                        LocalIpcRpcClientErrorKind::RuntimeUnavailable
                    } else {
                        LocalIpcRpcClientErrorKind::VersionMismatch
                    };
                contract_error(
                    operation_id,
                    kind,
                    format!("failed to read handshake.response frame: {err}"),
                )
            })?;

        let handshake_response = handshake_response.ok_or_else(|| {
            contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::RuntimeUnavailable,
                "runtime closed local_ipc_rpc stream before handshake response",
            )
        })?;

        if handshake_response.frame_type != LocalIpcRpcFrameType::HandshakeResponse {
            return Err(contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::UnsupportedFrame,
                format!(
                    "expected handshake.response but received {}",
                    handshake_response.frame_type.as_str()
                ),
            ));
        }

        handshake_response.payload.validate().map_err(|message| {
            contract_error(
                operation_id,
                if message.contains("v1") {
                    LocalIpcRpcClientErrorKind::VersionMismatch
                } else {
                    LocalIpcRpcClientErrorKind::HandshakeRejected
                },
                message,
            )
        })?;

        if !handshake_response.payload.accepted {
            return Err(contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::HandshakeRejected,
                handshake_response
                    .payload
                    .rejection_error
                    .clone()
                    .unwrap_or_else(|| "handshake rejected".to_string()),
            ));
        }

        write_frame_json(&mut stream, &operation_frame).map_err(|err| {
            contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::RuntimeUnavailable,
                format!("failed to write operation.request frame: {err}"),
            )
        })?;

        let operation_response = read_frame_json::<LocalIpcRpcResponseEnvelope<TData>, _>(
            &mut reader,
        )
        .map_err(|err| {
            let kind = if err.kind() == ErrorKind::TimedOut || err.kind() == ErrorKind::WouldBlock {
                LocalIpcRpcClientErrorKind::RuntimeUnavailable
            } else {
                LocalIpcRpcClientErrorKind::UnsupportedFrame
            };
            contract_error(
                operation_id,
                kind,
                format!("failed to read operation.response frame: {err}"),
            )
        })?;

        let operation_response = operation_response.ok_or_else(|| {
            contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::RuntimeUnavailable,
                "runtime did not return an operation.response frame; RT.02 listener dispatch is still partial",
            )
        })?;

        if operation_response.frame_type != LocalIpcRpcFrameType::OperationResponse {
            return Err(contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::UnsupportedFrame,
                format!(
                    "expected operation.response but received {}",
                    operation_response.frame_type.as_str()
                ),
            ));
        }

        if let Some(error) = operation_response.payload.error {
            return Err(YaiError::ApiError {
                operation_id,
                message: format!("local_ipc_rpc response error payload: {error}"),
            });
        }

        Ok(YaiEnvelope {
            operation_id: operation_response.payload.operation_id,
            status: operation_response.payload.status,
            execution_claim: false,
            implementation_status: LOCAL_IPC_RPC_TRANSPORT.to_string(),
            system_call_ref: operation_response.payload.system_call_ref,
            client_subject_ref: operation_response.payload.client_subject_ref,
            client_connection_ref: operation_response.payload.client_connection_ref,
            client_attachment_ref: operation_response.payload.client_attachment_ref,
            system_root_context_ref: operation_response.payload.system_root_context_ref,
            work_case_ref: operation_response.payload.work_case_ref,
            control_admission_ref: operation_response.payload.control_admission_ref,
            message: operation_response.payload.message,
            data: operation_response.payload.result,
        })
    }
}

impl YaiTransport for LocalIpcRpcTransport {
    fn invoke<TData>(
        &self,
        operation_id: &'static str,
        request: Option<Value>,
    ) -> YaiResult<YaiEnvelope<TData>>
    where
        TData: DeserializeOwned,
    {
        let context = self.call_context_config().build(LOCAL_IPC_RPC_TRANSPORT);
        self.invoke_with_context(operation_id, request, context)
    }

    fn invoke_with_context<TData>(
        &self,
        operation_id: &'static str,
        request: Option<Value>,
        context: YaiCallContext,
    ) -> YaiResult<YaiEnvelope<TData>>
    where
        TData: DeserializeOwned,
    {
        let endpoint = self.discover_endpoint(operation_id)?;

        #[cfg(unix)]
        {
            self.invoke_over_unix(operation_id, &endpoint, request, context)
        }

        #[cfg(not(unix))]
        {
            let _ = (request, context);
            Err(contract_error(
                operation_id,
                LocalIpcRpcClientErrorKind::PlatformDeferred,
                format!(
                    "Windows named pipe support is deferred for endpoint {}",
                    endpoint.path.display()
                ),
            ))
        }
    }
}

fn timestamp_string() -> String {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap_or_default()
        .as_secs()
        .to_string()
}
