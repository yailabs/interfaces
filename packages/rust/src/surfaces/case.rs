use serde::{Deserialize, Serialize};
use serde_json::Value;

use crate::envelope::YaiEnvelope;
use crate::operations::YAI_OPERATIONS;
use crate::status::YaiResult;
use crate::transport::YaiTransport;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CaseCurrent {
    pub status: Option<String>,
    pub case_uri: Option<String>,
}

pub struct CaseSurface<TTransport: YaiTransport> {
    transport: TTransport,
}

impl<TTransport: YaiTransport> CaseSurface<TTransport> {
    pub fn new(transport: TTransport) -> Self {
        Self { transport }
    }

    pub fn current(&self) -> YaiResult<YaiEnvelope<CaseCurrent>> {
        self.transport
            .invoke::<CaseCurrent>(YAI_OPERATIONS.case_current, None)
    }

    pub fn list(&self) -> YaiResult<YaiEnvelope<Value>> {
        self.transport
            .invoke::<Value>(YAI_OPERATIONS.case_list, None)
    }

    pub fn show(&self) -> YaiResult<YaiEnvelope<Value>> {
        self.transport
            .invoke::<Value>(YAI_OPERATIONS.case_show, None)
    }

    pub fn records_tail(&self) -> YaiResult<YaiEnvelope<Value>> {
        self.transport
            .invoke::<Value>(YAI_OPERATIONS.case_records_tail, None)
    }

    pub fn current_inspect(&self) -> YaiResult<YaiEnvelope<CaseCurrent>> {
        self.current()
    }
}

#[cfg(test)]
mod tests {
    use crate::{NotConfiguredTransport, YaiClient, YaiError};

    #[test]
    fn case_current_not_configured_is_not_success() {
        let client = YaiClient::new(NotConfiguredTransport);
        let result = client.case().current_inspect();
        assert!(matches!(
            result,
            Err(YaiError::TransportNotConfigured {
                operation_id: "case.current"
            })
        ));
    }
}
