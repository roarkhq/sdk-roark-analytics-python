# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BenchmarkListTargetHistoryParams"]


class BenchmarkListTargetHistoryParams(TypedDict, total=False):
    suite: Required[str]

    limit: int
    """Maximum number of records to return (default: 20, max: 100)"""

    offset: int
    """Pagination offset"""

    suite_version: Annotated[str, PropertyInfo(alias="suiteVersion")]
