# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SimulationToolFixtureDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool


class SimulationToolFixtureDeleteResponse(BaseModel):
    data: Data
