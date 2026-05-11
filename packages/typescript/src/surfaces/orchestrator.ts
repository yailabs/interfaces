import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class OrchestratorSurface extends TransportBackedSurface {
  routesResolve(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.orchestratorRoutesResolve, request);
  }
}
