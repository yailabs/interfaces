import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class StateSurface extends TransportBackedSurface {
  recordsQuery(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.stateRecordsQuery, request);
  }

  recordsTail(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.stateRecordsTail, request);
  }
}
