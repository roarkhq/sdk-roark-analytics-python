# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SimulationRunPlanDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the run plan was deleted"""


class SimulationRunPlanDeleteResponse(BaseModel):
    data: Data
