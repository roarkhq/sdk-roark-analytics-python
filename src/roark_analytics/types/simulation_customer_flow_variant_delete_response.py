# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SimulationCustomerFlowVariantDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the variant was deleted"""


class SimulationCustomerFlowVariantDeleteResponse(BaseModel):
    data: Data
