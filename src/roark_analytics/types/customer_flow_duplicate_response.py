# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .flow_step import FlowStep

__all__ = [
    "CustomerFlowDuplicateResponse",
    "ImprovCustomerFlow",
    "ImprovCustomerFlowEdgeCase",
    "ImprovCustomerFlowEdgeCaseHandoffPersona",
    "ScriptedCustomerFlow",
    "ScriptedCustomerFlowAgent",
    "ScriptedCustomerFlowAgentExpectation",
    "ScriptedCustomerFlowEdgeCase",
    "ScriptedCustomerFlowEdgeCaseEnvironment",
    "ScriptedCustomerFlowEdgeCaseEnvironmentLineCustom",
    "ScriptedCustomerFlowEdgeCaseEnvironmentLineCustomFromAgent",
    "ScriptedCustomerFlowEdgeCasePersonaOverride",
    "ScriptedCustomerFlowFolder",
    "ScriptedCustomerFlowOffScriptPolicy",
    "VoicemailCustomerFlow",
    "VoicemailCustomerFlowEdgeCase",
]


class ScriptedCustomerFlowAgentExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class ScriptedCustomerFlowAgent(BaseModel):
    id: str
    """Unique identifier of the agent"""

    capabilities: Optional[
        List[
            Literal[
                "APPOINTMENT_BOOKING",
                "FAQ",
                "IDENTITY_VERIFICATION",
                "ACCOUNT_MANAGEMENT",
                "BILLING_AND_PAYMENTS",
                "ORDER_MANAGEMENT",
                "TROUBLESHOOTING",
                "CALL_ROUTING",
                "LEAD_QUALIFICATION",
                "COLLECTIONS",
                "OUTBOUND_CALLING",
            ]
        ]
    ]
    """What the agent handles. Null until it has been said."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    custom_id: Optional[str] = FieldInfo(alias="customId")
    """Custom identifier for the agent"""

    description: Optional[str]
    """Description of the agent"""

    industry: Optional[
        Literal[
            "HEALTHCARE",
            "FINANCIAL_SERVICES",
            "INSURANCE",
            "DEBT_COLLECTION",
            "RETAIL",
            "TRAVEL_AND_HOSPITALITY",
            "TELECOMMUNICATIONS",
            "TECHNOLOGY",
            "PUBLIC_SECTOR",
            "UTILITIES",
            "LOGISTICS",
            "AUTOMOTIVE",
            "HOME_SERVICES",
            "RESTAURANTS",
            "EDUCATION",
            "RECRUITING_AND_STAFFING",
            "OTHER",
        ]
    ]
    """The industry the agent serves"""

    industry_description: Optional[str] = FieldInfo(alias="industryDescription")
    """
    The industry in the customer's own words, when none of the listed ones fits
    (industry OTHER)
    """

    name: str
    """Name of the agent"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    website_url: Optional[str] = FieldInfo(alias="websiteUrl")
    """The business's website, which simulation setup reads"""


class ScriptedCustomerFlowEdgeCaseEnvironmentLineCustomFromAgent(BaseModel):
    packet_loss_percent: float = FieldInfo(alias="packetLossPercent")
    """Share of packets lost, 0 to 20 in steps of 0.5."""

    mean_burst_packets: Optional[int] = FieldInfo(alias="meanBurstPackets", default=None)
    """Mean length of a loss gap in 20 ms packets, 2 to 10. Omit for random loss."""


class ScriptedCustomerFlowEdgeCaseEnvironmentLineCustom(BaseModel):
    """The per-direction loss of a CUSTOM line."""

    from_agent: Optional[ScriptedCustomerFlowEdgeCaseEnvironmentLineCustomFromAgent] = FieldInfo(
        alias="fromAgent", default=None
    )
    """
    The agent's audio on its way to the caller: what the caller hears. Omit for no
    loss.
    """

    to_agent: Optional[ScriptedCustomerFlowEdgeCaseEnvironmentLineCustomFromAgent] = FieldInfo(
        alias="toAgent", default=None
    )
    """
    The caller's audio on its way to the agent: what the agent hears. Omit for no
    loss.
    """


