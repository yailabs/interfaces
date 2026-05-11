import type { YaiEnvelope } from '../envelope';
import { YAI_COMPAT_OPERATIONS } from '../operations';
import { WorkflowSurface } from './workflow';

// Deprecated compatibility alias; prefer WorkflowSurface and client.workflow.
export class FlowSurface extends WorkflowSurface {
  readiness(): Promise<YaiEnvelope> {
    return this.invoke(YAI_COMPAT_OPERATIONS.flowBindingReadinessInspect);
  }
}
