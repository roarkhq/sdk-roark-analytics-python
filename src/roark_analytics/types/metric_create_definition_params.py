# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetricCreateDefinitionParams", "ClassificationOption", "ScaleLabel"]


class MetricCreateDefinitionParams(TypedDict, total=False):
    analysis_package_id: Required[Annotated[str, PropertyInfo(alias="analysisPackageId")]]
    """ID of the analysis package to add this metric to"""

    name: Required[str]
    """Name of the metric"""

    output_type: Required[
        Annotated[
            Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"],
            PropertyInfo(alias="outputType"),
        ]
    ]
    """Type of value this metric produces"""

    boolean_false_label: Annotated[str, PropertyInfo(alias="booleanFalseLabel")]
    """Label for the false/negative case (only for BOOLEAN type)"""

    boolean_true_label: Annotated[str, PropertyInfo(alias="booleanTrueLabel")]
    """Label for the true/positive case (only for BOOLEAN type)"""

    classification_options: Annotated[Iterable[ClassificationOption], PropertyInfo(alias="classificationOptions")]
    """Options for classification. Required for CLASSIFICATION type."""

    llm_prompt: Annotated[str, PropertyInfo(alias="llmPrompt")]
    """LLM prompt/criteria for evaluating this metric.

    Used to instruct the model on how to score. Required for BOOLEAN, NUMERIC, TEXT,
    and SCALE types.
    """

    max_classifications: Annotated[int, PropertyInfo(alias="maxClassifications")]
    """
    Maximum number of classifications that can be selected (only for CLASSIFICATION
    type)
    """

    metric_id: Annotated[str, PropertyInfo(alias="metricId")]
    """Unique identifier for the metric (e.g.

    "customer_satisfaction"). Auto-generated from name if not provided.
    """

    participant_role: Annotated[
        Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"], PropertyInfo(alias="participantRole")
    ]
    """Participant role to evaluate. Required when scope is PER_PARTICIPANT."""

    scale_labels: Annotated[Iterable[ScaleLabel], PropertyInfo(alias="scaleLabels")]
    """Labels for scale ranges (only for SCALE type)"""

    scale_max: Annotated[int, PropertyInfo(alias="scaleMax")]
    """Maximum value for scale. Required for SCALE type."""

    scale_min: Annotated[int, PropertyInfo(alias="scaleMin")]
    """Minimum value for scale. Required for SCALE type."""

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]
    """Whether metric is global or per-participant (default: GLOBAL)"""

    supported_contexts: Annotated[List[Literal["CALL", "SEGMENT", "TURN"]], PropertyInfo(alias="supportedContexts")]
    """Which levels this metric can produce values at (default: ["CALL"])"""


class ClassificationOption(TypedDict, total=False):
    description: Required[str]
    """Description of what this option means"""

    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]
    """Display order of this option"""

    label: Required[str]
    """Label for this classification option"""


class ScaleLabel(TypedDict, total=False):
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
