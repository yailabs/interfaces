use crate::status::YaiError;

use super::local_ipc_rpc_endpoint::{LocalIpcRpcDiscoveryFailure, LocalIpcRpcDiscoveryStatus};

pub const LOCAL_IPC_RPC_TRANSPORT: &str = "local_ipc_rpc";

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum LocalIpcRpcClientErrorKind {
    NotConfigured,
    EndpointMissing,
    PermissionDenied,
    VersionMismatch,
    RuntimeUnavailable,
    HandshakeRejected,
    UnsupportedFrame,
    PlatformDeferred,
}

impl LocalIpcRpcClientErrorKind {
    pub fn as_str(self) -> &'static str {
        match self {
            Self::NotConfigured => "not_configured",
            Self::EndpointMissing => "endpoint_missing",
            Self::PermissionDenied => "permission_denied",
            Self::VersionMismatch => "version_mismatch",
            Self::RuntimeUnavailable => "runtime_unavailable",
            Self::HandshakeRejected => "handshake_rejected",
            Self::UnsupportedFrame => "unsupported_frame",
            Self::PlatformDeferred => "platform_deferred",
        }
    }
}

pub fn discovery_failure(
    operation_id: &'static str,
    failure: LocalIpcRpcDiscoveryFailure,
) -> YaiError {
    match failure.status {
        LocalIpcRpcDiscoveryStatus::NotConfigured => {
            YaiError::TransportNotConfigured { operation_id }
        }
        _ => YaiError::TransportContract {
            operation_id,
            transport: LOCAL_IPC_RPC_TRANSPORT,
            status: failure.status.as_str(),
            message: failure.message,
        },
    }
}

pub fn contract_error(
    operation_id: &'static str,
    kind: LocalIpcRpcClientErrorKind,
    message: impl Into<String>,
) -> YaiError {
    match kind {
        LocalIpcRpcClientErrorKind::NotConfigured => {
            YaiError::TransportNotConfigured { operation_id }
        }
        _ => YaiError::TransportContract {
            operation_id,
            transport: LOCAL_IPC_RPC_TRANSPORT,
            status: kind.as_str(),
            message: message.into(),
        },
    }
}
