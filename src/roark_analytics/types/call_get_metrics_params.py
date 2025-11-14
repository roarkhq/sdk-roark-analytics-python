# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CallGetMetricsParams"]


class CallGetMetricsParams(TypedDict, total=False):
    flatten: str
    """
    Whether to return a flat list instead of grouped by metric definition (default:
    false)
    """
