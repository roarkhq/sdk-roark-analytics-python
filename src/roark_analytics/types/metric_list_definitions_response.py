# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetricListDefinitionsResponse", "Data", "DataUnit"]


class DataUnit(BaseModel):
    """Unit information if applicable"""

    name: str
    """Name of the unit"""

    symbol: Optional[str] = None
    """Symbol for the unit"""


class Data(BaseModel):
    """Metric definition data"""

    id: str
    """Unique identifier for the metric definition"""

    description: str
    """Description of what the metric measures"""

    metric_id: str = FieldInfo(alias="metricId")
    """Stable metric identifier (e.g. "call_reason", "customer_satisfaction")"""

    name: str
    """Name of the metric"""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] = FieldInfo(alias="supportedContexts")
    """Which levels this metric can produce values at"""

    type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"]
    """Type of value this metric produces"""

    unit: Optional[DataUnit] = None
    """Unit information if applicable"""


class MetricListDefinitionsResponse(BaseModel):
    data: List[Data]
    """Metrics response payload"""
