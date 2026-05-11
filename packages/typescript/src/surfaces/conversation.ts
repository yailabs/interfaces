import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class ConversationSurface extends TransportBackedSurface {
  current(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.conversationCurrent, request);
  }

  messagesSend(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.conversationMessagesSend, request);
  }
}
