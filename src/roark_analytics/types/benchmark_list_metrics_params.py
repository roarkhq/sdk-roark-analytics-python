# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BenchmarkListMetricsParams"]


class BenchmarkListMetricsParams(TypedDict, total=False):
    suite: Required[str]

    suite_version: Annotated[str, PropertyInfo(alias="suiteVersion")]
