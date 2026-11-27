# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CalendarConnectionDeleteTargetResponse", "Data"]


class Data(BaseModel):
    id: str
    """Identifier of the deleted target."""

    deleted: Literal[True]


class CalendarConnectionDeleteTargetResponse(BaseModel):
    data: Data
