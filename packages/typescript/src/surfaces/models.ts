import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class ModelsSurface extends TransportBackedSurface {
  list(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.modelsList, request);
  }

  capabilitiesShow(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.modelsCapabilitiesShow, request);
  }
}
