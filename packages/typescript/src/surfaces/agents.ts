import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class AgentsSurface extends TransportBackedSurface {
  list(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.agentsList, request);
  }

  trace(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.agentsTrace, request);
  }
}
