# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DashboardGetWidgetDataParams"]


class DashboardGetWidgetDataParams(TypedDict, total=False):
    dashboard_id: Required[Annotated[str, PropertyInfo(alias="dashboardId")]]

    from_: Annotated[str, PropertyInfo(alias="from")]
    """ISO 8601 start. Overrides the saved window; without `to`, runs until now."""

    timezone: str
    """IANA zone buckets and calendar periods align to. Default UTC."""

    to: str
    """ISO 8601 end. Requires `from`."""
