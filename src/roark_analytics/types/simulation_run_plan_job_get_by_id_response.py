# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationRunPlanJobGetByIDResponse",
    "Data",
    "DataSimulationJob",
    "DataSimulationJobAgentEndpoint",
    "DataSimulationJobInvalidation",
    "DataSimulationJobPersona",
    "DataSimulationJobScenario",
    "DataSweepAttribution",
    "DataSweepAttributionCheck",
    "DataSweepAttributionCheckWorseValue",
    "DataSweepAttributionValue",
    "DataVerdict",
    "DataVerdictCheck",
    "DataVerdictFailureUnionMember0",
    "DataVerdictFailureUnionMember1",
    "DataVerdictFailureUnionMember2",
    "DataVerdictFailureUnionMember3",
]


class DataSimulationJobAgentEndpoint(BaseModel):
    """Agent endpoint used in a simulation"""

    id: str
    """Agent endpoint ID"""

    name: str
    """Agent endpoint name"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber")
    """Agent endpoint phone number"""

    type: Literal["PHONE", "WEBSOCKET", "LIVEKIT", "SMALL_WEBRTC", "ELEVENLABS_WS", "KORE", "GOOGLE_CES", "DAILY"]
    """Agent endpoint type"""


class DataSimulationJobInvalidation(BaseModel):
    """
    Present when the run was invalidated: the call ended before a step its flow
    requires for a valid run, or a strict flow went off script at a step whose
    policy invalidates the run. It keeps its transcript and recording, but nothing
    scored it and it is excluded from every run total.
    """

    invalidated_at: str = FieldInfo(alias="invalidatedAt")
    """When the run was invalidated."""

    reason: Literal[
        "SCRIPT_DIVERGED", "REQUIRED_STEP_NOT_REACHED", "REQUIRED_STAGE_INCOMPLETE", "CALLER_NEVER_TOOK_OVER"
    ]
    """
    Why the result does not count. `SCRIPT_DIVERGED`: a strict flow went off script
    at a step whose off-script policy is HANG_UP_INVALIDATE.
    `REQUIRED_STAGE_INCOMPLETE`: the call ended before it got through a stage its
    flow requires. `CALLER_NEVER_TOOK_OVER`: the call opened on the persona of a
    preceding flow, which never handed the phone to the persona under test, so none
    of that persona's properties were exercised.
    """

    detail: Optional[str] = None
    """One sentence: where the script was left and what your agent did instead."""


class DataSimulationJobPersona(BaseModel):
    id: str
    """Unique identifier of the persona"""

    accent: Literal[
        "US",
        "US_X_SOUTH",
        "GB",
        "ES",
        "DE",
        "IN",
        "FR",
        "NL",
        "SA",
        "GR",
        "AU",
        "IT",
        "ID",
        "TH",
        "JP",
        "NZ",
        "PH",
        "SG",
        "MY",
        "HK",
        "TR",
        "PT",
        "IL",
    ]
    """
    Accent of the persona, defined using ISO 3166-1 alpha-2 country codes with
    optional variants
    """

    age: Literal["CHILD", "TEENAGER", "ADULT", "ELDERLY"]
    """
    How old the caller sounds and behaves. Only ages the persona's accent has a
    voice for are accepted; defaults to ADULT, which every accent supports.
    """

    background_noise: Literal[
        "NONE",
        "AIRPORT",
        "CHILDREN_PLAYING",
        "CITY",
        "COFFEE_SHOP",
        "CONSTRUCTION",
        "CRYING_BABY",
        "DRIVING",
        "LIBRARY",
        "OFFICE",
        "THUNDERSTORM",
        "TRAIN",
    ] = FieldInfo(alias="backgroundNoise")
    """Background noise setting"""

    base_emotion: Literal[
        "NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED", "DISTRACTED", "ANGRY", "ANXIOUS", "SAD"
    ] = FieldInfo(alias="baseEmotion")
    """Base emotional state of the persona"""

    confirmation_style: Literal["EXPLICIT", "VAGUE"] = FieldInfo(alias="confirmationStyle")
    """How the persona confirms information"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    gender: Literal["MALE", "FEMALE"]
    """Gender of the persona"""

    has_disfluencies: bool = FieldInfo(alias="hasDisfluencies")
    """
    Whether the persona uses filler words like "um" and "uh"
    """

    idle_message_max_spoken_count: int = FieldInfo(alias="idleMessageMaxSpokenCount")
    """Maximum number of idle messages the persona will send before giving up"""

    idle_message_reset_count_on_user_speech_enabled: bool = FieldInfo(alias="idleMessageResetCountOnUserSpeechEnabled")
    """Whether the idle message counter resets when the agent speaks"""

    idle_messages: Optional[List[str]] = FieldInfo(alias="idleMessages")
    """
    Messages the persona will say when the agent goes silent during a call. null =
    "Automatic": language-appropriate defaults are used at call time.
    """

    idle_timeout_seconds: int = FieldInfo(alias="idleTimeoutSeconds")
    """Seconds of silence before the persona sends an idle message"""

    intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] = FieldInfo(alias="intentClarity")
    """How clearly the persona expresses their intentions"""

    interruption: Literal["OFF", "BACKCHANNEL", "OCCASIONAL", "HEAVY"]
    """
    How much the persona talks over the agent while it is still speaking. OFF waits
    its turn. BACKCHANNEL makes listening noises ("mm-hm") over the agent without
    taking the floor, which tests whether the agent wrongly stops for them.
    OCCASIONAL adds cutting in on some long agent turns, HEAVY on most of them.
    Timing is randomised per turn, so two runs of the same persona do not interrupt
    at identical moments.
    """

    language: Literal[
        "EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT", "ID", "TH", "JA", "TL", "MS", "ZH", "TR", "PT", "HE"
    ]
    """Primary language ISO 639-1 code for the persona"""

    memory_reliability: Literal["HIGH", "LOW"] = FieldInfo(alias="memoryReliability")
    """How reliable the persona's memory is"""

    name: str
    """The name the agent will identify as during conversations"""

    properties: Dict[str, object]
    """Additional custom properties about the persona"""

    response_timing: Literal["RELAXED", "NORMAL", "QUICK", "BARGE_IN"] = FieldInfo(alias="responseTiming")
    """
    Deprecated and inert: it no longer affects the call. It set how long the persona
    waited once the agent stopped talking, and measured across production
    simulations it moved the reply gap by less than the noise floor, because model
    and speech latency dominate it. Every persona now uses one voice-activity
    profile. Use `interruption` for a caller who talks over the agent. Still
    accepted and stored so existing clients keep working. BARGE_IN is stored as
    `responseTiming: QUICK` with `interruption: OCCASIONAL`.
    """

    speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] = FieldInfo(alias="speechClarity")
    """Speech clarity of the persona"""

    speech_pace: Literal["SUPER_SLOW", "SLOW", "NORMAL", "FAST", "SUPER_FAST"] = FieldInfo(alias="speechPace")
    """Speech pace of the persona"""

    understood_languages: List[
        Literal[
            "EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT", "ID", "TH", "JA", "TL", "MS", "ZH", "TR", "PT", "HE"
        ]
    ] = FieldInfo(alias="understoodLanguages")
    """
    Languages the persona can understand. Multilingual combinations are limited by
    multilingual speech recognition support.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    backstory_prompt: Optional[str] = FieldInfo(alias="backstoryPrompt", default=None)
    """Background story and behavioral patterns for the persona"""

    description: Optional[str] = None
    """Human-readable description of the persona"""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """
    Label shown in place of the name across the dashboard (e.g. a short descriptor
    like "Irate Escalator"). The persona still identifies as `name` on calls. Omit
    or set null to display the name itself.
    """

    secondary_language: Optional[Literal["EN"]] = FieldInfo(alias="secondaryLanguage", default=None)
    """Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)"""


class DataSimulationJobScenario(BaseModel):
    """Scenario used in a simulation"""

    id: str
    """Scenario ID"""

    description: Optional[str] = None
    """Scenario description"""


class DataSimulationJob(BaseModel):
    agent_endpoint: DataSimulationJobAgentEndpoint = FieldInfo(alias="agentEndpoint")
    """Agent endpoint used in a simulation"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the simulation job was created"""

    invalidation: Optional[DataSimulationJobInvalidation]
    """
    Present when the result does not count (a strict flow went off script and its
    policy invalidated the run); null otherwise.
    """

    persona: DataSimulationJobPersona

    processing_status: Literal[
        "PENDING",
        "RESERVING_CAPACITY",
        "CONNECTING",
        "WAITING_FOR_OUTBOUND_CALL",
        "SIMULATING",
        "ENDING",
        "ANALYZING",
        "WAITING_FOR_LIVE_CONVERSATION",
        "EVALUATING",
        "COLLECTING_METRICS",
        "COMPLETED",
    ] = FieldInfo(alias="processingStatus")
    """Processing status. PENDING until the job starts connecting."""

    scenario: DataSimulationJobScenario
    """Scenario used in a simulation"""

    simulation_job_id: str = FieldInfo(alias="simulationJobId")
    """Simulation job ID"""

    status: Literal["PENDING", "QUEUED", "PROCESSING", "COMPLETED", "FAILED", "TIMED_OUT", "CANCELLED", "CANCELLING"]
    """Job status"""

    call_id: Optional[str] = FieldInfo(alias="callId", default=None)
    """
    ID of the call created for this simulation job. Null if the call has not been
    created yet.
    """

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)
    """When the simulation job completed"""

    roark_phone_number: Optional[str] = FieldInfo(alias="roarkPhoneNumber", default=None)
    """
    Phone number provisioned by Roark for this simulation job in E.164 format. Null
    if the simulation job is queued and has not been assigned a phone number yet.
    """

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)
    """When the simulation job started"""


