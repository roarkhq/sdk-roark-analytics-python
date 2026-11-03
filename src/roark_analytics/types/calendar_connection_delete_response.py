# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CalendarConnectionDeleteResponse", "Data"]


class Data(BaseModel):
    id: str
    """Identifier of the deleted connection."""

    deleted: Literal[True]
    """Always true. The credential is hard-deleted, not archived."""


class CalendarConnectionDeleteResponse(BaseModel):
    data: Data
