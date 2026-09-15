# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BenchmarkListTargetScoreSamplesResponse", "Data", "Pagination", "Target"]


class Data(BaseModel):
    """
    One un-aggregated score behind a result cell, with the reasoning that produced
    it
    """

    boolean_value: Optional[bool] = FieldInfo(alias="booleanValue")

    condition_key: str = FieldInfo(alias="conditionKey")

    metric_key: str = FieldInfo(alias="metricKey")

    numeric_value: Optional[float] = FieldInfo(alias="numericValue")

    reasoning: str
    """The scorer's rationale for this individual score."""

    source_call_id: str = FieldInfo(alias="sourceCallId")
    """
    Opaque id of the call this single score came from. Groups samples that share a
    call; it is not resolvable through this API.
    """


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: int

    offset: int

    total: int
    """Total matching records, ignoring this page."""


class Target(BaseModel):
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


class BenchmarkListTargetScoreSamplesResponse(BaseModel):
    data: List[Data]

    pagination: Pagination

    target: Target
    """A model or stack with a published result on a benchmark suite"""
