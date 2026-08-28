# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MetricCreateDefinitionParams",
    "FormulaMetricInput",
    "FormulaMetricInputSource",
    "PatternMetricInput",
    "PatternMetricInputOutcome",
    "PatternMetricInputTrigger",
    "PromptMetricInput",
    "PromptMetricInputClassificationOption",
    "PromptMetricInputScaleLabel",
]


class PromptMetricInputClassificationOption(TypedDict, total=False):
    """Option for classification metrics."""

    description: Required[str]

    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]

    label: Required[str]


class PromptMetricInputScaleLabel(TypedDict, total=False):
    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]
    """Display order of this label"""

    label: Required[str]
    """Label for this range"""

    range_max: Required[Annotated[float, PropertyInfo(alias="rangeMax")]]
    """Maximum value for this label range"""

    range_min: Required[Annotated[float, PropertyInfo(alias="rangeMin")]]
    """Minimum value for this label range"""

    color_hex: Annotated[str, PropertyInfo(alias="colorHex")]
    """Hex color code for this label (e.g. "#FF0000")"""

    description: str
    """Description of what this range means"""


class PromptMetricInput(TypedDict, total=False):
    calculation_type: Required[Annotated[Literal["LLM_JUDGE"], PropertyInfo(alias="calculationType")]]
    """LLM-evaluated metric."""

    name: Required[str]
    """Name of the metric"""

    output_type: Required[
        Annotated[
            Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"],
            PropertyInfo(alias="outputType"),
        ]
    ]
    """Type of value this metric produces"""

    analysis_package_id: Annotated[str, PropertyInfo(alias="analysisPackageId")]
    """
    ID of the analysis package to add this metric to. Optional: when omitted, the
    metric is added to a default "Custom Metrics" package for your project (created
    automatically the first time).
    """

    boolean_false_label: Annotated[str, PropertyInfo(alias="booleanFalseLabel")]
    """Label for the false case (only for BOOLEAN type)"""

    boolean_true_label: Annotated[str, PropertyInfo(alias="booleanTrueLabel")]
    """Label for the true case (only for BOOLEAN type)"""

    classification_options: Annotated[
        Iterable[PromptMetricInputClassificationOption], PropertyInfo(alias="classificationOptions")
    ]
    """Options for classification. Required for CLASSIFICATION type."""

    llm_prompt: Annotated[str, PropertyInfo(alias="llmPrompt")]
    """
    LLM prompt/criteria for evaluating this metric. Required for BOOLEAN, NUMERIC,
    TEXT, and SCALE types.
    """

    max_classifications: Annotated[int, PropertyInfo(alias="maxClassifications")]
    """
    Maximum number of classifications that can be selected (only for CLASSIFICATION
    type)
    """

    metric_id: Annotated[str, PropertyInfo(alias="metricId")]
    """
    Alias of `slug` accepted for backwards compatibility. Use `slug` for new
    integrations.
    """

    participant_role: Annotated[
        Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"], PropertyInfo(alias="participantRole")
    ]
    """Participant role to evaluate. Required when scope is PER_PARTICIPANT."""

    scale_labels: Annotated[Iterable[PromptMetricInputScaleLabel], PropertyInfo(alias="scaleLabels")]
    """Labels for scale ranges (only for SCALE type)"""

    scale_max: Annotated[int, PropertyInfo(alias="scaleMax")]
    """Maximum value for scale. Required for SCALE type."""

    scale_min: Annotated[int, PropertyInfo(alias="scaleMin")]
    """Minimum value for scale. Required for SCALE type."""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant (default: GLOBAL)"""

    slug: str
    """Stable slug for the metric. Auto-generated from name if omitted."""

    supported_contexts: Annotated[List[Literal["CALL", "SEGMENT", "TURN"]], PropertyInfo(alias="supportedContexts")]
    """Which levels this metric can produce values at (default: ["CALL"])"""


class FormulaMetricInputSource(TypedDict, total=False):
    source_metric_definition_id: Required[Annotated[str, PropertyInfo(alias="sourceMetricDefinitionId")]]
    """ID of a metric referenced in the formula"""

    source_variant_id: Annotated[str, PropertyInfo(alias="sourceVariantId")]
    """Variant of the source metric to use"""


class FormulaMetricInput(TypedDict, total=False):
    calculation_type: Required[Annotated[Literal["FORMULA"], PropertyInfo(alias="calculationType")]]
    """Metric computed by evaluating a mathematical expression over other metrics."""

    formula: Required[str]
    """
    Formula expression using `{{id:<uuid>}}` references to source metrics. Operators
    depend on output type: +, -, *, / for NUMERIC; ==, !=, >=, <=, >, < for BOOLEAN.
    """

    name: Required[str]
    """Name of the metric"""

    output_type: Required[Annotated[Literal["NUMERIC", "BOOLEAN"], PropertyInfo(alias="outputType")]]
    """
    Output type of the formula. NUMERIC for arithmetic expressions, BOOLEAN for
    comparison expressions.
    """

    sources: Required[Iterable[FormulaMetricInputSource]]
    """Source metrics referenced by the formula. Minimum 2."""

    analysis_package_id: Annotated[str, PropertyInfo(alias="analysisPackageId")]
    """
    ID of the analysis package to add this metric to. Optional: when omitted, the
    metric is added to a default "Custom Metrics" package for your project (created
    automatically the first time).
    """

    metric_id: Annotated[str, PropertyInfo(alias="metricId")]
    """
    Alias of `slug` accepted for backwards compatibility. Use `slug` for new
    integrations.
    """

    slug: str
    """Stable slug for the metric. Auto-generated from name if omitted."""


class PatternMetricInputOutcome(TypedDict, total=False):
    """Outcome condition evaluated within the window relative to the trigger."""

    operator: Required[
        Literal["GREATER_THAN", "GREATER_THAN_OR_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUALS", "EQUALS", "NOT_EQUALS"]
    ]

    source_metric_definition_id: Required[Annotated[str, PropertyInfo(alias="sourceMetricDefinitionId")]]

    threshold_value: Required[Annotated[str, PropertyInfo(alias="thresholdValue")]]

    window_after: Required[Annotated[int, PropertyInfo(alias="windowAfter")]]
    """
    How far after the trigger to look for the outcome (in seconds or segments, see
    windowMode)
    """

    source_participant_role: Annotated[
        Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"],
        PropertyInfo(alias="sourceParticipantRole"),
    ]

    source_variant_id: Annotated[str, PropertyInfo(alias="sourceVariantId")]

    window_before: Annotated[int, PropertyInfo(alias="windowBefore")]
    """How far before the trigger to look for the outcome (default: 0)"""


class PatternMetricInputTrigger(TypedDict, total=False):
    """Single trigger condition. Use either trigger or triggers + triggerCombinator."""

    operator: Required[
        Literal["GREATER_THAN", "GREATER_THAN_OR_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUALS", "EQUALS", "NOT_EQUALS"]
    ]

    source_metric_definition_id: Required[Annotated[str, PropertyInfo(alias="sourceMetricDefinitionId")]]

    threshold_value: Required[Annotated[str, PropertyInfo(alias="thresholdValue")]]

    source_participant_role: Annotated[
        Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"],
        PropertyInfo(alias="sourceParticipantRole"),
    ]

    source_variant_id: Annotated[str, PropertyInfo(alias="sourceVariantId")]


class PatternMetricInput(TypedDict, total=False):
    calculation_type: Required[Annotated[Literal["PATTERN"], PropertyInfo(alias="calculationType")]]
    """
    Metric detecting temporal patterns: a trigger condition followed by an outcome
    within a window.
    """

    name: Required[str]
    """Name of the metric"""

    operation: Required[Literal["PATTERN_EXISTS", "PATTERN_COUNT", "OUTCOME_AGGREGATE"]]
    """
    Pattern operation. PATTERN_EXISTS produces a BOOLEAN; PATTERN_COUNT produces a
    NUMERIC count; OUTCOME_AGGREGATE aggregates a numeric outcome.
    """

    outcome: Required[PatternMetricInputOutcome]
    """Outcome condition evaluated within the window relative to the trigger."""

    analysis_package_id: Annotated[str, PropertyInfo(alias="analysisPackageId")]
    """
    ID of the analysis package to add this metric to. Optional: when omitted, the
    metric is added to a default "Custom Metrics" package for your project (created
    automatically the first time).
    """

    metric_id: Annotated[str, PropertyInfo(alias="metricId")]
    """
    Alias of `slug` accepted for backwards compatibility. Use `slug` for new
    integrations.
    """

    slug: str
    """Stable slug for the metric. Auto-generated from name if omitted."""

    trigger: PatternMetricInputTrigger
    """Single trigger condition. Use either trigger or triggers + triggerCombinator."""

    trigger_combinator: Annotated[Literal["AND", "OR"], PropertyInfo(alias="triggerCombinator")]
    """How to combine multiple triggers. Required when triggers has more than 1 entry."""

    triggers: Iterable[PatternMetricInputTrigger]
    """Multiple trigger conditions. Use with triggerCombinator."""

    window_mode: Annotated[Literal["seconds", "segments"], PropertyInfo(alias="windowMode")]
    """Unit for trigger/outcome window values (default: seconds)"""


MetricCreateDefinitionParams: TypeAlias = Union[PromptMetricInput, FormulaMetricInput, PatternMetricInput]
