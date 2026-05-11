use serde::{Deserialize, Serialize};

use crate::envelope::YaiEnvelope;
use crate::operations::YAI_OPERATIONS;
use crate::status::YaiResult;
use crate::transport::YaiTransport;

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct RuntimeControlPlanAction {
    #[serde(default)]
    pub available: bool,
    #[serde(default)]
    pub availability: Option<String>,
    #[serde(default)]
    pub reason: Option<String>,
    #[serde(rename = "executionClaim", alias = "execution_claim", default)]
    pub execution_claim: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct RuntimeControlPlan {
    #[serde(rename = "serviceManager", alias = "service_manager", default)]
    pub service_manager: Option<String>,
    #[serde(default)]
    pub start: Option<RuntimeControlPlanAction>,
    #[serde(default)]
    pub stop: Option<RuntimeControlPlanAction>,
    #[serde(default)]
    pub restart: Option<RuntimeControlPlanAction>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RuntimeServiceStatus {
    #[serde(default)]
    pub schema: Option<String>,
    pub status: String,
    #[serde(rename = "lifecycleState", alias = "lifecycle_state", default)]
    pub lifecycle_state: Option<String>,
    #[serde(default)]
    pub lifecycle: Option<String>,
    #[serde(default)]
    pub readiness: Option<String>,
    #[serde(default)]
    pub health: Option<String>,
    #[serde(default)]
    pub transport: Option<String>,
    #[serde(
        rename = "operationalReadiness",
        alias = "operational_readiness",
        default
    )]
    pub operational_readiness: Option<String>,
    #[serde(rename = "sealReason", alias = "seal_reason", default)]
    pub seal_reason: Option<String>,
    #[serde(rename = "authPosture", alias = "auth_posture", default)]
    pub auth_posture: Option<String>,
    #[serde(rename = "casePosture", alias = "case_posture", default)]
    pub case_posture: Option<String>,
    #[serde(
        rename = "operatorContextPosture",
        alias = "operator_context_posture",
        default
    )]
    pub operator_context_posture: Option<String>,
    #[serde(rename = "clientPosture", alias = "client_posture", default)]
    pub client_posture: Option<String>,
    #[serde(rename = "sessionPosture", alias = "session_posture", default)]
    pub session_posture: Option<String>,
    #[serde(rename = "controlPlan", alias = "control_plan", default)]
    pub control_plan: Option<RuntimeControlPlan>,
    #[serde(default)]
    pub message: Option<String>,
}

pub struct SystemSurface<TTransport: YaiTransport> {
    transport: TTransport,
}

impl<TTransport: YaiTransport> SystemSurface<TTransport> {
    pub fn new(transport: TTransport) -> Self {
        Self { transport }
    }

    pub fn status(&self) -> YaiResult<YaiEnvelope<RuntimeServiceStatus>> {
        self.transport
            .invoke::<RuntimeServiceStatus>(YAI_OPERATIONS.system_status, None)
    }

    pub fn check(&self) -> YaiResult<YaiEnvelope<RuntimeServiceStatus>> {
        self.transport
            .invoke::<RuntimeServiceStatus>(YAI_OPERATIONS.system_check, None)
    }

    pub fn runtime_inspect(&self) -> YaiResult<YaiEnvelope<RuntimeServiceStatus>> {
        self.transport
            .invoke::<RuntimeServiceStatus>(YAI_OPERATIONS.system_runtime_inspect, None)
    }
}

#[cfg(test)]
mod tests {
    use serde_json::json;

    use crate::{NotConfiguredTransport, YaiClient, YaiError};

    use super::RuntimeServiceStatus;

    #[test]
    fn system_status_not_configured_is_not_success() {
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
    fn system_status_deserializes_canonical_runtime_posture_fields() {
        let data: RuntimeServiceStatus = serde_json::from_value(json!({
            "schema": "api.runtime.service.status.v1",
            "status": "unavailable",
            "lifecycle": "unavailable",
            "lifecycleState": "unavailable",
            "health": "unavailable",
            "readiness": "unavailable",
            "transport": "runtime_transport_unavailable",
            "operationalReadiness": "sealed",
            "sealReason": "missing_auth_context",
            "authPosture": "unauthenticated",
            "casePosture": "unavailable",
            "operatorContextPosture": "unavailable",
            "clientPosture": "sdk-embedded",
            "sessionPosture": "legacy_ignored",
            "controlPlan": {
                "serviceManager": "unavailable",
                "start": {
                    "available": false,
                    "availability": "unavailable",
                    "reason": "not_implemented",
                    "executionClaim": false
                },
                "stop": {
                    "available": false,
                    "availability": "unavailable",
                    "reason": "not_implemented",
                    "executionClaim": false
                },
                "restart": {
                    "available": false,
                    "availability": "unavailable",
                    "reason": "not_implemented",
                    "executionClaim": false
                }
            }
        }))
        .expect("canonical runtime posture fields should deserialize");

        assert_eq!(data.operational_readiness.as_deref(), Some("sealed"));
        assert_eq!(data.seal_reason.as_deref(), Some("missing_auth_context"));
        assert_eq!(data.client_posture.as_deref(), Some("sdk-embedded"));
        assert_eq!(
            data.control_plan
                .as_ref()
                .and_then(|plan| plan.start.as_ref())
                .map(|action| action.execution_claim),
            Some(false)
        );
    }
}
