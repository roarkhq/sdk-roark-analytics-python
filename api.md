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
    EvaluationCreateJobResponse,
    EvaluationGetEvaluatorByIDResponse,
    EvaluationGetEvaluatorsResponse,
    EvaluationGetJobResponse,
    EvaluationGetJobRunsResponse,
)
```

Methods:

- <code title="post /v1/evaluation/job">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">create_job</a>(\*\*<a href="src/roark_analytics/types/evaluation_create_job_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_create_job_response.py">EvaluationCreateJobResponse</a></code>
- <code title="get /v1/evaluation/evaluators/{evaluatorId}">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">get_evaluator_by_id</a>(evaluator_id) -> <a href="./src/roark_analytics/types/evaluation_get_evaluator_by_id_response.py">EvaluationGetEvaluatorByIDResponse</a></code>
- <code title="get /v1/evaluation/evaluators">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">get_evaluators</a>(\*\*<a href="src/roark_analytics/types/evaluation_get_evaluators_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_get_evaluators_response.py">EvaluationGetEvaluatorsResponse</a></code>
- <code title="get /v1/evaluation/job/{jobId}">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">get_job</a>(job_id) -> <a href="./src/roark_analytics/types/evaluation_get_job_response.py">EvaluationGetJobResponse</a></code>
- <code title="get /v1/evaluation/job/{jobId}/runs">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">get_job_runs</a>(job_id, \*\*<a href="src/roark_analytics/types/evaluation_get_job_runs_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_get_job_runs_response.py">EvaluationGetJobRunsResponse</a></code>

# Call

Types:

```python
from roark_analytics.types import CallGetEvaluationRunsResponse, CallGetSentimentRunsResponse
```

Methods:

- <code title="get /v1/call/{callId}/evaluation-run">client.call.<a href="./src/roark_analytics/resources/call.py">get_evaluation_runs</a>(call_id) -> <a href="./src/roark_analytics/types/call_get_evaluation_runs_response.py">CallGetEvaluationRunsResponse</a></code>
- <code title="get /v1/call/{callId}/sentiment-run">client.call.<a href="./src/roark_analytics/resources/call.py">get_sentiment_runs</a>(call_id) -> <a href="./src/roark_analytics/types/call_get_sentiment_runs_response.py">CallGetSentimentRunsResponse</a></code>

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
