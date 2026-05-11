use serde_json::Value;

use crate::envelope::YaiEnvelope;
use crate::operations::YAI_OPERATIONS;
use crate::status::YaiResult;
use crate::surfaces::providers::ProvidersList;
use crate::transport::YaiTransport;

pub type ProviderList = ProvidersList;

pub struct ProviderSurface<TTransport: YaiTransport> {
    transport: TTransport,
}

impl<TTransport: YaiTransport> ProviderSurface<TTransport> {
    pub fn new(transport: TTransport) -> Self {
        Self { transport }
    }

    pub fn list_inspect(&self) -> YaiResult<YaiEnvelope<ProviderList>> {
        self.transport
            .invoke::<ProviderList>(YAI_OPERATIONS.providers_list, None)
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
    fn provider_list_not_configured_is_not_success() {
        let client = YaiClient::new(NotConfiguredTransport);
        let result = client.provider().list_inspect();
        assert!(matches!(
            result,
            Err(YaiError::TransportNotConfigured {
                operation_id: "providers.list"
            })
        ));
    }
}
