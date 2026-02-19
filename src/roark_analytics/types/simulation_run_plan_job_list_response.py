# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationRunPlanJobListResponse", "Data", "Pagination"]


class Data(BaseModel):
    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    simulation_run_plan_id: str = FieldInfo(alias="simulationRunPlanId")
    """ID of the simulation run plan"""

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")
    """ID of the simulation run plan job"""

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
    ]
    """Job status"""

    triggered_by: Literal["SCHEDULED", "USER_TRIGGERED_FROM_UI", "RE_RUN", "TRIGGERED_FROM_API"] = FieldInfo(
        alias="triggeredBy"
    )
    """
    How the job was triggered (SCHEDULED, USER_TRIGGERED_FROM_UI,
    TRIGGERED_FROM_API, or RE_RUN)
    """

    ended_at: Optional[str] = FieldInfo(alias="endedAt", default=None)
    """When the job ended"""

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)
    """When the job started"""


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """Whether there are more results available"""

    total: float
    """Total number of matching plan jobs"""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor to use for fetching the next page"""


class SimulationRunPlanJobListResponse(BaseModel):
    """Paginated list of simulation run plan jobs"""

    data: List[Data]

    pagination: Pagination
