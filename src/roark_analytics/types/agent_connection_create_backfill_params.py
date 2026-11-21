# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentConnectionCreateBackfillParams"]


class AgentConnectionCreateBackfillParams(TypedDict, total=False):
    max_calls: Required[Annotated[int, PropertyInfo(alias="maxCalls")]]
    """How many of the most recent past calls to import, up to 1000."""