class DataSweepAttributionCheckWorseValue(BaseModel):
    """A value that failed a check significantly more often than the rest of the run."""

    adjusted_p_value: float = FieldInfo(alias="adjustedPValue")
    """
    How likely a difference at least this large would be by chance alone, after
    correcting for every comparison in the run (Benjamini-Hochberg). The value is
    called worse only when this is at most `falseDiscoveryRate`.
    """

    evaluated: int

    failed: int

    failure_rate: Optional[float] = FieldInfo(alias="failureRate")
    """Share of the counted simulations at this value that failed the check, 0-100."""

    label: str

    rest_failure_rate: Optional[float] = FieldInfo(alias="restFailureRate")
    """
    The same share across every other value combined, 0-100. This is what the value
    is compared with.
    """

    value: str


class DataSweepAttributionCheck(BaseModel):
    """How one check's failures relate to the swept property."""

    attribution: Literal["PROPERTY_ATTRIBUTABLE", "FOUND_UNATTRIBUTED", "WITHIN_NOISE"]
    """
    How this check relates to the swept property:
    - `PROPERTY_ATTRIBUTABLE`: at least one value failed it significantly more often
    than every other value combined. `worseValues` names them. This is the only case
    in which a value is called worse. - `FOUND_UNATTRIBUTED`: no value stands out,
    but the check failed on at least `foundUnattributedFailureRate`% of counted
    simulations overall. A real issue with the agent on which no value stood out, so
    the run cannot tie it to the property. It does not show the property had no
    effect: a small run may be unable to see one. - `WITHIN_NOISE`: neither. Any
    differences between values are within what chance produces.
    """

    evaluated: int

    failed: int

    failure_rate: Optional[float] = FieldInfo(alias="failureRate")
    """Share of counted simulations across every value that failed the check, 0-100."""

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    metric_name: str = FieldInfo(alias="metricName")

    worse_values: List[DataSweepAttributionCheckWorseValue] = FieldInfo(alias="worseValues")
    """
    The values significantly worse than the rest, most significant first. Empty
    unless `attribution` is `PROPERTY_ATTRIBUTABLE`.
    """


