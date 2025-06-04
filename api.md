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
    EvaluationGetJobResponse,
    EvaluationGetJobRunsResponse,
)
```

Methods:

- <code title="post /v1/evaluation/job">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">create_job</a>(\*\*<a href="src/roark_analytics/types/evaluation_create_job_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_create_job_response.py">EvaluationCreateJobResponse</a></code>
- <code title="get /v1/evaluation/job/{jobId}">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">get_job</a>(job_id) -> <a href="./src/roark_analytics/types/evaluation_get_job_response.py">EvaluationGetJobResponse</a></code>
- <code title="get /v1/evaluation/job/{jobId}/runs">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">get_job_runs</a>(job_id, \*\*<a href="src/roark_analytics/types/evaluation_get_job_runs_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_get_job_runs_response.py">EvaluationGetJobRunsResponse</a></code>
