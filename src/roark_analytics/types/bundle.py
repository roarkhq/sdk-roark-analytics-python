# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .config_flow_step import ConfigFlowStep

__all__ = [
    "Bundle",
    "ResourceUnionMember0",
    "ResourceUnionMember0Endpoint",
    "ResourceUnionMember1",
    "ResourceUnionMember2",
    "ResourceUnionMember2EdgeCase",
    "ResourceUnionMember2HappyPath",
    "ResourceUnionMember3",
    "ResourceUnionMember4",
    "ResourceUnionMember4Filter",
    "ResourceUnionMember4FilterCondition",
    "ResourceUnionMember5",
    "ResourceUnionMember5Option",
    "ResourceUnionMember5ScaleLabel",
]


class ResourceUnionMember0Endpoint(BaseModel):
    direction: Literal["INCOMING", "OUTGOING", "INCOMING_AND_OUTGOING"]

    name: str

    value: str

    environment: Optional[str] = None


class ResourceUnionMember0(BaseModel):
    kind: Literal["agent"]

    name: str

    custom_id: Optional[str] = FieldInfo(alias="customId", default=None)

    description: Optional[str] = None

    endpoints: Optional[List[ResourceUnionMember0Endpoint]] = None


class ResourceUnionMember1(BaseModel):
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

    gender: Literal["MALE", "FEMALE"]

    kind: Literal["persona"]

    language: Literal[
        "EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT", "ID", "TH", "JA", "TL", "MS", "ZH", "TR", "PT", "HE"
    ]

    name: str

    background_noise: Optional[
        Literal["NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"]
    ] = FieldInfo(alias="backgroundNoise", default=None)

    backstory_prompt: Optional[str] = FieldInfo(alias="backstoryPrompt", default=None)

    base_emotion: Optional[
        Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED", "DISTRACTED"]
    ] = FieldInfo(alias="baseEmotion", default=None)

    confirmation_style: Optional[Literal["EXPLICIT", "VAGUE"]] = FieldInfo(alias="confirmationStyle", default=None)

    description: Optional[str] = None

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    has_disfluencies: Optional[bool] = FieldInfo(alias="hasDisfluencies", default=None)

    idle_message_max_spoken_count: Optional[int] = FieldInfo(alias="idleMessageMaxSpokenCount", default=None)

    idle_message_reset_count_on_user_speech_enabled: Optional[bool] = FieldInfo(
        alias="idleMessageResetCountOnUserSpeechEnabled", default=None
    )

    idle_messages: Optional[List[str]] = FieldInfo(alias="idleMessages", default=None)

    idle_timeout_seconds: Optional[int] = FieldInfo(alias="idleTimeoutSeconds", default=None)

    intent_clarity: Optional[Literal["CLEAR", "INDIRECT", "VAGUE"]] = FieldInfo(alias="intentClarity", default=None)

    memory_reliability: Optional[Literal["HIGH", "LOW"]] = FieldInfo(alias="memoryReliability", default=None)

    properties: Optional[Dict[str, object]] = None

    response_timing: Optional[Literal["RELAXED", "NORMAL", "QUICK"]] = FieldInfo(alias="responseTiming", default=None)

    secondary_language: Optional[Literal["EN"]] = FieldInfo(alias="secondaryLanguage", default=None)

    speech_clarity: Optional[Literal["CLEAR", "VAGUE", "RAMBLING"]] = FieldInfo(alias="speechClarity", default=None)

    speech_pace: Optional[Literal["SUPER_SLOW", "SLOW", "NORMAL", "FAST", "SUPER_FAST"]] = FieldInfo(
        alias="speechPace", default=None
    )

    understood_languages: Optional[
        List[
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
            ]
        ]
    ] = FieldInfo(alias="understoodLanguages", default=None)


class ResourceUnionMember2HappyPath(BaseModel):
    environment: str

    persona: str

    expectations: Optional[List[str]] = None

    prompt: Optional[str] = None

    title: Optional[str] = None


