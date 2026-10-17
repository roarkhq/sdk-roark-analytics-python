# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SimulationGroupDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the group was deleted"""


class SimulationGroupDeleteResponse(BaseModel):
    data: Data
