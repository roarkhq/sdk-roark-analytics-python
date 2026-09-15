# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BenchmarkGetLeaderboardParams"]


class BenchmarkGetLeaderboardParams(TypedDict, total=False):
    suite: Required[str]

    condition_key: Annotated[str, PropertyInfo(alias="conditionKey")]

    limit: int
    """Maximum number of records to return (default: 20, max: 100)"""

    metrics: str
    """Comma-separated metric keys to project per row. Defaults to the headline set."""

    offset: int
    """Pagination offset"""

    order: Literal["asc", "desc"]

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]

    suite_version: Annotated[str, PropertyInfo(alias="suiteVersion")]
