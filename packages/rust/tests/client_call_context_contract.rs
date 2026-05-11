use serde_json::json;
use yai_sdk_rust::{
    is_client_subject_ref, HttpTransport, HttpTransportConfig, LocalIpcRpcTransport,
    LocalIpcRpcTransportConfig, YaiCallContext, DEFAULT_SYSTEM_ROOT_CONTEXT_REF,
};

#[test]
fn call_context_constructs_with_client_subject_ref() {
    let context = YaiCallContext::with_request_ids(
        "sdk-rust",
        "client-subject://sdk-rust",
        "local_ipc_rpc",
        "request-a5-0001",
        "correlation-a5-0001",
    );

    assert_eq!(context.request_id, "request-a5-0001");
    assert_eq!(context.correlation_id, "correlation-a5-0001");
    assert_eq!(context.client_ref, "sdk-rust");
    assert_eq!(context.client_subject_ref, "client-subject://sdk-rust");
    assert_eq!(
        context.system_root_context_ref,
        DEFAULT_SYSTEM_ROOT_CONTEXT_REF
    );
    assert!(context.work_case_ref.is_none());
    assert!(context.system_call_ref.is_none());
    assert!(is_client_subject_ref(&context.client_subject_ref));
    assert!(!is_client_subject_ref(
        "case://acme-inc/customer-onboarding"
    ));
}

#[test]
fn call_context_can_generate_request_and_correlation_ids() {
    let context = YaiCallContext::new("sdk-rust", "client-subject://sdk-rust", "local_ipc_rpc");

    assert!(context.request_id.starts_with("sdk-request-"));
    assert_eq!(context.correlation_id, context.request_id);
    assert!(context.system_call_ref.is_none());
}

#[test]
fn local_ipc_request_includes_call_context_when_available() {
    let transport = LocalIpcRpcTransport::new(LocalIpcRpcTransportConfig {
        client_ref: "sdk-rust-test".to_string(),
        ..LocalIpcRpcTransportConfig::default()
    });
    let context = YaiCallContext::with_request_ids(
        "sdk-rust-test",
        "client-subject://sdk-rust",
        "local_ipc_rpc",
        "request-a5-ipc",
        "correlation-a5-ipc",
    )
    .with_client_connection_ref("client-connection://local-ipc-rpc/a5-test")
    .with_client_attachment_ref("client-attachment://sdk-rust/local-ipc-rpc/a5-test")
    .with_work_case_ref("case://acme-inc/customer-onboarding");

    let envelope =
        transport.prepare_request_envelope("case.show", Some(json!({"case": "demo"})), context);
    let encoded = serde_json::to_value(&envelope).expect("envelope should encode");

    assert_eq!(encoded["request_id"], "request-a5-ipc");
    assert_eq!(encoded["correlation_id"], "correlation-a5-ipc");
    assert_eq!(encoded["client_ref"], "sdk-rust-test");
    assert_eq!(encoded["client_subject_ref"], "client-subject://sdk-rust");
    assert_eq!(
        encoded["client_connection_ref"],
        "client-connection://local-ipc-rpc/a5-test"
    );
    assert_eq!(
        encoded["client_attachment_ref"],
        "client-attachment://sdk-rust/local-ipc-rpc/a5-test"
    );
    assert_eq!(
        encoded["system_root_context_ref"],
        DEFAULT_SYSTEM_ROOT_CONTEXT_REF
    );
    assert_eq!(
        encoded["work_case_ref"],
        "case://acme-inc/customer-onboarding"
    );
    assert!(encoded.get("system_call_ref").is_none());
}

#[test]
fn http_request_includes_call_context_when_available() {
    let transport = HttpTransport::new(HttpTransportConfig::default())
        .expect("HTTP transport should construct without endpoint");
    let context = YaiCallContext::with_request_ids(
        "sdk-rust-http-test",
        "client-subject://sdk-rust",
        "local_http_loopback",
        "request-a5-http",
        "correlation-a5-http",
    )
    .with_client_connection_ref("client-connection://local-http-loopback/a5-test")
    .with_client_attachment_ref("client-attachment://sdk-rust/local-http-loopback/a5-test")
    .with_system_call_ref("system-call://test/a5-preprovided");

    let request = transport.prepare_invoke_request("system.status", None, context);
    let encoded = serde_json::to_value(&request).expect("request should encode");

    assert_eq!(encoded["request_id"], "request-a5-http");
    assert_eq!(encoded["correlation_id"], "correlation-a5-http");
    assert_eq!(encoded["client_ref"], "sdk-rust-http-test");
    assert_eq!(encoded["client_subject_ref"], "client-subject://sdk-rust");
    assert_eq!(
        encoded["client_connection_ref"],
        "client-connection://local-http-loopback/a5-test"
    );
    assert_eq!(
        encoded["client_attachment_ref"],
        "client-attachment://sdk-rust/local-http-loopback/a5-test"
    );
    assert_eq!(
        encoded["system_root_context_ref"],
        DEFAULT_SYSTEM_ROOT_CONTEXT_REF
    );
    assert!(encoded.get("work_case_ref").is_none());
    assert_eq!(
        encoded["system_call_ref"],
        "system-call://test/a5-preprovided"
    );
}

#[test]
fn transport_default_posture_is_unchanged() {
    assert!(!LocalIpcRpcTransport::is_default_transport());
    assert!(!LocalIpcRpcTransport::supports_provider_transport_boundary());
}
