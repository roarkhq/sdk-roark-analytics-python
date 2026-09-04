# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MetricUpdateDefinitionParams", "ClassificationOption", "ScaleLabel", "Source"]


class ClassificationOption(TypedDict, total=False):
    """Option for classification metrics."""

    description: Required[str]

    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]

    label: Required[str]


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


class Source(TypedDict, total=False):
    source_metric_definition_id: Required[Annotated[str, PropertyInfo(alias="sourceMetricDefinitionId")]]
    """ID of a metric referenced in the formula"""

    source_variant_id: Annotated[str, PropertyInfo(alias="sourceVariantId")]
    """Variant of the source metric to use"""


class MetricUpdateDefinitionParams(TypedDict, total=False):
    analysis_package_id: Annotated[object, PropertyInfo(alias="analysisPackageId")]

    boolean_false_label: Annotated[str, PropertyInfo(alias="booleanFalseLabel")]
    """New label for the false case (BOOLEAN output only)"""

    boolean_true_label: Annotated[str, PropertyInfo(alias="booleanTrueLabel")]
    """New label for the true case (BOOLEAN output only)"""

    calc_type: Annotated[object, PropertyInfo(alias="calcType")]

    change_reason: Annotated[str, PropertyInfo(alias="changeReason")]
    """Optional free-text audit note recorded on the new version."""

    classification_options: Annotated[Iterable[ClassificationOption], PropertyInfo(alias="classificationOptions")]
    """Replacement set of classification options (CLASSIFICATION output only)"""

    formula: str
    """
    New formula expression (FORMULA only). Pass `sources` alongside if the
    referenced metrics change.
    """

    llm_prompt: Annotated[str, PropertyInfo(alias="llmPrompt")]
    """New LLM prompt (only for LLM_JUDGE metrics whose prompt is editable)"""

    max_classifications: Annotated[int, PropertyInfo(alias="maxClassifications")]
    """New maximum number of classifications (CLASSIFICATION output only)"""

    metric_id: Annotated[object, PropertyInfo(alias="metricId")]

    name: str
    """New name (only for metrics whose name is editable)"""

    organization_id: Annotated[object, PropertyInfo(alias="organizationId")]

    output_type: Annotated[object, PropertyInfo(alias="outputType")]

    participant_role: Annotated[object, PropertyInfo(alias="participantRole")]

    project_id: Annotated[object, PropertyInfo(alias="projectId")]

    scale_labels: Annotated[Iterable[ScaleLabel], PropertyInfo(alias="scaleLabels")]
    """Replacement set of scale-range labels (SCALE output only)"""

    scale_max: Annotated[int, PropertyInfo(alias="scaleMax")]
    """New scale maximum (SCALE output only)"""

    scale_min: Annotated[int, PropertyInfo(alias="scaleMin")]
    """New scale minimum (SCALE output only)"""

    scope: object

    slug: object

    source: object

    sources: Iterable[Source]
    """
    Replacement formula sources, required when `formula` changes the referenced
    metrics (FORMULA only).
    """

    supported_contexts: Annotated[List[Literal["CALL", "SEGMENT", "TURN"]], PropertyInfo(alias="supportedContexts")]
    """Replacement set of supported contexts. Omit to leave unchanged."""

    supports_multiple_variants: Annotated[object, PropertyInfo(alias="supportsMultipleVariants")]

    tool_definition_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="toolDefinitionIds")]
    """
    Replacement set of scoped tool-definition ids (only for metrics whose tool
    scoping is editable)
    """
