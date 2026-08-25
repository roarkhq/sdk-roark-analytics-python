# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationRunResponse", "Data"]


class Data(BaseModel):
    """A started simulation run."""

    created_at: str = FieldInfo(alias="createdAt")
    """When the run was created, ISO 8601."""

    saved_as_plan: bool = FieldInfo(alias="savedAsPlan")
    """
    Whether that plan is listed by GET /v1/simulation/plan. False for an unsaved
    run, whose plan is hidden.
    """

    simulation_job_count: int = FieldInfo(alias="simulationJobCount")
    """How many simulated calls this run places."""

    simulation_run_plan_id: str = FieldInfo(alias="simulationRunPlanId")
    """
    The run plan behind this run, present whether or not it was saved. Pass it back
    as `planId` to run the same configuration again.
    """

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")
    """The run. Poll it with GET /v1/simulation/plan/job/{jobId}."""

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
    """
    Initial status. PENDING normally, or QUEUED when the plan runs sequentially and
    another job of its is still active.
    """


class SimulationRunResponse(BaseModel):
    data: Data
    """A started simulation run."""
