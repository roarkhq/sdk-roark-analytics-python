# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AutoimproveLogEntry"]


class AutoimproveLogEntry(BaseModel):
    """
    One entry in the job's worklog: what Roark did or observed at that step.
    VALIDATION entries carry the batch's trial count and pass-rate movement;
    QUESTION entries carry the quick-reply options Roark is waiting on.
    """

    id: str

    config_push_id: Optional[str] = FieldInfo(alias="configPushId")

    created_at: str = FieldInfo(alias="createdAt")
    """When the entry was written (ISO 8601)."""

    kind: Literal[
        "STARTED",
        "REASONING",
        "CHANGE",
        "VALIDATION",
        "VERDICT",
        "SLEEP",
        "QUESTION",
        "GUIDANCE",
        "STATUS",
        "SETUP",
        "SUITE",
    ]

    order_index: int = FieldInfo(alias="orderIndex")

    pass_rate_after: Optional[float] = FieldInfo(alias="passRateAfter")

    pass_rate_before: Optional[float] = FieldInfo(alias="passRateBefore")

    question_options: Optional[List[str]] = FieldInfo(alias="questionOptions")

    simulation_run_plan_job_id: Optional[str] = FieldInfo(alias="simulationRunPlanJobId")

    text: str

    trial_count: Optional[int] = FieldInfo(alias="trialCount")
