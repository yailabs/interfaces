pub mod call_context;
pub mod client;
pub mod envelope;
pub mod operations;
pub mod status;
pub mod surfaces;
pub mod transport;
pub mod transports;

pub use call_context::{
    is_client_subject_ref, YaiCallContext, YaiCallContextConfig, DEFAULT_RUST_CLIENT_REF,
    DEFAULT_RUST_CLIENT_SUBJECT_REF, DEFAULT_SYSTEM_ROOT_CONTEXT_REF,
};
pub use client::YaiClient;
pub use envelope::YaiEnvelope;
pub use operations::YAI_OPERATIONS;
pub use status::{YaiError, YaiResult, YaiStatus};
pub use transport::{NotConfiguredTransport, YaiTransport};
pub use transports::http::{HttpTransport, HttpTransportConfig};
pub use transports::local_ipc_rpc::{LocalIpcRpcTransport, LocalIpcRpcTransportConfig};
pub use transports::local_ipc_rpc_endpoint::{
    platform_default_endpoint_path, runtime_discovery_file_path, LocalIpcRpcDiscoveryFailure,
    LocalIpcRpcDiscoveryStatus, LocalIpcRpcEndpoint, LocalIpcRpcEndpointSource,
};
pub use transports::local_ipc_rpc_error::{LocalIpcRpcClientErrorKind, LOCAL_IPC_RPC_TRANSPORT};
pub use transports::local_ipc_rpc_frame::{LocalIpcRpcFrame, LocalIpcRpcFrameType};
pub use transports::local_ipc_rpc_handshake::{
    LocalIpcRpcHandshakeRequest, LocalIpcRpcHandshakeResponse,
};
