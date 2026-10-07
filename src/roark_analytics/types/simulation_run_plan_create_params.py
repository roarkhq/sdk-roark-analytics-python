# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SimulationRunPlanCreateParams",
    "ComparisonArm",
    "CreateRunPlanFromConfig",
    "CreateRunPlanFromConfigAgentEndpoint",
    "CreateRunPlanFromConfigFlow",
    "CreateRunPlanFromConfigFlowEdgeCaseUnionMember1",
    "CreateRunPlanFromConfigFlowOverride",
    "CreateRunPlanFromConfigMetric",
    "CreateRunPlanFromConfigScenario",
    "CreateRunPlanFromTemplate",
    "CreateRunPlanFromTemplateQuestion",
]


class CreateRunPlanFromConfigAgentEndpoint(TypedDict, total=False):
    id: Required[str]


class ComparisonArm(TypedDict, total=False):
    """
    One arm of a sweep: the swept value it runs, and what it pins besides that
    value. The OFFICE arm of a BACKGROUND_NOISE sweep playing at 60% while the other
    beds keep their level is `{ "value": "OFFICE", "backgroundNoiseVolume": 0.6 }`.
    The report compares the arms on the swept property only, so each sweep may pin
    just what its experiment calls for: a BACKGROUND_NOISE sweep may pin
    `backgroundNoiseVolume`, and no other sweep pins anything yet. A pin the sweep
    cannot account for is rejected with `400`.
    """

    value: Required[str]
    """The swept value this arm runs, a value of `comparisonProperty`."""

    background_noise_volume: Annotated[float, PropertyInfo(alias="backgroundNoiseVolume")]
    """
    The noise level this arm plays at, 0 to 1. The environment default is 0.1. Only
    a `BACKGROUND_NOISE` sweep may pin it.
    """


class CreateRunPlanFromConfigFlowEdgeCaseUnionMember1(TypedDict, total=False):
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


class CreateRunPlanFromConfigFlowOverride(TypedDict, total=False):
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


class CreateRunPlanFromConfigFlow(TypedDict, total=False):
    """
    One customer flow attached to a run plan, and which of its ways of running you
    cover.
    Attaching the same flow more than once with different overrides is how you fan
    it out across personas or values.
    """

    id: str
    """The customer flow to run."""

    edge_cases: Annotated[
        Union[Literal["ALL"], Iterable[CreateRunPlanFromConfigFlowEdgeCaseUnionMember1]],
        PropertyInfo(alias="edgeCases"),
    ]
    """
    `"ALL"` runs every edge case the flow has when the run starts, so one added
    later is covered. An array runs only the ones you name, each able to carry its
    own persona override and values.
    """

    happy_path: Annotated[bool, PropertyInfo(alias="happyPath")]
    """Run the flow's happy path. Resolved when the run starts, so it follows the flow."""

    overrides: Iterable[CreateRunPlanFromConfigFlowOverride]
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


class CreateRunPlanFromConfigMetric(TypedDict, total=False):
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


class CreateRunPlanFromConfigScenario(TypedDict, total=False):
    id: Required[str]
    """Scenario ID"""

    variables: Dict[str, str]
    """
    Template variables for this scenario instance. The same scenario can appear
    multiple times with different variables.
    """


