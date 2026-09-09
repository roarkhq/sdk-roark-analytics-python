# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MetricListDefinitionsResponse",
    "FormulaMetricResponse",
    "FormulaMetricResponseFormula",
    "FormulaMetricResponseFormulaSource",
    "LlmJudgeMetricResponse",
    "LlmJudgeMetricResponseUnit",
    "Pagination",
    "PatternMetricResponse",
    "PatternMetricResponsePattern",
    "PatternMetricResponsePatternOutcome",
    "PatternMetricResponsePatternTrigger",
    "ProviderMetricResponse",
    "ThresholdMetricResponse",
    "ThresholdMetricResponseThreshold",
]


class LlmJudgeMetricResponseUnit(BaseModel):
    """Unit information if applicable"""

    name: str
    """Name of the unit"""

    symbol: Optional[str]
    """Symbol for the unit"""


class LlmJudgeMetricResponse(BaseModel):
    id: str
    """Unique identifier for the metric definition"""

    boolean_false_label: Optional[str] = FieldInfo(alias="booleanFalseLabel")
    """
    For a BOOLEAN metric, what a `false` value means. Also given to the judge as its
    polarity rule.
    """

    boolean_true_label: Optional[str] = FieldInfo(alias="booleanTrueLabel")
    """
    For a BOOLEAN metric, what a `true` value means. Also given to the judge as its
    polarity rule.
    """

    calculation_type: Literal["LLM_JUDGE"] = FieldInfo(alias="calculationType")
    """Metric evaluated by an LLM against a prompt."""

    description: str
    """Description of what the metric measures"""

    llm_prompt: Optional[str] = FieldInfo(alias="llmPrompt")
    """
    The rubric this judge applies, as stored. Read it back to confirm which criteria
    are live after a create or update.
    """

    metric_id: str = FieldInfo(alias="metricId")
    """Alias of `slug` retained for backwards compatibility. Same value as `slug`."""

    name: str
    """Name of the metric"""

    requires_live_conversation: bool = FieldInfo(alias="requiresLiveConversation")
    """
    True when this metric can only be scored from a live recording
    (`supportedConversationSources` is `["LIVE"]`). Selecting one of these on a
    simulation run forces live enrichment: the run waits for your recording and, if
    none arrives, the metric produces no value. Check this before a run rather than
    discovering the wait afterwards.
    """

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

    supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] = FieldInfo(alias="supportedContexts")
    """Which levels this metric can produce values at"""

    supported_conversation_sources: Optional[List[Literal["SIMULATED", "LIVE"]]] = FieldInfo(
        alias="supportedConversationSources"
    )
    """
    Which kinds of conversation this metric can be scored on. `null` means both.
    `["LIVE"]` marks a metric that can only be scored from your own recording of a
    real call, and `["SIMULATED"]` one that only applies to simulations.
    """

    supports_variants: bool = FieldInfo(alias="supportsVariants")
    """
    Whether you can create a variant of this metric with POST
    /v1/metric/definitions/{idOrSlug}/variants. False for threshold metrics (their
    configuration comes from the metric they derive from), for provider-computed
    metrics whose calculation lives in the collector rather than an editable prompt,
    and for metrics in a package that manages its own variants. Most of Roark’s own
    metrics are false, so read this rather than discovering it from a 403.
    """

    type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"]
    """Type of value this metric produces"""

    variant_id: str = FieldInfo(alias="variantId")
    """
    The resolved variant this response reflects (org-scoped Default if the org has
    customized it, otherwise the system Default). Pass this as sourceVariantId when
    building a derived metric off this one to pin the exact config.
    """

    version_id: str = FieldInfo(alias="versionId")
    """
    The variant's current version. Immutable snapshot of the config — editing the
    metric produces a new versionId. Use it to detect config changes.
    """

    unit: Optional[LlmJudgeMetricResponseUnit] = None
    """Unit information if applicable"""


