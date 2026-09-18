# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AutoimproveFixCancelResponse", "Data"]


class Data(BaseModel):
    accepted: Literal[True]


class AutoimproveFixCancelResponse(BaseModel):
    data: Data
