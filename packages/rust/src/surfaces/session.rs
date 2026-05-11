use serde::{Deserialize, Serialize};
use serde_json::Value;

use crate::envelope::YaiEnvelope;
use crate::operations::YAI_OPERATIONS;
use crate::status::YaiResult;
use crate::transport::YaiTransport;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SessionStatus {
    pub status: Option<String>,
    pub session_id: Option<String>,
    pub user: Option<String>,
    pub case_route: Option<String>,
}

pub struct SessionSurface<TTransport: YaiTransport> {
    transport: TTransport,
}

impl<TTransport: YaiTransport> SessionSurface<TTransport> {
    pub fn new(transport: TTransport) -> Self {
        Self { transport }
    }

    pub fn current(&self) -> YaiResult<YaiEnvelope<Value>> {
        self.transport
            .invoke::<Value>(YAI_OPERATIONS.session_current, None)
    }

    pub fn status(&self) -> YaiResult<YaiEnvelope<SessionStatus>> {
        self.transport
            .invoke::<SessionStatus>(YAI_OPERATIONS.session_status, None)
    }

    pub fn status_inspect(&self) -> YaiResult<YaiEnvelope<SessionStatus>> {
        self.status()
    }
}

#[cfg(test)]
mod tests {
    use crate::{NotConfiguredTransport, YaiClient, YaiError};

    #[test]
    fn session_status_not_configured_is_not_success() {
        let client = YaiClient::new(NotConfiguredTransport);
        let result = client.session().status_inspect();
        assert!(matches!(
            result,
            Err(YaiError::TransportNotConfigured {
                operation_id: "session.status"
            })
        ));
    }
}
