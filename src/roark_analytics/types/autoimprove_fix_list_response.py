# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .autoimprove_fix import AutoimproveFix

__all__ = ["AutoimproveFixListResponse"]


class AutoimproveFixListResponse(BaseModel):
    data: List[AutoimproveFix]