class ProviderMetricResponse(BaseModel):
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

    requires_live_conversation: bool = FieldInfo(alias="requiresLiveConversation")
    """
    True when this metric can only be scored from a live recording
    (`supportedConversationSources` is `["LIVE"]`). Selecting one of these on a
    simulation run forces live enrichment: the run waits for your recording and, if
    none arrives, the metric produces no value. Check this before a run rather than
    discovering the wait afterwards.
    """

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

    supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] = FieldInfo(alias="supportedContexts")
    """Which levels this metric can produce values at"""

    supported_conversation_sources: Optional[List[Literal["SIMULATED", "LIVE"]]] = FieldInfo(
        alias="supportedConversationSources"
    )
    """
    Which kinds of conversation this metric can be scored on. `null` means both.
    `["LIVE"]` marks a metric that can only be scored from your own recording of a
    real call, and `["SIMULATED"]` one that only applies to simulations.
    """

    supports_variants: bool = FieldInfo(alias="supportsVariants")
    """
    Whether you can create a variant of this metric with POST
    /v1/metric/definitions/{idOrSlug}/variants. False for threshold metrics (their
    configuration comes from the metric they derive from), for provider-computed
    metrics whose calculation lives in the collector rather than an editable prompt,
    and for metrics in a package that manages its own variants. Most of Roark’s own
    metrics are false, so read this rather than discovering it from a 403.
    """

    type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"]
    """Type of value this metric produces"""

    variant_id: str = FieldInfo(alias="variantId")
    """
    The resolved variant this response reflects (org-scoped Default if the org has
    customized it, otherwise the system Default). Pass this as sourceVariantId when
    building a derived metric off this one to pin the exact config.
    """

    version_id: str = FieldInfo(alias="versionId")
    """
    The variant's current version. Immutable snapshot of the config — editing the
    metric produces a new versionId. Use it to detect config changes.
    """

    unit: Optional[LlmJudgeMetricResponseUnit] = None
    """Unit information if applicable"""


class ThresholdMetricResponseThreshold(BaseModel):
    aggregation_mode: Literal["EACH", "COUNT", "AVERAGE", "MIN", "MAX", "MEDIAN", "P95", "P99", "SUM"] = FieldInfo(
        alias="aggregationMode"
    )

    count_threshold: Optional[int] = FieldInfo(alias="countThreshold")

    operator: Literal[
        "GREATER_THAN", "GREATER_THAN_OR_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUALS", "EQUALS", "NOT_EQUALS"
    ]

    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_participant_role: Optional[Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"]] = (
        FieldInfo(alias="sourceParticipantRole")
    )

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId")

    threshold_value: str = FieldInfo(alias="thresholdValue")


class ThresholdMetricResponse(BaseModel):
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

    requires_live_conversation: bool = FieldInfo(alias="requiresLiveConversation")
    """
    True when this metric can only be scored from a live recording
    (`supportedConversationSources` is `["LIVE"]`). Selecting one of these on a
    simulation run forces live enrichment: the run waits for your recording and, if
    none arrives, the metric produces no value. Check this before a run rather than
    discovering the wait afterwards.
    """

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

    supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] = FieldInfo(alias="supportedContexts")
    """Which levels this metric can produce values at"""

    supported_conversation_sources: Optional[List[Literal["SIMULATED", "LIVE"]]] = FieldInfo(
        alias="supportedConversationSources"
    )
    """
    Which kinds of conversation this metric can be scored on. `null` means both.
    `["LIVE"]` marks a metric that can only be scored from your own recording of a
    real call, and `["SIMULATED"]` one that only applies to simulations.
    """

    supports_variants: bool = FieldInfo(alias="supportsVariants")
    """
    Whether you can create a variant of this metric with POST
    /v1/metric/definitions/{idOrSlug}/variants. False for threshold metrics (their
    configuration comes from the metric they derive from), for provider-computed
    metrics whose calculation lives in the collector rather than an editable prompt,
    and for metrics in a package that manages its own variants. Most of Roark’s own
    metrics are false, so read this rather than discovering it from a 403.
    """

    type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"]
    """Type of value this metric produces"""

    variant_id: str = FieldInfo(alias="variantId")
    """
    The resolved variant this response reflects (org-scoped Default if the org has
    customized it, otherwise the system Default). Pass this as sourceVariantId when
    building a derived metric off this one to pin the exact config.
    """

    version_id: str = FieldInfo(alias="versionId")
    """
    The variant's current version. Immutable snapshot of the config — editing the
    metric produces a new versionId. Use it to detect config changes.
    """

    threshold: Optional[ThresholdMetricResponseThreshold] = None
    """Threshold configuration."""

    unit: Optional[LlmJudgeMetricResponseUnit] = None
    """Unit information if applicable"""


