import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class KnowledgeSurface extends TransportBackedSurface {
  query(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.knowledgeQuery, request);
  }

  lineageTrace(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.knowledgeLineageTrace, request);
  }
}
