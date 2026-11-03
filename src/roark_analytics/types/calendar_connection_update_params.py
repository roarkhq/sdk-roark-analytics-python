# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CalendarConnectionUpdateParams"]


class CalendarConnectionUpdateParams(TypedDict, total=False):
    api_key: Annotated[Optional[str], PropertyInfo(alias="apiKey")]
    """
    Rotate the credential. The new key is verified before it is stored, and a
    verified key returns the connection to ACTIVE, which is how a connection
    recovers from INVALID_CREDENTIALS.
    """

    label: Optional[str]
    """Rename the connection."""

    timezone: Optional[str]
    """Change the named IANA timezone slots are offered in."""
