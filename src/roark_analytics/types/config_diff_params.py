# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .config_flow_step_param import ConfigFlowStepParam

__all__ = [
    "ConfigDiffParams",
    "AgentConfig",
    "AgentConfigEndpoint",
    "AlertConfig",
    "AlertConfigAction",
    "AlertConfigActionSlack",
    "AlertEventTrigger",
    "AlertSimulationTrigger",
    "AlertThresholdTrigger",
    "CollectorConfig",
    "CollectorConfigFilter",
    "CollectorConfigFilterCondition",
    "ImprovFlowConfig",
    "ImprovFlowConfigEdgeCase",
    "ImprovFlowConfigHappyPath",
    "MetricConfig",
    "MetricConfigOption",
    "MetricConfigScaleLabel",
    "PersonaConfig",
    "ScriptedFlowConfig",
]


class AgentConfigEndpoint(TypedDict, total=False):
    direction: Required[Literal["INCOMING", "OUTGOING", "INCOMING_AND_OUTGOING"]]

    name: Required[str]

    value: Required[str]

    environment: str


class AgentConfig(TypedDict, total=False):
    kind: Required[Literal["agent"]]

    name: Required[str]

    custom_id: Annotated[Optional[str], PropertyInfo(alias="customId")]

    description: Optional[str]

    endpoints: Iterable[AgentConfigEndpoint]


class PersonaConfig(TypedDict, total=False):
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

    age: Literal["CHILD", "TEENAGER", "ADULT", "ELDERLY"]

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

    secondary_language: Annotated[Literal["EN"], PropertyInfo(alias="secondaryLanguage")]

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


class ImprovFlowConfigHappyPath(TypedDict, total=False):
    environment: Required[str]

    persona: Required[str]

    expectations: SequenceNotStr[str]

    prompt: str

    title: str


class ImprovFlowConfigEdgeCase(TypedDict, total=False):
    name: Required[str]

    environment: str

    expectations: SequenceNotStr[str]

    persona: str

    prompt: str

    title: str


class ImprovFlowConfig(TypedDict, total=False):
    agents: Required[SequenceNotStr[str]]

    happy_path: Required[Annotated[ImprovFlowConfigHappyPath, PropertyInfo(alias="happyPath")]]

    kind: Required[Literal["flow"]]

    name: Required[str]

    type: Required[Literal["improv"]]

    description: Optional[str]

    edge_cases: Annotated[Iterable[ImprovFlowConfigEdgeCase], PropertyInfo(alias="edgeCases")]

    expectations: SequenceNotStr[str]

    title: str


class ScriptedFlowConfig(TypedDict, total=False):
    graph: Required[List[ConfigFlowStepParam]]

    kind: Required[Literal["flow"]]

    name: Required[str]

    type: Required[Literal["scripted"]]

    agents: SequenceNotStr[str]

    branching_mode: Annotated[Literal["DETERMINISTIC", "ADAPTIVE"], PropertyInfo(alias="branchingMode")]

    description: Optional[str]

    expectations: SequenceNotStr[str]

    title: str


class CollectorConfigFilterCondition(TypedDict, total=False):
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


class CollectorConfigFilter(TypedDict, total=False):
    conditions: Required[Iterable[CollectorConfigFilterCondition]]


class CollectorConfig(TypedDict, total=False):
    kind: Required[Literal["collector"]]

    metrics: Required[SequenceNotStr[str]]

    modality: Required[Literal["call", "chat"]]

    name: Required[str]

    filters: Iterable[CollectorConfigFilter]

    status: Literal["ACTIVE", "INACTIVE"]


class MetricConfigOption(TypedDict, total=False):
    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]

    label: Required[str]

    description: str


class MetricConfigScaleLabel(TypedDict, total=False):
    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]

    label: Required[str]

    range_max: Required[Annotated[float, PropertyInfo(alias="rangeMax")]]

    range_min: Required[Annotated[float, PropertyInfo(alias="rangeMin")]]

    color_hex: Annotated[str, PropertyInfo(alias="colorHex")]

    description: str


