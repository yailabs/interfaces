use serde::{Deserialize, Serialize};

use super::local_ipc_rpc_error::LOCAL_IPC_RPC_TRANSPORT;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct LocalIpcRpcHandshakeRequest {
    pub transport_name: String,
    pub transport_version: String,
    pub api_envelope_version: String,
    pub client_ref: String,
    pub supported_frame_versions: Vec<String>,
    pub supported_stream_modes: Vec<String>,
    pub requested_capabilities: Vec<String>,
}

impl LocalIpcRpcHandshakeRequest {
    pub fn new(client_ref: impl Into<String>) -> Self {
        Self {
            transport_name: LOCAL_IPC_RPC_TRANSPORT.to_string(),
            transport_version: "v1".to_string(),
            api_envelope_version: "v1".to_string(),
            client_ref: client_ref.into(),
            supported_frame_versions: vec!["v1".to_string()],
            supported_stream_modes: vec!["rpc_stream".to_string()],
            requested_capabilities: vec![
                "operation.request".to_string(),
                "operation.response".to_string(),
            ],
        }
    }

    pub fn validate(&self) -> Result<(), String> {
        if self.transport_name != LOCAL_IPC_RPC_TRANSPORT {
            return Err("transport_name must be local_ipc_rpc".to_string());
        }
        if self.transport_version != "v1" {
            return Err("transport_version must be v1".to_string());
        }
        if self.api_envelope_version != "v1" {
            return Err("api_envelope_version must be v1".to_string());
        }
        if self.client_ref.trim().is_empty() {
            return Err("client_ref is required".to_string());
        }
        if !self.supported_frame_versions.iter().any(|v| v == "v1") {
            return Err("supported_frame_versions must include v1".to_string());
        }
        if self.supported_stream_modes.is_empty() {
            return Err("supported_stream_modes must not be empty".to_string());
        }
        Ok(())
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct LocalIpcRpcHandshakeResponse {
    pub accepted: bool,
    #[serde(default)]
    pub runtime_ref: Option<String>,
    pub negotiated_frame_version: String,
    pub negotiated_api_envelope_version: String,
    #[serde(default)]
    pub supported_features: Vec<String>,
    #[serde(default)]
    pub rejection_error: Option<String>,
}

impl LocalIpcRpcHandshakeResponse {
    pub fn validate(&self) -> Result<(), String> {
        if self.accepted {
            if self.negotiated_frame_version != "v1" {
                return Err("negotiated_frame_version must be v1".to_string());
            }
            if self.negotiated_api_envelope_version != "v1" {
                return Err("negotiated_api_envelope_version must be v1".to_string());
            }
            return Ok(());
        }

        if self
            .rejection_error
            .as_deref()
            .unwrap_or("")
            .trim()
            .is_empty()
        {
            return Err("rejected handshakes must include rejection_error".to_string());
        }

        Ok(())
    }
}
