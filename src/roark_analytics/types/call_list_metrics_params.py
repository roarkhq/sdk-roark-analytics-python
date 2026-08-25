# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CallListMetricsParams"]


class CallListMetricsParams(TypedDict, total=False):
    flatten: str
    """
    Whether to return a flat list instead of grouped by metric definition (default:
    false)
    """

    status: Literal["success", "all"]
    """
    Filter metrics by capture status. `success` (default) returns only successfully
    computed metrics — backwards-compatible with the historical behavior. `all` also
    returns NOT_APPLICABLE / DATA_MISSING / ERROR rows (with `value` omitted), so
    clients can distinguish "still computing" from "computed but no value" and exit
    retry loops correctly.
    """
