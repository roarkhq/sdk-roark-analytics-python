# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanListParams"]


class SimulationRunPlanListParams(TypedDict, total=False):
    after: str
    """Cursor for pagination - use the nextCursor value from a previous response"""

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """Filter run plans by agent ID"""

    limit: int
    """Maximum number of run plans to return (default: 20, max: 50)"""

    search_text: Annotated[str, PropertyInfo(alias="searchText")]
    """Search text to filter run plans by name"""
