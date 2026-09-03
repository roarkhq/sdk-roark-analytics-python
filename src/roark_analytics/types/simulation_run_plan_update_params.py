# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanUpdateParams", "AgentEndpoint", "Flow", "FlowEdgeCaseUnionMember1", "Metric", "Scenario"]


class AgentEndpoint(TypedDict, total=False):
    id: Required[str]


class FlowEdgeCaseUnionMember1(TypedDict, total=False):
    id: Required[str]
    """The edge case to run."""

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """Run this one as that persona instead of its own."""

    variables: Dict[str, str]
    """Values for this one only."""


class Flow(TypedDict, total=False):
    """
    One customer flow attached to a run plan, and which of its ways of running you
    cover.
    Attaching the same flow more than once with different overrides is how you fan
    it out across personas or values.
    """

    id: Required[str]
    """The customer flow to run."""

    edge_cases: Annotated[Union[Literal["ALL"], Iterable[FlowEdgeCaseUnionMember1]], PropertyInfo(alias="edgeCases")]
    """
    `"ALL"` runs every edge case the flow has when the run starts, so one added
    later is covered. An array runs only the ones you name, each able to carry its
    own persona override and values.
    """

    happy_path: Annotated[bool, PropertyInfo(alias="happyPath")]
    """Run the flow's happy path. Resolved when the run starts, so it follows the flow."""

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """Runs everything this attachment resolves as that persona instead of its own."""

    variables: Dict[str, str]
    """Values for everything it resolves."""


class Metric(TypedDict, total=False):
    id: str
    """Metric definition UUID. Provide either this or `slug`, not both."""

    conversation_source: Annotated[Optional[Literal["SIMULATED", "LIVE"]], PropertyInfo(alias="conversationSource")]
    """
    Which side of an enriched run this metric is scored on. Only meaningful with
    `enrichWithLiveConversation: true`, where a run has both a simulated
    conversation and the customer's own live recording of it.
    Defaults to `SIMULATED`. Use `LIVE` for a metric that must be measured against
    the real recording (audio quality, provider latency) rather than the simulated
    leg. `null` means the same as omitting it, so a plan read back from GET can be
    sent straight to PUT.
    """

    metric_id: Annotated[str, PropertyInfo(alias="metricId")]
    """
    Alias of `slug` accepted for backwards compatibility. Use `slug` for new
    integrations.
    """

    slug: str
    """
    Stable metric slug (e.g. `customer_satisfaction`). Provide either this or `id`,
    not both.
    """


class Scenario(TypedDict, total=False):
    id: Required[str]
    """Scenario ID"""

    variables: Dict[str, str]
    """
    Template variables for this scenario instance. The same scenario can appear
    multiple times with different variables.
    """


class SimulationRunPlanUpdateParams(TypedDict, total=False):
    agent_endpoints: Annotated[Iterable[AgentEndpoint], PropertyInfo(alias="agentEndpoints")]
    """Agent endpoints to include in this run plan"""

    description: str
    """Description of the run plan"""

    direction: Literal["INBOUND", "OUTBOUND"]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

    end_call_phrases: Annotated[SequenceNotStr[str], PropertyInfo(alias="endCallPhrases")]
    """Phrases that trigger end of call. Empty array disables the feature."""

    end_call_reasons: Annotated[SequenceNotStr[str], PropertyInfo(alias="endCallReasons")]
    """
    Semantic conditions that trigger end of call. The LLM evaluates the conversation
    against these conditions. Empty array disables the feature.
    """

    enrich_with_live_conversation: Annotated[bool, PropertyInfo(alias="enrichWithLiveConversation")]
    """
    Whether to merge the customer's own live recording into each simulation of this
    plan.
    """

    execution_mode: Annotated[
        Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"], PropertyInfo(alias="executionMode")
    ]
    """Execution mode (PARALLEL or SEQUENTIAL)"""

    flows: Iterable[Flow]
    """
    Replaces the customer flows attached to this run plan. Omit to leave them
    unchanged; send an empty array to detach them all.
    """

    is_hidden: Annotated[bool, PropertyInfo(alias="isHidden")]
    """
    Whether this plan is hidden from GET /v1/simulation/plan.
    A run started without `saveAsPlan` creates a hidden plan to carry it. Send `{
    "name": "...", "isHidden": false }` to keep that configuration as a reusable
    plan, which is what the app does when you save a one-off run.
    """

    iteration_count: Annotated[int, PropertyInfo(alias="iterationCount")]
    """Number of iterations to run for each test case (1-10000)"""

    max_concurrent_jobs: Annotated[int, PropertyInfo(alias="maxConcurrentJobs")]
    """Maximum number of concurrent simulation jobs"""

    max_simulation_duration_seconds: Annotated[int, PropertyInfo(alias="maxSimulationDurationSeconds")]
    """Maximum duration in seconds for each simulation"""

    metrics: Iterable[Metric]
    """
    Metric definitions to include in this run plan. Reference each by `id` (UUID) or
    `slug`.
    """

    name: str
    """Name of the run plan"""

    personas: Iterable[AgentEndpoint]
    """Personas to include in this run plan"""

    scenarios: Iterable[Scenario]
    """
    Deprecated: use `flows` instead. Replaces the scenarios on this run plan. Omit
    to leave them unchanged; send an empty array to detach them all, which is how a
    scenario-based plan is moved over to flows.
    """

    silence_timeout_seconds: Annotated[int, PropertyInfo(alias="silenceTimeoutSeconds")]
    """Timeout in seconds for silence detection"""
