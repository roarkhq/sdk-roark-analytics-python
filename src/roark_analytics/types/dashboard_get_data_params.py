# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DashboardGetDataParams"]


class DashboardGetDataParams(TypedDict, total=False):
    from_: Annotated[str, PropertyInfo(alias="from")]
    """ISO 8601 start. Overrides the saved window; without `to`, runs until now."""

    timezone: str
    """IANA zone buckets and calendar periods align to. Default UTC."""

    to: str
    """ISO 8601 end. Requires `from`."""
