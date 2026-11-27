# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CalendarConnectionUpdateTargetParams", "Hour"]


class Hour(TypedDict, total=False):
    """
    One window of the week appointments are offered in. A window that runs past
    midnight is two entries on two weekdays; a day the business is closed is simply
    absent.
    """

    end_minute: Required[Annotated[int, PropertyInfo(alias="endMinute")]]

    start_minute: Required[Annotated[int, PropertyInfo(alias="startMinute")]]
    """Minutes from local midnight, in the connection’s timezone."""

    weekday: Required[int]
    """ISO weekday: Monday is 1, Sunday is 7."""


class CalendarConnectionUpdateTargetParams(TypedDict, total=False):
    connection_id: Required[Annotated[str, PropertyInfo(alias="connectionId")]]

    all_day_events_block: Annotated[Optional[bool], PropertyInfo(alias="allDayEventsBlock")]
    """
    Whether an all-day event closes the day. Defaults to true, because a calendar
    marks all-day events free unless their creator says otherwise and a public
    holiday entered as one would otherwise be bookable.
    """

    buffer_after_minutes: Annotated[Optional[int], PropertyInfo(alias="bufferAfterMinutes")]

    buffer_before_minutes: Annotated[Optional[int], PropertyInfo(alias="bufferBeforeMinutes")]
    """
    Dead time before an appointment, counted as busy when a slot is offered.
    Defaults to 0.
    """

    duration_minutes: Annotated[int, PropertyInfo(alias="durationMinutes")]

    horizon_days: Annotated[Optional[int], PropertyInfo(alias="horizonDays")]
    """How far ahead appointments may be made. Defaults to 30."""

    hours: Optional[Iterable[Hour]]
    """
    The windows of the week appointments are offered in. Omit to adopt Monday to
    Friday, 09:00 to 17:00. A target with no windows offers nothing at all, which
    reads to a caller as a permanently full diary.
    """

    min_notice_minutes: Annotated[Optional[int], PropertyInfo(alias="minNoticeMinutes")]
    """How soon from now an appointment may be made. Defaults to 120."""

    name: str
    """
    Unique within the connection, and how a config file refers to this target.
    Letters, digits, spaces, _ or -.
    """

    slot_interval_minutes: Annotated[Optional[int], PropertyInfo(alias="slotIntervalMinutes")]
    """
    The grid slots are offered on. Defaults to the duration, which gives
    back-to-back appointments.
    """
