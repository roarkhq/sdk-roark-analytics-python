# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ConfigApplyParams",
    "Resource",
    "ResourceUnionMember0",
    "ResourceUnionMember0Endpoint",
    "ResourceUnionMember1",
    "ResourceUnionMember2",
    "ResourceUnionMember2HappyPath",
    "ResourceUnionMember2EdgeCase",
    "ResourceUnionMember3",
    "ResourceUnionMember3Graph",
    "ResourceUnionMember4",
    "ResourceUnionMember4Filter",
    "ResourceUnionMember4FilterCondition",
    "ResourceUnionMember5",
    "ResourceUnionMember5Option",
    "ResourceUnionMember5ScaleLabel",
]


class ConfigApplyParams(TypedDict, total=False):
    resources: Required[Iterable[Resource]]

    prune: bool


class ResourceUnionMember0Endpoint(TypedDict, total=False):
    direction: Required[Literal["INCOMING", "OUTGOING", "INCOMING_AND_OUTGOING"]]

    name: Required[str]

    value: Required[str]

    environment: str


class ResourceUnionMember0(TypedDict, total=False):
    kind: Required[Literal["agent"]]

    name: Required[str]

    custom_id: Annotated[Optional[str], PropertyInfo(alias="customId")]

    description: Optional[str]

    endpoints: Iterable[ResourceUnionMember0Endpoint]


class ResourceUnionMember1(TypedDict, total=False):
    accent: Required[
        Literal[
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
    ]

    gender: Required[Literal["MALE", "FEMALE"]]

    kind: Required[Literal["persona"]]

    language: Required[
        Literal[
            "EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT", "ID", "TH", "JA", "TL", "MS", "ZH", "TR", "PT", "HE"
        ]
    ]

    name: Required[str]

    background_noise: Annotated[
        Literal["NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"],
        PropertyInfo(alias="backgroundNoise"),
    ]

    backstory_prompt: Annotated[Optional[str], PropertyInfo(alias="backstoryPrompt")]

    base_emotion: Annotated[
        Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED", "DISTRACTED"],
        PropertyInfo(alias="baseEmotion"),
    ]

    confirmation_style: Annotated[Literal["EXPLICIT", "VAGUE"], PropertyInfo(alias="confirmationStyle")]

    description: Optional[str]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    has_disfluencies: Annotated[bool, PropertyInfo(alias="hasDisfluencies")]

    idle_message_max_spoken_count: Annotated[int, PropertyInfo(alias="idleMessageMaxSpokenCount")]

    idle_message_reset_count_on_user_speech_enabled: Annotated[
        bool, PropertyInfo(alias="idleMessageResetCountOnUserSpeechEnabled")
    ]

    idle_messages: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="idleMessages")]

    idle_timeout_seconds: Annotated[int, PropertyInfo(alias="idleTimeoutSeconds")]

    intent_clarity: Annotated[Literal["CLEAR", "INDIRECT", "VAGUE"], PropertyInfo(alias="intentClarity")]

    memory_reliability: Annotated[Literal["HIGH", "LOW"], PropertyInfo(alias="memoryReliability")]

    properties: Dict[str, object]

    response_timing: Annotated[Literal["RELAXED", "NORMAL", "QUICK"], PropertyInfo(alias="responseTiming")]

    secondary_language: Annotated[Optional[Literal["EN"]], PropertyInfo(alias="secondaryLanguage")]

    speech_clarity: Annotated[Literal["CLEAR", "VAGUE", "RAMBLING"], PropertyInfo(alias="speechClarity")]

    speech_pace: Annotated[
        Literal["SUPER_SLOW", "SLOW", "NORMAL", "FAST", "SUPER_FAST"], PropertyInfo(alias="speechPace")
    ]

    understood_languages: Annotated[
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
        ],
        PropertyInfo(alias="understoodLanguages"),
    ]


class ResourceUnionMember2HappyPath(TypedDict, total=False):
    environment: Required[str]

    persona: Required[str]

    expectations: SequenceNotStr[str]

    prompt: str

    title: str


class ResourceUnionMember2EdgeCase(TypedDict, total=False):
    name: Required[str]

    environment: str

    expectations: SequenceNotStr[str]

    persona: str

    prompt: str

    title: str


