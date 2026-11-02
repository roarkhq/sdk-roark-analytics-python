# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LiveReportListParams"]


class LiveReportListParams(TypedDict, total=False):
    limit: int
    """Page size, at most 100."""

    offset: int