class FormulaMetricResponseFormulaSource(BaseModel):
    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId")


class FormulaMetricResponseFormula(BaseModel):
    expression: str

    sources: List[FormulaMetricResponseFormulaSource]


class FormulaMetricResponse(BaseModel):
    id: str
    """Unique identifier for the metric definition"""

    calculation_type: Literal["FORMULA"] = FieldInfo(alias="calculationType")
    """Metric computed by evaluating an expression over other metrics."""

    description: str
    """Description of what the metric measures"""

    formula: FormulaMetricResponseFormula
    """Formula configuration."""

    metric_id: str = FieldInfo(alias="metricId")
    """Alias of `slug` retained for backwards compatibility. Same value as `slug`."""

    name: str
    """Name of the metric"""

    requires_live_conversation: bool = FieldInfo(alias="requiresLiveConversation")
    """
    True when this metric can only be scored from a live recording
    (`supportedConversationSources` is `["LIVE"]`). Selecting one of these on a
    simulation run forces live enrichment: the run waits for your recording and, if
    none arrives, the metric produces no value. Check this before a run rather than
    discovering the wait afterwards.
    """

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

    supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] = FieldInfo(alias="supportedContexts")
    """Which levels this metric can produce values at"""

    supported_conversation_sources: Optional[List[Literal["SIMULATED", "LIVE"]]] = FieldInfo(
        alias="supportedConversationSources"
    )
    """
    Which kinds of conversation this metric can be scored on. `null` means both.
    `["LIVE"]` marks a metric that can only be scored from your own recording of a
    real call, and `["SIMULATED"]` one that only applies to simulations.
    """

    supports_variants: bool = FieldInfo(alias="supportsVariants")
    """
    Whether you can create a variant of this metric with POST
    /v1/metric/definitions/{idOrSlug}/variants. False for threshold metrics (their
    configuration comes from the metric they derive from), for provider-computed
    metrics whose calculation lives in the collector rather than an editable prompt,
    and for metrics in a package that manages its own variants. Most of Roark’s own
    metrics are false, so read this rather than discovering it from a 403.
    """

    type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"]
    """Type of value this metric produces"""

    variant_id: str = FieldInfo(alias="variantId")
    """
    The resolved variant this response reflects (org-scoped Default if the org has
    customized it, otherwise the system Default). Pass this as sourceVariantId when
    building a derived metric off this one to pin the exact config.
    """

    version_id: str = FieldInfo(alias="versionId")
    """
    The variant's current version. Immutable snapshot of the config — editing the
    metric produces a new versionId. Use it to detect config changes.
    """

    unit: Optional[LlmJudgeMetricResponseUnit] = None
    """Unit information if applicable"""


class PatternMetricResponsePatternOutcome(BaseModel):
    operator: Literal[
        "GREATER_THAN", "GREATER_THAN_OR_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUALS", "EQUALS", "NOT_EQUALS"
    ]

    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_participant_role: Optional[Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"]] = (
        FieldInfo(alias="sourceParticipantRole")
    )

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId")

    threshold_value: str = FieldInfo(alias="thresholdValue")

    window_after: Optional[int] = FieldInfo(alias="windowAfter")

    window_before: Optional[int] = FieldInfo(alias="windowBefore")


