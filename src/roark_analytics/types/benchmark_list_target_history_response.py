# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BenchmarkListTargetHistoryResponse", "Data", "Pagination"]


class Data(BaseModel):
    """One published sweep of a target, current or superseded — an entry in its history"""

    is_current: bool = FieldInfo(alias="isCurrent")
    """Whether this is the generation the other endpoints return."""

    iterations: int

    publication_id: str = FieldInfo(alias="publicationId")

    published_at: str = FieldInfo(alias="publishedAt")

    sample_call_count: int = FieldInfo(alias="sampleCallCount")

    suite: str

    suite_version: str = FieldInfo(alias="suiteVersion")

    superseded_at: Optional[str] = FieldInfo(alias="supersededAt")
    """When a later sweep replaced this generation. Null means it is the current one."""

    target_key: str = FieldInfo(alias="targetKey")

    target_name: str = FieldInfo(alias="targetName")


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: int

    offset: int

    total: int
    """Total matching records, ignoring this page."""


class BenchmarkListTargetHistoryResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
