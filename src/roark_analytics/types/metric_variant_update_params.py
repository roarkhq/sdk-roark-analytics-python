# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetricVariantUpdateParams"]


class MetricVariantUpdateParams(TypedDict, total=False):
    id_or_slug: Required[Annotated[str, PropertyInfo(alias="idOrSlug")]]

    boolean_false_label: Annotated[str, PropertyInfo(alias="booleanFalseLabel")]
    """
    What a `false` value means. Given to the judge as its polarity rule, so keep it
    accurate.
    """

    boolean_true_label: Annotated[str, PropertyInfo(alias="booleanTrueLabel")]
    """
    What a `true` value means. Given to the judge as its polarity rule, so keep it
    accurate.
    """

    change_reason: Annotated[str, PropertyInfo(alias="changeReason")]
    """Free-text audit note recorded on the new version."""

    grades_short_calls: Annotated[bool, PropertyInfo(alias="gradesShortCalls")]
    """
    Score this metric on a simulated call with fewer than 4 transcript lines or
    where your agent never spoke (custom metrics only, not ones that judge the
    audio). Such calls skip every other metric. Default false.
    """

    llm_prompt: Annotated[str, PropertyInfo(alias="llmPrompt")]
    """The rubric this variant applies. LLM judge metrics only."""

    max_classifications: Annotated[int, PropertyInfo(alias="maxClassifications")]
    """Maximum classifications returned. CLASSIFICATION output only."""

    name: str
    """
    Rename the variant. Does not change its configuration, so `versionId` is
    unaffected. `Default` is reserved.
    """

    scale_max: Annotated[int, PropertyInfo(alias="scaleMax")]
    """Scale maximum. SCALE output only."""

    scale_min: Annotated[int, PropertyInfo(alias="scaleMin")]
    """Scale minimum. SCALE output only."""
