# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CallListMetricsResponse",
    "Data",
    "DataValue",
    "DataValueStandardMetricValue",
    "DataValueStandardMetricValueFromSegment",
    "DataValueStandardMetricValueSegment",
    "DataValueStandardMetricValueToSegment",
    "DataValuePropertyVerificationMetricValue",
    "DataValuePropertyVerificationMetricValueFromSegment",
    "DataValuePropertyVerificationMetricValuePropertyVerdict",
    "DataValuePropertyVerificationMetricValuePropertyVerdictSegment",
    "DataValuePropertyVerificationMetricValueSegment",
    "DataValuePropertyVerificationMetricValueToSegment",
    "DataUnit",
]


class DataValueStandardMetricValueFromSegment(BaseModel):
    """Starting segment information (for SEGMENT_RANGE context metrics)"""

    id: str
    """Segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Segment text content"""


class DataValueStandardMetricValueSegment(BaseModel):
    """Segment information (for SEGMENT context metrics)"""

    id: str
    """Segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Segment text content"""


class DataValueStandardMetricValueToSegment(BaseModel):
    """Ending segment information (for SEGMENT_RANGE context metrics)"""

    id: str
    """Segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Segment text content"""


class DataValueStandardMetricValue(BaseModel):
    """A metric value entry. Applies to every metric."""

    capture_status: Literal["SUCCESS", "NOT_APPLICABLE", "DATA_MISSING", "ERROR"] = FieldInfo(alias="captureStatus")
    """Result state of this metric computation.

    SUCCESS carries a real `value`; NOT_APPLICABLE / DATA_MISSING / ERROR do not
    (the `value` field is omitted). Non-SUCCESS rows only appear when the request
    includes ?status=all.
    """

    computed_at: datetime = FieldInfo(alias="computedAt")
    """ISO 8601 timestamp when the metric was computed"""

    context: Literal["CALL", "SEGMENT", "SEGMENT_RANGE"]
    """
    Context level: CALL (entire conversation), SEGMENT (single segment),
    SEGMENT_RANGE (between/across segments)
    """

    call_id: Optional[str] = FieldInfo(alias="callId", default=None)
    """ID of the call this value was computed on.

    Only set when the response spans multiple conversations (e.g. job-scoped metric
    values).
    """

    chat_id: Optional[str] = FieldInfo(alias="chatId", default=None)
    """ID of the chat this value was computed on.

    Only set when the response spans multiple conversations (e.g. job-scoped metric
    values).
    """

    confidence: Optional[float] = None
    """Confidence score (0-1) for the computed value.

    Defaults to 1.0 for deterministic metrics. Omitted on non-SUCCESS rows.
    """

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Error detail when captureStatus is ERROR — e.g.

    provider down, LLM timeout. Undefined for other statuses.
    """

    from_segment: Optional[DataValueStandardMetricValueFromSegment] = FieldInfo(alias="fromSegment", default=None)
    """Starting segment information (for SEGMENT_RANGE context metrics)"""

    participant_role: Optional[Literal["agent", "customer"]] = FieldInfo(alias="participantRole", default=None)
    """Role of participant (only for PER_PARTICIPANT metrics)"""

    policy_ids: Optional[List[str]] = FieldInfo(alias="policyIds", default=None)
    """IDs of metric policies that triggered this metric computation"""

    segment: Optional[DataValueStandardMetricValueSegment] = None
    """Segment information (for SEGMENT context metrics)"""

    to_segment: Optional[DataValueStandardMetricValueToSegment] = FieldInfo(alias="toSegment", default=None)
    """Ending segment information (for SEGMENT_RANGE context metrics)"""

    value: Union[float, bool, str, None] = None
    """The metric value (type depends on outputType).

    Present only on SUCCESS rows; omitted for NOT_APPLICABLE / DATA_MISSING / ERROR.
    """

    value_reasoning: Optional[str] = FieldInfo(alias="valueReasoning", default=None)
    """Explanation for the metric value (especially useful for AI-computed metrics)"""


class DataValuePropertyVerificationMetricValueFromSegment(BaseModel):
    """Starting segment information (for SEGMENT_RANGE context metrics)"""

    id: str
    """Segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Segment text content"""


class DataValuePropertyVerificationMetricValuePropertyVerdictSegment(BaseModel):
    """
    The transcript segment this property was referred to in: the conflicting value for MISMATCH, the confirming reference for MATCH. Omitted for NOT_MENTIONED and when the verdict could not be anchored.
    """

    id: str
    """Segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Segment text content"""


class DataValuePropertyVerificationMetricValuePropertyVerdict(BaseModel):
    expected_value: str = FieldInfo(alias="expectedValue")
    """The value supplied at ingest, frozen at scoring time"""

    property_name: str = FieldInfo(alias="propertyName")
    """The call property checked, as sent at ingest"""

    verdict: Literal["MATCH", "MISMATCH", "NOT_MENTIONED"]
    """How this property resolved against the transcript.

    NOT_MENTIONED means the subject never came up and is not a mismatch.
    """

    observed_value: Optional[str] = FieldInfo(alias="observedValue", default=None)
    """What the transcript said instead. Only present when verdict is MISMATCH."""

    reasoning: Optional[str] = None
    """Judge reasoning for this verdict"""

    segment: Optional[DataValuePropertyVerificationMetricValuePropertyVerdictSegment] = None
    """
    The transcript segment this property was referred to in: the conflicting value
    for MISMATCH, the confirming reference for MATCH. Omitted for NOT_MENTIONED and
    when the verdict could not be anchored.
    """


class DataValuePropertyVerificationMetricValueSegment(BaseModel):
    """Segment information (for SEGMENT context metrics)"""

    id: str
    """Segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Segment text content"""


class DataValuePropertyVerificationMetricValueToSegment(BaseModel):
    """Ending segment information (for SEGMENT_RANGE context metrics)"""

    id: str
    """Segment ID"""

    end_offset_ms: float = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds"""

    start_offset_ms: float = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds"""

    text: str
    """Segment text content"""


class DataValuePropertyVerificationMetricValue(BaseModel):
    """
    Returned for the Property Mismatch metric (`property_transcript_mismatch`): the standard entry plus the per-property verdict breakdown.
    """

    capture_status: Literal["SUCCESS", "NOT_APPLICABLE", "DATA_MISSING", "ERROR"] = FieldInfo(alias="captureStatus")
    """Result state of this metric computation.

    SUCCESS carries a real `value`; NOT_APPLICABLE / DATA_MISSING / ERROR do not
    (the `value` field is omitted). Non-SUCCESS rows only appear when the request
    includes ?status=all.
    """

    computed_at: datetime = FieldInfo(alias="computedAt")
    """ISO 8601 timestamp when the metric was computed"""

    context: Literal["CALL", "SEGMENT", "SEGMENT_RANGE"]
    """
    Context level: CALL (entire conversation), SEGMENT (single segment),
    SEGMENT_RANGE (between/across segments)
    """

    call_id: Optional[str] = FieldInfo(alias="callId", default=None)
    """ID of the call this value was computed on.

    Only set when the response spans multiple conversations (e.g. job-scoped metric
    values).
    """

    chat_id: Optional[str] = FieldInfo(alias="chatId", default=None)
    """ID of the chat this value was computed on.

    Only set when the response spans multiple conversations (e.g. job-scoped metric
    values).
    """

    confidence: Optional[float] = None
    """Confidence score (0-1) for the computed value.

    Defaults to 1.0 for deterministic metrics. Omitted on non-SUCCESS rows.
    """

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Error detail when captureStatus is ERROR — e.g.

    provider down, LLM timeout. Undefined for other statuses.
    """

    from_segment: Optional[DataValuePropertyVerificationMetricValueFromSegment] = FieldInfo(
        alias="fromSegment", default=None
    )
    """Starting segment information (for SEGMENT_RANGE context metrics)"""

    participant_role: Optional[Literal["agent", "customer"]] = FieldInfo(alias="participantRole", default=None)
    """Role of participant (only for PER_PARTICIPANT metrics)"""

    policy_ids: Optional[List[str]] = FieldInfo(alias="policyIds", default=None)
    """IDs of metric policies that triggered this metric computation"""

    property_verdicts: Optional[List[DataValuePropertyVerificationMetricValuePropertyVerdict]] = FieldInfo(
        alias="propertyVerdicts", default=None
    )
    """
    Per-property verdicts for the Property Mismatch metric, in the order the
    properties were checked. Omitted for every other metric.
    """

    segment: Optional[DataValuePropertyVerificationMetricValueSegment] = None
    """Segment information (for SEGMENT context metrics)"""

    to_segment: Optional[DataValuePropertyVerificationMetricValueToSegment] = FieldInfo(alias="toSegment", default=None)
    """Ending segment information (for SEGMENT_RANGE context metrics)"""

    value: Union[float, bool, str, None] = None
    """The metric value (type depends on outputType).

    Present only on SUCCESS rows; omitted for NOT_APPLICABLE / DATA_MISSING / ERROR.
    """

    value_reasoning: Optional[str] = FieldInfo(alias="valueReasoning", default=None)
    """Explanation for the metric value (especially useful for AI-computed metrics)"""


DataValue: TypeAlias = Union[DataValueStandardMetricValue, DataValuePropertyVerificationMetricValue]


class DataUnit(BaseModel):
    """Unit information if applicable"""

    name: str
    """Name of the unit"""

    symbol: Optional[str] = None
    """Symbol for the unit"""


class Data(BaseModel):
    """Metric data grouped by metric definition"""

    description: str
    """Description of what the metric measures"""

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")
    """Unique identifier for the metric definition"""

    metric_id: str = FieldInfo(alias="metricId")
    """Alias of `slug` retained for backwards compatibility. Same value as `slug`."""

    name: str
    """Name of the metric"""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug"""

    type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"]
    """Type of value this metric produces"""

    values: List[DataValue]
    """
    Array of metric values (multiple for PER_PARTICIPANT metrics, or multiple
    segments/turns)
    """

    unit: Optional[DataUnit] = None
    """Unit information if applicable"""


class CallListMetricsResponse(BaseModel):
    data: List[Data]
    """Conversation metrics response payload grouped by metric definition"""
