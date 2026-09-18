# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AutoimproveLogEntryParam"]


class AutoimproveLogEntryParam(TypedDict, total=False):
    id: Required[str]

    config_push_id: Required[Annotated[Optional[str], PropertyInfo(alias="configPushId")]]

    created_at: Required[Annotated[str, PropertyInfo(alias="createdAt")]]
    """When the entry was written (ISO 8601)."""

    kind: Required[
        Literal[
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
    ]

    order_index: Required[Annotated[int, PropertyInfo(alias="orderIndex")]]

    pass_rate_after: Required[Annotated[Optional[float], PropertyInfo(alias="passRateAfter")]]

    pass_rate_before: Required[Annotated[Optional[float], PropertyInfo(alias="passRateBefore")]]

    question_options: Required[Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="questionOptions")]]

    simulation_run_plan_job_id: Required[Annotated[Optional[str], PropertyInfo(alias="simulationRunPlanJobId")]]

    text: Required[str]

    trial_count: Required[Annotated[Optional[int], PropertyInfo(alias="trialCount")]]
