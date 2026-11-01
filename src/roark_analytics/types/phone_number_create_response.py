# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PhoneNumberCreateResponse", "Data"]


class Data(BaseModel):
    """A phone number the project owns"""

    id: str
    """Phone number ID"""

    agent_id: Optional[str] = FieldInfo(alias="agentId")
    """The agent the number is assigned to, if any"""

    e164: str
    """The number in E.164 format"""

    is_free: bool = FieldInfo(alias="isFree")
    """Whether the number sits inside the plan free allowance right now"""

    locality_code: Optional[str] = FieldInfo(alias="localityCode")
    """ISO 3166-2 code of the region the number is from, when the carrier gave one"""

    monthly_rent_micros: int = FieldInfo(alias="monthlyRentMicros")
    """What a month of this number costs in micro-dollars; 0 while it is free"""

    name: Optional[str]
    """Label the project gave the number"""

    purchased_at: str = FieldInfo(alias="purchasedAt")
    """When the number was bought (ISO 8601)"""

    rent_next_charge_at: str = FieldInfo(alias="rentNextChargeAt")
    """When the next month of rent is due (ISO 8601)"""


class PhoneNumberCreateResponse(BaseModel):
    data: Data
    """A phone number the project owns"""
