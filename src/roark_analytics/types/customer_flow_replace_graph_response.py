# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "CustomerFlowReplaceGraphResponse",
    "Data",
    "DataEdgeCase",
    "DataEdgeCaseScriptedFlowVariant",
    "DataEdgeCaseScriptedFlowVariantAdditionalExpectation",
    "DataEdgeCaseScriptedFlowVariantEnvironment",
    "DataEdgeCaseScriptedFlowVariantPersonaOverride",
    "DataEdgeCaseImprovFlowVariant",
    "DataEdgeCaseImprovFlowVariantAdditionalExpectation",
    "DataEdgeCaseImprovFlowVariantEnvironment",
    "DataEdgeCaseImprovFlowVariantPersonaOverride",
    "DataEdgeCaseVoicemailFlowVariant",
    "DataEdgeCaseVoicemailFlowVariantAdditionalExpectation",
    "DataEdgeCaseVoicemailFlowVariantEnvironment",
    "DataEdgeCaseVoicemailFlowVariantPersonaOverride",
    "DataHappyPath",
    "DataHappyPathScriptedFlowVariant",
    "DataHappyPathScriptedFlowVariantAdditionalExpectation",
    "DataHappyPathScriptedFlowVariantEnvironment",
    "DataHappyPathScriptedFlowVariantPersonaOverride",
    "DataHappyPathImprovFlowVariant",
    "DataHappyPathImprovFlowVariantAdditionalExpectation",
    "DataHappyPathImprovFlowVariantEnvironment",
    "DataHappyPathImprovFlowVariantPersonaOverride",
    "DataHappyPathVoicemailFlowVariant",
    "DataHappyPathVoicemailFlowVariantAdditionalExpectation",
    "DataHappyPathVoicemailFlowVariantEnvironment",
    "DataHappyPathVoicemailFlowVariantPersonaOverride",
]


class DataEdgeCaseScriptedFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataEdgeCaseScriptedFlowVariantEnvironment(BaseModel):
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


class DataEdgeCaseScriptedFlowVariantPersonaOverride(BaseModel):
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


class DataEdgeCaseScriptedFlowVariant(BaseModel):
    """One path through a scripted flow.

    The path engine owns which paths exist, so editing the graph is what creates and removes these.
    """

    id: str

    additional_expectations: List[DataEdgeCaseScriptedFlowVariantAdditionalExpectation] = FieldInfo(
        alias="additionalExpectations"
    )
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[DataEdgeCaseScriptedFlowVariantEnvironment] = None
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[DataEdgeCaseScriptedFlowVariantPersonaOverride] = FieldInfo(
        alias="personaOverride", default=None
    )
    """The persona this runs as instead of the happy path's. Null means it inherits."""

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


class DataEdgeCaseImprovFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataEdgeCaseImprovFlowVariantEnvironment(BaseModel):
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


class DataEdgeCaseImprovFlowVariantPersonaOverride(BaseModel):
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


class DataEdgeCaseImprovFlowVariant(BaseModel):
    """One brief to run an improv flow with."""

    id: str

    additional_expectations: List[DataEdgeCaseImprovFlowVariantAdditionalExpectation] = FieldInfo(
        alias="additionalExpectations"
    )
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[DataEdgeCaseImprovFlowVariantEnvironment] = None
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[DataEdgeCaseImprovFlowVariantPersonaOverride] = FieldInfo(
        alias="personaOverride", default=None
    )
    """The persona this runs as instead of the happy path's. Null means it inherits."""

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


class DataEdgeCaseVoicemailFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataEdgeCaseVoicemailFlowVariantEnvironment(BaseModel):
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


class DataEdgeCaseVoicemailFlowVariantPersonaOverride(BaseModel):
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


