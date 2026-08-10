# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationCustomerFlowVariantCreateParams"]


class SimulationCustomerFlowVariantCreateParams(TypedDict, total=False):
    title: Required[str]

    environment_id: Annotated[Optional[str], PropertyInfo(alias="environmentId")]

    is_default: Annotated[bool, PropertyInfo(alias="isDefault")]

    persona_id: Annotated[Optional[str], PropertyInfo(alias="personaId")]

    preceded_by_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="precededByCustomerFlowId")]

    preceded_by_customer_flow_variant_id: Annotated[
        Optional[str], PropertyInfo(alias="precededByCustomerFlowVariantId")
    ]

    prompt: Optional[str]
