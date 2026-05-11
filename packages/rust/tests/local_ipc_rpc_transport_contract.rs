use std::fs;
use std::path::PathBuf;
use std::sync::{Mutex, OnceLock};
use std::time::{SystemTime, UNIX_EPOCH};

use yai_sdk_rust::{
    platform_default_endpoint_path, runtime_discovery_file_path, LocalIpcRpcDiscoveryStatus,
    LocalIpcRpcFrame, LocalIpcRpcFrameType, LocalIpcRpcHandshakeRequest,
    LocalIpcRpcHandshakeResponse, LocalIpcRpcTransport, LocalIpcRpcTransportConfig,
    NotConfiguredTransport, YaiClient, YaiError, YaiTransport,
};

fn env_lock() -> &'static Mutex<()> {
    static LOCK: OnceLock<Mutex<()>> = OnceLock::new();
    LOCK.get_or_init(|| Mutex::new(()))
}

fn unique_path(label: &str) -> PathBuf {
    let stamp = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap_or_default()
        .as_nanos();
    std::env::temp_dir().join(format!("sdk01-{label}-{stamp}.sock"))
}

#[test]
fn local_ipc_rpc_explicit_endpoint_discovery_wins() {
    let endpoint = unique_path("explicit-endpoint");
    fs::write(&endpoint, b"socket-placeholder").expect("should create placeholder endpoint file");

    let transport = LocalIpcRpcTransport::new(LocalIpcRpcTransportConfig {
        endpoint: Some(endpoint.clone()),
        ..LocalIpcRpcTransportConfig::default()
    });

    let discovered = transport
        .discover_endpoint("system.status")
        .expect("explicit endpoint should discover");

    assert_eq!(discovered.path, endpoint);
    assert_eq!(discovered.status, LocalIpcRpcDiscoveryStatus::Configured);

    fs::remove_file(&endpoint).ok();
}

#[test]
fn local_ipc_rpc_env_endpoint_discovery_works() {
    let _guard = env_lock().lock().expect("env lock");
    let endpoint = unique_path("env-endpoint");
    fs::write(&endpoint, b"socket-placeholder").expect("should create placeholder endpoint file");
    std::env::set_var("YAI_LOCAL_IPC_ENDPOINT", &endpoint);

    let transport = LocalIpcRpcTransport::new(LocalIpcRpcTransportConfig::default());
    let discovered = transport
        .discover_endpoint("system.status")
        .expect("env endpoint should discover");

    assert_eq!(discovered.path, endpoint);
    assert_eq!(discovered.status, LocalIpcRpcDiscoveryStatus::Configured);

    std::env::remove_var("YAI_LOCAL_IPC_ENDPOINT");
    fs::remove_file(&endpoint).ok();
}

#[test]
fn local_ipc_rpc_not_configured_is_truthful() {
    let _guard = env_lock().lock().expect("env lock");
    std::env::remove_var("YAI_LOCAL_IPC_ENDPOINT");

    let transport = LocalIpcRpcTransport::new(LocalIpcRpcTransportConfig::default());
    let result = transport.invoke::<serde_json::Value>("system.status", None);

    assert!(matches!(
        result,
        Err(YaiError::TransportNotConfigured {
            operation_id: "system.status"
        })
    ));
}

#[test]
fn local_ipc_rpc_frame_type_mapping_roundtrips() {
    let frame_type: LocalIpcRpcFrameType = "operation.request"
        .parse()
        .expect("operation.request should parse");
    assert_eq!(frame_type, LocalIpcRpcFrameType::OperationRequest);
    assert_eq!(frame_type.as_str(), "operation.request");

    let frame = LocalIpcRpcFrame::new(
        "frame-1",
        LocalIpcRpcFrameType::Heartbeat,
        "v1",
        None,
        None,
        None,
        serde_json::json!({"ping": true}),
    )
    .expect("frame should encode");

    let encoded = serde_json::to_string(&frame).expect("frame should serialize");
    assert!(encoded.contains("\"frame_type\":\"heartbeat\""));
}

#[test]
fn local_ipc_rpc_handshake_validation_is_structural() {
    let request = LocalIpcRpcHandshakeRequest::new("sdk-rust-test");
    request
        .validate()
        .expect("handshake request should validate");

    let response = LocalIpcRpcHandshakeResponse {
        accepted: true,
        runtime_ref: Some("runtime://local".to_string()),
        negotiated_frame_version: "v1".to_string(),
        negotiated_api_envelope_version: "v1".to_string(),
        supported_features: vec!["operation.request".to_string()],
        rejection_error: None,
    };
    response
        .validate()
        .expect("accepted handshake response should validate");
}

#[test]
fn local_ipc_rpc_excludes_provider_transport_boundary() {
    assert!(!LocalIpcRpcTransport::supports_provider_transport_boundary());
}

#[test]
fn local_ipc_rpc_is_not_default_transport() {
    assert!(!LocalIpcRpcTransport::is_default_transport());

    let client = YaiClient::new(NotConfiguredTransport);
    let result = client.system().status();
    assert!(matches!(
        result,
        Err(YaiError::TransportNotConfigured {
            operation_id: "system.status"
        })
    ));
}

#[test]
fn local_ipc_rpc_endpoint_helpers_are_exposed() {
    let discovery_file = runtime_discovery_file_path();
    let platform_default = platform_default_endpoint_path();

    assert!(!discovery_file.as_os_str().is_empty());
    assert!(!platform_default.as_os_str().is_empty());
}
