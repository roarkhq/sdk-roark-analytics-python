# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SimulationCustomerFlowDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the flow was deleted"""


class SimulationCustomerFlowDeleteResponse(BaseModel):
    data: Data
