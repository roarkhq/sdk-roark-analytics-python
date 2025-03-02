# Health

Types:

```python
from roark_analytics.types import HealthGetResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/roark_analytics/resources/health.py">get</a>() -> <a href="./src/roark_analytics/types/health_get_response.py">HealthGetResponse</a></code>

# CallAnalysis

Types:

```python
from roark_analytics.types import CallAnalysisCreateResponse, CallAnalysisRetrieveResponse
```

Methods:

- <code title="post /v1/call-analysis">client.call_analysis.<a href="./src/roark_analytics/resources/call_analysis.py">create</a>(\*\*<a href="src/roark_analytics/types/call_analysis_create_params.py">params</a>) -> <a href="./src/roark_analytics/types/call_analysis_create_response.py">CallAnalysisCreateResponse</a></code>
- <code title="get /v1/call-analysis/{jobId}">client.call_analysis.<a href="./src/roark_analytics/resources/call_analysis.py">retrieve</a>(job_id) -> <a href="./src/roark_analytics/types/call_analysis_retrieve_response.py">CallAnalysisRetrieveResponse</a></code>
