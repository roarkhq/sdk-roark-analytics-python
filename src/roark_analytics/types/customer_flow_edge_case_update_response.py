# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .flow_step import FlowStep

__all__ = [
    "CustomerFlowEdgeCaseUpdateResponse",
    "ImprovFlowVariant",
    "ImprovFlowVariantHandoffPersona",
    "ScriptedFlowVariant",
    "ScriptedFlowVariantAdditionalExpectation",
    "ScriptedFlowVariantEnvironment",
    "ScriptedFlowVariantEnvironmentLineCustom",
    "ScriptedFlowVariantEnvironmentLineCustomFromAgent",
    "ScriptedFlowVariantPersonaOverride",
    "VoicemailFlowVariant",
]


class ScriptedFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class ScriptedFlowVariantEnvironmentLineCustomFromAgent(BaseModel):
    packet_loss_percent: float = FieldInfo(alias="packetLossPercent")
    """Share of packets lost, 0 to 20 in steps of 0.5."""

    mean_burst_packets: Optional[int] = FieldInfo(alias="meanBurstPackets", default=None)
    """Mean length of a loss gap in 20 ms packets, 2 to 10. Omit for random loss."""


class ScriptedFlowVariantEnvironmentLineCustom(BaseModel):
    """The per-direction loss of a CUSTOM line."""

    from_agent: Optional[ScriptedFlowVariantEnvironmentLineCustomFromAgent] = FieldInfo(alias="fromAgent", default=None)
    """
    The agent's audio on its way to the caller: what the caller hears. Omit for no
    loss.
    """

    to_agent: Optional[ScriptedFlowVariantEnvironmentLineCustomFromAgent] = FieldInfo(alias="toAgent", default=None)
    """
    The caller's audio on its way to the agent: what the agent hears. Omit for no
    loss.
    """


class ScriptedFlowVariantEnvironment(BaseModel):
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

    line_custom: Optional[ScriptedFlowVariantEnvironmentLineCustom] = FieldInfo(alias="lineCustom")
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


class ScriptedFlowVariantPersonaOverride(BaseModel):
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


class ScriptedFlowVariant(BaseModel):
    """
    One path through a scripted flow. The path engine owns which paths exist, so
    editing the graph is what creates and removes these.
    """

    id: str

    additional_expectations: List[ScriptedFlowVariantAdditionalExpectation] = FieldInfo(alias="additionalExpectations")
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[ScriptedFlowVariantEnvironment]
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

    persona_override: Optional[ScriptedFlowVariantPersonaOverride] = FieldInfo(alias="personaOverride")
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


class ImprovFlowVariantHandoffPersona(BaseModel):
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


class ImprovFlowVariant(BaseModel):
    """One brief to run an improv flow with."""

    id: str

    additional_expectations: List[ScriptedFlowVariantAdditionalExpectation] = FieldInfo(alias="additionalExpectations")
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[ScriptedFlowVariantEnvironment]
    """The conditions this runs under. Null means it inherits the happy path's."""

    handoff_personas: List[ImprovFlowVariantHandoffPersona] = FieldInfo(alias="handoffPersonas")
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

    persona_override: Optional[ScriptedFlowVariantPersonaOverride] = FieldInfo(alias="personaOverride")
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


class VoicemailFlowVariant(BaseModel):
    """One voicemail greeting."""

    id: str

    additional_expectations: List[ScriptedFlowVariantAdditionalExpectation] = FieldInfo(alias="additionalExpectations")
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[ScriptedFlowVariantEnvironment]
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

    persona_override: Optional[ScriptedFlowVariantPersonaOverride] = FieldInfo(alias="personaOverride")
    """The persona this runs as instead of the happy path's. Null means it inherits."""

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId")

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowVariantId")

    title: str

    type: Literal["VOICEMAIL"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    opening_line: Optional[str] = FieldInfo(alias="openingLine", default=None)

    system_key: Optional[str] = FieldInfo(alias="systemKey", default=None)


class CustomerFlowEdgeCaseUpdateResponse(BaseModel):
    data: Union[ScriptedFlowVariant, ImprovFlowVariant, VoicemailFlowVariant]
    """One way of running a customer flow."""
