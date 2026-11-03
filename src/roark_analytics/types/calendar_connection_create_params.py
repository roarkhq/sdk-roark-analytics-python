# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CalendarConnectionCreateParams"]


class CalendarConnectionCreateParams(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """
    For CAL_COM: a Cal.com API key (starts with `cal_`). It is verified against
    Cal.com before anything is stored, so an invalid key is a 400 and no connection
    is created. Stored encrypted and never returned.
    """

    label: Required[str]
    """Customer-facing name for this account, unique within the project. Required."""

    provider: Required[Literal["CAL_COM", "GOOGLE", "CALENDLY"]]
    """
    Who holds the calendar. CAL_COM is the only provider that can be connected
    today; GOOGLE and CALENDLY are described by `capabilities` but not yet
    connectable.
    """

    timezone: Optional[str]
    """
    The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
    Omit to adopt the provider account’s own timezone. A fixed offset such as
    `-08:00` is rejected: it does not observe DST.
    """
