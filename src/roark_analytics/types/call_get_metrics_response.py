# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CallGetMetricsResponse",
    "Data",
    "DataValue",
    "DataValueFromSegment",
    "DataValueSegment",
    "DataValueToSegment",
    "DataUnit",
]


class DataValueFromSegment(BaseModel):
    id: str
    """Starting segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Starting segment text content"""


class DataValueSegment(BaseModel):
    id: str
    """Segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Segment text content"""


class DataValueToSegment(BaseModel):
    id: str
    """Ending segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Ending segment text content"""


class DataValue(BaseModel):
    computed_at: datetime = FieldInfo(alias="computedAt")
    """ISO 8601 timestamp when the metric was computed"""

    confidence: float
    """Confidence score (0-1) for the computed value.

    Defaults to 1.0 for deterministic metrics.
    """

    context: Literal["CALL", "SEGMENT", "SEGMENT_RANGE"]
    """
    Context level: CALL (entire call), SEGMENT (single segment), SEGMENT_RANGE
    (between/across segments)
    """

    value: Union[float, bool, str]
    """The metric value (type depends on outputType)"""

    from_segment: Optional[DataValueFromSegment] = FieldInfo(alias="fromSegment", default=None)
    """Starting segment information (for SEGMENT_RANGE context metrics)"""

    participant_role: Optional[Literal["agent", "customer"]] = FieldInfo(alias="participantRole", default=None)
    """Role of participant (only for PER_PARTICIPANT metrics)"""

    segment: Optional[DataValueSegment] = None
    """Segment information (for SEGMENT context metrics)"""

    to_segment: Optional[DataValueToSegment] = FieldInfo(alias="toSegment", default=None)
    """Ending segment information (for SEGMENT_RANGE context metrics)"""

    value_reasoning: Optional[str] = FieldInfo(alias="valueReasoning", default=None)
    """Explanation for the metric value (especially useful for AI-computed metrics)"""


class DataUnit(BaseModel):
    name: str
    """Name of the unit"""

    symbol: Optional[str] = None
    """Symbol for the unit"""


class Data(BaseModel):
    description: str
    """Description of what the metric measures"""

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")
    """Unique identifier for the metric definition"""

    metric_id: str = FieldInfo(alias="metricId")
    """Stable metric identifier"""

    name: str
    """Name of the metric"""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"]
    """Type of value this metric produces"""

    values: List[DataValue]
    """
    Array of metric values (multiple for PER_PARTICIPANT metrics, or multiple
    segments/turns)
    """

    unit: Optional[DataUnit] = None
    """Unit information if applicable"""


class CallGetMetricsResponse(BaseModel):
    data: List[Data]
    """Call metrics response payload grouped by metric definition"""