class PatternMetricResponsePatternTrigger(BaseModel):
    operator: Literal[
        "GREATER_THAN", "GREATER_THAN_OR_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUALS", "EQUALS", "NOT_EQUALS"
    ]

    source_metric_definition_id: str = FieldInfo(alias="sourceMetricDefinitionId")

    source_participant_role: Optional[Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"]] = (
        FieldInfo(alias="sourceParticipantRole")
    )

    source_variant_id: Optional[str] = FieldInfo(alias="sourceVariantId")

    threshold_value: str = FieldInfo(alias="thresholdValue")


class PatternMetricResponsePattern(BaseModel):
    operation: Literal["PATTERN_EXISTS", "PATTERN_COUNT", "OUTCOME_AGGREGATE"]

    outcome: Optional[PatternMetricResponsePatternOutcome]

    trigger_combinator: Optional[Literal["AND", "OR"]] = FieldInfo(alias="triggerCombinator")

    triggers: List[PatternMetricResponsePatternTrigger]

    window_mode: Optional[str] = FieldInfo(alias="windowMode")


class PatternMetricResponse(BaseModel):
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

    pattern: PatternMetricResponsePattern
    """Pattern configuration."""

    requires_live_conversation: bool = FieldInfo(alias="requiresLiveConversation")
    """
    True when this metric can only be scored from a live recording
    (`supportedConversationSources` is `["LIVE"]`). Selecting one of these on a
    simulation run forces live enrichment: the run waits for your recording and, if
    none arrives, the metric produces no value. Check this before a run rather than
    discovering the wait afterwards.
    """

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant"""

    slug: str
    """Stable metric slug (e.g. "call_reason", "customer_satisfaction")"""

    supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] = FieldInfo(alias="supportedContexts")
    """Which levels this metric can produce values at"""

    supported_conversation_sources: Optional[List[Literal["SIMULATED", "LIVE"]]] = FieldInfo(
        alias="supportedConversationSources"
    )
    """
    Which kinds of conversation this metric can be scored on. `null` means both.
    `["LIVE"]` marks a metric that can only be scored from your own recording of a
    real call, and `["SIMULATED"]` one that only applies to simulations.
    """

    supports_variants: bool = FieldInfo(alias="supportsVariants")
    """
    Whether you can create a variant of this metric with POST
    /v1/metric/definitions/{idOrSlug}/variants. False for threshold metrics (their
    configuration comes from the metric they derive from), for provider-computed
    metrics whose calculation lives in the collector rather than an editable prompt,
    and for metrics in a package that manages its own variants. Most of Roark’s own
    metrics are false, so read this rather than discovering it from a 403.
    """

    type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"]
    """Type of value this metric produces"""

    variant_id: str = FieldInfo(alias="variantId")
    """
    The resolved variant this response reflects (org-scoped Default if the org has
    customized it, otherwise the system Default). Pass this as sourceVariantId when
    building a derived metric off this one to pin the exact config.
    """

    version_id: str = FieldInfo(alias="versionId")
    """
    The variant's current version. Immutable snapshot of the config — editing the
    metric produces a new versionId. Use it to detect config changes.
    """

    unit: Optional[LlmJudgeMetricResponseUnit] = None
    """Unit information if applicable"""


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: int

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor")


class MetricListDefinitionsResponse(BaseModel):
    """Cursor-paginated metric definitions available in the project"""

    data: List[
        Union[
            LlmJudgeMetricResponse,
            ProviderMetricResponse,
            ThresholdMetricResponse,
            FormulaMetricResponse,
            PatternMetricResponse,
        ]
    ]

    pagination: Pagination
