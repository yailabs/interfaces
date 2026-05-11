import type { YaiEnvelope } from '../envelope';
import { YAI_COMPAT_OPERATIONS, YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class ControlSurface extends TransportBackedSurface {
  decisionsExplain(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.controlDecisionsExplain, request);
  }

  gatesList(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.controlGatesList, request);
  }

  gatesShow(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.controlGatesShow, request);
  }

  // Deprecated compatibility method; canonical control surfaces use decisionsExplain/gatesList/gatesShow.
  readiness(): Promise<YaiEnvelope> {
    return this.invoke(YAI_COMPAT_OPERATIONS.controlReadinessInspect);
  }
}
