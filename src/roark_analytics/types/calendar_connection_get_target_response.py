# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CalendarConnectionGetTargetResponse",
    "Data",
    "DataPolicy",
    "DataPolicyHour",
    "DataTargetUnionMember0",
    "DataTargetUnionMember1",
    "DataTargetUnionMember2",
    "DataTargetUnionMember3",
]


class DataPolicyHour(BaseModel):
    """
    One window of the week appointments are offered in. A window that runs past
    midnight is two entries on two weekdays; a day the business is closed is simply
    absent.
    """

    end_minute: int = FieldInfo(alias="endMinute")

    start_minute: int = FieldInfo(alias="startMinute")
    """Minutes from local midnight, in the connection’s timezone."""

    weekday: int
    """ISO weekday: Monday is 1, Sunday is 7."""


class DataPolicy(BaseModel):
    """
    The booking policy Roark applies, for a calendar with no scheduling of its own.
    Null on a scheduling system, which owns its own rules, so this one field says
    which kind of provider you are looking at without matching on the provider name.
    """

    all_day_events_block: bool = FieldInfo(alias="allDayEventsBlock")
    """
    Whether an all-day event closes the day. On by default: a calendar marks all-day
    events free unless their creator says otherwise, so a public holiday entered as
    one would otherwise still be bookable.
    """

    buffer_after_minutes: int = FieldInfo(alias="bufferAfterMinutes")

    buffer_before_minutes: int = FieldInfo(alias="bufferBeforeMinutes")
    """Dead time before an appointment, counted as busy."""

    duration_minutes: int = FieldInfo(alias="durationMinutes")

    horizon_days: int = FieldInfo(alias="horizonDays")
    """How far ahead appointments may be made."""

    hours: List[DataPolicyHour]

    min_notice_minutes: int = FieldInfo(alias="minNoticeMinutes")
    """How soon from now an appointment may be made."""

    slot_interval_minutes: int = FieldInfo(alias="slotIntervalMinutes")
    """
    The grid slots are offered on, measured from each bookable window’s own start
    rather than the hour.
    """


class DataTargetUnionMember0(BaseModel):
    event_type_id: int = FieldInfo(alias="eventTypeId")

    provider: Literal["CAL_COM"]


class DataTargetUnionMember1(BaseModel):
    calendar_id: str = FieldInfo(alias="calendarId")

    provider: Literal["GOOGLE"]

    target_id: str = FieldInfo(alias="targetId")


class DataTargetUnionMember2(BaseModel):
    event_type_uri: str = FieldInfo(alias="eventTypeUri")
    """
    The event type, by URI rather than by id: Calendly names every resource with an
    absolute URL and its own API takes that URL back.
    """

    provider: Literal["CALENDLY"]


class DataTargetUnionMember3(BaseModel):
    go_high_level_calendar: str = FieldInfo(alias="goHighLevelCalendar")
    """The calendar, by its own GoHighLevel id."""

    provider: Literal["GO_HIGH_LEVEL"]

    duration_minutes: Optional[int] = FieldInfo(alias="durationMinutes", default=None)
    """
    The length to book, for a calendar offering the booker a choice. GoHighLevel
    takes it on the availability read, so it decides which slots are offered. Omit
    to use the calendar’s own length.
    """


class Data(BaseModel):
    """
    Something on a connected account an agent can be pointed at: a Cal.com event
    type, or a bookable target on a calendar whose booking policy Roark owns.
    """

    id: str
    """Identifier within this connection. Pass it back to read one target in detail."""

    duration_minutes: Optional[float] = FieldInfo(alias="durationMinutes")
    """How long an appointment runs, when the provider fixes one length."""

    duration_options: List[float] = FieldInfo(alias="durationOptions")
    """
    Other lengths this target offers, when it offers a choice. A calendar tool pins
    one of these with `durationMinutes`; an empty list means the length is not the
    customer’s to choose.
    """

    is_hidden: bool = FieldInfo(alias="isHidden")
    """Hidden on the provider’s own booking page. Still bookable through this API."""

    label: str
    """What the customer called it on the provider."""

    policy: Optional[DataPolicy]
    """
    The booking policy Roark applies, for a calendar with no scheduling of its own.
    Null on a scheduling system, which owns its own rules, so this one field says
    which kind of provider you are looking at without matching on the provider name.
    """

    required_booking_fields: List[str] = FieldInfo(alias="requiredBookingFields")
    """
    What a booking is refused without, as the provider names it (`email`, `name`, or
    a Calendly event type’s own required questions). On Cal.com the attendee object
    itself needs only a name and a timezone, so this is the only place that says
    whether an agent has to collect an email; on Calendly both are always required.
    """

    requires_attendee_email: bool = FieldInfo(alias="requiresAttendeeEmail")
    """
    The common case of the above, lifted out because it decides the agent’s design:
    an agent that cannot collect an email cannot book on a target that demands one.
    """

    requires_confirmation: bool = FieldInfo(alias="requiresConfirmation")
    """
    A human has to accept before it is an appointment. An agent booking one of these
    must say "requested", never "confirmed".
    """

    target: Union[DataTargetUnionMember0, DataTargetUnionMember1, DataTargetUnionMember2, DataTargetUnionMember3]
    """Ready to put on a calendar tool, so nothing has to assemble one by hand."""


class CalendarConnectionGetTargetResponse(BaseModel):
    data: Data
    """
    Something on a connected account an agent can be pointed at: a Cal.com event
    type, or a bookable target on a calendar whose booking policy Roark owns.
    """
