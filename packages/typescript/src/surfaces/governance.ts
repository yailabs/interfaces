import type { YaiEnvelope } from '../envelope';
import { YAI_COMPAT_OPERATIONS, YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class GovernanceSurface extends TransportBackedSurface {
  posture(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.governancePosture, request);
  }

  policyResolve(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.governancePolicyResolve, request);
  }

  // Deprecated compatibility method; canonical governance surfaces use posture/policyResolve.
  readiness(): Promise<YaiEnvelope> {
    return this.invoke(YAI_COMPAT_OPERATIONS.governanceReadinessInspect);
  }
}
