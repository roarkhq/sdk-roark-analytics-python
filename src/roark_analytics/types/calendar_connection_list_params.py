# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CalendarConnectionListParams"]


class CalendarConnectionListParams(TypedDict, total=False):
    provider: Literal["CAL_COM", "GOOGLE", "CALENDLY", "GO_HIGH_LEVEL"]
    """
    Who holds the calendar. CAL_COM and GO_HIGH_LEVEL are connected with a key,
    GO_HIGH_LEVEL also needing the sub-account the key belongs to; GOOGLE and
    CALENDLY are connected by consent, through `POST
    /v1/connections/calendar/google/authorize-url` and `POST
    /v1/connections/calendar/calendly/authorize-url`.
    """
