import type { YaiStatus } from './status';

export interface YaiEnvelope<TData = unknown> {
  operation_id: string;
  status: YaiStatus;
  execution_claim: boolean;
  implementation_status: string;
  system_call_ref?: string;
  client_subject_ref?: string;
  client_connection_ref?: string;
  client_attachment_ref?: string;
  system_root_context_ref?: string;
  work_case_ref?: string;
  control_admission_ref?: string;
  message?: string;
  data?: TData;
}
