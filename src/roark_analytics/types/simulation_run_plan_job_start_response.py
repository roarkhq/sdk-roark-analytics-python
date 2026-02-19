# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationRunPlanJobStartResponse", "Data"]


class Data(BaseModel):
    """Response when triggering a simulation run plan"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    simulation_run_plan_id: str = FieldInfo(alias="simulationRunPlanId")
    """ID of the simulation run plan that was executed"""

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")
    """ID of the simulation run plan job that was created"""

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
    """Initial status of the job"""


class SimulationRunPlanJobStartResponse(BaseModel):
    data: Data
    """Response when triggering a simulation run plan"""
