import type { YaiEnvelope } from '../envelope';
import { YAI_COMPAT_OPERATIONS } from '../operations';
import { StateSurface } from './state';

// Deprecated compatibility alias; prefer StateSurface and client.state.
export class RecordsSurface extends StateSurface {
  projections(): Promise<YaiEnvelope> {
    return this.invoke(YAI_COMPAT_OPERATIONS.recordsProjectionList);
  }
}
