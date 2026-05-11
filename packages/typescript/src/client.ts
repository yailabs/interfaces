import type { YaiTransport } from './transport';
import { SystemSurface } from './surfaces/system';
import { RuntimeSurface } from './surfaces/runtime';
import { CaseSurface } from './surfaces/case';
import { ConversationSurface } from './surfaces/conversation';
import { PromptingSurface } from './surfaces/prompting';
import { WorkflowSurface } from './surfaces/workflow';
import { KnowledgeSurface } from './surfaces/knowledge';
import { StateSurface } from './surfaces/state';
import { RecordsSurface } from './surfaces/records';
import { FlowSurface } from './surfaces/flow';
import { GovernanceSurface } from './surfaces/governance';
import { ControlSurface } from './surfaces/control';
import { SupervisorSurface } from './surfaces/supervisor';
import { ProvidersSurface } from './surfaces/providers';
import { ModelsSurface } from './surfaces/models';
import { AgentsSurface } from './surfaces/agents';
import { AgentSurface } from './surfaces/agent';
import { OrchestratorSurface } from './surfaces/orchestrator';
import { OutputSurface } from './surfaces/output';

export class YaiClient {
  readonly system: SystemSurface;
  readonly case: CaseSurface;
  readonly conversation: ConversationSurface;
  readonly prompting: PromptingSurface;
  readonly workflow: WorkflowSurface;
  readonly governance: GovernanceSurface;
  readonly control: ControlSurface;
  readonly knowledge: KnowledgeSurface;
  readonly state: StateSurface;
  readonly providers: ProvidersSurface;
  readonly models: ModelsSurface;
  readonly agents: AgentsSurface;
  readonly orchestrator: OrchestratorSurface;
  readonly output: OutputSurface;

  // Legacy compatibility aliases retained for downstream imports.
  readonly runtime: RuntimeSurface;
  readonly records: RecordsSurface;
  readonly flow: FlowSurface;
  readonly supervisor: SupervisorSurface;
  readonly agent: AgentSurface;

  constructor(transport?: YaiTransport) {
    this.system = new SystemSurface(transport);
    this.case = new CaseSurface(transport);
    this.conversation = new ConversationSurface(transport);
    this.prompting = new PromptingSurface(transport);
    this.workflow = new WorkflowSurface(transport);
    this.governance = new GovernanceSurface(transport);
    this.control = new ControlSurface(transport);
    this.knowledge = new KnowledgeSurface(transport);
    this.state = new StateSurface(transport);
    this.providers = new ProvidersSurface(transport);
    this.models = new ModelsSurface(transport);
    this.agents = new AgentsSurface(transport);
    this.orchestrator = new OrchestratorSurface(transport);
    this.output = new OutputSurface(transport);

    this.runtime = new RuntimeSurface(transport);
    this.records = new RecordsSurface(transport);
    this.flow = new FlowSurface(transport);
    this.supervisor = new SupervisorSurface(transport);
    this.agent = new AgentSurface(transport);
  }
}