class DataSweepAttributionValue(BaseModel):
    """One value of the swept property."""

    attempted: int
    """
    Simulations run at this value. Simulations that failed on the Roark platform are
    left out, since they say nothing about your agent.
    """

    counted: int
    """
    Simulations that actually tested the property: not invalidated, and graded by at
    least one check. Only these are used in the comparison.
    """

    is_baseline: bool = FieldInfo(alias="isBaseline")
    """Whether this is the baseline the plan named."""

    label: str
    """The value in words, e.g. `American`."""

    score: Optional[float]
    """
    The mean of each check's pass rate at this value, 0-100, the same rule as the
    run's `score`. Descriptive only: a lower score alone never makes a value worse.
    Null when nothing counted.
    """

    testable: bool
    """
    Whether this value had at least `minArmCalls` counted simulations. A value below
    that is "insufficient data": it is reported with its numbers but never compared
    or ranked, because a rate from one or two calls cannot be told apart from luck.
    """

    value: str
    """The stored value of the swept property, e.g. `US`."""


class DataSweepAttribution(BaseModel):
    """
    For a run that swept a property (accent, background noise, speech pace and so
    on): which check failures the property caused.
    Each value is compared with every other value combined using a one-sided Fisher
    exact test, and every comparison in the run is corrected together with
    Benjamini-Hochberg. A value is only called worse when the difference is
    statistically significant, so a value that happened to fail a few more
    simulations by chance is not reported as a problem. Invalidated simulations and
    simulations that failed on the Roark platform are left out.
    """

    caveats: List[str]
    """Plain sentences on what this run could not see, ready to show to a reader."""

    checks: List[DataSweepAttributionCheck]
    """
    Every check the run was graded on: `PROPERTY_ATTRIBUTABLE` first, then
    `FOUND_UNATTRIBUTED`, then `WITHIN_NOISE`.
    """

    false_discovery_rate: float = FieldInfo(alias="falseDiscoveryRate")
    """The Benjamini-Hochberg false discovery rate the comparisons are held to."""

    found_unattributed_failure_rate: float = FieldInfo(alias="foundUnattributedFailureRate")
    """
    The overall failure rate, 0-100, at which a check with no standout value is
    reported as `FOUND_UNATTRIBUTED`.
    """

    min_arm_calls: int = FieldInfo(alias="minArmCalls")
    """Counted simulations a value needs before it is compared."""

    minimum_detectable_gap: Optional[float] = FieldInfo(alias="minimumDetectableGap")
    """
    Roughly how many percentage points more often a value would need to fail than
    the rest of the run to be flagged at this sample size. Optimistic: it uses
    simulation counts rather than the verdicts on each check and ignores the
    correction, so checks graded on fewer simulations need larger gaps. Large when
    few simulations ran per value: finding no significant difference then means the
    run could not see one, not that none exists.
    """

    testable_value_count: int = FieldInfo(alias="testableValueCount")
    """How many values had enough counted simulations to be compared."""

    tested_comparison_count: int = FieldInfo(alias="testedComparisonCount")
    """
    How many value and check pairs were actually tested. A value can have enough
    simulations and still go untested (no other value graded that check, or too few
    verdicts on it). When this is 0 no comparison ran, so an empty `worseValues`
    everywhere means nothing was tested, not that no value did worse.
    """

    values: List[DataSweepAttributionValue]
    """Every value of the swept property, baseline first."""


