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
from roark_analytics.types import EvaluationCreateResponse
```

Methods:

- <code title="post /v1/evaluation">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">create</a>(\*\*<a href="src/roark_analytics/types/evaluation_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/evaluation_create_response.py">EvaluationCreateResponse</a></code>
- <code title="get /v1/evaluation/{jobId}">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">retrieve</a>(job_id) -> object</code>
- <code title="get /v1/evaluation/{jobId}/runs">client.evaluation.<a href="./src/roark_analytics/resources/evaluation.py">get_runs</a>(job_id, \*\*<a href="src/roark_analytics/types/evaluation_get_runs_params.py">params</a>) -> object</code>
