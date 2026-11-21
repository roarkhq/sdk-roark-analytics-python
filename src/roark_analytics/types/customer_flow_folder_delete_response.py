# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomerFlowFolderDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the folder was deleted"""


class CustomerFlowFolderDeleteResponse(BaseModel):
    data: Data
