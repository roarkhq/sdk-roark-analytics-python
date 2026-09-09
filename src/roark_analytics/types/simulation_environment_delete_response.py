# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SimulationEnvironmentDeleteResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier of the deleted environment"""

    deleted: Literal[True]
    """Always true when the environment was deleted"""


class SimulationEnvironmentDeleteResponse(BaseModel):
    data: Data
