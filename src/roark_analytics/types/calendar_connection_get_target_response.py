# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CalendarConnectionGetTargetResponse", "Data", "DataTarget"]


class DataTarget(BaseModel):
    """Ready to put on a calendar tool, so nothing has to assemble one by hand."""

    event_type_id: int = FieldInfo(alias="eventTypeId")

    provider: Literal["CAL_COM"]


class Data(BaseModel):
    """
    Something on a connected account an agent can be pointed at: a Cal.com event
    type today, a Google calendar when that lands.
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

    required_booking_fields: List[str] = FieldInfo(alias="requiredBookingFields")
    """
    Slugs a booking is refused without, as the provider names them (`email`,
    `name`). The attendee object itself needs only a name and a timezone, so this is
    the only place that says whether an agent has to collect an email.
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

    target: DataTarget
    """Ready to put on a calendar tool, so nothing has to assemble one by hand."""


class CalendarConnectionGetTargetResponse(BaseModel):
    data: Data
    """
    Something on a connected account an agent can be pointed at: a Cal.com event
    type today, a Google calendar when that lands.
    """
