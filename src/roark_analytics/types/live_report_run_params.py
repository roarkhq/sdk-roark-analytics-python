# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LiveReportRunParams"]


class LiveReportRunParams(TypedDict, total=False):
    period_end: Annotated[str, PropertyInfo(alias="periodEnd")]
    """ISO 8601 end (exclusive) of a custom window. Requires periodStart."""

    period_start: Annotated[str, PropertyInfo(alias="periodStart")]
    """ISO 8601 start of a custom window. Omit both for the latest closed period."""
