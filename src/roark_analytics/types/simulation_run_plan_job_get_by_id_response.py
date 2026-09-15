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
    Present when the run was invalidated: it keeps its transcript and recording, but
    nothing scored it and it is excluded from every run total.
    """

    invalidated_at: str = FieldInfo(alias="invalidatedAt")
    """When the run was invalidated."""

    reason: Literal["SCRIPT_DIVERGED"]
    """
    Why the result does not count. `SCRIPT_DIVERGED`: a strict flow went off script
    at a step whose off-script policy is HANG_UP_INVALIDATE.
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
        "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
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
    Controls how quickly the persona responds to pauses in conversation (QUICK,
    NORMAL, RELAXED). BARGE_IN also talks over the agent once it has held the floor
    for several seconds.
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


class DataVerdictCheck(BaseModel):
    """How one pass/fail metric did. Present for every check, passing or not."""

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

    verdict: Optional[DataVerdict] = None
    """
    Pass/fail verdict for this run. Null when the plan carried no pass/fail metric
    to judge, so an absent verdict means "nothing to judge", never a pass.
    """


class SimulationRunPlanJobGetByIDResponse(BaseModel):
    data: Data
    """Simulation run plan job with all associated simulation jobs"""
