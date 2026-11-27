# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationPhoneNumberListResponse", "Data"]


class Data(BaseModel):
    """A number Roark may place simulation calls from"""

    e164: str
    """The number in E.164 format"""

    locality_code: Optional[str] = FieldInfo(alias="localityCode")
    """ISO 3166-2 code of the region the number is from, when known"""

    reserved_for_project: bool = FieldInfo(alias="reservedForProject")
    """
    True when the number is reserved for this project: only personas that pin it
    call from it. False for the shared pool, which any simulation call may use.
    """


class SimulationPhoneNumberListResponse(BaseModel):
    data: List[Data]
