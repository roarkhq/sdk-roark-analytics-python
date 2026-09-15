# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BenchmarkListSuitesResponse", "Data"]


class Data(BaseModel):
    """A benchmark suite with published results"""

    latest_published_at: str = FieldInfo(alias="latestPublishedAt")

    latest_suite_version: str = FieldInfo(alias="latestSuiteVersion")
    """The version every endpoint defaults to for this suite."""

    suite: str

    target_count: int = FieldInfo(alias="targetCount")
    """Targets currently published under the latest version."""


class BenchmarkListSuitesResponse(BaseModel):
    data: List[Data]
