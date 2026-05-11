use crate::surfaces::case::CaseSurface;
use crate::surfaces::conversation::ConversationSurface;
use crate::surfaces::models::ModelsSurface;
use crate::surfaces::prompting::PromptingSurface;
use crate::surfaces::provider::ProviderSurface;
use crate::surfaces::providers::ProvidersSurface;
use crate::surfaces::runtime::RuntimeSurface;
use crate::surfaces::session::SessionSurface;
use crate::surfaces::system::SystemSurface;
use crate::transport::YaiTransport;

pub struct YaiClient<TTransport: YaiTransport + Clone> {
    system: SystemSurface<TTransport>,
    runtime: RuntimeSurface<TTransport>,
    session: SessionSurface<TTransport>,
    case: CaseSurface<TTransport>,
    conversation: ConversationSurface<TTransport>,
    prompting: PromptingSurface<TTransport>,
    providers: ProvidersSurface<TTransport>,
    provider: ProviderSurface<TTransport>,
    models: ModelsSurface<TTransport>,
}

impl<TTransport: YaiTransport + Clone> YaiClient<TTransport> {
    pub fn new(transport: TTransport) -> Self {
        Self {
            system: SystemSurface::new(transport.clone()),
            runtime: RuntimeSurface::new(transport.clone()),
            session: SessionSurface::new(transport.clone()),
            case: CaseSurface::new(transport.clone()),
            conversation: ConversationSurface::new(transport.clone()),
            prompting: PromptingSurface::new(transport.clone()),
            providers: ProvidersSurface::new(transport.clone()),
            provider: ProviderSurface::new(transport.clone()),
            models: ModelsSurface::new(transport),
        }
    }

    pub fn system(&self) -> &SystemSurface<TTransport> {
        &self.system
    }

    // Deprecated compatibility alias; prefer system().
    pub fn runtime(&self) -> &RuntimeSurface<TTransport> {
        &self.runtime
    }

    pub fn session(&self) -> &SessionSurface<TTransport> {
        &self.session
    }

    pub fn case(&self) -> &CaseSurface<TTransport> {
        &self.case
    }

    pub fn conversation(&self) -> &ConversationSurface<TTransport> {
        &self.conversation
    }

    pub fn prompting(&self) -> &PromptingSurface<TTransport> {
        &self.prompting
    }

    pub fn providers(&self) -> &ProvidersSurface<TTransport> {
        &self.providers
    }

    // Deprecated compatibility alias; prefer providers().
    pub fn provider(&self) -> &ProviderSurface<TTransport> {
        &self.provider
    }

    pub fn models(&self) -> &ModelsSurface<TTransport> {
        &self.models
    }
}
