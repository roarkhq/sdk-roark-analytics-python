# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationRunPlanJobRescoreResponse", "Data", "DataMetric"]


class DataMetric(BaseModel):
    customer_flow_id: Optional[str] = FieldInfo(alias="customerFlowId")
    """
    The flow whose simulations it grades. Null when it grades every simulation of
    the run.
    """

    customer_flow_name: Optional[str] = FieldInfo(alias="customerFlowName")
    """The flow's title. Null for a run-wide metric."""

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")
    """The metric graded"""


class Data(BaseModel):
    completed_at: Optional[str] = FieldInfo(alias="completedAt")
    """When the grading finished. Null while it runs."""

    created_at: str = FieldInfo(alias="createdAt")
    """When the re-score was requested"""

    debrief_requested_at: Optional[str] = FieldInfo(alias="debriefRequestedAt")
    """
    When the run's debrief was queued for a rewrite after this re-score. Null until
    then, and for a run without a debrief.
    """

    error_message: Optional[str] = FieldInfo(alias="errorMessage")
    """Why the re-score failed to start, when it did"""

    job_id: str = FieldInfo(alias="jobId")
    """The simulation run plan job that was re-scored"""

    metrics: List[DataMetric]
    """
    The metrics this re-score grades, one per metric and scope: the run plan's
    metrics when it was requested. They become the run's metric set.
    """

    rescore_id: str = FieldInfo(alias="rescoreId")
    """Re-score ID"""

    scored_conversations: int = FieldInfo(alias="scoredConversations")
    """Conversations whose grading has finished"""

    status: Literal["RUNNING", "COMPLETED", "FAILED"]
    """
    RUNNING while the calls are graded again, then COMPLETED. FAILED when the
    re-score could not start or its grading failed.
    """

    total_conversations: int = FieldInfo(alias="totalConversations")
    """Conversations this re-score grades"""


class SimulationRunPlanJobRescoreResponse(BaseModel):
    data: Data