class DataVerdictCheck(BaseModel):
    """
    How one check did. Present for every check the run was judged on, passing or
    not.
    A check is a metric that yields a pass/fail: a threshold (`Silence Duration <=
    2s`) or a yes/no metric you authored. Provider readings such as `Comprehension
    Failure` are observations, not checks: their `true` is whatever the underlying
    field happens to mean, so they carry no passing side and never appear here. Put
    a threshold on one to judge it.
    """

    evaluated_sims: int = FieldInfo(alias="evaluatedSims")

    inherited: bool
    """
    Whether `minPassRate` is the 80% default (`true`) or a minimum this metric set
    for itself.
    """

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    min_pass_rate: float = FieldInfo(alias="minPassRate")
    """
    THE BAR it was judged against: the share of the run's simulations it had to
    pass.
    """

    pass_rate: Optional[float] = FieldInfo(alias="passRate")
    """
    This check's own pass rate, 0-100: the share of sims it evaluated that passed
    it. Null when it evaluated nothing.
    """

    passed: bool
    """`passRate >= minPassRate`."""

    passed_sims: int = FieldInfo(alias="passedSims")

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)


class DataVerdictFailureUnionMember0(BaseModel):
    status: Literal[
        "PENDING",
        "QUEUED",
        "CREATING_SNAPSHOTS",
        "CREATING_SIMULATIONS",
        "PREPARING_CAPACITY",
        "RUNNING_SIMULATIONS",
        "COMPLETED",
        "FAILED",
        "TIMED_OUT",
        "CANCELLED",
        "CANCELLING",
        "ENDING_SIMULATIONS",
    ]
    """The status the run actually ended in."""

    type: Literal["RUN_NOT_COMPLETED"]


