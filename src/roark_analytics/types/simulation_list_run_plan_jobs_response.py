# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationListRunPlanJobsResponse", "Data", "Pagination"]


class Data(BaseModel):
    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    simulation_run_plan_id: str = FieldInfo(alias="simulationRunPlanId")
    """ID of the simulation run plan"""

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")
    """ID of the simulation run plan job"""

    status: str
    """Job status"""

    triggered_by: str = FieldInfo(alias="triggeredBy")
    """How the job was triggered (SCHEDULED or USER_TRIGGERED_FROM_UI)"""

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


class SimulationListRunPlanJobsResponse(BaseModel):
    """Paginated list of simulation run plan jobs"""

    data: List[Data]

    pagination: Pagination
