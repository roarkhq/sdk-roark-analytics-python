# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvaluationGetRunsParams"]


class EvaluationGetRunsParams(TypedDict, total=False):
    limit: str
    """Number of items to return per page"""

    next_cursor: Annotated[str, PropertyInfo(alias="nextCursor")]
    """Cursor for the next page of items"""
