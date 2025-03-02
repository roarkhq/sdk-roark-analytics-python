# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HealthGetResponse", "Data"]


class Data(BaseModel):
    status: Literal["healthy", "degraded", "unhealthy"]

    timestamp: str

    version: str


class HealthGetResponse(BaseModel):
    data: Data
    """Health check response payload"""
