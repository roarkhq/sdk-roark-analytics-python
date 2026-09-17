# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SimulationRunPlanCreateParams",
    "AgentEndpoint",
    "Flow",
    "FlowEdgeCaseUnionMember1",
    "FlowOverride",
    "Metric",
    "Scenario",
]


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

    comparison_baseline: Annotated[Optional[str], PropertyInfo(alias="comparisonBaseline")]
    """
    The value of `comparisonProperty` every other value is measured against, for
    example `NONE` for `BACKGROUND_NOISE` or `NORMAL` for `SPEECH_PACE`. Must be a
    value that property can take.
    Stored rather than assumed, so the report can say "compared against US accent"
    instead of implying Roark decided which value is normal. Most properties have an
    obvious baseline and the dashboard prefills it; `GENDER` has none, so choose the
    one you are testing against.
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
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ],
        PropertyInfo(alias="comparisonProperty"),
    ]
    """
    The property this run plan investigates: the one thing its arms differ by.
    Set it and the run report compares the arms on that property, so a run answers
    "what did background noise cost" rather than just "what did each arm score".
    Every value is a field already recorded on each call, so the report can label an
    arm `CRYING_BABY` rather than repeating a flow variant's title.
    Omit it and the report still compares when it can: it detects which property
    varies across the arms. Setting it is what tells the written summary what you
    were trying to find out, which detection cannot infer.
    """

    comparison_values: Annotated[SequenceNotStr[str], PropertyInfo(alias="comparisonValues")]
    """
    Which values of `comparisonProperty` to run. This is what the plan costs: the
    flow is attached once per value, so ten values is ten times the calls of one.
    Omit it to run every value the property has, which for `ACCENT` is more than
    twenty. Send a subset to narrow the sweep, for example three accents you
    actually serve. A `comparisonBaseline` outside this set is rejected, because it
    would anchor every difference to an arm the run never made.
    Not stored as a field: the arms are the values. Reading the plan back returns
    them as its flow attachments.
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
    once with a different persona override, different variables, or different
    `overrides`: attaching it once per value of one property is how you compare that
    property without a template.
    """

    include_automatic_metrics: Annotated[bool, PropertyInfo(alias="includeAutomaticMetrics")]
    """
    Let the run add metrics by itself off the attached flows, on top of the
    `metrics` named here.
    Two attach this way today: Agent Expectations wherever an attached flow has
    agent expectations written on it, and Keypad Entry wherever one has steps where
    the agent is expected to press keys. Both grade something authored on the flow
    that nothing else measures, which is why it is on by default.
    Set false when the `metrics` list is meant to be exhaustive: a plan testing only
    whether the caller can complete the flow may not want the agent graded on its
    expectations as well. False also pins the plan against any automatic metric
    Roark adds later.
    """

    include_flow_metrics: Annotated[bool, PropertyInfo(alias="includeFlowMetrics")]
    """
    Also collect each attached flow's own metrics, on top of the `metrics` named
    here.
    Default true, which is what you want when you brought your own flows and their
    graders. Set false for a run whose metric list is meant to be exhaustive: a
    template like Load Testing or Voicemail deliberately grades a narrow set, and
    inheriting every flow metric on top multiplies analysis cost across the volume
    without adding signal.
    GET /v1/simulation/template returns the value each template expects.
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
