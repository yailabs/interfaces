import type { YaiEnvelope } from '../envelope';
import { YAI_COMPAT_OPERATIONS } from '../operations';
import {
  type RuntimeActiveCaseReason,
  type RuntimeAuthPosture,
  type RuntimeCasePosture,
  type RuntimeClientPosture,
  type RuntimeControlActionAvailability,
  type RuntimeControlActionReason,
  type RuntimeControlPlan,
  type RuntimeControlPlanAction,
  type RuntimeControlPlanServiceManager,
  type RuntimeLifecycleState,
  type RuntimeOperatorContextPosture,
  type RuntimeSealReason,
  type RuntimeSealedPosture,
  type RuntimeServiceControlPosture,
  type RuntimeServiceInstallPosture,
  type RuntimeServiceManagerPosture,
  type RuntimeServiceMode,
  type RuntimeOperationalReadiness,
  type RuntimeSessionPosture,
  type RuntimeServiceReadiness,
  type RuntimeServiceStatus,
  SystemSurface
} from './system';

export type {
  RuntimeActiveCaseReason,
  RuntimeAuthPosture,
  RuntimeCasePosture,
  RuntimeClientPosture,
  RuntimeControlActionAvailability,
  RuntimeControlActionReason,
  RuntimeControlPlan,
  RuntimeControlPlanAction,
  RuntimeControlPlanServiceManager,
  RuntimeLifecycleState,
  RuntimeOperatorContextPosture,
  RuntimeSealReason,
  RuntimeSealedPosture,
  RuntimeServiceControlPosture,
  RuntimeServiceInstallPosture,
  RuntimeServiceManagerPosture,
  RuntimeServiceMode,
  RuntimeOperationalReadiness,
  RuntimeSessionPosture,
  RuntimeServiceReadiness,
  RuntimeServiceStatus
};

export interface RuntimeControlPlanStatus extends RuntimeServiceStatus {
  controlPlan?: RuntimeControlPlan;
}

// Deprecated compatibility alias; prefer SystemSurface and client.system.
export class RuntimeSurface extends SystemSurface {
  lifecycle(request?: unknown): Promise<YaiEnvelope<RuntimeServiceStatus>> {
    return this.invoke<RuntimeServiceStatus>(
      YAI_COMPAT_OPERATIONS.runtimeServiceLifecycleInspect,
      request,
      'Runtime service transport not configured; lifecycle status is unavailable until a real transport is attached'
    );
  }

  health(request?: unknown): Promise<YaiEnvelope<RuntimeServiceStatus>> {
    return this.invoke<RuntimeServiceStatus>(
      YAI_COMPAT_OPERATIONS.runtimeServiceHealthInspect,
      request,
      'Runtime service transport not configured; health status is unavailable until a real transport is attached'
    );
  }

  controlPlan(): Promise<YaiEnvelope<RuntimeControlPlanStatus>> {
    return this.invoke<RuntimeControlPlanStatus>(
      YAI_COMPAT_OPERATIONS.runtimeServiceControlPlan,
      { mode: 'plan-only' },
      'Runtime service transport not configured; control planning is unavailable until a real transport is attached'
    );
  }
}
