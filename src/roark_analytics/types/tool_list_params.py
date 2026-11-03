# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """Only tools scoped to this agent"""

    include_built_in: Annotated[Literal["true", "false"], PropertyInfo(alias="includeBuiltIn")]
    """Include the built-in tools (default true)"""
