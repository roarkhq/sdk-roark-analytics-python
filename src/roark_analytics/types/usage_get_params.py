# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UsageGetParams"]


class UsageGetParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start of the window (inclusive), ISO 8601."""

    to: Required[str]
    """
    End of the window (exclusive), ISO 8601. Must be after `from`, and the window
    may not exceed 366 days.
    """

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Limit the report to a single project. Omit for the whole organization."""
