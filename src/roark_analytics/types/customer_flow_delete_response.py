# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomerFlowDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the flow was deleted"""


class CustomerFlowDeleteResponse(BaseModel):
    data: Data
