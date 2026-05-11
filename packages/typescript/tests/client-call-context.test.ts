import {
  DEFAULT_SYSTEM_ROOT_CONTEXT_REF,
  createDefaultTypeScriptCallContext,
  createYaiCallContext,
  isClientSubjectRef,
  unavailableEnvelope,
  type YaiCallContext,
  type YaiTransport
} from '../src/index';

const explicit = createYaiCallContext({
  request_id: 'request-a5-ts',
  correlation_id: 'correlation-a5-ts',
  client_ref: 'sdk-typescript-test',
  client_subject_ref: 'client-subject://sdk-typescript',
  client_connection_ref: 'client-connection://local-http-loopback/a5-ts',
  client_attachment_ref: 'client-attachment://sdk-typescript/local-http-loopback/a5-ts',
  work_case_ref: 'case://acme-inc/customer-onboarding',
  transport: 'local_http_loopback'
});

assertEqual(explicit.request_id, 'request-a5-ts');
assertEqual(explicit.correlation_id, 'correlation-a5-ts');
assertEqual(explicit.client_subject_ref, 'client-subject://sdk-typescript');
assertEqual(explicit.system_root_context_ref, DEFAULT_SYSTEM_ROOT_CONTEXT_REF);
assertEqual(explicit.work_case_ref, 'case://acme-inc/customer-onboarding');
assertEqual(explicit.system_call_ref, undefined);

const generated = createDefaultTypeScriptCallContext('local_http_loopback');
if (!generated.request_id.startsWith('sdk-request-')) {
  throw new Error('expected generated request_id');
}
assertEqual(generated.correlation_id, generated.request_id);
assertEqual(generated.work_case_ref, undefined);
assertEqual(generated.system_call_ref, undefined);

if (!isClientSubjectRef('client-subject://sdk-typescript')) {
  throw new Error('expected client-subject ref to validate');
}
if (isClientSubjectRef('case://acme-inc/customer-onboarding')) {
  throw new Error('case ref must not validate as client subject');
}

const transport: YaiTransport = {
  async invoke(_operationId, _request, callContext?: YaiCallContext) {
    return {
      ...unavailableEnvelope('system.status', 'test only'),
      client_subject_ref: callContext?.client_subject_ref,
      system_root_context_ref: callContext?.system_root_context_ref
    };
  }
};

void transport.invoke('system.status', undefined, explicit);

function assertEqual(actual: unknown, expected: unknown): void {
  if (actual !== expected) {
    throw new Error(`expected ${String(expected)}, got ${String(actual)}`);
  }
}
