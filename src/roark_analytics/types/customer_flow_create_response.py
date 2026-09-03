# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .flow_step import FlowStep

__all__ = [
    "CustomerFlowCreateResponse",
    "ImprovCustomerFlow",
    "ImprovCustomerFlowEdgeCase",
    "ScriptedCustomerFlow",
    "ScriptedCustomerFlowAgent",
    "ScriptedCustomerFlowAgentExpectation",
    "ScriptedCustomerFlowEdgeCase",
    "ScriptedCustomerFlowEdgeCaseEnvironment",
    "ScriptedCustomerFlowEdgeCasePersonaOverride",
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

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    custom_id: Optional[str] = FieldInfo(alias="customId")
    """Custom identifier for the agent"""

    description: Optional[str]
    """Description of the agent"""

    name: str
    """Name of the agent"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class ScriptedCustomerFlowEdgeCaseEnvironment(BaseModel):
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    id: str

    background_noise: Literal[
        "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
    ] = FieldInfo(alias="backgroundNoise")

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    name: str

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
        "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
    ] = FieldInfo(alias="backgroundNoise")
    """Background noise setting"""

    base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED", "DISTRACTED"] = (
        FieldInfo(alias="baseEmotion")
    )
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

    response_timing: Literal["RELAXED", "NORMAL", "QUICK"] = FieldInfo(alias="responseTiming")
    """
    Controls how quickly the persona responds to pauses in conversation (QUICK,
    NORMAL, RELAXED)
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

    happy_path: Optional[ScriptedCustomerFlowEdgeCase] = FieldInfo(alias="happyPath")
    """
    The way this flow is meant to go. Null when the flow has none, and then every
    way is an edge case.
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


class ImprovCustomerFlowEdgeCase(BaseModel):
    """One brief to run an improv flow with."""

    id: str

    additional_expectations: List[ScriptedCustomerFlowAgentExpectation] = FieldInfo(alias="additionalExpectations")
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[ScriptedCustomerFlowEdgeCaseEnvironment]
    """The conditions this runs under. Null means it inherits the happy path's."""

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[ScriptedCustomerFlowEdgeCasePersonaOverride] = FieldInfo(alias="personaOverride")
    """The persona this runs as instead of the happy path's. Null means it inherits."""

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId")

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowVariantId")

    title: str

    type: Literal["IMPROV"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    prompt: Optional[str] = None
    """The brief the simulated customer improvises from."""


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

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[ScriptedCustomerFlowEdgeCasePersonaOverride] = FieldInfo(alias="personaOverride")
    """The persona this runs as instead of the happy path's. Null means it inherits."""

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId")

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowVariantId")

    title: str

    type: Literal["VOICEMAIL"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


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


class CustomerFlowCreateResponse(BaseModel):
    data: Union[ScriptedCustomerFlow, ImprovCustomerFlow, VoicemailCustomerFlow]
    """The conversation a simulated customer has with the agent under test."""
