import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class OutputSurface extends TransportBackedSurface {
  show(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.outputShow, request);
  }
}
