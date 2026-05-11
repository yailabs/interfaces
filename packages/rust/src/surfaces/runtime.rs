use crate::envelope::YaiEnvelope;
use crate::operations::{YAI_COMPAT_OPERATIONS, YAI_OPERATIONS};
use crate::status::YaiResult;
use crate::surfaces::system::RuntimeServiceStatus;
use crate::transport::YaiTransport;

pub struct RuntimeSurface<TTransport: YaiTransport> {
    transport: TTransport,
}

impl<TTransport: YaiTransport> RuntimeSurface<TTransport> {
    pub fn new(transport: TTransport) -> Self {
        Self { transport }
    }

    pub fn status_inspect(&self) -> YaiResult<YaiEnvelope<RuntimeServiceStatus>> {
        self.transport
            .invoke::<RuntimeServiceStatus>(YAI_OPERATIONS.system_status, None)
    }

    pub fn control_plan_inspect(&self) -> YaiResult<YaiEnvelope<RuntimeServiceStatus>> {
        self.transport.invoke::<RuntimeServiceStatus>(
            YAI_COMPAT_OPERATIONS.runtime_service_control_plan,
            Some(serde_json::json!({ "mode": "plan-only" })),
        )
    }
}

#[cfg(test)]
mod tests {
    use crate::{NotConfiguredTransport, YaiClient, YaiError};

    #[test]
    fn runtime_status_not_configured_is_not_success() {
        let client = YaiClient::new(NotConfiguredTransport);
        let result = client.runtime().status_inspect();
        assert!(matches!(
            result,
            Err(YaiError::TransportNotConfigured {
                operation_id: "system.status"
            })
        ));
    }

    #[test]
    fn runtime_control_plan_not_configured_is_not_success() {
        let client = YaiClient::new(NotConfiguredTransport);
        let result = client.runtime().control_plan_inspect();
        assert!(matches!(
            result,
            Err(YaiError::TransportNotConfigured {
                operation_id: "runtime.service.control.plan"
            })
        ));
    }
}
