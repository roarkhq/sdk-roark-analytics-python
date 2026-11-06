# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationRunPlanJobDeleteResponse", "Data"]


class Data(BaseModel):
    """Result of deleting a simulation plan job"""

    deleted: bool
    """True when the run was removed from the run history."""

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")


class SimulationRunPlanJobDeleteResponse(BaseModel):
    data: Data
    """Result of deleting a simulation plan job"""
