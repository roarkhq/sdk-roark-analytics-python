# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanJobListParams"]


class SimulationRunPlanJobListParams(TypedDict, total=False):
    after: str
    """Cursor for pagination - use the nextCursor value from a previous response"""

    label_id: Annotated[str, PropertyInfo(alias="labelId")]
    """Filter by label ID attached to the plan job. Use this if you know the label ID."""

    label_name: Annotated[str, PropertyInfo(alias="labelName")]
    """Filter by label name attached to the plan job.

    More user-friendly alternative to labelId. Case-insensitive.
    """

    limit: int
    """Maximum number of plan jobs to return (default: 20, max: 50)"""

    simulation_run_plan_id: Annotated[str, PropertyInfo(alias="simulationRunPlanId")]
    """Filter by simulation run plan ID"""

    status: Literal[
        "PENDING",
        "QUEUED",
        "CREATING_SNAPSHOTS",
        "CREATING_SIMULATIONS",
        "RUNNING_SIMULATIONS",
        "COMPLETED",
        "FAILED",
        "TIMED_OUT",
        "CANCELLED",
        "CANCELLING",
        "ENDING_SIMULATIONS",
    ]
    """
    Filter by plan job status (PENDING, CREATING_SNAPSHOTS, CREATING_SIMULATIONS,
    RUNNING_SIMULATIONS, ENDING_SIMULATIONS, COMPLETED, FAILED, TIMED_OUT,
    CANCELLED, CANCELLING)
    """