class MetricConfig(TypedDict, total=False):
    kind: Required[Literal["metric"]]

    name: Required[str]

    prompt: Required[str]

    type: Required[Literal["BOOLEAN", "SCALE", "NUMERIC", "TEXT", "CLASSIFICATION"]]

    contexts: List[Literal["CALL", "SEGMENT", "TURN"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    false_label: Annotated[str, PropertyInfo(alias="falseLabel")]

    max_selections: Annotated[int, PropertyInfo(alias="maxSelections")]

    options: Iterable[MetricConfigOption]

    participant_role: Annotated[Literal["AGENT", "CUSTOMER"], PropertyInfo(alias="participantRole")]

    scale_labels: Annotated[Iterable[MetricConfigScaleLabel], PropertyInfo(alias="scaleLabels")]

    scale_max: Annotated[int, PropertyInfo(alias="scaleMax")]

    scale_min: Annotated[int, PropertyInfo(alias="scaleMin")]

    scope: Literal["GLOBAL", "PER_PARTICIPANT"]

    true_label: Annotated[str, PropertyInfo(alias="trueLabel")]


class AlertThresholdTrigger(TypedDict, total=False):
    aggregation: Required[Literal["COUNT", "RATE_PER_MINUTE", "MEAN"]]

    metric: Required[str]

    operator: Required[Literal["GT", "GTE", "LT", "LTE"]]

    threshold_value: Required[Annotated[float, PropertyInfo(alias="thresholdValue")]]

    type: Required[Literal["threshold"]]

    window_minutes: Required[Annotated[int, PropertyInfo(alias="windowMinutes")]]

    consecutive_open: Annotated[int, PropertyInfo(alias="consecutiveOpen")]

    consecutive_resolve: Annotated[int, PropertyInfo(alias="consecutiveResolve")]

    grouping: Literal["NONE", "BY_AGENT"]

    metric_variant: Annotated[str, PropertyInfo(alias="metricVariant")]

    min_sample_size: Annotated[int, PropertyInfo(alias="minSampleSize")]


class AlertEventTrigger(TypedDict, total=False):
    events: Required[
        List[
            Literal[
                "CALL_ANALYSIS_COMPLETED",
                "CALL_ANALYSIS_FAILED",
                "CALL_ANALYSIS_CANCELLED",
                "SIMULATION_RUN_PLAN_JOB_STARTED",
                "SIMULATION_RUN_PLAN_JOB_COMPLETED",
                "SIMULATION_RUN_PLAN_JOB_FAILED",
                "SIMULATION_RUN_PLAN_JOB_CANCELLED",
                "SIMULATION_JOB_STARTED",
                "SIMULATION_JOB_COMPLETED",
                "SIMULATION_JOB_FAILED",
                "SIMULATION_JOB_CANCELLED",
                "METRIC_COLLECTION_JOB_COMPLETED",
                "METRIC_COLLECTION_JOB_FAILED",
                "CHAT_ANALYSIS_COMPLETED",
                "CHAT_ANALYSIS_FAILED",
                "ISSUE_OPENED",
                "ISSUE_RESOLVED",
            ]
        ]
    ]

    type: Required[Literal["event"]]


class AlertSimulationTrigger(TypedDict, total=False):
    conditions: Required[List[Literal["SUCCESS", "FAILURE", "THRESHOLD_FAILED"]]]

    type: Required[Literal["simulation"]]

    delivery_format: Annotated[Literal["MESSAGE", "PDF"], PropertyInfo(alias="deliveryFormat")]

    run_plan: Annotated[str, PropertyInfo(alias="runPlan")]


class AlertConfigActionSlack(TypedDict, total=False):
    channel_id: Required[Annotated[str, PropertyInfo(alias="channelId")]]

    channel_name: Required[Annotated[str, PropertyInfo(alias="channelName")]]


class AlertConfigAction(TypedDict, total=False):
    slack: Iterable[AlertConfigActionSlack]

    webhooks: SequenceNotStr[str]


class AlertConfig(TypedDict, total=False):
    kind: Required[Literal["alert"]]

    name: Required[str]

    trigger: Required[Union[AlertThresholdTrigger, AlertEventTrigger, AlertSimulationTrigger]]

    actions: AlertConfigAction

    enabled: bool


class ConfigDiffParams(TypedDict, total=False):
    resources: Required[
        List[
            Union[
                AgentConfig,
                PersonaConfig,
                ImprovFlowConfig,
                ScriptedFlowConfig,
                CollectorConfig,
                MetricConfig,
                AlertConfig,
            ]
        ]
    ]

    prune: bool