class CreateRunPlanFromConfig(TypedDict, total=False):
    """Describe a run plan: what to call, who calls it, and what to measure."""

    agent_endpoints: Required[
        Annotated[Iterable[CreateRunPlanFromConfigAgentEndpoint], PropertyInfo(alias="agentEndpoints")]
    ]
    """Agent endpoints to include in this run plan"""

    direction: Required[Literal["INBOUND", "OUTBOUND"]]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

    max_simulation_duration_seconds: Required[Annotated[int, PropertyInfo(alias="maxSimulationDurationSeconds")]]
    """Maximum duration in seconds for each simulation"""

    name: Required[str]
    """Name of the run plan"""

    auto_run: Annotated[bool, PropertyInfo(alias="autoRun")]
    """
    Deprecated: use POST /v1/simulation/run, which starts a run and accepts runtime
    `variables` as well. This flag runs the plan with only the values pinned on it.
    """

    comparison_baseline: Annotated[Optional[str], PropertyInfo(alias="comparisonBaseline")]
    """
    The reference value of `comparisonProperty`, for example `NONE` for
    `BACKGROUND_NOISE` or `NORMAL` for `SPEECH_PACE`: shown first in the results.
    Must be a value that property can take. Whether a value did significantly worse
    does not depend on it: that is decided against every other value combined (see
    `sweepAttribution`).
    Stored rather than assumed, so the report can say "compared against US accent"
    instead of implying Roark decided which value is normal. Omit it and the
    property's own norm is used, as the dashboard prefills it, or none when your
    `comparisonValues` leave the norm out. `GENDER` has no norm, so choose the one
    you are testing against.
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
    The property this run plan investigates: the one thing its arms differ by.
    Set it and the run report compares the arms on that property, so a run answers
    "what did background noise cost" rather than just "what did each arm score".
    Every value is a field already recorded on each call, so the report can label an
    arm `CRYING_BABY` rather than repeating a flow variant's title.
    Omit it and the report still compares when it can: it detects which property
    varies across the arms. Setting it is what tells the written summary what you
    were trying to find out, which detection cannot infer.
    """

    comparison_values: Annotated[List[Union[str, ComparisonArm]], PropertyInfo(alias="comparisonValues")]
    """
    The arms to run, for a plan that sweeps `comparisonProperty`. This is what the
    plan costs: the flow is attached once per arm, so ten arms is ten times the
    calls of one.
    Attach each flow once, as you would without a comparison: the plan builds the
    arms, running the happy path or edge cases you selected under every arm. Built
    arms need at least 5 calls per arm (`iterationCount` times the test cases per
    arm), or the plan is refused with `400`. Flows that all carry `overrides` on
    `comparisonProperty` already are the arms and are kept as you wrote them; a mix
    of flows with and without one is refused.
    Each entry is one arm. A bare value runs it plain: `"CITY"`. An object runs the
    value with something pinned on that arm only, such as a noise level per bed: `{
    "value": "OFFICE", "backgroundNoiseVolume": 0.6 }` plays OFFICE at 60% while the
    other beds keep the default. List a value more than once with different pins to
    run it as several arms: DRIVING at 0.7 and DRIVING at 1 are two arms, reported
    as `Driving (70% noise)` and `Driving (100% noise)`, and `"DRIVING"` beside them
    keeps the plain arm too. The sweep still varies one property; what an arm pins
    is part of "everything else" for that arm only, so the report still compares the
    arms on `comparisonProperty`.
    Omit it to run every value the property has, plain, which for `ACCENT` is more
    than twenty. A `comparisonBaseline` outside the values listed is rejected,
    because it would anchor every difference to an arm the run never made. A value
    the property cannot take, a pin the sweep cannot account for, or the same arm
    listed twice is rejected with `400`.
    Not stored as a field: the arms are the values. Reading the plan back returns
    them as its flow attachments, each with its pins as `overrides`.
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

    flows: Iterable[CreateRunPlanFromConfigFlow]
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

    max_no_response_retries: Annotated[int, PropertyInfo(alias="maxNoResponseRetries")]
    """
    How many more times to run a test case when the agent under test never responds:
    it never speaks on a call or never replies in a chat (0-10). 0 turns retries
    off. Failed checks and failures on Roark’s side are never retried.
    Each retry is a separate attempt, billed like any other, so a plan retrying N
    times can place up to N + 1 calls per test case. Every silent attempt stays on
    the run with its own call; the run settles once each test case has a final
    attempt, and the agent never spoke verdict is judged on each test case’s last
    attempt.
    """

    metrics: Iterable[CreateRunPlanFromConfigMetric]
    """
    Metric definitions to include in this run plan. Reference each by `id` (UUID) or
    `slug`.
    Optional when the attached `flows` carry the grading: metrics a flow declares
    itself (with `includeFlowMetrics`), or the Agent Expectations and Keypad Entry
    metrics a run adds for flows with expectations or expected keypad entries (with
    `includeAutomaticMetrics`). A plan with nothing to grade is rejected with a 400.
    """

    no_response_retry_backoff_seconds: Annotated[int, PropertyInfo(alias="noResponseRetryBackoffSeconds")]
    """
    Seconds a retry waits before it dials (30-600). Only used when
    `maxNoResponseRetries` is above 0.
    """

    personas: Iterable[CreateRunPlanFromConfigAgentEndpoint]
    """
    Personas to include in this run plan. Required with `scenarios`; ignored with
    `flows`, where each variant carries its own persona.
    """

    scenarios: Iterable[CreateRunPlanFromConfigScenario]
    """
    Deprecated: use `flows` instead. Scenarios to include in this run plan. The same
    scenario ID can appear multiple times with different variables.
    """

    silence_timeout_seconds: Annotated[int, PropertyInfo(alias="silenceTimeoutSeconds")]
    """Timeout in seconds for silence detection"""


class CreateRunPlanFromTemplateQuestion(TypedDict, total=False):
    ask: Required[str]
    """The question the caller asks the agent."""

    expect: Required[str]
    """The answer the agent must give, judged against the transcript."""


class CreateRunPlanFromTemplate(TypedDict, total=False):
    """
    Save one of the built-in templates as a run plan, configured for your agent,
    without running it.
    """

    agent_endpoints: Required[
        Annotated[Iterable[CreateRunPlanFromConfigAgentEndpoint], PropertyInfo(alias="agentEndpoints")]
    ]
    """The agent endpoints to call. No template can know these."""

    direction: Required[Literal["INBOUND", "OUTBOUND"]]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

    template: Required[str]
    """The template to run, as listed by GET /v1/simulation/template."""

    additional_metrics: Annotated[Iterable[CreateRunPlanFromConfigMetric], PropertyInfo(alias="additionalMetrics")]
    """
    Metrics to collect on top of the template's own, referenced by `id` or `slug`
    like a plan's `metrics`. The template's metrics and checks always run; naming
    one of them here again keeps it once, with the success criteria you set on it.
    """

    comparison_baseline: Annotated[Optional[str], PropertyInfo(alias="comparisonBaseline")]
    """
    The sweep's reference value, shown first in the results. Defaults to the
    template's own baseline, as returned by GET /v1/simulation/template. Whether a
    value did significantly worse does not depend on it: that is decided against
    every other value combined.
    Send it with `comparisonValues` and it must be one of them, or the request is
    rejected: anchoring every difference to an arm the run never made would measure
    it against nothing. Leave it out and the template's own baseline is used, and
    quietly dropped if your narrowing excluded it, since that one you did not
    choose.
    """

    comparison_values: Annotated[List[Union[str, ComparisonArm]], PropertyInfo(alias="comparisonValues")]
    """
    The arms of the sweep to run, for a template that sweeps one (GET
    /v1/simulation/template returns `sweep.property` for those that do). This is
    what the run costs: the flow is called once per arm, so ten arms is ten times
    the calls of one.
    Omit it to run every value the property has, plain, which for `accent-handling`
    is more than twenty. Send a subset to narrow it, for example the three accents
    you actually serve. An object entry pins something on that arm only, such as a
    noise level per bed on `background-noise-robustness`: `{ "value": "OFFICE",
    "backgroundNoiseVolume": 0.6 }` plays OFFICE at 60% while the other beds keep
    the default. See `POST /v1/simulation/plan`.
    """

    end_call_phrases: Annotated[SequenceNotStr[str], PropertyInfo(alias="endCallPhrases")]
    """Phrases that trigger end of call. Empty array disables the feature."""

    end_call_reasons: Annotated[SequenceNotStr[str], PropertyInfo(alias="endCallReasons")]
    """
    Semantic conditions that trigger end of call. The LLM evaluates the conversation
    against these conditions. Defaults to the template's `defaultEndCallReasons`, as
    returned by GET /v1/simulation/template. Pass an empty array to run with none.
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

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """For `question-answer-check`: the environment the calls run in."""

    execution_mode: Annotated[
        Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"], PropertyInfo(alias="executionMode")
    ]
    """Execution mode (PARALLEL or SEQUENTIAL)"""

    flows: Iterable[CreateRunPlanFromConfigFlow]
    """
    The flows to run, in the same shape a run plan takes them.
    Required when the template lists no flows of its own: it presets what to
    measure, and this says what to measure it on. Optional when it does, where these
    REPLACE the ones it would have run, so you can narrow a suite to the cases you
    care about. Either way, GET /v1/simulation/template lists the flows and variant
    ids each template covers.
    On a template that sweeps a property, every value runs exactly what you select
    here: the happy path, the edge cases you name, or `edgeCases: "ALL"`. Each
    selected case is a call per value per iteration, so naming three edge cases
    triples the run.
    """

    iteration_count: Annotated[int, PropertyInfo(alias="iterationCount")]
    """
    Runs per test case (1-10000). Defaults to 1, or to 6 for a template that sweeps
    a property. A sweep needs at least 5 calls per value (test cases per value times
    iterations) to compare its values, and a lower count is refused with 400.
    """

    max_concurrent_jobs: Annotated[int, PropertyInfo(alias="maxConcurrentJobs")]
    """Maximum number of concurrent simulation jobs"""

    max_no_response_retries: Annotated[int, PropertyInfo(alias="maxNoResponseRetries")]
    """
    How many more times to run a test case when the agent under test never responds:
    it never speaks on a call or never replies in a chat (0-10). 0 turns retries
    off. Failed checks and failures on Roark’s side are never retried.
    Each retry is a separate attempt, billed like any other, so a plan retrying N
    times can place up to N + 1 calls per test case. Every silent attempt stays on
    the run with its own call; the run settles once each test case has a final
    attempt, and the agent never spoke verdict is judged on each test case’s last
    attempt.
    """

    max_simulation_duration_seconds: Annotated[int, PropertyInfo(alias="maxSimulationDurationSeconds")]
    """
    Defaults to the template's `defaultMaxSimulationDurationSeconds`, as returned by
    GET /v1/simulation/template.
    """

    name: str
    """Name of the run plan. Defaults to the template's name and the date."""

    no_response_retry_backoff_seconds: Annotated[int, PropertyInfo(alias="noResponseRetryBackoffSeconds")]
    """
    Seconds a retry waits before it dials (30-600). Only used when
    `maxNoResponseRetries` is above 0.
    """

    persona_id: Annotated[str, PropertyInfo(alias="personaId")]
    """For `question-answer-check`: the persona that asks the questions."""

    questions: Iterable[CreateRunPlanFromTemplateQuestion]
    """
    For the `question-answer-check` template: the questions to ask and the answer
    expected for each. Every question runs as its own graded call.
    """

    silence_timeout_seconds: Annotated[int, PropertyInfo(alias="silenceTimeoutSeconds")]
    """Timeout in seconds for silence detection"""


SimulationRunPlanCreateParams: TypeAlias = Union[CreateRunPlanFromConfig, CreateRunPlanFromTemplate]
