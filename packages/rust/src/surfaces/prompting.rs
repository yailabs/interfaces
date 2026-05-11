use serde_json::Value;

use crate::envelope::YaiEnvelope;
use crate::operations::YAI_OPERATIONS;
use crate::status::YaiResult;
use crate::transport::YaiTransport;

pub struct PromptingSurface<TTransport: YaiTransport> {
    transport: TTransport,
}

impl<TTransport: YaiTransport> PromptingSurface<TTransport> {
    pub fn new(transport: TTransport) -> Self {
        Self { transport }
    }

    pub fn context_assemble(&self, request: Option<Value>) -> YaiResult<YaiEnvelope<Value>> {
        self.transport
            .invoke::<Value>(YAI_OPERATIONS.prompting_context_assemble, request)
    }
}
