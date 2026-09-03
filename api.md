# Health

Types:

```python
from roark_analytics.types import HealthGetResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/roark_analytics/resources/health.py">get</a>() -> <a href="./src/roark_analytics/types/health_get_response.py">HealthGetResponse</a></code>

# Call

Types:

```python
from roark_analytics.types import (
    CallCreateResponse,
    CallListResponse,
    CallGetByIDResponse,
    CallGetTranscriptResponse,
    CallListMetricsResponse,
    CallListSentimentRunsResponse,
)
```

Methods:

- <code title="post /v1/call">client.call.<a href="./src/roark_analytics/resources/call.py">create</a>(\*\*<a href="src/roark_analytics/types/call_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/call_create_response.py">CallCreateResponse</a></code>
- <code title="get /v1/call">client.call.<a href="./src/roark_analytics/resources/call.py">list</a>(\*\*<a href="src/roark_analytics/types/call_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/call_list_response.py">CallListResponse</a></code>
- <code title="get /v1/call/{callId}">client.call.<a href="./src/roark_analytics/resources/call.py">get_by_id</a>(call_id) -> <a href="./src/roark_analytics/types/call_get_by_id_response.py">CallGetByIDResponse</a></code>
- <code title="get /v1/call/{callId}/transcript">client.call.<a href="./src/roark_analytics/resources/call.py">get_transcript</a>(call_id, \*\*<a href="src/roark_analytics/types/call_get_transcript_params.py">params</a>) -> <a href="./src/roark_analytics/types/call_get_transcript_response.py">CallGetTranscriptResponse</a></code>
- <code title="get /v1/call/{callId}/metrics">client.call.<a href="./src/roark_analytics/resources/call.py">list_metrics</a>(call_id, \*\*<a href="src/roark_analytics/types/call_list_metrics_params.py">params</a>) -> <a href="./src/roark_analytics/types/call_list_metrics_response.py">CallListMetricsResponse</a></code>
- <code title="get /v1/call/{callId}/sentiment-run">client.call.<a href="./src/roark_analytics/resources/call.py">list_sentiment_runs</a>(call_id) -> <a href="./src/roark_analytics/types/call_list_sentiment_runs_response.py">CallListSentimentRunsResponse</a></code>

# Metric

Types:

```python
from roark_analytics.types import MetricCreateDefinitionResponse, MetricListDefinitionsResponse
```

Methods:

- <code title="post /v1/metric/definitions">client.metric.<a href="./src/roark_analytics/resources/metric.py">create_definition</a>(\*\*<a href="src/roark_analytics/types/metric_create_definition_params.py">params</a>) -> <a href="./src/roark_analytics/types/metric_create_definition_response.py">MetricCreateDefinitionResponse</a></code>
- <code title="get /v1/metric/definitions">client.metric.<a href="./src/roark_analytics/resources/metric.py">list_definitions</a>(\*\*<a href="src/roark_analytics/types/metric_list_definitions_params.py">params</a>) -> <a href="./src/roark_analytics/types/metric_list_definitions_response.py">MetricListDefinitionsResponse</a></code>

# MetricPolicy

Types:

```python
from roark_analytics.types import (
    MetricPolicyCreateResponse,
    MetricPolicyUpdateResponse,
    MetricPolicyListResponse,
    MetricPolicyDeleteResponse,
    MetricPolicyGetByIDResponse,
)
```

Methods:

- <code title="post /v1/metric/policies">client.metric_policy.<a href="./src/roark_analytics/resources/metric_policy.py">create</a>(\*\*<a href="src/roark_analytics/types/metric_policy_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/metric_policy_create_response.py">MetricPolicyCreateResponse</a></code>
- <code title="put /v1/metric/policies/{policyId}">client.metric_policy.<a href="./src/roark_analytics/resources/metric_policy.py">update</a>(policy_id, \*\*<a href="src/roark_analytics/types/metric_policy_update_params.py">params</a>) -> <a href="./src/roark_analytics/types/metric_policy_update_response.py">MetricPolicyUpdateResponse</a></code>
- <code title="get /v1/metric/policies">client.metric_policy.<a href="./src/roark_analytics/resources/metric_policy.py">list</a>(\*\*<a href="src/roark_analytics/types/metric_policy_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/metric_policy_list_response.py">MetricPolicyListResponse</a></code>
- <code title="delete /v1/metric/policies/{policyId}">client.metric_policy.<a href="./src/roark_analytics/resources/metric_policy.py">delete</a>(policy_id) -> <a href="./src/roark_analytics/types/metric_policy_delete_response.py">MetricPolicyDeleteResponse</a></code>
- <code title="get /v1/metric/policies/{policyId}">client.metric_policy.<a href="./src/roark_analytics/resources/metric_policy.py">get_by_id</a>(policy_id) -> <a href="./src/roark_analytics/types/metric_policy_get_by_id_response.py">MetricPolicyGetByIDResponse</a></code>

# MetricCollectionJob

Types:

```python
from roark_analytics.types import (
    MetricCollectionJobCreateResponse,
    MetricCollectionJobListResponse,
    MetricCollectionJobGetByIDResponse,
)
```

Methods:

- <code title="post /v1/metric/collection-jobs">client.metric_collection_job.<a href="./src/roark_analytics/resources/metric_collection_job.py">create</a>(\*\*<a href="src/roark_analytics/types/metric_collection_job_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/metric_collection_job_create_response.py">MetricCollectionJobCreateResponse</a></code>
- <code title="get /v1/metric/collection-jobs">client.metric_collection_job.<a href="./src/roark_analytics/resources/metric_collection_job.py">list</a>(\*\*<a href="src/roark_analytics/types/metric_collection_job_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/metric_collection_job_list_response.py">MetricCollectionJobListResponse</a></code>
- <code title="get /v1/metric/collection-jobs/{jobId}">client.metric_collection_job.<a href="./src/roark_analytics/resources/metric_collection_job.py">get_by_id</a>(job_id) -> <a href="./src/roark_analytics/types/metric_collection_job_get_by_id_response.py">MetricCollectionJobGetByIDResponse</a></code>

# Simulation

Types:

```python
from roark_analytics.types import SimulationRunResponse
```

Methods:

- <code title="post /v1/simulation/run">client.simulation.<a href="./src/roark_analytics/resources/simulation.py">run</a>(\*\*<a href="src/roark_analytics/types/simulation_run_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_run_response.py">SimulationRunResponse</a></code>

# SimulationJob

Types:

```python
from roark_analytics.types import SimulationJobGetByIDResponse, SimulationJobLookupResponse
```

Methods:

- <code title="get /v1/simulation/job/{jobId}">client.simulation_job.<a href="./src/roark_analytics/resources/simulation_job.py">get_by_id</a>(job_id) -> <a href="./src/roark_analytics/types/simulation_job_get_by_id_response.py">SimulationJobGetByIDResponse</a></code>
- <code title="get /v1/simulation/job/lookup">client.simulation_job.<a href="./src/roark_analytics/resources/simulation_job.py">lookup</a>(\*\*<a href="src/roark_analytics/types/simulation_job_lookup_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_job_lookup_response.py">SimulationJobLookupResponse</a></code>

# SimulationRunPlan

Types:

```python
from roark_analytics.types import (
    SimulationRunPlanCreateResponse,
    SimulationRunPlanUpdateResponse,
    SimulationRunPlanListResponse,
    SimulationRunPlanDeleteResponse,
    SimulationRunPlanGetByIDResponse,
)
```

Methods:

- <code title="post /v1/simulation/plan">client.simulation_run_plan.<a href="./src/roark_analytics/resources/simulation_run_plan.py">create</a>(\*\*<a href="src/roark_analytics/types/simulation_run_plan_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_run_plan_create_response.py">SimulationRunPlanCreateResponse</a></code>
- <code title="put /v1/simulation/plan/{planId}">client.simulation_run_plan.<a href="./src/roark_analytics/resources/simulation_run_plan.py">update</a>(plan_id, \*\*<a href="src/roark_analytics/types/simulation_run_plan_update_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_run_plan_update_response.py">SimulationRunPlanUpdateResponse</a></code>
- <code title="get /v1/simulation/plan">client.simulation_run_plan.<a href="./src/roark_analytics/resources/simulation_run_plan.py">list</a>(\*\*<a href="src/roark_analytics/types/simulation_run_plan_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_run_plan_list_response.py">SimulationRunPlanListResponse</a></code>
- <code title="delete /v1/simulation/plan/{planId}">client.simulation_run_plan.<a href="./src/roark_analytics/resources/simulation_run_plan.py">delete</a>(plan_id) -> <a href="./src/roark_analytics/types/simulation_run_plan_delete_response.py">SimulationRunPlanDeleteResponse</a></code>
- <code title="get /v1/simulation/plan/{planId}">client.simulation_run_plan.<a href="./src/roark_analytics/resources/simulation_run_plan.py">get_by_id</a>(plan_id) -> <a href="./src/roark_analytics/types/simulation_run_plan_get_by_id_response.py">SimulationRunPlanGetByIDResponse</a></code>

# SimulationRunPlanJob

Types:

```python
from roark_analytics.types import (
    SimulationRunPlanJobListResponse,
    SimulationRunPlanJobGetByIDResponse,
    SimulationRunPlanJobStartResponse,
)
```

Methods:

- <code title="get /v1/simulation/plan/jobs">client.simulation_run_plan_job.<a href="./src/roark_analytics/resources/simulation_run_plan_job.py">list</a>(\*\*<a href="src/roark_analytics/types/simulation_run_plan_job_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_run_plan_job_list_response.py">SimulationRunPlanJobListResponse</a></code>
- <code title="get /v1/simulation/plan/job/{jobId}">client.simulation_run_plan_job.<a href="./src/roark_analytics/resources/simulation_run_plan_job.py">get_by_id</a>(job_id) -> <a href="./src/roark_analytics/types/simulation_run_plan_job_get_by_id_response.py">SimulationRunPlanJobGetByIDResponse</a></code>
- <code title="post /v1/simulation/plan/{planId}/job">client.simulation_run_plan_job.<a href="./src/roark_analytics/resources/simulation_run_plan_job.py">start</a>(plan_id, \*\*<a href="src/roark_analytics/types/simulation_run_plan_job_start_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_run_plan_job_start_response.py">SimulationRunPlanJobStartResponse</a></code>

# SimulationPersona

Types:

```python
from roark_analytics.types import (
    SimulationPersonaCreateResponse,
    SimulationPersonaUpdateResponse,
    SimulationPersonaListResponse,
    SimulationPersonaGetByIDResponse,
)
```

Methods:

- <code title="post /v1/persona">client.simulation_persona.<a href="./src/roark_analytics/resources/simulation_persona.py">create</a>(\*\*<a href="src/roark_analytics/types/simulation_persona_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_persona_create_response.py">SimulationPersonaCreateResponse</a></code>
- <code title="put /v1/persona/{personaId}">client.simulation_persona.<a href="./src/roark_analytics/resources/simulation_persona.py">update</a>(persona_id, \*\*<a href="src/roark_analytics/types/simulation_persona_update_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_persona_update_response.py">SimulationPersonaUpdateResponse</a></code>
- <code title="get /v1/persona">client.simulation_persona.<a href="./src/roark_analytics/resources/simulation_persona.py">list</a>(\*\*<a href="src/roark_analytics/types/simulation_persona_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_persona_list_response.py">SimulationPersonaListResponse</a></code>
- <code title="get /v1/persona/{personaId}">client.simulation_persona.<a href="./src/roark_analytics/resources/simulation_persona.py">get_by_id</a>(persona_id) -> <a href="./src/roark_analytics/types/simulation_persona_get_by_id_response.py">SimulationPersonaGetByIDResponse</a></code>

# SimulationEnvironment

Types:

```python
from roark_analytics.types import (
    SimulationEnvironmentListResponse,
    SimulationEnvironmentGetByIDResponse,
)
```

Methods:

- <code title="get /v1/simulation/environment">client.simulation_environment.<a href="./src/roark_analytics/resources/simulation_environment.py">list</a>(\*\*<a href="src/roark_analytics/types/simulation_environment_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_environment_list_response.py">SimulationEnvironmentListResponse</a></code>
- <code title="get /v1/simulation/environment/{environmentId}">client.simulation_environment.<a href="./src/roark_analytics/resources/simulation_environment.py">get_by_id</a>(environment_id) -> <a href="./src/roark_analytics/types/simulation_environment_get_by_id_response.py">SimulationEnvironmentGetByIDResponse</a></code>

# CustomerFlow

Types:

```python
from roark_analytics.types import (
    FlowStep,
    CustomerFlowCreateResponse,
    CustomerFlowUpdateResponse,
    CustomerFlowListResponse,
    CustomerFlowDeleteResponse,
    CustomerFlowGetByIDResponse,
    CustomerFlowReplaceGraphResponse,
    CustomerFlowUpdateHappyPathResponse,
)
```

Methods:

- <code title="post /v1/customer-flow">client.customer_flow.<a href="./src/roark_analytics/resources/customer_flow.py">create</a>(\*\*<a href="src/roark_analytics/types/customer_flow_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/customer_flow_create_response.py">CustomerFlowCreateResponse</a></code>
- <code title="put /v1/customer-flow/{flowId}">client.customer_flow.<a href="./src/roark_analytics/resources/customer_flow.py">update</a>(flow_id, \*\*<a href="src/roark_analytics/types/customer_flow_update_params.py">params</a>) -> <a href="./src/roark_analytics/types/customer_flow_update_response.py">CustomerFlowUpdateResponse</a></code>
- <code title="get /v1/customer-flow">client.customer_flow.<a href="./src/roark_analytics/resources/customer_flow.py">list</a>(\*\*<a href="src/roark_analytics/types/customer_flow_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/customer_flow_list_response.py">CustomerFlowListResponse</a></code>
- <code title="delete /v1/customer-flow/{flowId}">client.customer_flow.<a href="./src/roark_analytics/resources/customer_flow.py">delete</a>(flow_id) -> <a href="./src/roark_analytics/types/customer_flow_delete_response.py">CustomerFlowDeleteResponse</a></code>
- <code title="get /v1/customer-flow/{flowId}">client.customer_flow.<a href="./src/roark_analytics/resources/customer_flow.py">get_by_id</a>(flow_id) -> <a href="./src/roark_analytics/types/customer_flow_get_by_id_response.py">CustomerFlowGetByIDResponse</a></code>
- <code title="put /v1/customer-flow/{flowId}/graph">client.customer_flow.<a href="./src/roark_analytics/resources/customer_flow.py">replace_graph</a>(flow_id, \*\*<a href="src/roark_analytics/types/customer_flow_replace_graph_params.py">params</a>) -> <a href="./src/roark_analytics/types/customer_flow_replace_graph_response.py">CustomerFlowReplaceGraphResponse</a></code>
- <code title="put /v1/customer-flow/{flowId}/happy-path">client.customer_flow.<a href="./src/roark_analytics/resources/customer_flow.py">update_happy_path</a>(flow_id, \*\*<a href="src/roark_analytics/types/customer_flow_update_happy_path_params.py">params</a>) -> <a href="./src/roark_analytics/types/customer_flow_update_happy_path_response.py">CustomerFlowUpdateHappyPathResponse</a></code>

# CustomerFlowEdgeCase

Types:

```python
from roark_analytics.types import (
    CustomerFlowEdgeCaseUpdateResponse,
    CustomerFlowEdgeCaseAddResponse,
    CustomerFlowEdgeCasePromoteResponse,
    CustomerFlowEdgeCaseRemoveResponse,
)
```

Methods:

- <code title="put /v1/customer-flow/{flowId}/edge-case/{edgeCaseId}">client.customer_flow_edge_case.<a href="./src/roark_analytics/resources/customer_flow_edge_case.py">update</a>(edge_case_id, \*\*<a href="src/roark_analytics/types/customer_flow_edge_case_update_params.py">params</a>) -> <a href="./src/roark_analytics/types/customer_flow_edge_case_update_response.py">CustomerFlowEdgeCaseUpdateResponse</a></code>
- <code title="post /v1/customer-flow/{flowId}/edge-case">client.customer_flow_edge_case.<a href="./src/roark_analytics/resources/customer_flow_edge_case.py">add</a>(flow_id, \*\*<a href="src/roark_analytics/types/customer_flow_edge_case_add_params.py">params</a>) -> <a href="./src/roark_analytics/types/customer_flow_edge_case_add_response.py">CustomerFlowEdgeCaseAddResponse</a></code>
- <code title="post /v1/customer-flow/{flowId}/edge-case/{edgeCaseId}/promote">client.customer_flow_edge_case.<a href="./src/roark_analytics/resources/customer_flow_edge_case.py">promote</a>(edge_case_id, \*\*<a href="src/roark_analytics/types/customer_flow_edge_case_promote_params.py">params</a>) -> <a href="./src/roark_analytics/types/customer_flow_edge_case_promote_response.py">CustomerFlowEdgeCasePromoteResponse</a></code>
- <code title="delete /v1/customer-flow/{flowId}/edge-case/{edgeCaseId}">client.customer_flow_edge_case.<a href="./src/roark_analytics/resources/customer_flow_edge_case.py">remove</a>(edge_case_id, \*\*<a href="src/roark_analytics/types/customer_flow_edge_case_remove_params.py">params</a>) -> <a href="./src/roark_analytics/types/customer_flow_edge_case_remove_response.py">CustomerFlowEdgeCaseRemoveResponse</a></code>

# Agent

Types:

```python
from roark_analytics.types import (
    AgentCreateResponse,
    AgentUpdateResponse,
    AgentListResponse,
    AgentGetByIDResponse,
)
```

Methods:

- <code title="post /v1/agent">client.agent.<a href="./src/roark_analytics/resources/agent.py">create</a>(\*\*<a href="src/roark_analytics/types/agent_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="put /v1/agent/{agentId}">client.agent.<a href="./src/roark_analytics/resources/agent.py">update</a>(agent_id, \*\*<a href="src/roark_analytics/types/agent_update_params.py">params</a>) -> <a href="./src/roark_analytics/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /v1/agent">client.agent.<a href="./src/roark_analytics/resources/agent.py">list</a>(\*\*<a href="src/roark_analytics/types/agent_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="get /v1/agent/{agentId}">client.agent.<a href="./src/roark_analytics/resources/agent.py">get_by_id</a>(agent_id) -> <a href="./src/roark_analytics/types/agent_get_by_id_response.py">AgentGetByIDResponse</a></code>

# AgentEndpoint

Types:

```python
from roark_analytics.types import (
    AgentEndpointCreateResponse,
    AgentEndpointUpdateResponse,
    AgentEndpointListResponse,
    AgentEndpointGetByIDResponse,
)
```

Methods:

- <code title="post /v1/agent/endpoint">client.agent_endpoint.<a href="./src/roark_analytics/resources/agent_endpoint.py">create</a>(\*\*<a href="src/roark_analytics/types/agent_endpoint_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/agent_endpoint_create_response.py">AgentEndpointCreateResponse</a></code>
- <code title="put /v1/agent/endpoint/{endpointId}">client.agent_endpoint.<a href="./src/roark_analytics/resources/agent_endpoint.py">update</a>(endpoint_id, \*\*<a href="src/roark_analytics/types/agent_endpoint_update_params.py">params</a>) -> <a href="./src/roark_analytics/types/agent_endpoint_update_response.py">AgentEndpointUpdateResponse</a></code>
- <code title="get /v1/agent/endpoint">client.agent_endpoint.<a href="./src/roark_analytics/resources/agent_endpoint.py">list</a>(\*\*<a href="src/roark_analytics/types/agent_endpoint_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/agent_endpoint_list_response.py">AgentEndpointListResponse</a></code>
- <code title="get /v1/agent/endpoint/{endpointId}">client.agent_endpoint.<a href="./src/roark_analytics/resources/agent_endpoint.py">get_by_id</a>(endpoint_id) -> <a href="./src/roark_analytics/types/agent_endpoint_get_by_id_response.py">AgentEndpointGetByIDResponse</a></code>

# HTTPRequestDefinition

Types:

```python
from roark_analytics.types import (
    HTTPRequestDefinitionCreateResponse,
    HTTPRequestDefinitionUpdateResponse,
    HTTPRequestDefinitionListResponse,
    HTTPRequestDefinitionGetByIDResponse,
)
```

Methods:

- <code title="post /v1/http-request-definition">client.http_request_definition.<a href="./src/roark_analytics/resources/http_request_definition.py">create</a>(\*\*<a href="src/roark_analytics/types/http_request_definition_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/http_request_definition_create_response.py">HTTPRequestDefinitionCreateResponse</a></code>
- <code title="put /v1/http-request-definition/{definitionId}">client.http_request_definition.<a href="./src/roark_analytics/resources/http_request_definition.py">update</a>(definition_id, \*\*<a href="src/roark_analytics/types/http_request_definition_update_params.py">params</a>) -> <a href="./src/roark_analytics/types/http_request_definition_update_response.py">HTTPRequestDefinitionUpdateResponse</a></code>
- <code title="get /v1/http-request-definition">client.http_request_definition.<a href="./src/roark_analytics/resources/http_request_definition.py">list</a>(\*\*<a href="src/roark_analytics/types/http_request_definition_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/http_request_definition_list_response.py">HTTPRequestDefinitionListResponse</a></code>
- <code title="get /v1/http-request-definition/{definitionId}">client.http_request_definition.<a href="./src/roark_analytics/resources/http_request_definition.py">get_by_id</a>(definition_id) -> <a href="./src/roark_analytics/types/http_request_definition_get_by_id_response.py">HTTPRequestDefinitionGetByIDResponse</a></code>

# Webhook

Types:

```python
from roark_analytics.types import (
    WebhookCreateResponse,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookGetByIDResponse,
)
```

Methods:

- <code title="post /v1/webhook">client.webhook.<a href="./src/roark_analytics/resources/webhook.py">create</a>(\*\*<a href="src/roark_analytics/types/webhook_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /v1/webhook">client.webhook.<a href="./src/roark_analytics/resources/webhook.py">list</a>(\*\*<a href="src/roark_analytics/types/webhook_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v1/webhook/{webhookId}">client.webhook.<a href="./src/roark_analytics/resources/webhook.py">delete</a>(webhook_id) -> <a href="./src/roark_analytics/types/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="get /v1/webhook/{webhookId}">client.webhook.<a href="./src/roark_analytics/resources/webhook.py">get_by_id</a>(webhook_id) -> <a href="./src/roark_analytics/types/webhook_get_by_id_response.py">WebhookGetByIDResponse</a></code>

# Config

Types:

```python
from roark_analytics.types import Bundle, ConfigFlowStep, ConfigApplyResponse, ConfigDiffResponse
```

Methods:

- <code title="post /v1/config/apply">client.config.<a href="./src/roark_analytics/resources/config.py">apply</a>(\*\*<a href="src/roark_analytics/types/config_apply_params.py">params</a>) -> <a href="./src/roark_analytics/types/config_apply_response.py">ConfigApplyResponse</a></code>
- <code title="post /v1/config/diff">client.config.<a href="./src/roark_analytics/resources/config.py">diff</a>(\*\*<a href="src/roark_analytics/types/config_diff_params.py">params</a>) -> <a href="./src/roark_analytics/types/config_diff_response.py">ConfigDiffResponse</a></code>
