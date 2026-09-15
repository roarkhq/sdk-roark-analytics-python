# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BenchmarkGetTargetParams"]


class BenchmarkGetTargetParams(TypedDict, total=False):
    suite: Required[str]

    publication_id: Annotated[str, PropertyInfo(alias="publicationId")]

    suite_version: Annotated[str, PropertyInfo(alias="suiteVersion")]
