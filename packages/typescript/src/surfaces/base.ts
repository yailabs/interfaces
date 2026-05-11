import type { YaiEnvelope } from '../envelope';
import type { YaiOperationId } from '../operations';
import type { YaiTransport } from '../transport';
import { unavailableEnvelope } from '../transport';

export class TransportBackedSurface {
  constructor(protected readonly transport?: YaiTransport) {}

  protected invoke<TData = unknown>(
    operationId: YaiOperationId,
    request?: unknown,
    message = 'Transport not configured'
  ): Promise<YaiEnvelope<TData>> {
    if (!this.transport) {
      return Promise.resolve(unavailableEnvelope<TData>(operationId, message));
    }
    return this.transport.invoke<TData>(operationId, request);
  }
}
