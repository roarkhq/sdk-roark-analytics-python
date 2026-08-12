# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerFlowEdgeCaseUpdateParams", "AdditionalExpectation"]


class CustomerFlowEdgeCaseUpdateParams(TypedDict, total=False):
    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]

    additional_expectations: Annotated[Iterable[AdditionalExpectation], PropertyInfo(alias="additionalExpectations")]
    """Replaces the expectations that apply to this variant on top of the flow's.

    Omit to leave them alone, send [] to clear. Improv flows only: a scripted
    variant's expectations come from the agent turns on its path and are rewritten
    on the next graph edit.
    """

    environment_id: Annotated[Optional[str], PropertyInfo(alias="environmentId")]

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """The persona this runs as. Null on an edge case inherits the happy path's."""

    preceded_by_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="precededByCustomerFlowId")]

    preceded_by_customer_flow_variant_id: Annotated[
        Optional[str], PropertyInfo(alias="precededByCustomerFlowVariantId")
    ]

    prompt: Optional[str]

    title: str


class AdditionalExpectation(TypedDict, total=False):
    prompt: Required[str]
    """What the agent under test is graded against."""
