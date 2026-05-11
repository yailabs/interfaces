pub struct YaiOperations {
    pub system_status: &'static str,
    pub system_check: &'static str,
    pub system_runtime_inspect: &'static str,
    pub case_current: &'static str,
    pub case_list: &'static str,
    pub case_show: &'static str,
    pub case_records_tail: &'static str,
    pub conversation_current: &'static str,
    pub conversation_messages_send: &'static str,
    pub prompting_context_assemble: &'static str,
    pub workflow_list: &'static str,
    pub workflow_show: &'static str,
    pub workflow_steps_pending: &'static str,
    pub workflow_runs_watch: &'static str,
    pub governance_posture: &'static str,
    pub governance_policy_resolve: &'static str,
    pub control_decisions_explain: &'static str,
    pub control_gates_list: &'static str,
    pub control_gates_show: &'static str,
    pub knowledge_lineage_trace: &'static str,
    pub knowledge_query: &'static str,
    pub state_records_query: &'static str,
    pub state_records_tail: &'static str,
    pub providers_list: &'static str,
    pub providers_probe: &'static str,
    pub models_list: &'static str,
    pub models_capabilities_show: &'static str,
    pub agents_list: &'static str,
    pub agents_trace: &'static str,
    pub orchestrator_routes_resolve: &'static str,
    pub output_show: &'static str,
    pub session_current: &'static str,
    pub session_status: &'static str,
}

pub struct YaiCompatOperations {
    pub runtime_service_control_plan: &'static str,
}

pub const YAI_OPERATIONS: YaiOperations = YaiOperations {
    system_status: "system.status",
    system_check: "system.check",
    system_runtime_inspect: "system.runtime.inspect",
    case_current: "case.current",
    case_list: "case.list",
    case_show: "case.show",
    case_records_tail: "case.records.tail",
    conversation_current: "conversation.current",
    conversation_messages_send: "conversation.messages.send",
    prompting_context_assemble: "prompting.context.assemble",
    workflow_list: "workflow.list",
    workflow_show: "workflow.show",
    workflow_steps_pending: "workflow.steps.pending",
    workflow_runs_watch: "workflow.runs.watch",
    governance_posture: "governance.posture",
    governance_policy_resolve: "governance.policy.resolve",
    control_decisions_explain: "control.decisions.explain",
    control_gates_list: "control.gates.list",
    control_gates_show: "control.gates.show",
    knowledge_lineage_trace: "knowledge.lineage.trace",
    knowledge_query: "knowledge.query",
    state_records_query: "state.records.query",
    state_records_tail: "state.records.tail",
    providers_list: "providers.list",
    providers_probe: "providers.probe",
    models_list: "models.list",
    models_capabilities_show: "models.capabilities.show",
    agents_list: "agents.list",
    agents_trace: "agents.trace",
    orchestrator_routes_resolve: "orchestrator.routes.resolve",
    output_show: "output.show",
    session_current: "session.current",
    session_status: "session.status",
};

pub const YAI_COMPAT_OPERATIONS: YaiCompatOperations = YaiCompatOperations {
    runtime_service_control_plan: "runtime.service.control.plan",
};

#[cfg(test)]
mod tests {
    use super::{YAI_COMPAT_OPERATIONS, YAI_OPERATIONS};

    #[test]
    fn operation_constants_match() {
        assert_eq!(YAI_OPERATIONS.system_status, "system.status");
        assert_eq!(YAI_OPERATIONS.system_check, "system.check");
        assert_eq!(
            YAI_OPERATIONS.system_runtime_inspect,
            "system.runtime.inspect"
        );
        assert_eq!(
            YAI_COMPAT_OPERATIONS.runtime_service_control_plan,
            "runtime.service.control.plan"
        );
        assert_eq!(YAI_OPERATIONS.case_current, "case.current");
        assert_eq!(YAI_OPERATIONS.providers_list, "providers.list");
        assert_eq!(YAI_OPERATIONS.models_list, "models.list");
        assert_eq!(
            YAI_OPERATIONS.prompting_context_assemble,
            "prompting.context.assemble"
        );
    }
}
