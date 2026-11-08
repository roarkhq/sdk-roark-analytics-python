# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomerProfileDeleteResponse", "Data"]


class Data(BaseModel):
    success: bool


class CustomerProfileDeleteResponse(BaseModel):
    data: Data
