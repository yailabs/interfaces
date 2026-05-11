use reqwest::blocking::Client;
use reqwest::StatusCode;
use serde::de::DeserializeOwned;
use serde::{Deserialize, Serialize};
use serde_json::Value;

use crate::call_context::{YaiCallContext, YaiCallContextConfig};
use crate::envelope::YaiEnvelope;
use crate::status::{YaiError, YaiResult};
use crate::transport::YaiTransport;

const DEFAULT_TIMEOUT_SECS: u64 = 5;

#[derive(Debug, Clone)]
pub struct HttpTransportConfig {
    pub endpoint: Option<String>,
    pub timeout_secs: u64,
}

impl Default for HttpTransportConfig {
    fn default() -> Self {
        Self {
            endpoint: None,
            timeout_secs: DEFAULT_TIMEOUT_SECS,
        }
    }
}

impl HttpTransportConfig {
    pub fn from_env() -> Self {
        let endpoint = std::env::var("YAI_API_ENDPOINT")
            .ok()
            .filter(|v| !v.trim().is_empty());
        Self {
            endpoint,
            ..Self::default()
        }
    }
}

#[derive(Debug, Serialize)]
pub struct OperationInvokeRequest {
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
    pub transport: String,
    pub request: Option<Value>,
}

#[derive(Debug, Deserialize)]
struct EnvelopeWire<TData> {
    operation_id: String,
    status: String,
    execution_claim: Option<bool>,
    implementation_status: Option<String>,
    system_call_ref: Option<String>,
    client_subject_ref: Option<String>,
    client_connection_ref: Option<String>,
    client_attachment_ref: Option<String>,
    system_root_context_ref: Option<String>,
    work_case_ref: Option<String>,
    control_admission_ref: Option<String>,
    message: Option<String>,
    data: Option<TData>,
}

#[derive(Debug, Clone)]
pub struct HttpTransport {
    config: HttpTransportConfig,
    client: Client,
}

impl HttpTransport {
    pub fn new(config: HttpTransportConfig) -> YaiResult<Self> {
        let client = Client::builder()
            .timeout(std::time::Duration::from_secs(config.timeout_secs))
            .build()
            .map_err(|err| YaiError::Unsupported {
                operation_id: "transport.init",
                message: format!("http client init failed: {err}"),
            })?;

        Ok(Self { config, client })
    }

    fn endpoint_for(&self, operation_id: &'static str) -> YaiResult<&str> {
        self.config
            .endpoint
            .as_deref()
            .ok_or(YaiError::TransportNotConfigured { operation_id })
    }

    pub fn call_context_config(&self) -> YaiCallContextConfig {
        YaiCallContextConfig::default()
    }

    pub fn prepare_invoke_request(
        &self,
        operation_id: &'static str,
        request: Option<Value>,
        context: YaiCallContext,
    ) -> OperationInvokeRequest {
        OperationInvokeRequest {
            operation_id: operation_id.to_string(),
            request_id: context.request_id,
            correlation_id: context.correlation_id,
            client_ref: context.client_ref,
            client_subject_ref: context.client_subject_ref,
            client_connection_ref: context.client_connection_ref,
            client_attachment_ref: context.client_attachment_ref,
            system_root_context_ref: context.system_root_context_ref,
            work_case_ref: context.work_case_ref,
            system_call_ref: context.system_call_ref,
            transport: context.transport,
            request,
        }
    }
}

impl YaiTransport for HttpTransport {
    fn invoke<TData>(
        &self,
        operation_id: &'static str,
        request: Option<Value>,
    ) -> YaiResult<YaiEnvelope<TData>>
    where
        TData: DeserializeOwned,
    {
        let context = self.call_context_config().build("local_http_loopback");
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
        let endpoint = self.endpoint_for(operation_id)?;
        let body = self.prepare_invoke_request(operation_id, request, context);

        let response = self
            .client
            .post(endpoint)
            .json(&body)
            .send()
            .map_err(|err| YaiError::TransportUnavailable {
                operation_id,
                message: err.to_string(),
            })?;

        let status = response.status();
        let text = response
            .text()
            .map_err(|err| YaiError::TransportUnavailable {
                operation_id,
                message: err.to_string(),
            })?;

        if status == StatusCode::NOT_IMPLEMENTED {
            return Err(YaiError::OperationUnavailable {
                operation_id,
                message: text,
            });
        }

        if !status.is_success() {
            return Err(YaiError::ApiError {
                operation_id,
                message: format!("http_status={} body={text}", status.as_u16()),
            });
        }

        let wire: EnvelopeWire<TData> =
            serde_json::from_str(&text).map_err(|err| YaiError::DecodeError {
                operation_id,
                message: format!("{err}; body={text}"),
            })?;

        Ok(YaiEnvelope {
            operation_id: wire.operation_id,
            status: wire.status,
            execution_claim: wire.execution_claim.unwrap_or(false),
            implementation_status: wire
                .implementation_status
                .unwrap_or_else(|| "transport-bound".to_string()),
            system_call_ref: wire.system_call_ref,
            client_subject_ref: wire.client_subject_ref,
            client_connection_ref: wire.client_connection_ref,
            client_attachment_ref: wire.client_attachment_ref,
            system_root_context_ref: wire.system_root_context_ref,
            work_case_ref: wire.work_case_ref,
            control_admission_ref: wire.control_admission_ref,
            message: wire.message,
            data: wire.data,
        })
    }
}
