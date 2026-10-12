# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SimulationRunGroupDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the run group was deleted"""


class SimulationRunGroupDeleteResponse(BaseModel):
    data: Data
