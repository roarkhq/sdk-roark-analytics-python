# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BenchmarkGetLeaderboardResponse", "Data", "DataMetric", "DataTarget", "Pagination", "SortedBy"]


class DataMetric(BaseModel):
    """One aggregate cell: a metric measured for one target under one condition"""

    ci_high: Optional[float] = FieldInfo(alias="ciHigh")

    ci_low: Optional[float] = FieldInfo(alias="ciLow")
    """Low bound of the 95% CI of the mean (NUMERIC metrics)."""

    condition_key: str = FieldInfo(alias="conditionKey")
    """
    The flow variant these numbers were measured under. The empty string is the
    overall rollup across all conditions.
    """

    condition_label: str = FieldInfo(alias="conditionLabel")

    mean: Optional[float]

    metric_key: str = FieldInfo(alias="metricKey")
    """Stable metric id, e.g. `response_time`."""

    metric_kind: Literal["NUMERIC", "BOOLEAN"] = FieldInfo(alias="metricKind")
    """
    Which statistics are populated on a result. NUMERIC fills p50/p95/mean/ci;
    BOOLEAN fills passRate and its interval.
    """

    metric_name: str = FieldInfo(alias="metricName")

    n: int
    """Scored samples behind this aggregate."""

    p50: Optional[float]

    p95: Optional[float]

    pass_rate: Optional[float] = FieldInfo(alias="passRate")
    """Fraction passed, 0..1 (BOOLEAN metrics)."""

    pass_rate_ci_high: Optional[float] = FieldInfo(alias="passRateCiHigh")

    pass_rate_ci_low: Optional[float] = FieldInfo(alias="passRateCiLow")
    """Low bound of the 95% Wilson interval on the pass rate."""

    unit_symbol: Optional[str] = FieldInfo(alias="unitSymbol")
    """Display unit for numeric metrics, e.g. `ms`."""


class DataTarget(BaseModel):
    """A model or stack with a published result on a benchmark suite"""

    is_current: bool = FieldInfo(alias="isCurrent")
    """Whether these are the numbers Roark publishes for this target today."""

    iterations: int
    """Calls the sweep requested per condition."""

    publication_id: str = FieldInfo(alias="publicationId")
    """
    Id of this one sweep. Changes every time the target is re-published, so it is a
    render key, not an identity.
    """

    published_at: str = FieldInfo(alias="publishedAt")
    """When this sweep was published (ISO-8601), i.e. data freshness."""

    sample_call_count: int = FieldInfo(alias="sampleCallCount")
    """Executed calls that contributed at least one score to these numbers."""

    suite: str

    suite_version: str = FieldInfo(alias="suiteVersion")

    superseded_at: Optional[str] = FieldInfo(alias="supersededAt")
    """When a later sweep replaced this one. Null means it is the current generation."""

    target_key: str = FieldInfo(alias="targetKey")
    """
    Stable identity of the model/stack across sweeps. Cite this, and pass it to the
    target endpoints.
    """

    target_name: str = FieldInfo(alias="targetName")
    """Human-readable name of the model/stack."""


class Data(BaseModel):
    metrics: List[DataMetric]
    """The projected cells for this row, measured under the requested condition."""

    target: DataTarget
    """A model or stack with a published result on a benchmark suite"""


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: int

    offset: int

    total: int
    """Total matching records, ignoring this page."""


class SortedBy(BaseModel):
    """The ranking this page was produced under"""

    metric_key: str = FieldInfo(alias="metricKey")

    order: Literal["asc", "desc"]


class BenchmarkGetLeaderboardResponse(BaseModel):
    condition_key: str = FieldInfo(alias="conditionKey")

    data: List[Data]

    pagination: Pagination

    sorted_by: SortedBy = FieldInfo(alias="sortedBy")
    """The ranking this page was produced under"""

    suite: str

    suite_version: str = FieldInfo(alias="suiteVersion")
    """The version actually read, after defaulting."""
