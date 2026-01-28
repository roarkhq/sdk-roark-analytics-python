# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallListParams"]


class CallListParams(TypedDict, total=False):
    after: str
    """Cursor for pagination - use the nextCursor value from a previous response"""

    limit: int
    """Maximum number of calls to return (default: 20, max: 100)"""

    search_text: Annotated[str, PropertyInfo(alias="searchText")]
    """Search text to filter calls by title, summary, or transcript"""

    simulation_run_plan_job_id: Annotated[str, PropertyInfo(alias="simulationRunPlanJobId")]
    """
    Filter by simulation run plan job ID to get all calls from a specific simulation
    batch
    """

    sort_by: Annotated[
        Literal["createdAt", "startedAt", "endedAt", "duration", "title", "status"], PropertyInfo(alias="sortBy")
    ]
    """Field to sort by (default: createdAt)"""

    sort_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortDirection")]
    """Sort direction (default: desc)"""

    status: Literal["RINGING", "IN_PROGRESS", "ENDED"]
    """Filter by call status"""
