# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallListParams", "Property"]


class Property(TypedDict, total=False):
    exists: bool
    """true: the property is set. false: the property is missing."""


class CallListParams(TypedDict, total=False):
    after: str
    """Cursor for pagination - use the nextCursor value from a previous response"""

    counted_in_results: Annotated[Literal["true", "false"], PropertyInfo(alias="countedInResults")]
    """
    true: only simulated calls their run's results count (not invalidated, for
    example because the agent never spoke). false: only the simulated calls the
    results leave out, each invalidated. Live calls, and calls removed from their
    run, match neither.
    """

    exclude_hidden_runs: Annotated[Literal["true", "false"], PropertyInfo(alias="excludeHiddenRuns")]
    """
    true: leave out calls from runs hidden from the runs list. Live calls stay in.
    false is the same as leaving it out.
    """

    limit: int
    """Maximum number of calls to return (default: 20, max: 100)"""

    properties: Dict[str, Property]
    """
    Filter on custom properties, one entry per property name:
    properties[<name>][exists]=true keeps calls that have the property set (whatever
    the value), properties[<name>][exists]=false keeps calls missing it (never sent,
    sent as null, or removed). A property the project has never seen is missing on
    every call. Names match the way properties are stored, so planTier and plan_tier
    are one property. At most 20 properties; a name taken by a built-in call filter,
    such as status, is rejected with 400.
    """

    search_text: Annotated[str, PropertyInfo(alias="searchText")]
    """Search text to filter calls by title, summary, or transcript"""

    simulation_run_plan_ids: Annotated[str, PropertyInfo(alias="simulationRunPlanIds")]
    """Calls from every run of any of these run plans, comma-separated, at most 100"""

    simulation_run_plan_job_id: Annotated[str, PropertyInfo(alias="simulationRunPlanJobId")]
    """
    Filter by simulation run plan job ID to get all calls from a specific simulation
    batch
    """

    simulation_run_plan_job_ids: Annotated[str, PropertyInfo(alias="simulationRunPlanJobIds")]
    """
    Calls from any of these simulation runs (run plan job ids), comma-separated, at
    most 100
    """

    sort_by: Annotated[
        Literal["createdAt", "startedAt", "endedAt", "duration", "title", "status"], PropertyInfo(alias="sortBy")
    ]
    """Field to sort by (default: createdAt)"""

    sort_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortDirection")]
    """Sort direction (default: desc)"""

    status: Literal["RINGING", "IN_PROGRESS", "ENDED"]
    """Filter by call status"""
