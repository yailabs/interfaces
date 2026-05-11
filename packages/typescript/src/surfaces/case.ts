import type { YaiEnvelope } from '../envelope';
import { YAI_COMPAT_OPERATIONS, YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class CaseSurface extends TransportBackedSurface {
  current(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.caseCurrent, request);
  }

  list(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.caseList, request);
  }

  show(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.caseShow, request);
  }

  recordsTail(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.caseRecordsTail, request);
  }

  // Deprecated compatibility method; canonical case surfaces use current/list/show.
  watchSnapshot(): Promise<YaiEnvelope> {
    return this.invoke(YAI_COMPAT_OPERATIONS.caseWatchSnapshot);
  }

  // Deprecated compatibility method; canonical case surfaces use show/current projections.
  memoryProjection(): Promise<YaiEnvelope> {
    return this.invoke(YAI_COMPAT_OPERATIONS.caseMemoryProjectionInspect);
  }
}
