# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AutoimproveFixParam"]


class AutoimproveFixParam(TypedDict, total=False):
    id: Required[str]

    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    baseline_value: Required[Annotated[Optional[float], PropertyInfo(alias="baselineValue")]]

    concluded_at: Required[Annotated[Optional[str], PropertyInfo(alias="concludedAt")]]
    """When the fix reached a terminal status (ISO 8601)."""

    created_at: Required[Annotated[str, PropertyInfo(alias="createdAt")]]
    """When the fix was created (ISO 8601)."""

    current_value: Required[Annotated[Optional[float], PropertyInfo(alias="currentValue")]]

    customer_integration_id: Required[Annotated[str, PropertyInfo(alias="customerIntegrationId")]]

    final_report: Required[Annotated[Optional[str], PropertyInfo(alias="finalReport")]]

    initiated_by_user_id: Required[Annotated[Optional[str], PropertyInfo(alias="initiatedByUserId")]]

    issue_id: Required[Annotated[Optional[str], PropertyInfo(alias="issueId")]]

    iteration_count: Required[Annotated[int, PropertyInfo(alias="iterationCount")]]

    max_iterations: Required[Annotated[int, PropertyInfo(alias="maxIterations")]]

    max_sim_calls: Required[Annotated[int, PropertyInfo(alias="maxSimCalls")]]

    objective_id: Required[Annotated[Optional[str], PropertyInfo(alias="objectiveId")]]

    objective_label: Required[Annotated[str, PropertyInfo(alias="objectiveLabel")]]

    objective_metric_definition_id: Required[Annotated[str, PropertyInfo(alias="objectiveMetricDefinitionId")]]

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    sim_calls_used: Required[Annotated[int, PropertyInfo(alias="simCallsUsed")]]

    staging_agent_id: Required[Annotated[str, PropertyInfo(alias="stagingAgentId")]]

    staging_kind: Required[Annotated[Literal["DESIGNATED", "SHADOW"], PropertyInfo(alias="stagingKind")]]

    status: Required[
        Literal["RUNNING", "NEEDS_INPUT", "PAUSED", "AWAITING_PROMOTE", "PROMOTED", "NO_FIX", "CANCELLED", "FAILED"]
    ]

    target_value: Required[Annotated[float, PropertyInfo(alias="targetValue")]]

    trigger: Required[Literal["ISSUE", "RUN_THRESHOLD_FAILED", "USER", "DEGRADATION"]]

    updated_at: Required[Annotated[str, PropertyInfo(alias="updatedAt")]]
    """When the fix last changed (ISO 8601)."""

    validation_run_plan_id: Required[Annotated[Optional[str], PropertyInfo(alias="validationRunPlanId")]]

    working_memory: Required[Annotated[Optional[str], PropertyInfo(alias="workingMemory")]]
