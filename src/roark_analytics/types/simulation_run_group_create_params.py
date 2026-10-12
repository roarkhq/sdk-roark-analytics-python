# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationRunGroupCreateParams"]


class SimulationRunGroupCreateParams(TypedDict, total=False):
    name: str
    """
    What to call the group. Defaults to the plans' names when starting plans, and to
    the runs' plan names when grouping existing runs.
    """

    simulation_run_plan_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="simulationRunPlanIds")]
    """
    Plans to run once each, in display order (2 to 20). Each plan starts a run,
    exactly as POST /v1/simulation/plan/{planId}/job would. Send this or
    `simulationRunPlanJobIds`, not both.
    """

    simulation_run_plan_job_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="simulationRunPlanJobIds")]
    """
    Runs that already exist, in display order (2 to 20). Runs still in progress are
    fine: the group report waits for them. Send this or `simulationRunPlanIds`, not
    both.
    """
