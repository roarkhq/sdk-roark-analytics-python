# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BenchmarkListMetricsResponse", "Data"]


class Data(BaseModel):
    """A metric a suite version published, and the direction that counts as better"""

    goal: Literal["higher", "lower", "neutral"]
    """
    Which end of the scale is better. `higher` and `lower` can be ranked; `neutral`
    is an observational metric that describes a conversation rather than grading it,
    so sorting on it names no winner.
    """

    metric_key: str = FieldInfo(alias="metricKey")

    metric_kind: Literal["NUMERIC", "BOOLEAN"] = FieldInfo(alias="metricKind")
    """
    Which statistics are populated on a result. NUMERIC fills p50/p95/mean/ci;
    BOOLEAN fills passRate and its interval.
    """

    metric_name: str = FieldInfo(alias="metricName")

    unit_symbol: Optional[str] = FieldInfo(alias="unitSymbol")


class BenchmarkListMetricsResponse(BaseModel):
    data: List[Data]

    suite: str

    suite_version: str = FieldInfo(alias="suiteVersion")
