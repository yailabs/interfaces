import type { YaiEnvelope } from '../envelope';
import { YAI_COMPAT_OPERATIONS } from '../operations';
import { AgentsSurface } from './agents';

// Deprecated compatibility alias; prefer AgentsSurface and client.agents.
export class AgentSurface extends AgentsSurface {
  entryProposal(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_COMPAT_OPERATIONS.agentOrchestrationEntryPropose, request);
  }
}
