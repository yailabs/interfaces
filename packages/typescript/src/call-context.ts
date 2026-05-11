export const DEFAULT_SYSTEM_ROOT_CONTEXT_REF = 'root-context://system/default';
export const DEFAULT_TYPESCRIPT_CLIENT_REF = 'sdk-typescript';
export const DEFAULT_TYPESCRIPT_CLIENT_SUBJECT_REF = 'client-subject://sdk-typescript';

export interface YaiCallContext {
  request_id: string;
  correlation_id: string;
  client_ref: string;
  client_subject_ref: string;
  client_connection_ref?: string;
  client_attachment_ref?: string;
  system_root_context_ref: string;
  work_case_ref?: string;
  system_call_ref?: string;
  transport: string;
}

export interface YaiCallContextInput {
  request_id?: string;
  correlation_id?: string;
  client_ref?: string;
  client_subject_ref: string;
  client_connection_ref?: string;
  client_attachment_ref?: string;
  system_root_context_ref?: string;
  work_case_ref?: string;
  system_call_ref?: string;
  transport: string;
}

export function createYaiCallContext(input: YaiCallContextInput): YaiCallContext {
  const requestId = input.request_id ?? generatedRequestId();
  return {
    request_id: requestId,
    correlation_id: input.correlation_id ?? requestId,
    client_ref: input.client_ref ?? DEFAULT_TYPESCRIPT_CLIENT_REF,
    client_subject_ref: input.client_subject_ref,
    client_connection_ref: input.client_connection_ref,
    client_attachment_ref: input.client_attachment_ref,
    system_root_context_ref: input.system_root_context_ref ?? DEFAULT_SYSTEM_ROOT_CONTEXT_REF,
    work_case_ref: input.work_case_ref,
    system_call_ref: input.system_call_ref,
    transport: input.transport
  };
}

export function createDefaultTypeScriptCallContext(
  transport: string,
  input: Partial<Omit<YaiCallContextInput, 'client_subject_ref' | 'transport'>> = {}
): YaiCallContext {
  return createYaiCallContext({
    ...input,
    client_ref: input.client_ref ?? DEFAULT_TYPESCRIPT_CLIENT_REF,
    client_subject_ref: DEFAULT_TYPESCRIPT_CLIENT_SUBJECT_REF,
    transport
  });
}

export function isClientSubjectRef(value: string): boolean {
  return (
    value.startsWith('client-subject://') &&
    !value.startsWith('case://') &&
    !value.startsWith('principal://') &&
    !value.startsWith('session://')
  );
}

function generatedRequestId(): string {
  return `sdk-request-${Date.now()}-${Math.random().toString(36).slice(2)}`;
}