class ResourceUnionMember2EdgeCase(BaseModel):
    name: str

    environment: Optional[str] = None

    expectations: Optional[List[str]] = None

    persona: Optional[str] = None

    prompt: Optional[str] = None

    title: Optional[str] = None


class ResourceUnionMember2(BaseModel):
    agents: List[str]

    happy_path: ResourceUnionMember2HappyPath = FieldInfo(alias="happyPath")

    kind: Literal["flow"]

    name: str

    type: Literal["improv"]

    description: Optional[str] = None

    edge_cases: Optional[List[ResourceUnionMember2EdgeCase]] = FieldInfo(alias="edgeCases", default=None)

    expectations: Optional[List[str]] = None

    title: Optional[str] = None


class ResourceUnionMember3(BaseModel):
    graph: List[ConfigFlowStep]

    kind: Literal["flow"]

    name: str

    type: Literal["scripted"]

    agents: Optional[List[str]] = None

    branching_mode: Optional[Literal["DETERMINISTIC", "ADAPTIVE"]] = FieldInfo(alias="branchingMode", default=None)

    description: Optional[str] = None

    expectations: Optional[List[str]] = None

    title: Optional[str] = None


class ResourceUnionMember4FilterCondition(BaseModel):
    key: str

    type: Literal["AGENT", "CALL_SOURCE", "CALL_PROPERTY", "INTEGRATION"]

    operator: Optional[
        Literal[
            "EQUALS",
            "NOT_EQUALS",
            "CONTAINS",
            "STARTS_WITH",
            "GREATER_THAN",
            "LESS_THAN",
            "GREATER_THAN_OR_EQUALS",
            "LESS_THAN_OR_EQUALS",
        ]
    ] = None

    value: Optional[str] = None


class ResourceUnionMember4Filter(BaseModel):
    conditions: List[ResourceUnionMember4FilterCondition]


class ResourceUnionMember4(BaseModel):
    kind: Literal["collector"]

    metrics: List[str]

    modality: Literal["call", "chat"]

    name: str

    filters: Optional[List[ResourceUnionMember4Filter]] = None

    status: Optional[Literal["ACTIVE", "INACTIVE"]] = None


class ResourceUnionMember5Option(BaseModel):
    display_order: int = FieldInfo(alias="displayOrder")

    label: str

    description: Optional[str] = None


class ResourceUnionMember5ScaleLabel(BaseModel):
    display_order: int = FieldInfo(alias="displayOrder")

    label: str

    range_max: float = FieldInfo(alias="rangeMax")

    range_min: float = FieldInfo(alias="rangeMin")

    color_hex: Optional[str] = FieldInfo(alias="colorHex", default=None)

    description: Optional[str] = None


class ResourceUnionMember5(BaseModel):
    kind: Literal["metric"]

    name: str

    prompt: str

    type: Literal["BOOLEAN", "SCALE", "NUMERIC", "TEXT", "CLASSIFICATION"]

    contexts: Optional[List[Literal["CALL", "SEGMENT", "TURN"]]] = None

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    false_label: Optional[str] = FieldInfo(alias="falseLabel", default=None)

    max_selections: Optional[int] = FieldInfo(alias="maxSelections", default=None)

    options: Optional[List[ResourceUnionMember5Option]] = None

    participant_role: Optional[Literal["AGENT", "CUSTOMER"]] = FieldInfo(alias="participantRole", default=None)

    scale_labels: Optional[List[ResourceUnionMember5ScaleLabel]] = FieldInfo(alias="scaleLabels", default=None)

    scale_max: Optional[int] = FieldInfo(alias="scaleMax", default=None)

    scale_min: Optional[int] = FieldInfo(alias="scaleMin", default=None)

    scope: Optional[Literal["GLOBAL", "PER_PARTICIPANT"]] = None

    true_label: Optional[str] = FieldInfo(alias="trueLabel", default=None)


class Bundle(BaseModel):
    resources: List[
        Union[
            ResourceUnionMember0,
            ResourceUnionMember1,
            ResourceUnionMember2,
            ResourceUnionMember3,
            ResourceUnionMember4,
            ResourceUnionMember5,
        ]
    ]

    prune: Optional[bool] = None
