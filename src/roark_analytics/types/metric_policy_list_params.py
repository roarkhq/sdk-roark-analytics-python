# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MetricPolicyListParams"]


class MetricPolicyListParams(TypedDict, total=False):
    after: str
    """Cursor for pagination - use the nextCursor value from a previous response"""

    limit: int
    """Maximum number of policies to return (default: 20, max: 50)"""

    status: Literal["ACTIVE", "INACTIVE"]
    """Filter by policy status"""
