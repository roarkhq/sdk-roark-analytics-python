# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CalendarConnectionListCalendarsResponse", "Data"]


class Data(BaseModel):
    """A calendar on the connected account that a bookable target can be created on."""

    id: str
    """Pass this as `calendarId` when creating a target."""

    can_write: bool = FieldInfo(alias="canWrite")
    """Always true: a calendar that cannot be written to is not listed."""

    is_primary: bool = FieldInfo(alias="isPrimary")

    label: str
    """What the calendar is called on the account."""

    timezone: Optional[str]
    """The calendar’s own timezone, when it reports one."""


class CalendarConnectionListCalendarsResponse(BaseModel):
    data: List[Data]
