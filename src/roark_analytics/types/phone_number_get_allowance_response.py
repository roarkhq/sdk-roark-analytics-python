# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PhoneNumberGetAllowanceResponse", "Data"]


class Data(BaseModel):
    """
    How many numbers the organization gets for free and whether it may buy the next
    one
    """

    blocked_reason: Optional[
        Literal["PAYMENT_METHOD_REQUIRED", "INSUFFICIENT_CREDITS", "SPEND_CAP_REACHED", "PLAN_LIMIT_REACHED"]
    ] = FieldInfo(alias="blockedReason")
    """Why a purchase would be refused; null when canPurchase is true"""

    can_purchase: bool = FieldInfo(alias="canPurchase")
    """Whether a purchase would be admitted right now"""

    free_limit: int = FieldInfo(alias="freeLimit")
    """Numbers included at no charge"""

    is_overridden: bool = FieldInfo(alias="isOverridden")
    """True when the free allowance comes from a per-organization override"""

    monthly_rent_micros: int = FieldInfo(alias="monthlyRentMicros")
    """What one paid number costs a month, in micro-dollars"""

    next_is_free: bool = FieldInfo(alias="nextIsFree")
    """Whether the next number would be free"""

    paid_count: int = FieldInfo(alias="paidCount")
    """How many of those sit outside the free allowance"""

    plan: Literal["PAYG", "TEAM", "ENTERPRISE"]
    """The billing plan the allowance comes from"""

    used: int
    """Numbers the organization holds right now"""


class PhoneNumberGetAllowanceResponse(BaseModel):
    data: Data
    """
    How many numbers the organization gets for free and whether it may buy the next
    one
    """
