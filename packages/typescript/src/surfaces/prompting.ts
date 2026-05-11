import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class PromptingSurface extends TransportBackedSurface {
  contextAssemble(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.promptingContextAssemble, request);
  }
}
