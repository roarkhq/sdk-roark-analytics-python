# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CalendarConnectionStartCalendlyOauthParams"]


class CalendarConnectionStartCalendlyOauthParams(TypedDict, total=False):
    calendar_connection_id: Annotated[Optional[str], PropertyInfo(alias="calendarConnectionId")]
    """
    Reconnect an existing connection instead of creating one: the consent screen
    replaces that connection’s credential in place, so every tool bound to it keeps
    working. Use this when a connection reports `INVALID_CREDENTIALS`. The
    connection’s existing name and timezone are kept, so `label` is ignored when
    this is set.
    """

    label: Optional[str]
    """
    Customer-facing name for the connection, unique within the project. Required
    unless `calendarConnectionId` is set, and decided now because the consent screen
    has nowhere to carry it.
    """

    timezone: Optional[str]
    """
    The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
    Omit to adopt the Calendly account’s own. A fixed offset such as `-08:00` is
    rejected: it does not observe DST.
    """
