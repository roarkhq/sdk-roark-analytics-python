# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PhoneNumberListAvailableResponse", "Data"]


class Data(BaseModel):
    """A number the carrier has for sale"""

    best_effort: bool = FieldInfo(alias="bestEffort")
    """
    True when the area code asked for had no numbers and the carrier offered this
    nearby one instead
    """

    e164: str
    """The number in E.164 format"""

    locality: Optional[str]
    """Locality the carrier lists, e.g. a city"""

    region: Optional[str]
    """Region the carrier lists, e.g. a state code"""


class PhoneNumberListAvailableResponse(BaseModel):
    data: List[Data]
