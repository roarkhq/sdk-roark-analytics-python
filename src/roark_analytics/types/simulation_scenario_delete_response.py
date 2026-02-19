# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SimulationScenarioDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the scenario was deleted"""


class SimulationScenarioDeleteResponse(BaseModel):
    data: Data