class ScriptedCustomerFlowEdgeCaseEnvironment(BaseModel):
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    id: str

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

    background_noise_volume: float = FieldInfo(alias="backgroundNoiseVolume")

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    line_custom: Optional[ScriptedCustomerFlowEdgeCaseEnvironmentLineCustom] = FieldInfo(alias="lineCustom")
    """The loss of a CUSTOM line; null on every other."""

    line_noise: float = FieldInfo(alias="lineNoise")
    """
    Hiss on the line, both ways, from 0 (none) to 1 (heavy, about 10 dB under phone
    speech). Combines with the phone and lineQuality.
    """

    line_quality: Literal["CLEAR", "MINOR_LOSS", "CELL_EDGE", "POOR_CONNECTION", "ONE_WAY_DEGRADED", "CUSTOM"] = (
        FieldInfo(alias="lineQuality")
    )
    """
    The phone line the simulated caller is on: packet loss applied to its 20 ms
    audio packets, per direction. The loss pattern is seeded per call, so a redial
    loses the same packets. CLEAR: No loss. MINOR_LOSS: 1% random, both ways.
    CELL_EDGE: 5% in 80 ms gaps, both ways. POOR_CONNECTION: 10% in 120 ms gaps,
    both ways. ONE_WAY_DEGRADED: 8% in 80 ms gaps, toward the agent only. CUSTOM:
    the per-direction loss in `lineCustom`, up to 20% in 0.5 steps, with a mean
    burst of up to 10 packets (omit it for random loss).
    """

    name: str

    phone: Optional[Literal["LANDLINE", "MOBILE", "BLUETOOTH"]]
    """
    The phone the simulated caller is on: the codecs the call passes through, both
    ways, on top of any loss in lineQuality. Null is no phone. LANDLINE: The narrow
    band of a phone handset and the codec of the phone network. MOBILE: The narrow
    band and the compressed voice codec of a mobile call. BLUETOOTH: A mobile on a
    car kit or headset: the Bluetooth link adds fizz under the voice, then the
    mobile codec.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    description: Optional[str] = None


class ScriptedCustomerFlowEdgeCasePersonaOverride(BaseModel):
    """The persona this runs as instead of the happy path's. Null means it inherits."""

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
    OCCASIONAL also cuts in where a caller like this plausibly would, and HEAVY does
    so readily, though never on every turn. The moments are chosen from what the
    agent is saying, such as reading back a number or starting a long explanation,
    not on a timer. A customer flow can also say exactly when to cut in, which
    applies at any level.
    """

    language: Literal[
        "EN",
        "ES",
        "DE",
        "HI",
        "FR",
        "NL",
        "AR",
        "EL",
        "IT",
        "ID",
        "TH",
        "JA",
        "TL",
        "MS",
        "ZH",
        "TR",
        "PT",
        "HE",
        "GU",
        "MR",
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
            "EN",
            "ES",
            "DE",
            "HI",
            "FR",
            "NL",
            "AR",
            "EL",
            "IT",
            "ID",
            "TH",
            "JA",
            "TL",
            "MS",
            "ZH",
            "TR",
            "PT",
            "HE",
            "GU",
            "MR",
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

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """
    The E.164 number every call with this persona uses, when Roark has pinned one
    for your project. Present only when set; read-only.
    """

    secondary_language: Optional[Literal["EN"]] = FieldInfo(alias="secondaryLanguage", default=None)
    """Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)"""


class ScriptedCustomerFlowEdgeCase(BaseModel):
    """
    One path through a scripted flow. The path engine owns which paths exist, so
    editing the graph is what creates and removes these.
    """

    id: str

    additional_expectations: List[ScriptedCustomerFlowAgentExpectation] = FieldInfo(alias="additionalExpectations")
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[ScriptedCustomerFlowEdgeCaseEnvironment]
    """The conditions this runs under. Null means it inherits the happy path's."""

    hold_instructions: Optional[str] = FieldInfo(alias="holdInstructions")
    """
    CUSTOM only: when the simulated customer waits quietly, written as instructions
    it follows. It stays silent until the agent speaks again or the longest wait
    runs out, then takes the turn back. Required when holdMode is CUSTOM. Up to 4000
    characters.
    """

    hold_max_seconds: Optional[int] = FieldInfo(alias="holdMaxSeconds")
    """
    The longest one wait on hold can run, in seconds, from 5 to 600. When it runs
    out the simulated customer takes the turn back. Null uses the default, 180.
    Ignored when holdMode is NEVER.
    """

    hold_mode: Optional[Literal["DEFAULT", "CUSTOM", "NEVER"]] = FieldInfo(alias="holdMode")
    """
    How the simulated customer waits quietly on hold while your agent is busy.
    DEFAULT follows Roark's built-in rules: wait when the agent asks for a moment
    ("bear with me", "let me pull that up"), and never in place of answering a
    question. CUSTOM follows holdInstructions. NEVER means this customer never
    holds. Null on an edge case uses the happy path's mode, instructions and longest
    wait together; null on the happy path is DEFAULT. Applies to improv variants and
    to the improvised turns of scripted ones.
    """

    include_flow_expectations: bool = FieldInfo(alias="includeFlowExpectations")
    """
    Whether this variant is graded on the flow's agentExpectations as well as its
    additionalExpectations. False grades it on its additionalExpectations only.
    Always true on the happy path.
    """

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[ScriptedCustomerFlowEdgeCasePersonaOverride] = FieldInfo(alias="personaOverride")
    """The persona this runs as instead of the happy path's. Null means it inherits."""

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId")

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowVariantId")

    steps: List[FlowStep]
    """
    The one path through the graph this variant runs, in order. Linear by
    construction, so these steps never nest.
    """

    title: str

    type: Literal["SCRIPTED"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    opening_line: Optional[str] = FieldInfo(alias="openingLine", default=None)

    system_key: Optional[str] = FieldInfo(alias="systemKey", default=None)


class ScriptedCustomerFlowFolder(BaseModel):
    """
    A folder that groups customer flows. A flow sits in at most one folder. Folders
    can sit inside other folders, up to 5 levels deep.
    """

    id: str

    built_in: bool = FieldInfo(alias="builtIn")
    """
    Whether Roark curates this folder. Built-in folders cannot be deleted or have
    your flows filed in them.
    """

    color: Literal[
        "GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"
    ]
    """
    The color the folder is shown with in the app. Folders share the palette labels
    use.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    description: Optional[str]
    """What belongs in this folder."""

    name: str
    """The folder name, unique within its parent folder."""

    parent_id: Optional[str] = FieldInfo(alias="parentId")
    """The folder this one sits inside, or null when it is a top-level folder."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class ScriptedCustomerFlowOffScriptPolicy(BaseModel):
    """
    STRICT only. What the simulated customer does when your agent does not say the
    expected line. Each unmatched agent utterance is an attempt: `reaction` runs per
    attempt (STAY_SILENT, REPEAT its last scripted line, RESPOND once in character
    without moving on, or SAY `sayLine`), and `then` runs when attempts reach
    `maxAttempts` or your agent stays silent for `waitSeconds` (HANG_UP ends the
    call with ended reason SCRIPT_DIVERGED, HANG_UP_INVALIDATE ends it the same way
    and invalidates the run so it is scored by nothing and counted nowhere, MOVE_ON
    advances anyway, ADAPT hands the rest of the call to loose behaviour). Null:
    stay silent, 3 attempts, hang up. The default for every agent step; an
    AGENT_TURN step can carry its own.
    """

    max_attempts: int = FieldInfo(alias="maxAttempts")

    reaction: Literal["STAY_SILENT", "REPEAT", "RESPOND", "SAY"]

    then: Literal["HANG_UP", "MOVE_ON", "ADAPT", "HANG_UP_INVALIDATE"]

    say_line: Optional[str] = FieldInfo(alias="sayLine", default=None)

    wait_seconds: Optional[int] = FieldInfo(alias="waitSeconds", default=None)


class ScriptedCustomerFlow(BaseModel):
    """A flow whose conversation is written out as a graph of turns."""

    id: str

    agent_expectations: List[ScriptedCustomerFlowAgentExpectation] = FieldInfo(alias="agentExpectations")

    agents: List[ScriptedCustomerFlowAgent]
    """The agents this flow is run against."""

    branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] = FieldInfo(alias="branchingMode")
    """
    How a run walks the graph. DETERMINISTIC ("Simulate every path" in the app)
    places one call per variant, each following its path exactly whatever the agent
    says. ADAPTIVE ("Adapt to your agent") collapses the paths into one call PER
    PERSONA, on which the simulated customer picks a branch from what the agent
    actually said. Both modes speak the exact authored lines, and neither changes
    how metrics or expectations grade.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    edge_cases: List[ScriptedCustomerFlowEdgeCase] = FieldInfo(alias="edgeCases")
    """Every other way of running this flow."""

    folder: Optional[ScriptedCustomerFlowFolder]
    """The folder this flow sits in, or null."""

    happy_path: Optional[ScriptedCustomerFlowEdgeCase] = FieldInfo(alias="happyPath")
    """
    The way this flow is meant to go. Null when the flow has none, and then every
    way is an edge case.
    """

    off_script_policy: Optional[ScriptedCustomerFlowOffScriptPolicy] = FieldInfo(alias="offScriptPolicy")

    script_adherence: Literal["LOOSE", "STRICT"] = FieldInfo(alias="scriptAdherence")
    """
    How closely a run follows the script. LOOSE (default) hands the whole script to
    the simulated customer as one prompt; it keeps the call moving whatever your
    agent says. STRICT runs the script as a state machine on the agent service: at
    every agent step the simulated customer waits, silent, until your agent has said
    the expected line, and only then moves on. Scripted flows only; STRICT needs the
    agent-service transport and is not available on realtime models.
    """

    source: Literal["SYSTEM", "CUSTOM"]

    title: str

    type: Literal["SCRIPTED"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    description: Optional[str] = None

    graph: Optional[List[FlowStep]] = None
    """
    The conversation, as a graph of steps. Present on a single flow; omitted from
    the list, where reading it would mean walking the project step graph once per
    row.
    """


class ImprovCustomerFlowEdgeCaseHandoffPersona(BaseModel):
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
    OCCASIONAL also cuts in where a caller like this plausibly would, and HEAVY does
    so readily, though never on every turn. The moments are chosen from what the
    agent is saying, such as reading back a number or starting a long explanation,
    not on a timer. A customer flow can also say exactly when to cut in, which
    applies at any level.
    """

    language: Literal[
        "EN",
        "ES",
        "DE",
        "HI",
        "FR",
        "NL",
        "AR",
        "EL",
        "IT",
        "ID",
        "TH",
        "JA",
        "TL",
        "MS",
        "ZH",
        "TR",
        "PT",
        "HE",
        "GU",
        "MR",
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
            "EN",
            "ES",
            "DE",
            "HI",
            "FR",
            "NL",
            "AR",
            "EL",
            "IT",
            "ID",
            "TH",
            "JA",
            "TL",
            "MS",
            "ZH",
            "TR",
            "PT",
            "HE",
            "GU",
            "MR",
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

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """
    The E.164 number every call with this persona uses, when Roark has pinned one
    for your project. Present only when set; read-only.
    """

    secondary_language: Optional[Literal["EN"]] = FieldInfo(alias="secondaryLanguage", default=None)
    """Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)"""


class ImprovCustomerFlowEdgeCase(BaseModel):
    """One brief to run an improv flow with."""

    id: str

    additional_expectations: List[ScriptedCustomerFlowAgentExpectation] = FieldInfo(alias="additionalExpectations")
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[ScriptedCustomerFlowEdgeCaseEnvironment]
    """The conditions this runs under. Null means it inherits the happy path's."""

    handoff_personas: List[ImprovCustomerFlowEdgeCaseHandoffPersona] = FieldInfo(alias="handoffPersonas")
    """
    The personas this brief hands the phone to, in order of first mention. Empty
    when the brief inherits the happy path's: read the happy path's list.
    """

    hold_instructions: Optional[str] = FieldInfo(alias="holdInstructions")
    """
    CUSTOM only: when the simulated customer waits quietly, written as instructions
    it follows. It stays silent until the agent speaks again or the longest wait
    runs out, then takes the turn back. Required when holdMode is CUSTOM. Up to 4000
    characters.
    """

    hold_max_seconds: Optional[int] = FieldInfo(alias="holdMaxSeconds")
    """
    The longest one wait on hold can run, in seconds, from 5 to 600. When it runs
    out the simulated customer takes the turn back. Null uses the default, 180.
    Ignored when holdMode is NEVER.
    """

    hold_mode: Optional[Literal["DEFAULT", "CUSTOM", "NEVER"]] = FieldInfo(alias="holdMode")
    """
    How the simulated customer waits quietly on hold while your agent is busy.
    DEFAULT follows Roark's built-in rules: wait when the agent asks for a moment
    ("bear with me", "let me pull that up"), and never in place of answering a
    question. CUSTOM follows holdInstructions. NEVER means this customer never
    holds. Null on an edge case uses the happy path's mode, instructions and longest
    wait together; null on the happy path is DEFAULT. Applies to improv variants and
    to the improvised turns of scripted ones.
    """

    include_flow_expectations: bool = FieldInfo(alias="includeFlowExpectations")
    """
    Whether this variant is graded on the flow's agentExpectations as well as its
    additionalExpectations. False grades it on its additionalExpectations only.
    Always true on the happy path.
    """

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[ScriptedCustomerFlowEdgeCasePersonaOverride] = FieldInfo(alias="personaOverride")
    """The persona this runs as instead of the happy path's. Null means it inherits."""

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId")

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowVariantId")

    title: str

    type: Literal["IMPROV"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    opening_line: Optional[str] = FieldInfo(alias="openingLine", default=None)
    """
    What the simulated customer says word for word as the call connects. Null on an
    edge case inherits the happy path's; null on the happy path waits for your agent
    to speak first. Ignored when a preceding flow runs first. Cannot use
    {{variables}}.
    """

    prompt: Optional[str] = None
    """
    The brief the simulated customer improvises from. A `@{persona:<id>}` mention
    hands the phone to that persona mid-call; the sentences around the mention say
    when. Caller cues steer the caller from that point in the brief:
    `#{emotion:<emotion>}`, `#{language:<ISO 639-1 code>}`,
    `#{noise:<environmentId>}`, and `#{interrupt}`, whose sentence says when to cut
    in on your agent. Cues are voice only. See "Caller cues" in the customer flows
    concept.
    """

    system_key: Optional[str] = FieldInfo(alias="systemKey", default=None)


class ImprovCustomerFlow(BaseModel):
    """
    A flow whose conversation is not written out: each variant gives the simulated
    customer a brief and lets it improvise.
    """

    id: str

    agent_expectations: List[ScriptedCustomerFlowAgentExpectation] = FieldInfo(alias="agentExpectations")

    agents: List[ScriptedCustomerFlowAgent]
    """The agents this flow is run against."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    edge_cases: List[ImprovCustomerFlowEdgeCase] = FieldInfo(alias="edgeCases")
    """Every other way of running this flow."""

    folder: Optional[ScriptedCustomerFlowFolder]
    """The folder this flow sits in, or null."""

    happy_path: Optional[ImprovCustomerFlowEdgeCase] = FieldInfo(alias="happyPath")
    """
    The way this flow is meant to go. Null when the flow has none, and then every
    way is an edge case.
    """

    source: Literal["SYSTEM", "CUSTOM"]

    title: str

    type: Literal["IMPROV"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    description: Optional[str] = None


class VoicemailCustomerFlowEdgeCase(BaseModel):
    """One voicemail greeting."""

    id: str

    additional_expectations: List[ScriptedCustomerFlowAgentExpectation] = FieldInfo(alias="additionalExpectations")
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[ScriptedCustomerFlowEdgeCaseEnvironment]
    """The conditions this runs under. Null means it inherits the happy path's."""

    hold_instructions: Optional[str] = FieldInfo(alias="holdInstructions")
    """
    CUSTOM only: when the simulated customer waits quietly, written as instructions
    it follows. It stays silent until the agent speaks again or the longest wait
    runs out, then takes the turn back. Required when holdMode is CUSTOM. Up to 4000
    characters.
    """

    hold_max_seconds: Optional[int] = FieldInfo(alias="holdMaxSeconds")
    """
    The longest one wait on hold can run, in seconds, from 5 to 600. When it runs
    out the simulated customer takes the turn back. Null uses the default, 180.
    Ignored when holdMode is NEVER.
    """

    hold_mode: Optional[Literal["DEFAULT", "CUSTOM", "NEVER"]] = FieldInfo(alias="holdMode")
    """
    How the simulated customer waits quietly on hold while your agent is busy.
    DEFAULT follows Roark's built-in rules: wait when the agent asks for a moment
    ("bear with me", "let me pull that up"), and never in place of answering a
    question. CUSTOM follows holdInstructions. NEVER means this customer never
    holds. Null on an edge case uses the happy path's mode, instructions and longest
    wait together; null on the happy path is DEFAULT. Applies to improv variants and
    to the improvised turns of scripted ones.
    """

    include_flow_expectations: bool = FieldInfo(alias="includeFlowExpectations")
    """
    Whether this variant is graded on the flow's agentExpectations as well as its
    additionalExpectations. False grades it on its additionalExpectations only.
    Always true on the happy path.
    """

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[ScriptedCustomerFlowEdgeCasePersonaOverride] = FieldInfo(alias="personaOverride")
    """The persona this runs as instead of the happy path's. Null means it inherits."""

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId")

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowVariantId")

    title: str

    type: Literal["VOICEMAIL"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    opening_line: Optional[str] = FieldInfo(alias="openingLine", default=None)

    system_key: Optional[str] = FieldInfo(alias="systemKey", default=None)


class VoicemailCustomerFlow(BaseModel):
    """A flow that leaves a voicemail. Curated by Roark, read-only."""

    id: str

    agent_expectations: List[ScriptedCustomerFlowAgentExpectation] = FieldInfo(alias="agentExpectations")

    agents: List[ScriptedCustomerFlowAgent]
    """The agents this flow is run against."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    edge_cases: List[VoicemailCustomerFlowEdgeCase] = FieldInfo(alias="edgeCases")
    """Every other way of running this flow."""

    folder: Optional[ScriptedCustomerFlowFolder]
    """The folder this flow sits in, or null."""

    happy_path: Optional[VoicemailCustomerFlowEdgeCase] = FieldInfo(alias="happyPath")
    """
    The way this flow is meant to go. Null when the flow has none, and then every
    way is an edge case.
    """

    source: Literal["SYSTEM", "CUSTOM"]

    title: str

    type: Literal["VOICEMAIL"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    description: Optional[str] = None


class CustomerFlowDuplicateResponse(BaseModel):
    data: Union[ScriptedCustomerFlow, ImprovCustomerFlow, VoicemailCustomerFlow]
    """The conversation a simulated customer has with the agent under test."""
