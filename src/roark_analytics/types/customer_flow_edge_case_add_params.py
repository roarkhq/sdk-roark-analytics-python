# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerFlowEdgeCaseAddParams"]


class CustomerFlowEdgeCaseAddParams(TypedDict, total=False):
    title: Required[str]

    environment_id: Annotated[Optional[str], PropertyInfo(alias="environmentId")]

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """The persona this runs as. Omit to inherit the happy path's."""

    preceded_by_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="precededByCustomerFlowId")]

    preceded_by_customer_flow_variant_id: Annotated[
        Optional[str], PropertyInfo(alias="precededByCustomerFlowVariantId")
    ]

    prompt: Optional[str]
