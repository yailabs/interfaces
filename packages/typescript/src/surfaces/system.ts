import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export type RuntimeLifecycleState =
  | 'unknown'
  | 'unavailable'
  | 'stopped'
  | 'starting'
  | 'running'
  | 'stopping'
  | 'degraded'
  | 'error';

export type RuntimeServiceReadiness = 'ready' | 'pending' | 'unavailable' | 'degraded' | 'error';
export type RuntimeServiceMode = 'local-dev' | 'local-service-planned' | 'remote-service-planned';
export type RuntimeServiceControlPosture = 'dev-wrapper' | 'service-manager-planned' | 'unavailable';
export type RuntimeServiceManagerPosture = 'service-manager-planned' | 'unavailable';
export type RuntimeServiceInstallPosture = 'not-installed' | 'installed' | 'unavailable';
export type RuntimeOperationalReadiness = 'ready' | 'sealed' | 'pending' | 'blocked' | 'unavailable' | 'error';
export type RuntimeSealedPosture = 'sealed' | 'unsealed' | 'pending';
export type RuntimeAuthPosture = 'authenticated' | 'unauthenticated' | 'local-dev' | 'unavailable' | 'unknown';
export type RuntimeCasePosture =
  | 'root_present'
  | 'missing_root'
  | 'tree_present'
  | 'missing_tree'
  | 'root_present/tree_present'
  | 'unavailable'
  | 'unknown';
export type RuntimeOperatorContextPosture =
  | 'active_case_present'
  | 'active_case_missing'
  | 'unavailable'
  | 'pending'
  | 'planned'
  | 'available'
  | 'unknown';
export type RuntimeClientPosture = 'cli-one-shot' | 'loom-tui' | 'sdk-embedded' | 'unknown';
export type RuntimeSessionPosture = 'legacy_ignored' | 'legacy_compatibility' | 'unknown';
export type RuntimeControlPlanServiceManager = 'unavailable' | 'launchd' | 'systemd' | 'manual' | 'unknown';
export type RuntimeControlActionAvailability = 'available' | 'unavailable' | 'planned' | 'unsupported';
export type RuntimeControlActionReason =
  | 'service_manager_unavailable'
  | 'dev_wrapper_only'
  | 'not_implemented'
  | 'unsupported_platform'
  | 'insufficient_permission'
  | 'unknown';
export type RuntimeSealReason =
  | 'none'
  | 'missing_auth_context'
  | 'missing_root_case'
  | 'missing_case_tree'
  | 'missing_operator_context'
  | 'runtime_transport_unavailable'
  | 'unknown'
  | 'client_connection_unavailable'
  | 'operator_context_unavailable'
  | 'authorization_context_unavailable'
  | 'active_case_unselected'
  | 'unsealed';
export type RuntimeActiveCaseReason =
  | 'active_case_unselected'
  | 'active_case_unavailable'
  | 'active_case_blocked'
  | 'active_case_error'
  | 'none';

export interface RuntimeControlPlanAction {
  available: boolean;
  availability?: RuntimeControlActionAvailability;
  reason: RuntimeControlActionReason;
  executionClaim: boolean;
}

export interface RuntimeControlPlan {
  serviceManager: RuntimeControlPlanServiceManager;
  start: RuntimeControlPlanAction;
  stop: RuntimeControlPlanAction;
  restart: RuntimeControlPlanAction;
}

export interface RuntimeServiceStatus {
  schema: 'api.runtime.service.status.v1';
  serviceId?: string;
  status: RuntimeLifecycleState;
  lifecycle?: RuntimeLifecycleState;
  lifecycleState: RuntimeLifecycleState;
  readiness: RuntimeServiceReadiness;
  health: 'available' | 'pending' | 'unavailable' | 'degraded' | 'error' | 'unknown';
  transport?: string;
  sealed: boolean;
  sealedPosture: RuntimeSealedPosture;
  sealReason: RuntimeSealReason;
  authPosture?: RuntimeAuthPosture;
  casePosture?: RuntimeCasePosture;
  clientPosture?: RuntimeClientPosture;
  sessionPosture?: RuntimeSessionPosture;
  allowedSurfaces: Array<'health' | 'status' | 'readiness'>;
  blockedSurfaces: Array<'operational-actions'>;
  identityPosture: 'unavailable' | 'local-dev' | 'available';
  operatorContextPosture: RuntimeOperatorContextPosture;
  activeCasePosture: 'unavailable' | 'unselected' | 'pending' | 'planned' | 'selected';
  activeCaseReason: RuntimeActiveCaseReason;
  activeCaseRef: string;
  serviceLifecycle: RuntimeLifecycleState;
  serviceManagerPosture: RuntimeServiceManagerPosture;
  serviceControlPosture: RuntimeServiceControlPosture;
  serviceInstallPosture: RuntimeServiceInstallPosture;
  devWrapperStatus: RuntimeLifecycleState | 'pending' | 'unavailable';
  systemServiceStatus: 'running' | 'pending' | 'unavailable' | 'not-installed' | 'error';
  operationalReadiness: RuntimeOperationalReadiness;
  operationalReadinessReason: RuntimeSealReason | 'none';
  controlPlan?: RuntimeControlPlan;
  mode: RuntimeServiceMode;
  controlPosture: RuntimeServiceControlPosture;
  message: string;
  warnings?: string[];
  refs?: Record<string, string>;
}

function systemUnavailable(operationId: typeof YAI_OPERATIONS[keyof typeof YAI_OPERATIONS]): YaiEnvelope<RuntimeServiceStatus> {
  return {
    operation_id: operationId,
    status: 'unavailable',
    execution_claim: false,
    implementation_status: 'transport-unconfigured',
    message: 'System transport not configured; runtime/system status is unavailable until a real transport is attached'
  };
}

export class SystemSurface extends TransportBackedSurface {
  status(request?: unknown): Promise<YaiEnvelope<RuntimeServiceStatus>> {
    if (!this.transport) {
      return Promise.resolve(systemUnavailable(YAI_OPERATIONS.systemStatus));
    }
    return this.transport.invoke<RuntimeServiceStatus>(YAI_OPERATIONS.systemStatus, request);
  }

  check(request?: unknown): Promise<YaiEnvelope<RuntimeServiceStatus>> {
    if (!this.transport) {
      return Promise.resolve(systemUnavailable(YAI_OPERATIONS.systemCheck));
    }
    return this.transport.invoke<RuntimeServiceStatus>(YAI_OPERATIONS.systemCheck, request);
  }

  runtimeInspect(request?: unknown): Promise<YaiEnvelope<RuntimeServiceStatus>> {
    if (!this.transport) {
      return Promise.resolve(systemUnavailable(YAI_OPERATIONS.systemRuntimeInspect));
    }
    return this.transport.invoke<RuntimeServiceStatus>(YAI_OPERATIONS.systemRuntimeInspect, request);
  }
}
