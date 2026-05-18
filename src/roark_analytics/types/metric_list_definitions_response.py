# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "MetricListDefinitionsResponse",
    "Data",
    "DataLlmJudgeMetricResponse",
    "DataLlmJudgeMetricResponseUnit",
    "DataProviderMetricResponse",
    "DataProviderMetricResponseUnit",
    "DataThresholdMetricResponse",
    "DataThresholdMetricResponseThreshold",
    "DataThresholdMetricResponseUnit",
    "DataFormulaMetricResponse",
    "DataFormulaMetricResponseFormula",
    "DataFormulaMetricResponseFormulaSource",
    "DataFormulaMetricResponseUnit",
    "DataPatternMetricResponse",
    "DataPatternMetricResponsePattern",
    "DataPatternMetricResponsePatternOutcome",
    "DataPatternMetricResponsePatternTrigger",
    "DataPatternMetricResponseUnit",
]


class DataLlmJudgeMetricResponseUnit(BaseModel):
    """Unit information if applicable"""

    name: str
    """Name of the unit"""

    symbol: Optional[str] = None
    """Symbol for the unit"""


class DataLlmJudgeMetricResponse(BaseModel):
    id: str
    """Unique identifier for the metric definition"""

    calculation_type: Literal["LLM_JUDGE"] = FieldInfo(alias="calculationType")
    """Metric evaluated by an LLM against a prompt."""

    description: str
    """Description of what the metric measures"""

    metric_id: str = FieldInfo(alias="metricId")
    """Alias of `slug` retained for backwards compatibility. Same value as `slug`."""

    name: str
    """Name of the metric"""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

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

    unit: Optional[DataLlmJudgeMetricResponseUnit] = None
    """Unit information if applicable"""


class DataProviderMetricResponseUnit(BaseModel):
    """Unit information if applicable"""

    name: str
    """Name of the unit"""

    symbol: Optional[str] = None
    """Symbol for the unit"""


class DataProviderMetricResponse(BaseModel):
    id: str
    """Unique identifier for the metric definition"""

    calculation_type: Literal["PROVIDER"] = FieldInfo(alias="calculationType")
    """System-managed metric produced by an analysis provider."""

    description: str
    """Description of what the metric measures"""

    metric_id: str = FieldInfo(alias="metricId")
    """Alias of `slug` retained for backwards compatibility. Same value as `slug`."""

    name: str
    """Name of the metric"""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

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

    unit: Optional[DataProviderMetricResponseUnit] = None
    """Unit information if applicable"""


class DataThresholdMetricResponseThreshold(BaseModel):
    """Threshold configuration."""

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


class DataThresholdMetricResponseUnit(BaseModel):
    """Unit information if applicable"""

    name: str
    """Name of the unit"""

    symbol: Optional[str] = None
    """Symbol for the unit"""


class DataThresholdMetricResponse(BaseModel):
    id: str
    """Unique identifier for the metric definition"""

    calculation_type: Literal["THRESHOLD"] = FieldInfo(alias="calculationType")
    """Boolean metric derived by comparing a source metric against a threshold."""

    description: str
    """Description of what the metric measures"""

    metric_id: str = FieldInfo(alias="metricId")
    """Alias of `slug` retained for backwards compatibility. Same value as `slug`."""

    name: str
    """Name of the metric"""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

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

    threshold: Optional[DataThresholdMetricResponseThreshold] = None
    """Threshold configuration."""

    unit: Optional[DataThresholdMetricResponseUnit] = None
    """Unit information if applicable"""


class DataFormulaMetricResponseFormulaSource(BaseModel):
    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId", default=None)


class DataFormulaMetricResponseFormula(BaseModel):
    """Formula configuration."""

    expression: str

    sources: List[DataFormulaMetricResponseFormulaSource]


class DataFormulaMetricResponseUnit(BaseModel):
    """Unit information if applicable"""

    name: str
    """Name of the unit"""

    symbol: Optional[str] = None
    """Symbol for the unit"""


class DataFormulaMetricResponse(BaseModel):
    id: str
    """Unique identifier for the metric definition"""

    calculation_type: Literal["FORMULA"] = FieldInfo(alias="calculationType")
    """Metric computed by evaluating an expression over other metrics."""

    description: str
    """Description of what the metric measures"""

    formula: DataFormulaMetricResponseFormula
    """Formula configuration."""

    metric_id: str = FieldInfo(alias="metricId")
    """Alias of `slug` retained for backwards compatibility. Same value as `slug`."""

    name: str
    """Name of the metric"""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

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

    unit: Optional[DataFormulaMetricResponseUnit] = None
    """Unit information if applicable"""


class DataPatternMetricResponsePatternOutcome(BaseModel):
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


class DataPatternMetricResponsePatternTrigger(BaseModel):
    operator: Literal[
        "GREATER_THAN", "GREATER_THAN_OR_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUALS", "EQUALS", "NOT_EQUALS"
    ]

    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_participant_role: Optional[Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"]] = (
        FieldInfo(alias="sourceParticipantRole", default=None)
    )

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId", default=None)

    threshold_value: str = FieldInfo(alias="thresholdValue")


class DataPatternMetricResponsePattern(BaseModel):
    """Pattern configuration."""

    operation: Literal["PATTERN_EXISTS", "PATTERN_COUNT", "OUTCOME_AGGREGATE"]

    outcome: Optional[DataPatternMetricResponsePatternOutcome] = None

    trigger_combinator: Optional[Literal["AND", "OR"]] = FieldInfo(alias="triggerCombinator", default=None)

    triggers: List[DataPatternMetricResponsePatternTrigger]

    window_mode: Optional[str] = FieldInfo(alias="windowMode", default=None)


class DataPatternMetricResponseUnit(BaseModel):
    """Unit information if applicable"""

    name: str
    """Name of the unit"""

    symbol: Optional[str] = None
    """Symbol for the unit"""


class DataPatternMetricResponse(BaseModel):
    id: str
    """Unique identifier for the metric definition"""

    calculation_type: Literal["PATTERN"] = FieldInfo(alias="calculationType")
    """Metric detecting a trigger condition followed by an outcome within a window."""

    description: str
    """Description of what the metric measures"""

    metric_id: str = FieldInfo(alias="metricId")
    """Alias of `slug` retained for backwards compatibility. Same value as `slug`."""

    name: str
    """Name of the metric"""

    pattern: DataPatternMetricResponsePattern
    """Pattern configuration."""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

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

    unit: Optional[DataPatternMetricResponseUnit] = None
    """Unit information if applicable"""


Data: TypeAlias = Annotated[
    Union[
        DataLlmJudgeMetricResponse,
        DataProviderMetricResponse,
        DataThresholdMetricResponse,
        DataFormulaMetricResponse,
        DataPatternMetricResponse,
    ],
    PropertyInfo(discriminator="calculation_type"),
]


class MetricListDefinitionsResponse(BaseModel):
    data: List[Data]
    """Metrics response payload"""
