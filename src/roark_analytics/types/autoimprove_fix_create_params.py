# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AutoimproveFixCreateParams"]


class AutoimproveFixCreateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]
    """The production agent to improve. It is never modified until you promote."""

    objective_label: Required[Annotated[str, PropertyInfo(alias="objectiveLabel")]]
    """Human-readable label for the objective, shown everywhere the fix appears."""

    objective_metric_definition_id: Required[Annotated[str, PropertyInfo(alias="objectiveMetricDefinitionId")]]
    """
    The metric that defines success: a pass/fail metric, or a threshold variant of a
    scale metric (for example "PII Handling >= 4"). Roark measures the pass rate of
    this metric across simulated calls.
    """

    customer_integration_id: Annotated[str, PropertyInfo(alias="customerIntegrationId")]
    """
    The provider integration whose credentials Roark uses. Omit to use the project's
    active integration for the agent's provider. The integration must have agent
    config writes enabled.
    """

    max_iterations: Annotated[int, PropertyInfo(alias="maxIterations")]
    """Cap on decision turns. Defaults to 10."""

    max_sim_calls: Annotated[int, PropertyInfo(alias="maxSimCalls")]
    """Cap on simulated calls dialed. Defaults to 200."""

    staging_agent_id: Annotated[str, PropertyInfo(alias="stagingAgentId")]
    """
    An existing agent to stage changes on instead of the default shadow clone. Must
    be a different agent from agentId, on the same provider.
    """

    target_value: Annotated[float, PropertyInfo(alias="targetValue")]
    """The pass-rate percentage that counts as fixed. Defaults to 90."""

    validation_run_plan_id: Annotated[str, PropertyInfo(alias="validationRunPlanId")]
    """
    An existing simulation run plan to validate with. Omit to let Roark author its
    own suite.
    """
