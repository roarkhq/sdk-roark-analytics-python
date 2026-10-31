# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PhoneNumberListAvailableParams"]


class PhoneNumberListAvailableParams(TypedDict, total=False):
    area_code: Annotated[str, PropertyInfo(alias="areaCode")]
    """
    Three-digit area code, or a toll-free prefix such as 800. When it has no
    numbers, nearby ones are returned instead, flagged bestEffort.
    """

    contains: str
    """Digits or letters the number must contain (1 to 7, * matches any digit)"""

    country: Literal["US", "CA"]
    """ISO 3166-1 alpha-2 country of the number: US or CA"""

    limit: int
    """Maximum number of results (default: 20, max: 100)"""

    number_type: Annotated[Literal["LOCAL", "TOLL_FREE"], PropertyInfo(alias="numberType")]
    """
    LOCAL for a number in an area code, TOLL_FREE for one from the shared US and
    Canada toll-free pool
    """
