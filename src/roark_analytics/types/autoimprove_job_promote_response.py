# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AutoimproveJobPromoteResponse", "Data"]


class Data(BaseModel):
    """
    One Autoimprove job: Roark autonomously improving one agent toward one objective
    metric. Roark only ever changes the staging agent (a shadow clone by default);
    production changes exactly once, when verified changes are promoted.
    """

    id: str

    agent_id: str = FieldInfo(alias="agentId")

    baseline_value: Optional[float] = FieldInfo(alias="baselineValue")

    concluded_at: Optional[str] = FieldInfo(alias="concludedAt")
    """When the job reached a terminal status (ISO 8601)."""

    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created (ISO 8601)."""

    current_value: Optional[float] = FieldInfo(alias="currentValue")

    customer_integration_id: Optional[str] = FieldInfo(alias="customerIntegrationId")

    final_report: Optional[str] = FieldInfo(alias="finalReport")

    initiated_by_user_id: Optional[str] = FieldInfo(alias="initiatedByUserId")

    issue_id: Optional[str] = FieldInfo(alias="issueId")

    iteration_count: int = FieldInfo(alias="iterationCount")

    max_iterations: int = FieldInfo(alias="maxIterations")

    max_sim_calls: int = FieldInfo(alias="maxSimCalls")

    objective_id: Optional[str] = FieldInfo(alias="objectiveId")

    objective_label: str = FieldInfo(alias="objectiveLabel")

    objective_metric_definition_id: str = FieldInfo(alias="objectiveMetricDefinitionId")

    organization_id: str = FieldInfo(alias="organizationId")

    project_id: str = FieldInfo(alias="projectId")

    sim_calls_used: int = FieldInfo(alias="simCallsUsed")

    staging_agent_id: str = FieldInfo(alias="stagingAgentId")

    staging_kind: Literal["DESIGNATED", "SHADOW", "CHANNEL"] = FieldInfo(alias="stagingKind")

    status: Literal["RUNNING", "NEEDS_INPUT", "PAUSED", "AWAITING_PROMOTE", "PROMOTED", "NO_FIX", "CANCELLED", "FAILED"]

    target_value: float = FieldInfo(alias="targetValue")

    trigger: Literal["ISSUE", "RUN_THRESHOLD_FAILED", "USER", "DEGRADATION"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the job last changed (ISO 8601)."""

    validation_run_plan_id: Optional[str] = FieldInfo(alias="validationRunPlanId")

    working_memory: Optional[str] = FieldInfo(alias="workingMemory")


class AutoimproveJobPromoteResponse(BaseModel):
    data: Data
    """
    One Autoimprove job: Roark autonomously improving one agent toward one objective
    metric. Roark only ever changes the staging agent (a shadow clone by default);
    production changes exactly once, when verified changes are promoted.
    """
