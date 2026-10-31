# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberDeleteResponse", "Data"]


class Data(BaseModel):
    """Confirmation that a phone number was released"""

    id: str
    """Phone number ID"""

    released: Literal[True]
    """Always true; the number is gone and rent has stopped"""


class PhoneNumberDeleteResponse(BaseModel):
    data: Data
    """Confirmation that a phone number was released"""
