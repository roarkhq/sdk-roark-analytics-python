# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MetricListDefinitionsResponse",
    "Data",
    "DataFormula",
    "DataFormulaSource",
    "DataPattern",
    "DataPatternOutcome",
    "DataPatternTrigger",
    "DataThreshold",
    "DataUnit",
]


class DataFormulaSource(BaseModel):
    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId", default=None)


class DataFormula(BaseModel):
    """Formula configuration. Present only when calculationType is FORMULA."""

    expression: str

    sources: List[DataFormulaSource]


class DataPatternOutcome(BaseModel):
    operator: Literal[
        "GREATER_THAN", "GREATER_THAN_OR_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUALS", "EQUALS", "NOT_EQUALS"
    ]

    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_participant_role: Optional[Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"]] = (
        FieldInfo(alias="sourceParticipantRole", default=None)
    )

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId", default=None)

    threshold_value: str = FieldInfo(alias="thresholdValue")

    window_after: Optional[int] = FieldInfo(alias="windowAfter", default=None)

    window_before: Optional[int] = FieldInfo(alias="windowBefore", default=None)


class DataPatternTrigger(BaseModel):
    operator: Literal[
        "GREATER_THAN", "GREATER_THAN_OR_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUALS", "EQUALS", "NOT_EQUALS"
    ]

    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_participant_role: Optional[Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"]] = (
        FieldInfo(alias="sourceParticipantRole", default=None)
    )

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId", default=None)

    threshold_value: str = FieldInfo(alias="thresholdValue")


class DataPattern(BaseModel):
    """Pattern configuration. Present only when calculationType is PATTERN."""

    operation: Literal["PATTERN_EXISTS", "PATTERN_COUNT", "OUTCOME_AGGREGATE"]

    outcome: Optional[DataPatternOutcome] = None

    trigger_combinator: Optional[Literal["AND", "OR"]] = FieldInfo(alias="triggerCombinator", default=None)

    triggers: List[DataPatternTrigger]

    window_mode: Optional[str] = FieldInfo(alias="windowMode", default=None)


class DataThreshold(BaseModel):
    """Threshold configuration. Present only when calculationType is THRESHOLD."""

    aggregation_mode: Literal["EACH", "COUNT", "AVERAGE", "MIN", "MAX", "MEDIAN", "P95", "P99", "SUM"] = FieldInfo(
        alias="aggregationMode"
    )

    count_threshold: Optional[int] = FieldInfo(alias="countThreshold", default=None)

    operator: Literal[
        "GREATER_THAN", "GREATER_THAN_OR_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUALS", "EQUALS", "NOT_EQUALS"
    ]

    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_participant_role: Optional[Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"]] = (
        FieldInfo(alias="sourceParticipantRole", default=None)
    )

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId", default=None)

    threshold_value: str = FieldInfo(alias="thresholdValue")


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

    calculation_type: Literal["PROVIDER", "LLM_JUDGE", "THRESHOLD", "PATTERN", "FORMULA"] = FieldInfo(
        alias="calculationType"
    )
    """How the metric is calculated.

    LLM_JUDGE metrics are evaluated by an LLM against a prompt. THRESHOLD, FORMULA,
    and PATTERN metrics are derived from other metrics. PROVIDER metrics are
    system-managed.
    """

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

    variant_id: str = FieldInfo(alias="variantId")
    """
    The resolved variant this response reflects (org-scoped Default if the org has
    customized it, otherwise the system Default). Pass this as sourceVariantId when
    building a derived metric off this one to pin the exact config.
    """

    version_id: str = FieldInfo(alias="versionId")
    """The variant's current version.

    Immutable snapshot of the config — editing the metric produces a new versionId.
    Use it to detect config changes.
    """

    formula: Optional[DataFormula] = None
    """Formula configuration. Present only when calculationType is FORMULA."""

    pattern: Optional[DataPattern] = None
    """Pattern configuration. Present only when calculationType is PATTERN."""

    threshold: Optional[DataThreshold] = None
    """Threshold configuration. Present only when calculationType is THRESHOLD."""

    unit: Optional[DataUnit] = None
    """Unit information if applicable"""


class MetricListDefinitionsResponse(BaseModel):
    data: List[Data]
    """Metrics response payload"""
