# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["CallBatchDeleteParams"]


class CallBatchDeleteParams(TypedDict, total=False):
    call_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="callIds")]]
    """IDs of the calls to delete, at most 100. Repeated IDs are counted once."""
