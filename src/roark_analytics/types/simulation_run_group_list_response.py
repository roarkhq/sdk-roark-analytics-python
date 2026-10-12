# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationRunGroupListResponse", "Data", "DataLatestReport", "DataRun", "Pagination"]


class DataLatestReport(BaseModel):
    """Where the group report stands, without its document."""

    id: str

    completed_at: Optional[str] = FieldInfo(alias="completedAt")
    """ISO 8601. Null until the report settles."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    error_message: Optional[str] = FieldInfo(alias="errorMessage")

    status: Literal["PENDING", "GENERATING", "READY", "FAILED"]
    """
    PENDING and GENERATING are in flight; READY carries the document; FAILED carries
    errorMessage.
    """


class DataRun(BaseModel):
    """One run in the group, in group order."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    ended_at: Optional[str] = FieldInfo(alias="endedAt")

    plan_name: Optional[str] = FieldInfo(alias="planName")
    """The name of the plan the run ran. Null when the plan was deleted."""

    run_number: Optional[int] = FieldInfo(alias="runNumber")
    """Per-project run number, shown as SR-42 in the app."""

    simulation_run_plan_id: str = FieldInfo(alias="simulationRunPlanId")

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")
    """The run, readable at GET /v1/simulation/plan/job/{jobId}"""

    started_at: Optional[str] = FieldInfo(alias="startedAt")

    status: Literal[
        "PENDING",
        "QUEUED",
        "CREATING_SNAPSHOTS",
        "CREATING_SIMULATIONS",
        "PREPARING_CAPACITY",
        "RUNNING_SIMULATIONS",
        "COMPLETED",
        "FAILED",
        "TIMED_OUT",
        "CANCELLED",
        "CANCELLING",
        "ENDING_SIMULATIONS",
    ]


class Data(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    latest_report: Optional[DataLatestReport] = FieldInfo(alias="latestReport")
    """
    Where the latest group report stands. Read the document from GET
    /v1/simulation/run-group/{groupId}.
    """

    name: str

    run_count: int = FieldInfo(alias="runCount")

    runs: List[DataRun]


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: int

    offset: int

    total: int
    """Total run groups in the project, ignoring this page."""


class SimulationRunGroupListResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
