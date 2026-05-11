import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class ProvidersSurface extends TransportBackedSurface {
  list(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.providersList, request);
  }

  probe(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.providersProbe, request);
  }
}
