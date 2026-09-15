# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BenchmarkListTargetScoreSamplesParams"]


class BenchmarkListTargetScoreSamplesParams(TypedDict, total=False):
    suite: Required[str]

    condition_key: Annotated[str, PropertyInfo(alias="conditionKey")]

    limit: int
    """Maximum number of records to return (default: 20, max: 100)"""

    metric_key: Annotated[str, PropertyInfo(alias="metricKey")]

    offset: int
    """Pagination offset"""

    suite_version: Annotated[str, PropertyInfo(alias="suiteVersion")]
