export const YAI_OPERATIONS = {
  systemStatus: 'system.status',
  systemCheck: 'system.check',
  systemRuntimeInspect: 'system.runtime.inspect',
  caseCurrent: 'case.current',
  caseList: 'case.list',
  caseShow: 'case.show',
  caseRecordsTail: 'case.records.tail',
  conversationCurrent: 'conversation.current',
  conversationMessagesSend: 'conversation.messages.send',
  promptingContextAssemble: 'prompting.context.assemble',
  workflowList: 'workflow.list',
  workflowShow: 'workflow.show',
  workflowStepsPending: 'workflow.steps.pending',
  workflowRunsWatch: 'workflow.runs.watch',
  governancePosture: 'governance.posture',
  governancePolicyResolve: 'governance.policy.resolve',
  controlDecisionsExplain: 'control.decisions.explain',
  controlGatesList: 'control.gates.list',
  controlGatesShow: 'control.gates.show',
  knowledgeLineageTrace: 'knowledge.lineage.trace',
  knowledgeQuery: 'knowledge.query',
  stateRecordsQuery: 'state.records.query',
  stateRecordsTail: 'state.records.tail',
  providersList: 'providers.list',
  providersProbe: 'providers.probe',
  modelsList: 'models.list',
  modelsCapabilitiesShow: 'models.capabilities.show',
  agentsList: 'agents.list',
  agentsTrace: 'agents.trace',
  orchestratorRoutesResolve: 'orchestrator.routes.resolve',
  outputShow: 'output.show',
  sessionCurrent: 'session.current',
  sessionStatus: 'session.status'
} as const;

// Legacy operation ids retained only for compatibility paths. These are not
// canonical public SDK operation constants and do not track the current api
// registry.
export const YAI_COMPAT_OPERATIONS = {
  runtimeStatusInspect: 'runtime.status.inspect',
  runtimeServiceLifecycleInspect: 'runtime.service.lifecycle.inspect',
  runtimeServiceHealthInspect: 'runtime.service.health.inspect',
  runtimeServiceControlPlan: 'runtime.service.control.plan',
  caseWatchSnapshot: 'case.watch.snapshot',
  caseMemoryProjectionInspect: 'case.memory.projection.inspect',
  recordsProjectionList: 'records.projection.list',
  flowBindingReadinessInspect: 'flow.binding.readiness.inspect',
  governanceReadinessInspect: 'governance.readiness.inspect',
  controlReadinessInspect: 'control.readiness.inspect',
  supervisorReadinessInspect: 'control.readiness.inspect',
  agentOrchestrationEntryPropose: 'agent.orchestration.entry.propose'
} as const;

export type YaiCanonicalOperationId = (typeof YAI_OPERATIONS)[keyof typeof YAI_OPERATIONS];
export type YaiCompatOperationId = (typeof YAI_COMPAT_OPERATIONS)[keyof typeof YAI_COMPAT_OPERATIONS];
export type YaiOperationId = YaiCanonicalOperationId | YaiCompatOperationId;
