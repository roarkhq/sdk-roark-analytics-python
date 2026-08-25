# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomerFlowEdgeCaseRemoveResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the variant was deleted"""


class CustomerFlowEdgeCaseRemoveResponse(BaseModel):
    data: Data
