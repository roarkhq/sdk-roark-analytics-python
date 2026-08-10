# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "SimulationCustomerFlowGetByIDResponse",
    "Data",
    "DataScriptedCustomerFlow",
    "DataScriptedCustomerFlowAgentExpectation",
    "DataScriptedCustomerFlowAgent",
    "DataScriptedCustomerFlowVariant",
    "DataScriptedCustomerFlowVariantAdditionalExpectation",
    "DataScriptedCustomerFlowVariantEnvironment",
    "DataScriptedCustomerFlowVariantPersonaOverride",
    "DataImprovCustomerFlow",
    "DataImprovCustomerFlowAgentExpectation",
    "DataImprovCustomerFlowAgent",
    "DataImprovCustomerFlowVariant",
    "DataImprovCustomerFlowVariantAdditionalExpectation",
    "DataImprovCustomerFlowVariantEnvironment",
    "DataImprovCustomerFlowVariantPersonaOverride",
    "DataVoicemailCustomerFlow",
    "DataVoicemailCustomerFlowAgentExpectation",
    "DataVoicemailCustomerFlowAgent",
    "DataVoicemailCustomerFlowVariant",
    "DataVoicemailCustomerFlowVariantAdditionalExpectation",
    "DataVoicemailCustomerFlowVariantEnvironment",
    "DataVoicemailCustomerFlowVariantPersonaOverride",
]


class DataScriptedCustomerFlowAgentExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataScriptedCustomerFlowAgent(BaseModel):
    id: str
    """Unique identifier of the agent"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    custom_id: Optional[str] = FieldInfo(alias="customId", default=None)
    """Custom identifier for the agent"""

    description: Optional[str] = None
    """Description of the agent"""

    name: str
    """Name of the agent"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class DataScriptedCustomerFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataScriptedCustomerFlowVariantEnvironment(BaseModel):
    """
    A simulation environment: the ambient conditions a customer flow variant runs under. The list includes both your own and the ones Roark curates for every project.
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


class DataScriptedCustomerFlowVariantPersonaOverride(BaseModel):
    """The persona this variant runs as instead of the default variant's.

    Null means it inherits.
    """

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
    """Whether the persona uses filler words like "um" and "uh" """

    idle_message_max_spoken_count: int = FieldInfo(alias="idleMessageMaxSpokenCount")
    """Maximum number of idle messages the persona will send before giving up"""

    idle_message_reset_count_on_user_speech_enabled: bool = FieldInfo(alias="idleMessageResetCountOnUserSpeechEnabled")
    """Whether the idle message counter resets when the agent speaks"""

    idle_messages: Optional[List[str]] = FieldInfo(alias="idleMessages", default=None)
    """Messages the persona will say when the agent goes silent during a call.

    null = "Automatic": language-appropriate defaults are used at call time.
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
    """Languages the persona can understand.

    Multilingual combinations are limited by multilingual speech recognition
    support.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    backstory_prompt: Optional[str] = FieldInfo(alias="backstoryPrompt", default=None)
    """Background story and behavioral patterns for the persona"""

    description: Optional[str] = None
    """Human-readable description of the persona"""

    secondary_language: Optional[Literal["EN"]] = FieldInfo(alias="secondaryLanguage", default=None)
    """
    Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)
    """


class DataScriptedCustomerFlowVariant(BaseModel):
    """One path through a scripted flow.

    The path engine owns which paths exist, so editing the graph is what creates and removes these.
    """

    id: str

    additional_expectations: List[DataScriptedCustomerFlowVariantAdditionalExpectation] = FieldInfo(
        alias="additionalExpectations"
    )
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[DataScriptedCustomerFlowVariantEnvironment] = None
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    is_default: bool = FieldInfo(alias="isDefault")

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[DataScriptedCustomerFlowVariantPersonaOverride] = FieldInfo(
        alias="personaOverride", default=None
    )
    """The persona this variant runs as instead of the default variant's.

    Null means it inherits.
    """

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId", default=None)

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(
        alias="precededByCustomerFlowVariantId", default=None
    )

    steps: List["FlowStep"]
    """The one path through the graph this variant runs, in order.

    Linear by construction, so these steps never nest.
    """

    title: str

    type: Literal["SCRIPTED"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class DataScriptedCustomerFlow(BaseModel):
    """A flow whose conversation is written out as a graph of turns."""

    id: str

    agent_expectations: List[DataScriptedCustomerFlowAgentExpectation] = FieldInfo(alias="agentExpectations")

    agents: List[DataScriptedCustomerFlowAgent]
    """The agents this flow is run against."""

    branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] = FieldInfo(alias="branchingMode")
    """DETERMINISTIC runs one variant per path through the graph.

    ADAPTIVE collapses the paths into a single variant the simulated customer adapts
    across.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    source: Literal["SYSTEM", "CUSTOM"]

    title: str

    type: Literal["SCRIPTED"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    variants: List[DataScriptedCustomerFlowVariant]

    description: Optional[str] = None

    graph: Optional[List["FlowStep"]] = None
    """The conversation, as a graph of steps.

    Present on a single flow; omitted from the list, where reading it would mean
    walking the project step graph once per row.
    """


class DataImprovCustomerFlowAgentExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataImprovCustomerFlowAgent(BaseModel):
    id: str
    """Unique identifier of the agent"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    custom_id: Optional[str] = FieldInfo(alias="customId", default=None)
    """Custom identifier for the agent"""

    description: Optional[str] = None
    """Description of the agent"""

    name: str
    """Name of the agent"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class DataImprovCustomerFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataImprovCustomerFlowVariantEnvironment(BaseModel):
    """
    A simulation environment: the ambient conditions a customer flow variant runs under. The list includes both your own and the ones Roark curates for every project.
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


class DataImprovCustomerFlowVariantPersonaOverride(BaseModel):
    """The persona this variant runs as instead of the default variant's.

    Null means it inherits.
    """

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
    """Whether the persona uses filler words like "um" and "uh" """

    idle_message_max_spoken_count: int = FieldInfo(alias="idleMessageMaxSpokenCount")
    """Maximum number of idle messages the persona will send before giving up"""

    idle_message_reset_count_on_user_speech_enabled: bool = FieldInfo(alias="idleMessageResetCountOnUserSpeechEnabled")
    """Whether the idle message counter resets when the agent speaks"""

    idle_messages: Optional[List[str]] = FieldInfo(alias="idleMessages", default=None)
    """Messages the persona will say when the agent goes silent during a call.

    null = "Automatic": language-appropriate defaults are used at call time.
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
    """Languages the persona can understand.

    Multilingual combinations are limited by multilingual speech recognition
    support.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    backstory_prompt: Optional[str] = FieldInfo(alias="backstoryPrompt", default=None)
    """Background story and behavioral patterns for the persona"""

    description: Optional[str] = None
    """Human-readable description of the persona"""

    secondary_language: Optional[Literal["EN"]] = FieldInfo(alias="secondaryLanguage", default=None)
    """
    Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)
    """


class DataImprovCustomerFlowVariant(BaseModel):
    """One brief to run an improv flow with."""

    id: str

    additional_expectations: List[DataImprovCustomerFlowVariantAdditionalExpectation] = FieldInfo(
        alias="additionalExpectations"
    )
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[DataImprovCustomerFlowVariantEnvironment] = None
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    is_default: bool = FieldInfo(alias="isDefault")

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[DataImprovCustomerFlowVariantPersonaOverride] = FieldInfo(
        alias="personaOverride", default=None
    )
    """The persona this variant runs as instead of the default variant's.

    Null means it inherits.
    """

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId", default=None)

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(
        alias="precededByCustomerFlowVariantId", default=None
    )

    title: str

    type: Literal["IMPROV"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    prompt: Optional[str] = None
    """The brief the simulated customer improvises from."""


class DataImprovCustomerFlow(BaseModel):
    """
    A flow whose conversation is not written out: each variant gives the simulated customer a brief and lets it improvise.
    """

    id: str

    agent_expectations: List[DataImprovCustomerFlowAgentExpectation] = FieldInfo(alias="agentExpectations")

    agents: List[DataImprovCustomerFlowAgent]
    """The agents this flow is run against."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    source: Literal["SYSTEM", "CUSTOM"]

    title: str

    type: Literal["IMPROV"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    variants: List[DataImprovCustomerFlowVariant]

    description: Optional[str] = None


class DataVoicemailCustomerFlowAgentExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataVoicemailCustomerFlowAgent(BaseModel):
    id: str
    """Unique identifier of the agent"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    custom_id: Optional[str] = FieldInfo(alias="customId", default=None)
    """Custom identifier for the agent"""

    description: Optional[str] = None
    """Description of the agent"""

    name: str
    """Name of the agent"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class DataVoicemailCustomerFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataVoicemailCustomerFlowVariantEnvironment(BaseModel):
    """
    A simulation environment: the ambient conditions a customer flow variant runs under. The list includes both your own and the ones Roark curates for every project.
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


class DataVoicemailCustomerFlowVariantPersonaOverride(BaseModel):
    """The persona this variant runs as instead of the default variant's.

    Null means it inherits.
    """

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
    """Whether the persona uses filler words like "um" and "uh" """

    idle_message_max_spoken_count: int = FieldInfo(alias="idleMessageMaxSpokenCount")
    """Maximum number of idle messages the persona will send before giving up"""

    idle_message_reset_count_on_user_speech_enabled: bool = FieldInfo(alias="idleMessageResetCountOnUserSpeechEnabled")
    """Whether the idle message counter resets when the agent speaks"""

    idle_messages: Optional[List[str]] = FieldInfo(alias="idleMessages", default=None)
    """Messages the persona will say when the agent goes silent during a call.

    null = "Automatic": language-appropriate defaults are used at call time.
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
    """Languages the persona can understand.

    Multilingual combinations are limited by multilingual speech recognition
    support.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    backstory_prompt: Optional[str] = FieldInfo(alias="backstoryPrompt", default=None)
    """Background story and behavioral patterns for the persona"""

    description: Optional[str] = None
    """Human-readable description of the persona"""

    secondary_language: Optional[Literal["EN"]] = FieldInfo(alias="secondaryLanguage", default=None)
    """
    Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)
    """


class DataVoicemailCustomerFlowVariant(BaseModel):
    """One voicemail greeting."""

    id: str

    additional_expectations: List[DataVoicemailCustomerFlowVariantAdditionalExpectation] = FieldInfo(
        alias="additionalExpectations"
    )
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[DataVoicemailCustomerFlowVariantEnvironment] = None
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    is_default: bool = FieldInfo(alias="isDefault")

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[DataVoicemailCustomerFlowVariantPersonaOverride] = FieldInfo(
        alias="personaOverride", default=None
    )
    """The persona this variant runs as instead of the default variant's.

    Null means it inherits.
    """

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId", default=None)

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(
        alias="precededByCustomerFlowVariantId", default=None
    )

    title: str

    type: Literal["VOICEMAIL"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class DataVoicemailCustomerFlow(BaseModel):
    """A flow that leaves a voicemail. Curated by Roark, read-only."""

    id: str

    agent_expectations: List[DataVoicemailCustomerFlowAgentExpectation] = FieldInfo(alias="agentExpectations")

    agents: List[DataVoicemailCustomerFlowAgent]
    """The agents this flow is run against."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    source: Literal["SYSTEM", "CUSTOM"]

    title: str

    type: Literal["VOICEMAIL"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    variants: List[DataVoicemailCustomerFlowVariant]

    description: Optional[str] = None


Data: TypeAlias = Annotated[
    Union[DataScriptedCustomerFlow, DataImprovCustomerFlow, DataVoicemailCustomerFlow],
    PropertyInfo(discriminator="type"),
]


class SimulationCustomerFlowGetByIDResponse(BaseModel):
    data: Data
    """The conversation a simulated customer has with the agent under test."""


from .flow_step import FlowStep