class ResourceUnionMember2(TypedDict, total=False):
    agents: Required[SequenceNotStr[str]]

    happy_path: Required[Annotated[ResourceUnionMember2HappyPath, PropertyInfo(alias="happyPath")]]

    kind: Required[Literal["flow"]]

    name: Required[str]

    type: Required[Literal["improv"]]

    description: Optional[str]

    edge_cases: Annotated[Iterable[ResourceUnionMember2EdgeCase], PropertyInfo(alias="edgeCases")]

    expectations: SequenceNotStr[str]

    title: str


class ResourceUnionMember3Graph(TypedDict, total=False):
    type: Required[
        Literal[
            "AGENT_TURN",
            "CUSTOMER_TURN",
            "CUSTOMER_FIRST_MESSAGE",
            "CUSTOMER_SILENCE",
            "CUSTOMER_DTMF",
            "VOICEMAIL",
            "SCENARIO_LINK",
        ]
    ]

    content: str

    dtmf_digits: Annotated[str, PropertyInfo(alias="dtmfDigits")]

    flow: str

    merge_into: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeInto")]

    ref: str

    silence_duration_seconds: Annotated[int, PropertyInfo(alias="silenceDurationSeconds")]

    steps: Iterable[object]


class ResourceUnionMember3(TypedDict, total=False):
    graph: Required[Iterable[ResourceUnionMember3Graph]]

    kind: Required[Literal["flow"]]

    name: Required[str]

    type: Required[Literal["scripted"]]

    agents: SequenceNotStr[str]

    branching_mode: Annotated[Literal["DETERMINISTIC", "ADAPTIVE"], PropertyInfo(alias="branchingMode")]

    description: Optional[str]

    expectations: SequenceNotStr[str]

    title: str


class ResourceUnionMember4FilterCondition(TypedDict, total=False):
    key: Required[str]

    type: Required[Literal["AGENT", "CALL_SOURCE", "CALL_PROPERTY", "INTEGRATION"]]

    operator: Literal[
        "EQUALS",
        "NOT_EQUALS",
        "CONTAINS",
        "STARTS_WITH",
        "GREATER_THAN",
        "LESS_THAN",
        "GREATER_THAN_OR_EQUALS",
        "LESS_THAN_OR_EQUALS",
    ]

    value: str


class ResourceUnionMember4Filter(TypedDict, total=False):
    conditions: Required[Iterable[ResourceUnionMember4FilterCondition]]


class ResourceUnionMember4(TypedDict, total=False):
    kind: Required[Literal["collector"]]

    metrics: Required[SequenceNotStr[str]]

    modality: Required[Literal["call", "chat"]]

    name: Required[str]

    filters: Iterable[ResourceUnionMember4Filter]

    status: Literal["ACTIVE", "INACTIVE"]


class ResourceUnionMember5Option(TypedDict, total=False):
    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]

    label: Required[str]

    description: str


class ResourceUnionMember5ScaleLabel(TypedDict, total=False):
    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]

    label: Required[str]

    range_max: Required[Annotated[float, PropertyInfo(alias="rangeMax")]]

    range_min: Required[Annotated[float, PropertyInfo(alias="rangeMin")]]

    color_hex: Annotated[str, PropertyInfo(alias="colorHex")]

    description: str


class ResourceUnionMember5(TypedDict, total=False):
    kind: Required[Literal["metric"]]

    name: Required[str]

    prompt: Required[str]

    type: Required[Literal["BOOLEAN", "SCALE", "NUMERIC", "TEXT", "CLASSIFICATION"]]

    contexts: List[Literal["CALL", "SEGMENT", "TURN"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    false_label: Annotated[str, PropertyInfo(alias="falseLabel")]

    max_selections: Annotated[int, PropertyInfo(alias="maxSelections")]

    options: Iterable[ResourceUnionMember5Option]

    participant_role: Annotated[Literal["AGENT", "CUSTOMER"], PropertyInfo(alias="participantRole")]

    scale_labels: Annotated[Iterable[ResourceUnionMember5ScaleLabel], PropertyInfo(alias="scaleLabels")]

    scale_max: Annotated[int, PropertyInfo(alias="scaleMax")]

    scale_min: Annotated[int, PropertyInfo(alias="scaleMin")]

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]

    true_label: Annotated[str, PropertyInfo(alias="trueLabel")]


Resource: TypeAlias = Union[
    ResourceUnionMember0,
    ResourceUnionMember1,
    ResourceUnionMember2,
    ResourceUnionMember3,
    ResourceUnionMember4,
    ResourceUnionMember5,
]
