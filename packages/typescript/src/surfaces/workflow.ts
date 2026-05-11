import type { YaiEnvelope } from '../envelope';
import { YAI_OPERATIONS } from '../operations';
import { TransportBackedSurface } from './base';

export class WorkflowSurface extends TransportBackedSurface {
  list(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.workflowList, request);
  }

  show(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.workflowShow, request);
  }

  stepsPending(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.workflowStepsPending, request);
  }

  runsWatch(request?: unknown): Promise<YaiEnvelope> {
    return this.invoke(YAI_OPERATIONS.workflowRunsWatch, request);
  }
}
