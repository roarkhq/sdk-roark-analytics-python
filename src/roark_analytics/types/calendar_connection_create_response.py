# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CalendarConnectionCreateResponse", "Data", "DataCapability"]


class DataCapability(BaseModel):
    """
    What a calendar provider can actually do. Read this before configuring a
    calendar tool.
    """

    auth: Literal["API_KEY", "OAUTH"]
    """How this provider is authenticated."""

    availability_window_days: Optional[float] = FieldInfo(alias="availabilityWindowDays")
    """
    Hard cap on the width of one availability query, in days, when the provider has
    one.
    """

    operations: List[Literal["CHECK_AVAILABILITY", "BOOK", "LOOKUP_BOOKING", "RESCHEDULE", "CANCEL", "LIST_BOOKINGS"]]
    """
    The operations this provider supports. An operation that is absent is never
    registered as a tool, so the agent cannot promise it: Calendly, for example, has
    no reschedule API, and callers wanting to move an appointment must cancel and
    rebook.
    """

    requires_attendee_email: bool = FieldInfo(alias="requiresAttendeeEmail")
    """
    Whether a booking cannot be created without an attendee email address. True for
    every scheduling system, which decides how an agent has to identify the caller.
    """

    roark_owns_booking_policy: bool = FieldInfo(alias="roarkOwnsBookingPolicy")
    """
    True for a raw calendar, which exposes only events and free/busy. Roark then
    owns bookable hours, duration, buffers, lead time and horizon, because the
    provider has no notion of them.
    """

    slot_hold: Literal["RESERVATION", "NONE"] = FieldInfo(alias="slotHold")
    """
    Whether a slot can be held before committing. RESERVATION blocks other bookers
    in the provider’s own UI but is not consumed by the booking that follows, so it
    is a courtesy and not a guarantee.
    """


class Data(BaseModel):
    """
    A project’s credential for one calendar account, the thing a calendar tool books
    against. The credential itself is never returned.
    """

    id: str
    """Unique identifier of the calendar connection."""

    account_label: Optional[str] = FieldInfo(alias="accountLabel")
    """How the provider names the connected account (a Cal.com email). Read-only."""

    capabilities: DataCapability
    """
    What a calendar provider can actually do. Read this before configuring a
    calendar tool.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format."""

    credential_expires_at: Optional[str] = FieldInfo(alias="credentialExpiresAt")
    """When the credential expires, ISO 8601. Null when it does not expire."""

    label: str
    """Customer-supplied name for this account. Unique within the project."""

    last_checked_at: Optional[str] = FieldInfo(alias="lastCheckedAt")
    """When the credential was last verified against the provider, ISO 8601."""

    provider: Literal["CAL_COM", "GOOGLE", "CALENDLY"]
    """
    Who holds the calendar. CAL_COM is the only provider that can be connected
    today; GOOGLE and CALENDLY are described by `capabilities` but not yet
    connectable.
    """

    scopes: Optional[List[str]]
    """
    Scopes the credential carries, when the provider issues scoped credentials. Null
    for an API key.
    """

    status: Literal["ACTIVE", "INVALID_CREDENTIALS", "ERROR"]
    """
    Whether the stored credential still works, as of `lastCheckedAt`.
    INVALID_CREDENTIALS means the provider rejected it and the connection needs a
    new one. A provider outage never changes this.
    """

    status_message: Optional[str] = FieldInfo(alias="statusMessage")
    """Why the status is not ACTIVE, in the provider’s words. Null when ACTIVE."""

    timezone: str
    """
    The IANA timezone slots are offered in: the business’s, not the caller’s. A
    clinic’s 3pm is 3pm whoever dials it.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format."""


class CalendarConnectionCreateResponse(BaseModel):
    data: Data
    """
    A project’s credential for one calendar account, the thing a calendar tool books
    against. The credential itself is never returned.
    """