class DataEdgeCaseVoicemailFlowVariant(BaseModel):
    """One voicemail greeting."""

    id: str

    additional_expectations: List[DataEdgeCaseVoicemailFlowVariantAdditionalExpectation] = FieldInfo(
        alias="additionalExpectations"
    )
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[DataEdgeCaseVoicemailFlowVariantEnvironment] = None
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[DataEdgeCaseVoicemailFlowVariantPersonaOverride] = FieldInfo(
        alias="personaOverride", default=None
    )
    """The persona this runs as instead of the happy path's. Null means it inherits."""

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId", default=None)

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(
        alias="precededByCustomerFlowVariantId", default=None
    )

    title: str

    type: Literal["VOICEMAIL"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


DataEdgeCase: TypeAlias = Annotated[
    Union[DataEdgeCaseScriptedFlowVariant, DataEdgeCaseImprovFlowVariant, DataEdgeCaseVoicemailFlowVariant],
    PropertyInfo(discriminator="type"),
]


class DataHappyPathScriptedFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataHappyPathScriptedFlowVariantEnvironment(BaseModel):
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


class DataHappyPathScriptedFlowVariantPersonaOverride(BaseModel):
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


class DataHappyPathScriptedFlowVariant(BaseModel):
    """One path through a scripted flow.

    The path engine owns which paths exist, so editing the graph is what creates and removes these.
    """

    id: str

    additional_expectations: List[DataHappyPathScriptedFlowVariantAdditionalExpectation] = FieldInfo(
        alias="additionalExpectations"
    )
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[DataHappyPathScriptedFlowVariantEnvironment] = None
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[DataHappyPathScriptedFlowVariantPersonaOverride] = FieldInfo(
        alias="personaOverride", default=None
    )
    """The persona this runs as instead of the happy path's. Null means it inherits."""

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


class DataHappyPathImprovFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataHappyPathImprovFlowVariantEnvironment(BaseModel):
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


class DataHappyPathImprovFlowVariantPersonaOverride(BaseModel):
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


class DataHappyPathImprovFlowVariant(BaseModel):
    """One brief to run an improv flow with."""

    id: str

    additional_expectations: List[DataHappyPathImprovFlowVariantAdditionalExpectation] = FieldInfo(
        alias="additionalExpectations"
    )
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[DataHappyPathImprovFlowVariantEnvironment] = None
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[DataHappyPathImprovFlowVariantPersonaOverride] = FieldInfo(
        alias="personaOverride", default=None
    )
    """The persona this runs as instead of the happy path's. Null means it inherits."""

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


class DataHappyPathVoicemailFlowVariantAdditionalExpectation(BaseModel):
    """One thing the agent under test is graded against."""

    id: str

    prompt: str
    """What the agent under test is graded against."""


class DataHappyPathVoicemailFlowVariantEnvironment(BaseModel):
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


class DataHappyPathVoicemailFlowVariantPersonaOverride(BaseModel):
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


class DataHappyPathVoicemailFlowVariant(BaseModel):
    """One voicemail greeting."""

    id: str

    additional_expectations: List[DataHappyPathVoicemailFlowVariantAdditionalExpectation] = FieldInfo(
        alias="additionalExpectations"
    )
    """Graded on top of the flow's own expectations, for this variant only."""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    environment: Optional[DataHappyPathVoicemailFlowVariantEnvironment] = None
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    is_generated: bool = FieldInfo(alias="isGenerated")

    persona_override: Optional[DataHappyPathVoicemailFlowVariantPersonaOverride] = FieldInfo(
        alias="personaOverride", default=None
    )
    """The persona this runs as instead of the happy path's. Null means it inherits."""

    preceded_by_customer_flow_id: Optional[str] = FieldInfo(alias="precededByCustomerFlowId", default=None)

    preceded_by_customer_flow_variant_id: Optional[str] = FieldInfo(
        alias="precededByCustomerFlowVariantId", default=None
    )

    title: str

    type: Literal["VOICEMAIL"]

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


DataHappyPath: TypeAlias = Union[
    DataHappyPathScriptedFlowVariant, DataHappyPathImprovFlowVariant, DataHappyPathVoicemailFlowVariant, None
]


class Data(BaseModel):
    edge_cases: List[DataEdgeCase] = FieldInfo(alias="edgeCases")
    """The edge cases after the write."""

    graph: List["FlowStep"]

    happy_path: Optional[DataHappyPath] = FieldInfo(alias="happyPath", default=None)
    """The way a customer flow is meant to go."""

    variants_reshaped: bool = FieldInfo(alias="variantsReshaped")
    """
    True when the write changed the set of paths, so the flow's variants were
    re-seeded and any variant id you were holding may no longer exist.
    """

    warnings: List[str]


class CustomerFlowReplaceGraphResponse(BaseModel):
    data: Data


from .flow_step import FlowStep
