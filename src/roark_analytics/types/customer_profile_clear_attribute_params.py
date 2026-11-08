# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerProfileClearAttributeParams"]


class CustomerProfileClearAttributeParams(TypedDict, total=False):
    customer_profile_id: Required[Annotated[str, PropertyInfo(alias="customerProfileId")]]
