# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallBatchDeleteResponse", "Data"]


class Data(BaseModel):
    deleted_call_ids: List[str] = FieldInfo(alias="deletedCallIds")
    """Calls this request deleted"""

    not_found_call_ids: List[str] = FieldInfo(alias="notFoundCallIds")
    """
    Requested calls that were not deleted because they do not exist in this project
    or were already deleted
    """


class CallBatchDeleteResponse(BaseModel):
    data: Data
