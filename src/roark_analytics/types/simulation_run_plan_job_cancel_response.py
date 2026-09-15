# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationRunPlanJobCancelResponse", "Data"]


class Data(BaseModel):
    """Result of cancelling a simulation plan job"""

    cancelled: bool
    """
    True when this request stopped the run. False when it had already finished,
    which is not an error.
    """

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")

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
    """The job status after the request. Unchanged when the run had already finished."""


class SimulationRunPlanJobCancelResponse(BaseModel):
    data: Data
    """Result of cancelling a simulation plan job"""
