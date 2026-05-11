use serde::de::DeserializeOwned;

use crate::call_context::YaiCallContext;
use crate::envelope::YaiEnvelope;
use crate::status::{YaiError, YaiResult};

pub trait YaiTransport {
    fn invoke<TData>(
        &self,
        operation_id: &'static str,
        request: Option<serde_json::Value>,
    ) -> YaiResult<YaiEnvelope<TData>>
    where
        TData: DeserializeOwned;

    fn invoke_with_context<TData>(
        &self,
        operation_id: &'static str,
        request: Option<serde_json::Value>,
        _context: YaiCallContext,
    ) -> YaiResult<YaiEnvelope<TData>>
    where
        TData: DeserializeOwned,
    {
        self.invoke(operation_id, request)
    }
}

#[derive(Debug, Default, Clone)]
pub struct NotConfiguredTransport;

impl YaiTransport for NotConfiguredTransport {
    fn invoke<TData>(
        &self,
        operation_id: &'static str,
        _request: Option<serde_json::Value>,
    ) -> YaiResult<YaiEnvelope<TData>>
    where
        TData: DeserializeOwned,
    {
        Err(YaiError::TransportNotConfigured { operation_id })
    }
}

#[cfg(test)]
mod tests {
    use super::{NotConfiguredTransport, YaiTransport};
    use crate::status::YaiError;

    #[test]
    fn not_configured_transport_returns_not_configured() {
        let transport = NotConfiguredTransport;
        let result = transport.invoke::<serde_json::Value>("system.status", None);
        assert!(matches!(
            result,
            Err(YaiError::TransportNotConfigured {
                operation_id: "system.status"
            })
        ));
    }
}
