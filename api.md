# Health

Types:

```python
from roark_analytics.types import HealthGetResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/roark_analytics/resources/health.py">get</a>() -> <a href="./src/roark_analytics/types/health_get_response.py">HealthGetResponse</a></code>

# Evaluation

Types:

```python
from roark_analytics.types import (
    EvaluationCreateEvaluatorResponse,
    EvaluationCreateJobResponse,
    EvaluationGetEvaluatorByIDResponse,
    EvaluationGetJobResponse,
    EvaluationListEvaluatorsResponse,
    EvaluationListJobRunsResponse,
    EvaluationUpdateEvaluatorResponse,
)
```

Methods:

- <code title="post /v1/evaluation/evaluators">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">create_evaluator</a>(\*\*<a href="src/roark_analytics/types/evaluation_create_evaluator_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_create_evaluator_response.py">EvaluationCreateEvaluatorResponse</a></code>
- <code title="post /v1/evaluation/job">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">create_job</a>(\*\*<a href="src/roark_analytics/types/evaluation_create_job_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_create_job_response.py">EvaluationCreateJobResponse</a></code>
- <code title="get /v1/evaluation/evaluators/{evaluatorId}">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">get_evaluator_by_id</a>(evaluator_id) -> <a href="./src/roark_analytics/types/evaluation_get_evaluator_by_id_response.py">EvaluationGetEvaluatorByIDResponse</a></code>
- <code title="get /v1/evaluation/job/{jobId}">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">get_job</a>(job_id) -> <a href="./src/roark_analytics/types/evaluation_get_job_response.py">EvaluationGetJobResponse</a></code>
- <code title="get /v1/evaluation/evaluators">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">list_evaluators</a>(\*\*<a href="src/roark_analytics/types/evaluation_list_evaluators_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_list_evaluators_response.py">EvaluationListEvaluatorsResponse</a></code>
- <code title="get /v1/evaluation/job/{jobId}/runs">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">list_job_runs</a>(job_id, \*\*<a href="src/roark_analytics/types/evaluation_list_job_runs_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_list_job_runs_response.py">EvaluationListJobRunsResponse</a></code>
- <code title="put /v1/evaluation/evaluators/{evaluatorId}">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">update_evaluator</a>(evaluator_id, \*\*<a href="src/roark_analytics/types/evaluation_update_evaluator_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_update_evaluator_response.py">EvaluationUpdateEvaluatorResponse</a></code>

# Call

Types:

```python
from roark_analytics.types import (
    CallCreateResponse,
    CallListResponse,
    CallGetByIDResponse,
    CallGetTranscriptResponse,
    CallListEvaluationRunsResponse,
    CallListMetricsResponse,
    CallListSentimentRunsResponse,
)
```

Methods:

- <code title="post /v1/call">client.call.<a href="./src/roark_analytics/resources/call.py">create</a>(\*\*<a href="src/roark_analytics/types/call_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/call_create_response.py">CallCreateResponse</a></code>
- <code title="get /v1/call">client.call.<a href="./src/roark_analytics/resources/call.py">list</a>(\*\*<a href="src/roark_analytics/types/call_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/call_list_response.py">CallListResponse</a></code>
- <code title="get /v1/call/{callId}">client.call.<a href="./src/roark_analytics/resources/call.py">get_by_id</a>(call_id) -> <a href="./src/roark_analytics/types/call_get_by_id_response.py">CallGetByIDResponse</a></code>
- <code title="get /v1/call/{callId}/transcript">client.call.<a href="./src/roark_analytics/resources/call.py">get_transcript</a>(call_id, \*\*<a href="src/roark_analytics/types/call_get_transcript_params.py">params</a>) -> <a href="./src/roark_analytics/types/call_get_transcript_response.py">CallGetTranscriptResponse</a></code>
- <code title="get /v1/call/{callId}/evaluation-run">client.call.<a href="./src/roark_analytics/resources/call.py">list_evaluation_runs</a>(call_id) -> <a href="./src/roark_analytics/types/call_list_evaluation_runs_response.py">CallListEvaluationRunsResponse</a></code>
- <code title="get /v1/call/{callId}/metrics">client.call.<a href="./src/roark_analytics/resources/call.py">list_metrics</a>(call_id, \*\*<a href="src/roark_analytics/types/call_list_metrics_params.py">params</a>) -> <a href="./src/roark_analytics/types/call_list_metrics_response.py">CallListMetricsResponse</a></code>
- <code title="get /v1/call/{callId}/sentiment-run">client.call.<a href="./src/roark_analytics/resources/call.py">list_sentiment_runs</a>(call_id) -> <a href="./src/roark_analytics/types/call_list_sentiment_runs_response.py">CallListSentimentRunsResponse</a></code>

# Metric

Types:

```python
from roark_analytics.types import MetricListDefinitionsResponse
```

Methods:

- <code title="get /v1/metric/definitions">client.metric.<a href="./src/roark_analytics/resources/metric.py">list_definitions</a>() -> <a href="./src/roark_analytics/types/metric_list_definitions_response.py">MetricListDefinitionsResponse</a></code>

# Integrations

Types:

```python
from roark_analytics.types import (
    IntegrationCreateRetellCallResponse,
    IntegrationCreateVapiCallResponse,
)
```

Methods:

- <code title="post /v1/retell/call">client.integrations.<a href="./src/roark_analytics/resources/integrations.py">create_retell_call</a>(\*\*<a href="src/roark_analytics/types/integration_create_retell_call_params.py">params</a>) -> <a href="./src/roark_analytics/types/integration_create_retell_call_response.py">IntegrationCreateRetellCallResponse</a></code>
- <code title="post /v1/vapi/call">client.integrations.<a href="./src/roark_analytics/resources/integrations.py">create_vapi_call</a>(\*\*<a href="src/roark_analytics/types/integration_create_vapi_call_params.py">params</a>) -> <a href="./src/roark_analytics/types/integration_create_vapi_call_response.py">IntegrationCreateVapiCallResponse</a></code>

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

# SimulationScenario

Types:

```python
from roark_analytics.types import (
    SimulationScenarioCreateResponse,
    SimulationScenarioUpdateResponse,
    SimulationScenarioListResponse,
    SimulationScenarioDeleteResponse,
    SimulationScenarioGetByIDResponse,
)
```

Methods:

- <code title="post /v1/simulation/scenario">client.simulation_scenario.<a href="./src/roark_analytics/resources/simulation_scenario.py">create</a>(\*\*<a href="src/roark_analytics/types/simulation_scenario_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_scenario_create_response.py">SimulationScenarioCreateResponse</a></code>
- <code title="put /v1/simulation/scenario/{scenarioId}">client.simulation_scenario.<a href="./src/roark_analytics/resources/simulation_scenario.py">update</a>(scenario_id, \*\*<a href="src/roark_analytics/types/simulation_scenario_update_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_scenario_update_response.py">SimulationScenarioUpdateResponse</a></code>
- <code title="get /v1/simulation/scenario">client.simulation_scenario.<a href="./src/roark_analytics/resources/simulation_scenario.py">list</a>(\*\*<a href="src/roark_analytics/types/simulation_scenario_list_params.py">params</a>) -> <a href="./src/roark_analytics/types/simulation_scenario_list_response.py">SimulationScenarioListResponse</a></code>
- <code title="delete /v1/simulation/scenario/{scenarioId}">client.simulation_scenario.<a href="./src/roark_analytics/resources/simulation_scenario.py">delete</a>(scenario_id) -> <a href="./src/roark_analytics/types/simulation_scenario_delete_response.py">SimulationScenarioDeleteResponse</a></code>
- <code title="get /v1/simulation/scenario/{scenarioId}">client.simulation_scenario.<a href="./src/roark_analytics/resources/simulation_scenario.py">get_by_id</a>(scenario_id) -> <a href="./src/roark_analytics/types/simulation_scenario_get_by_id_response.py">SimulationScenarioGetByIDResponse</a></code>

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
