# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomerDeleteFieldResponse", "Data"]


class Data(BaseModel):
    success: bool


class CustomerDeleteFieldResponse(BaseModel):
    data: Data
