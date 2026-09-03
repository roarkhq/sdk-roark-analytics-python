# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanCreateParams", "AgentEndpoint", "Flow", "FlowEdgeCaseUnionMember1", "Metric", "Scenario"]


class AgentEndpoint(TypedDict, total=False):
    id: Required[str]


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


class Scenario(TypedDict, total=False):
    id: Required[str]
    """Scenario ID"""

    variables: Dict[str, str]
    """
    Template variables for this scenario instance. The same scenario can appear
    multiple times with different variables.
    """


class SimulationRunPlanCreateParams(TypedDict, total=False):
    agent_endpoints: Required[Annotated[Iterable[AgentEndpoint], PropertyInfo(alias="agentEndpoints")]]
    """Agent endpoints to include in this run plan"""

    direction: Required[Literal["INBOUND", "OUTBOUND"]]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

    max_simulation_duration_seconds: Required[Annotated[int, PropertyInfo(alias="maxSimulationDurationSeconds")]]
    """Maximum duration in seconds for each simulation"""

    metrics: Required[Iterable[Metric]]
    """
    Metric definitions to include in this run plan. Reference each by `id` (UUID) or
    `slug`.
    """

    name: Required[str]
    """Name of the run plan"""

    auto_run: Annotated[bool, PropertyInfo(alias="autoRun")]
    """
    Deprecated: use POST /v1/simulation/run, which starts a run and accepts runtime
    `variables` as well. This flag runs the plan with only the values pinned on it.
    """

    description: str
    """Description of the run plan"""

    end_call_phrases: Annotated[SequenceNotStr[str], PropertyInfo(alias="endCallPhrases")]
    """Phrases that trigger end of call. Empty array disables the feature."""

    end_call_reasons: Annotated[SequenceNotStr[str], PropertyInfo(alias="endCallReasons")]
    """
    Semantic conditions that trigger end of call. The LLM evaluates the conversation
    against these conditions. Empty array disables the feature.
    """

    enrich_with_live_conversation: Annotated[bool, PropertyInfo(alias="enrichWithLiveConversation")]
    """
    Merge the customer's own recording of the real call into each simulation, so
    metrics can be scored against the live leg as well as the simulated one. This is
    the API equivalent of the dashboard's live-enrichment toggle.
    With this on, the run provisions a phone number and holds each call open for up
    to 15 minutes waiting for a matching call to be posted to POST /v1/call. A call
    matches on the provisioned number (`roarkPhoneNumber` on the job) with a start
    time inside the simulation window. If nothing arrives, the simulation still
    completes and any `LIVE`-sourced metric produces no value.
    Required by any metric whose `requiresLiveConversation` is true: without it that
    metric is silently skipped.
    """

    execution_mode: Annotated[
        Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"], PropertyInfo(alias="executionMode")
    ]
    """Execution mode (PARALLEL or SEQUENTIAL)"""

    flows: Iterable[Flow]
    """
    Customer flows to include in this run plan. The same flow can appear more than
    once with a different persona override or different variables.
    """

    iteration_count: Annotated[int, PropertyInfo(alias="iterationCount")]
    """Number of iterations to run for each test case (1-10000)"""

    max_concurrent_jobs: Annotated[int, PropertyInfo(alias="maxConcurrentJobs")]
    """Maximum number of concurrent simulation jobs"""

    personas: Iterable[AgentEndpoint]
    """
    Personas to include in this run plan. Required with `scenarios`; ignored with
    `flows`, where each variant carries its own persona.
    """

    scenarios: Iterable[Scenario]
    """
    Deprecated: use `flows` instead. Scenarios to include in this run plan. The same
    scenario ID can appear multiple times with different variables.
    """

    silence_timeout_seconds: Annotated[int, PropertyInfo(alias="silenceTimeoutSeconds")]
    """Timeout in seconds for silence detection"""
