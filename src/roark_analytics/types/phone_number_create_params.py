# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PhoneNumberCreateParams", "AutoPick"]


class AutoPick(TypedDict, total=False):
    """
    What the number Roark picks should look like. Roark buys the first matching
    number the carrier will sell, preferring the area code and falling back to a
    nearby one.
    """

    area_code: Annotated[str, PropertyInfo(alias="areaCode")]
    """
    Three-digit area code, or a toll-free prefix such as 800. When it has no
    numbers, nearby ones are returned instead, flagged bestEffort.
    """

    contains: str
    """Digits or letters the number must contain (1 to 7, * matches any digit)"""

    country: Literal["US", "CA"]
    """ISO 3166-1 alpha-2 country of the number: US or CA"""

    number_type: Annotated[Literal["LOCAL", "TOLL_FREE"], PropertyInfo(alias="numberType")]
    """
    LOCAL for a number in an area code, TOLL_FREE for one from the shared US and
    Canada toll-free pool
    """


class PhoneNumberCreateParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """The agent to assign the number to"""

    auto_pick: Annotated[AutoPick, PropertyInfo(alias="autoPick")]
    """Let Roark pick a matching number instead of naming one. Give this or e164."""

    country: Literal["US", "CA"]
    """
    The country of the number given by e164 (default: US). An auto-picked number
    uses autoPick.country.
    """

    e164: str
    """The number to buy, in E.164 format, from a search result. Give this or autoPick."""

    expect_free: Annotated[bool, PropertyInfo(alias="expectFree")]
    """
    Whether you expect this number to be free (from the allowance). The purchase is
    refused with 409 if that has changed since you checked.
    """

    expect_monthly_rent_micros: Annotated[int, PropertyInfo(alias="expectMonthlyRentMicros")]
    """
    The monthly rent you expect for a paid number, in micros (from the allowance).
    The purchase is refused with 409 if that has changed since you checked.
    """

    name: str
    """A label for the number"""
