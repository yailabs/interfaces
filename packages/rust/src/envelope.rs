use serde::{Deserialize, Serialize};

use crate::status::YaiStatus;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct YaiEnvelope<TData> {
    pub operation_id: String,
    pub status: String,
    pub execution_claim: bool,
    pub implementation_status: String,
    pub system_call_ref: Option<String>,
    pub client_subject_ref: Option<String>,
    pub client_connection_ref: Option<String>,
    pub client_attachment_ref: Option<String>,
    pub system_root_context_ref: Option<String>,
    pub work_case_ref: Option<String>,
    pub control_admission_ref: Option<String>,
    pub message: Option<String>,
    pub data: Option<TData>,
}

impl<TData> YaiEnvelope<TData> {
    pub fn unavailable(operation_id: &'static str, message: impl Into<String>) -> Self {
        Self {
            operation_id: operation_id.to_string(),
            status: YaiStatus::Unavailable.as_str().to_string(),
            execution_claim: false,
            implementation_status: "transport-unconfigured".to_string(),
            system_call_ref: None,
            client_subject_ref: None,
            client_connection_ref: None,
            client_attachment_ref: None,
            system_root_context_ref: None,
            work_case_ref: None,
            control_admission_ref: None,
            message: Some(message.into()),
            data: None,
        }
    }
}
