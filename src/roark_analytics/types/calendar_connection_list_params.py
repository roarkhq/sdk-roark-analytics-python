# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CalendarConnectionListParams"]


class CalendarConnectionListParams(TypedDict, total=False):
    provider: Literal["CAL_COM", "GOOGLE", "CALENDLY"]
    """
    Who holds the calendar. CAL_COM is the only provider that can be connected
    today; GOOGLE and CALENDLY are described by `capabilities` but not yet
    connectable.
    """
