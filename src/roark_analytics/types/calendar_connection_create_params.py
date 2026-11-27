# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CalendarConnectionCreateParams"]


class CalendarConnectionCreateParams(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """
    The provider account’s API key. For CAL_COM, a Cal.com API key (starts with
    `cal_`). For GO_HIGH_LEVEL, a sub-account Private Integration Token, which must
    carry the `calendars.readonly`, `calendars/events.readonly`,
    `calendars/events.write`, `contacts.readonly`, `contacts.write` and
    `locations.readonly` scopes. It is verified against the provider before anything
    is stored, so an invalid key is a 400 and no connection is created. Stored
    encrypted and never returned.
    """

    label: Required[str]
    """Customer-facing name for this account, unique within the project. Required."""

    provider: Required[Literal["CAL_COM", "GOOGLE", "CALENDLY", "GO_HIGH_LEVEL"]]
    """
    Who holds the calendar. CAL_COM and GO_HIGH_LEVEL are connected with a key,
    GO_HIGH_LEVEL also needing the sub-account the key belongs to; GOOGLE and
    CALENDLY are connected by consent, through `POST
    /v1/connections/calendar/google/authorize-url` and `POST
    /v1/connections/calendar/calendly/authorize-url`.
    """

    go_high_level_location: Annotated[Optional[str], PropertyInfo(alias="goHighLevelLocation")]
    """
    Required for GO_HIGH_LEVEL and ignored by every other provider: the sub-account
    the token belongs to, for example `ve9EPM428h8vShlRW1KT`. A Private Integration
    Token does not name its own sub-account and every calendar call needs one, so
    the two are stored and verified together: a token minted in a different
    sub-account is a 400.
    """

    timezone: Optional[str]
    """
    The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
    Omit to adopt the provider account’s own timezone. A fixed offset such as
    `-08:00` is rejected: it does not observe DST.
    """
