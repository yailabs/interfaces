import type { YaiEnvelope } from './envelope';
import type { YaiOperationId } from './operations';
import type { YaiCallContext } from './call-context';

export interface YaiTransport {
  invoke<TData = unknown>(
    operationId: YaiOperationId,
    request?: unknown,
    callContext?: YaiCallContext
  ): Promise<YaiEnvelope<TData>>;
}

export class YaiTransportNotConfiguredError extends Error {
  constructor(operationId: string) {
    super(`YAI transport is not configured for operation ${operationId}`);
    this.name = 'YaiTransportNotConfiguredError';
  }
}

export function unavailableEnvelope<TData = unknown>(operationId: YaiOperationId, message: string): YaiEnvelope<TData> {
  return {
    operation_id: operationId,
    status: 'unavailable',
    execution_claim: false,
    implementation_status: 'transport-unconfigured',
    message
  };
}
