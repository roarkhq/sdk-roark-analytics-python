# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MetricCollectionJobCreateParams", "Metric"]


class MetricCollectionJobCreateParams(TypedDict, total=False):
    call_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="callIds")]]
    """Call IDs to collect metrics for"""

    metrics: Required[Iterable[Metric]]
    """Metric definitions to collect"""


class Metric(TypedDict, total=False):
    id: Required[str]
