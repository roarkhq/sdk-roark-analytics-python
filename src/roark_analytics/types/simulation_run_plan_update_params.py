# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SimulationRunPlanUpdateParams",
    "AgentEndpoint",
    "Flow",
    "FlowEdgeCaseUnionMember1",
    "FlowOverride",
    "Metric",
    "Scenario",
]


class AgentEndpoint(TypedDict, total=False):
    id: Required[str]


class FlowEdgeCaseUnionMember1(TypedDict, total=False):
    id: str
    """The edge case to run."""

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """Run this one as that persona instead of its own."""

    slug: str
    """
    The edge case to run, by its stable slug, matched within this flow. Use instead
    of `id` for a run you keep in version control: a curated edge case’s id differs
    between deployments and changes outright if it is renamed. Your own edge cases
    have no slug and are named by `id`.
    """

    variables: Dict[str, str]
    """Values for this one only."""


class FlowOverride(TypedDict, total=False):
    """One persona or environment property, changed for this flow attachment only."""

    property: Required[
        Literal[
            "ACCENT",
            "AGE",
            "BACKGROUND_NOISE",
            "BACKGROUND_NOISE_VOLUME",
            "BASE_EMOTION",
            "CONFIRMATION_STYLE",
            "GENDER",
            "INTENT_CLARITY",
            "LANGUAGE",
            "INTERRUPTION",
            "MEMORY_RELIABILITY",
            "RESPONSE_TIMING",
            "SPEECH_CLARITY",
            "SPEECH_PACE",
        ]
    ]

    value: Required[str]


class Flow(TypedDict, total=False):
    """
    One customer flow attached to a run plan, and which of its ways of running you
    cover.
    Attaching the same flow more than once with different overrides is how you fan
    it out across personas or values.
    """

    id: str
    """The customer flow to run."""

    edge_cases: Annotated[Union[Literal["ALL"], Iterable[FlowEdgeCaseUnionMember1]], PropertyInfo(alias="edgeCases")]
    """
    `"ALL"` runs every edge case the flow has when the run starts, so one added
    later is covered. An array runs only the ones you name, each able to carry its
    own persona override and values.
    """

    happy_path: Annotated[bool, PropertyInfo(alias="happyPath")]
    """Run the flow's happy path. Resolved when the run starts, so it follows the flow."""

    overrides: Iterable[FlowOverride]
    """
    Persona and environment properties to change for this attachment only, without
    editing the persona or the environment themselves. Each entry patches the
    per-run snapshot this attachment records, so the flow runs as a caller with that
    accent, or over that background noise, and everything else stays as authored.
    This is how you attach the same flow twice and vary one thing between them,
    which is what a sweep template builds for you. One value per property; a
    property named twice is rejected.
    """

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """Runs everything this attachment resolves as that persona instead of its own."""

    slug: str
    """
    The Roark-curated flow to run, by its stable slug. Use instead of `id` for a run
    you keep in version control: a curated flow’s id differs between deployments,
    its slug does not. Your own flows have no slug and are named by `id`.
    """

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

    min_pass_rate: Annotated[Optional[float], PropertyInfo(alias="minPassRate")]
    """
    THE BAR, and the only thing that decides pass/fail. The share of the run's
    simulations that must pass this check, 0-100.
    Applied to this check alone and never pooled: silence duration at 40 and word
    count at 80 means the run fails unless 40% of sims clear silence AND 80% clear
    word count. Omit or `null` for the 80% default.
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

    comparison_baseline: Annotated[Optional[str], PropertyInfo(alias="comparisonBaseline")]
    """
    The value every other value is measured against. See `POST /v1/simulation/plan`.
    A real value cannot be sent on its own: the property it belongs to decides which
    values are legal, and an omitted property means "leave unchanged", which this
    endpoint cannot check a baseline against. Send `comparisonProperty` with it, or
    get a `400`.
    `null` on its own IS allowed, and clears just the baseline while leaving the
    property set. Nothing needs validating when clearing, and a property with no
    baseline is a real state: the report falls back to that property's own norm, and
    `GENDER` has no norm to fall back to.
    """

    comparison_property: Annotated[
        Optional[
            Literal[
                "ACCENT",
                "AGE",
                "BACKGROUND_NOISE",
                "BACKGROUND_NOISE_VOLUME",
                "BASE_EMOTION",
                "CONFIRMATION_STYLE",
                "GENDER",
                "INTENT_CLARITY",
                "LANGUAGE",
                "INTERRUPTION",
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ],
        PropertyInfo(alias="comparisonProperty"),
    ]
    """
    The property this plan investigates. Send `null` to clear the comparison; omit
    the field to leave it unchanged. See `POST /v1/simulation/plan`.
    The pair moves together. Sending `comparisonProperty` also sets
    `comparisonBaseline` to whatever this request carries, or to `null` if it
    carries none, because a baseline is a value of one specific property and keeping
    the old one would store a pair that is not valid.
    """

    comparison_values: Annotated[SequenceNotStr[str], PropertyInfo(alias="comparisonValues")]
    """
    Which values of `comparisonProperty` to run. See `POST /v1/simulation/plan`.
    Omitting it keeps the arms the plan already has, so an edit that only renames
    the plan never widens a sweep you deliberately narrowed, and never multiplies
    what it costs.
    """

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

    include_automatic_metrics: Annotated[bool, PropertyInfo(alias="includeAutomaticMetrics")]
    """
    Whether to let the run add metrics by itself off the attached flows. See `POST
    /v1/simulation/plan`.
    """

    include_flow_metrics: Annotated[bool, PropertyInfo(alias="includeFlowMetrics")]
    """
    Whether to also collect each attached flow's own metrics, on top of this plan's
    list.
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
