# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationGetJobParams"]


class SimulationGetJobParams(TypedDict, total=False):
    phone_number: Required[Annotated[object, PropertyInfo(alias="phoneNumber")]]
    """Customer phone number in E.164 format"""

    roark_phone_number: Required[Annotated[object, PropertyInfo(alias="roarkPhoneNumber")]]
    """Roark-assigned phone number in E.164 format"""

    timestamp: object
    """ISO 8601 timestamp to check for active lease (defaults to current time)"""
