# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationEnvironmentGetByIDResponse", "Data"]


class Data(BaseModel):
    """
    A simulation environment: the ambient conditions a customer flow variant runs under. Environments with source SYSTEM are curated by Roark and shared across every project.
    """

    id: str

    background_noise: Literal[
        "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
    ] = FieldInfo(alias="backgroundNoise")

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    name: str

    source: Literal["SYSTEM", "CUSTOM"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    description: Optional[str] = None

    system_key: Optional[str] = FieldInfo(alias="systemKey", default=None)


class SimulationEnvironmentGetByIDResponse(BaseModel):
    data: Data
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. Environments with source SYSTEM are curated by Roark and shared across
    every project.
    """
