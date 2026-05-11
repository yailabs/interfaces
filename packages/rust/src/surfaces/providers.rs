use serde::{Deserialize, Serialize};
use serde_json::Value;

use crate::envelope::YaiEnvelope;
use crate::operations::YAI_OPERATIONS;
use crate::status::YaiResult;
use crate::transport::YaiTransport;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ProvidersList {
    pub providers: Option<Vec<Value>>,
    pub count: Option<u64>,
}

pub struct ProvidersSurface<TTransport: YaiTransport> {
    transport: TTransport,
}

impl<TTransport: YaiTransport> ProvidersSurface<TTransport> {
    pub fn new(transport: TTransport) -> Self {
        Self { transport }
    }

    pub fn list(&self) -> YaiResult<YaiEnvelope<ProvidersList>> {
        self.transport
            .invoke::<ProvidersList>(YAI_OPERATIONS.providers_list, None)
    }

    pub fn probe(&self) -> YaiResult<YaiEnvelope<Value>> {
        self.transport
            .invoke::<Value>(YAI_OPERATIONS.providers_probe, None)
    }
}

#[cfg(test)]
mod tests {
    use crate::{NotConfiguredTransport, YaiClient, YaiError};

    #[test]
    fn providers_list_not_configured_is_not_success() {
        let client = YaiClient::new(NotConfiguredTransport);
        let result = client.providers().list();
        assert!(matches!(
            result,
            Err(YaiError::TransportNotConfigured {
                operation_id: "providers.list"
            })
        ));
    }
}