class DataVerdictFailureUnionMember1(BaseModel):
    evaluated_calls: int = FieldInfo(alias="evaluatedCalls")

    expected_calls: int = FieldInfo(alias="expectedCalls")

    type: Literal["INCOMPLETE_COVERAGE"]


class DataVerdictFailureUnionMember2(BaseModel):
    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    type: Literal["METRIC_NOT_EVALUATED"]

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)
    """The check’s name, for rendering the failure."""


class DataVerdictFailureUnionMember3(BaseModel):
    inherited: bool
    """Whether the missed minimum was the 80% default (`true`) or this metric's own."""

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    min_pass_rate: float = FieldInfo(alias="minPassRate")

    pass_rate: float = FieldInfo(alias="passRate")

    type: Literal["METRIC_BELOW_MIN_PASS_RATE"]

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)
    """The check’s name, for rendering the failure."""


class DataVerdict(BaseModel):
    """
    Pass/fail verdict for the run, judged against the success criteria pinned on the
    run plan when the run started.
    """

    checks: List[DataVerdictCheck]
    """
    Every check the run was judged on, with its rate and the minimum it had to
    reach.
    Thresholds and authored yes/no metrics only. See `SimulationRunPlanJobCheck` for
    why a provider reading is not one.
    """

    failures: List[
        Union[
            DataVerdictFailureUnionMember0,
            DataVerdictFailureUnionMember1,
            DataVerdictFailureUnionMember2,
            DataVerdictFailureUnionMember3,
        ]
    ]
    """Every criterion the run missed. Empty when it passed."""

    passed: bool
    """
    Whether every check cleared its own `minPassRate` (and the run completed with
    full coverage). Use this as the CI exit status.
    Never derived from `score`: a run can score 95 and still fail, or score 40 and
    still pass.
    """

    score: Optional[float]
    """
    The run's headline quality number, 0-100: the mean of each check's own pass
    rate.
    Every check weighs the same, however many simulations it evaluated, which is the
    same way `passed` treats them. It is the number the Roark dashboard shows for
    this run.
    REPORTING ONLY, for dashboards and trend lines. Nothing is judged against it.
    Null when nothing was evaluated.
    """


class Data(BaseModel):
    """Simulation run plan job with all associated simulation jobs"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    simulation_jobs: List[DataSimulationJob] = FieldInfo(alias="simulationJobs")
    """List of simulation jobs (calls) in this run plan job"""

    simulation_run_plan_id: str = FieldInfo(alias="simulationRunPlanId")
    """ID of the simulation run plan"""

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")
    """ID of the simulation run plan job"""

    status: Literal[
        "PENDING",
        "QUEUED",
        "CREATING_SNAPSHOTS",
        "CREATING_SIMULATIONS",
        "PREPARING_CAPACITY",
        "RUNNING_SIMULATIONS",
        "COMPLETED",
        "FAILED",
        "TIMED_OUT",
        "CANCELLED",
        "CANCELLING",
        "ENDING_SIMULATIONS",
    ]
    """Job status"""

    ended_at: Optional[str] = FieldInfo(alias="endedAt", default=None)
    """When the job ended"""

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)
    """When the job started"""

    sweep_attribution: Optional[DataSweepAttribution] = FieldInfo(alias="sweepAttribution", default=None)
    """
    For a run that swept a property: which check failures the property caused, which
    were not specific to it, and which values had too few simulations to compare.
    Null for a run that swept nothing, and until the run has ended.
    """

    verdict: Optional[DataVerdict] = None
    """
    Pass/fail verdict for this run. Null when the plan carried no pass/fail metric
    to judge, so an absent verdict means "nothing to judge", never a pass.
    """


class SimulationRunPlanJobGetByIDResponse(BaseModel):
    data: Data
    """Simulation run plan job with all associated simulation jobs"""
