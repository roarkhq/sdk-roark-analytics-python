# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentEndpointListParams"]


class AgentEndpointListParams(TypedDict, total=False):
    after: str
    """Cursor for pagination - endpoint ID to start after"""

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """Filter by agent ID"""

    limit: int
    """Maximum number of endpoints to return (default: 20, max: 50)"""

    search_text: Annotated[str, PropertyInfo(alias="searchText")]
    """Search text to filter endpoints"""
