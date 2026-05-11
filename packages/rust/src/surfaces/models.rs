use serde::{Deserialize, Serialize};
use serde_json::Value;

use crate::envelope::YaiEnvelope;
use crate::operations::YAI_OPERATIONS;
use crate::status::YaiResult;
use crate::transport::YaiTransport;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ModelsList {
    pub models: Option<Vec<Value>>,
    pub count: Option<u64>,
}

pub struct ModelsSurface<TTransport: YaiTransport> {
    transport: TTransport,
}

impl<TTransport: YaiTransport> ModelsSurface<TTransport> {
    pub fn new(transport: TTransport) -> Self {
        Self { transport }
    }

    pub fn list(&self) -> YaiResult<YaiEnvelope<ModelsList>> {
        self.transport
            .invoke::<ModelsList>(YAI_OPERATIONS.models_list, None)
    }

    pub fn capabilities_show(&self) -> YaiResult<YaiEnvelope<Value>> {
        self.transport
            .invoke::<Value>(YAI_OPERATIONS.models_capabilities_show, None)
    }

    pub fn list_inspect(&self) -> YaiResult<YaiEnvelope<ModelsList>> {
        self.list()
    }
}

#[cfg(test)]
mod tests {
    use crate::{NotConfiguredTransport, YaiClient, YaiError};

    #[test]
    fn models_list_not_configured_is_not_success() {
        let client = YaiClient::new(NotConfiguredTransport);
        let result = client.models().list_inspect();
        assert!(matches!(
            result,
            Err(YaiError::TransportNotConfigured {
                operation_id: "models.list"
            })
        ));
    }
}
