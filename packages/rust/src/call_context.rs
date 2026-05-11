use std::time::{SystemTime, UNIX_EPOCH};

use serde::{Deserialize, Serialize};

pub const DEFAULT_SYSTEM_ROOT_CONTEXT_REF: &str = "root-context://system/default";
pub const DEFAULT_RUST_CLIENT_REF: &str = "sdk-rust";
pub const DEFAULT_RUST_CLIENT_SUBJECT_REF: &str = "client-subject://sdk-rust";

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct YaiCallContext {
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
}

impl YaiCallContext {
    pub fn new(
        client_ref: impl Into<String>,
        client_subject_ref: impl Into<String>,
        transport: impl Into<String>,
    ) -> Self {
        let request_id = generated_request_id("sdk-request");
        Self::with_request_ids(
            client_ref,
            client_subject_ref,
            transport,
            request_id.clone(),
            request_id,
        )
    }

    pub fn with_request_ids(
        client_ref: impl Into<String>,
        client_subject_ref: impl Into<String>,
        transport: impl Into<String>,
        request_id: impl Into<String>,
        correlation_id: impl Into<String>,
    ) -> Self {
        Self {
            request_id: request_id.into(),
            correlation_id: correlation_id.into(),
            client_ref: client_ref.into(),
            client_subject_ref: client_subject_ref.into(),
            client_connection_ref: None,
            client_attachment_ref: None,
            system_root_context_ref: DEFAULT_SYSTEM_ROOT_CONTEXT_REF.to_string(),
            work_case_ref: None,
            system_call_ref: None,
            transport: transport.into(),
        }
    }

    pub fn with_client_connection_ref(mut self, value: impl Into<String>) -> Self {
        self.client_connection_ref = Some(value.into());
        self
    }

    pub fn with_client_attachment_ref(mut self, value: impl Into<String>) -> Self {
        self.client_attachment_ref = Some(value.into());
        self
    }

    pub fn with_system_root_context_ref(mut self, value: impl Into<String>) -> Self {
        self.system_root_context_ref = value.into();
        self
    }

    pub fn with_work_case_ref(mut self, value: impl Into<String>) -> Self {
        self.work_case_ref = Some(value.into());
        self
    }

    pub fn with_system_call_ref(mut self, value: impl Into<String>) -> Self {
        self.system_call_ref = Some(value.into());
        self
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct YaiCallContextConfig {
    pub client_ref: String,
    pub client_subject_ref: String,
    pub client_connection_ref: Option<String>,
    pub client_attachment_ref: Option<String>,
    pub system_root_context_ref: String,
    pub work_case_ref: Option<String>,
    pub system_call_ref: Option<String>,
}

impl Default for YaiCallContextConfig {
    fn default() -> Self {
        Self {
            client_ref: DEFAULT_RUST_CLIENT_REF.to_string(),
            client_subject_ref: DEFAULT_RUST_CLIENT_SUBJECT_REF.to_string(),
            client_connection_ref: None,
            client_attachment_ref: None,
            system_root_context_ref: DEFAULT_SYSTEM_ROOT_CONTEXT_REF.to_string(),
            work_case_ref: None,
            system_call_ref: None,
        }
    }
}

impl YaiCallContextConfig {
    pub fn build(&self, transport: impl Into<String>) -> YaiCallContext {
        let request_id = generated_request_id("sdk-request");
        self.build_with_request_ids(transport, request_id.clone(), request_id)
    }

    pub fn build_with_request_ids(
        &self,
        transport: impl Into<String>,
        request_id: impl Into<String>,
        correlation_id: impl Into<String>,
    ) -> YaiCallContext {
        YaiCallContext {
            request_id: request_id.into(),
            correlation_id: correlation_id.into(),
            client_ref: self.client_ref.clone(),
            client_subject_ref: self.client_subject_ref.clone(),
            client_connection_ref: self.client_connection_ref.clone(),
            client_attachment_ref: self.client_attachment_ref.clone(),
            system_root_context_ref: self.system_root_context_ref.clone(),
            work_case_ref: self.work_case_ref.clone(),
            system_call_ref: self.system_call_ref.clone(),
            transport: transport.into(),
        }
    }
}

pub fn is_client_subject_ref(value: &str) -> bool {
    value.starts_with("client-subject://")
        && !value.starts_with("case://")
        && !value.starts_with("principal://")
        && !value.starts_with("session://")
}

fn generated_request_id(prefix: &str) -> String {
    let stamp = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap_or_default()
        .as_nanos();
    format!("{prefix}-{stamp}")
}
