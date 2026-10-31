# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "AgentDraftUpdateParams",
    "Setting",
    "SettingSubAgent",
    "SettingSubAgentHandoff",
    "SettingSubAgentModelConfigUnionMember0",
    "SettingSubAgentModelConfigUnionMember0Llm",
    "SettingSubAgentModelConfigUnionMember0Stt",
    "SettingSubAgentModelConfigUnionMember0Tt",
    "SettingSubAgentModelConfigUnionMember1",
    "SettingSubAgentModelConfigUnionMember1SpeechToSpeech",
    "SettingSubAgentTool",
]


class SettingSubAgentHandoff(TypedDict, total=False):
    description: Required[str]

    history: Required[Literal["SHARED", "NONE"]]

    note: Required[Optional[str]]

    once: Required[bool]

    to: Required[Union[Literal["main"], str]]


class SettingSubAgentModelConfigUnionMember0Llm(TypedDict, total=False):
    model: Required[str]

    provider: Required[Literal["OPENAI", "ANTHROPIC", "GOOGLE", "XAI", "ULTRAVOX", "AWS", "ELEVENLABS"]]

    max_tokens: Annotated[Optional[int], PropertyInfo(alias="maxTokens")]

    temperature: Optional[float]


class SettingSubAgentModelConfigUnionMember0Stt(TypedDict, total=False):
    model: Required[str]

    provider: Required[Literal["DEEPGRAM", "OPENAI_WHISPER", "SPEECHMATICS", "ASSEMBLYAI", "ELEVENLABS"]]

    endpointing_ms: Annotated[Optional[int], PropertyInfo(alias="endpointingMs")]

    keyterms: SequenceNotStr[str]

    smart_format: Annotated[Optional[bool], PropertyInfo(alias="smartFormat")]

    turn_detection: Annotated[Optional[Literal["pipeline", "provider"]], PropertyInfo(alias="turnDetection")]


class SettingSubAgentModelConfigUnionMember0Tt(TypedDict, total=False):
    model: Required[str]

    provider: Required[Literal["CARTESIA", "ELEVENLABS", "OPENAI", "RIME"]]

    voice_id: Required[Annotated[str, PropertyInfo(alias="voiceId")]]

    similarity_boost: Annotated[Optional[float], PropertyInfo(alias="similarityBoost")]

    speed: Optional[float]

    stability: Optional[float]


class SettingSubAgentModelConfigUnionMember0(TypedDict, total=False):
    llm: Required[Iterable[SettingSubAgentModelConfigUnionMember0Llm]]

    stt: Required[Iterable[SettingSubAgentModelConfigUnionMember0Stt]]

    tts: Required[Iterable[SettingSubAgentModelConfigUnionMember0Tt]]

    type: Required[Literal["CASCADE"]]


class SettingSubAgentModelConfigUnionMember1SpeechToSpeech(TypedDict, total=False):
    model: Required[str]

    provider: Required[Literal["OPENAI", "ANTHROPIC", "GOOGLE", "XAI", "ULTRAVOX", "AWS", "ELEVENLABS"]]

    backend_model: Annotated[Optional[str], PropertyInfo(alias="backendModel")]

    max_output_tokens: Annotated[Optional[int], PropertyInfo(alias="maxOutputTokens")]

    temperature: Optional[float]

    voice: Optional[str]


class SettingSubAgentModelConfigUnionMember1(TypedDict, total=False):
    speech_to_speech: Required[
        Annotated[SettingSubAgentModelConfigUnionMember1SpeechToSpeech, PropertyInfo(alias="speechToSpeech")]
    ]

    type: Required[Literal["SPEECH_TO_SPEECH"]]


class SettingSubAgentTool(TypedDict, total=False):
    pinned_version: Required[Annotated[Optional[int], PropertyInfo(alias="pinnedVersion")]]

    tool_definition_id: Required[Annotated[str, PropertyInfo(alias="toolDefinitionId")]]


class SettingSubAgent(TypedDict, total=False):
    handoffs: Required[Iterable[SettingSubAgentHandoff]]

    is_initial: Required[Annotated[bool, PropertyInfo(alias="isInitial")]]

    key: Required[Union[Literal["main"], str]]

    model_configs: Required[
        Annotated[
            List[Union[SettingSubAgentModelConfigUnionMember0, SettingSubAgentModelConfigUnionMember1]],
            PropertyInfo(alias="modelConfigs"),
        ]
    ]

    name: Required[Optional[str]]

    system_prompt: Required[Annotated[Optional[str], PropertyInfo(alias="systemPrompt")]]

    tools: Required[Iterable[SettingSubAgentTool]]


class Setting(TypedDict, total=False):
    """
    The settings to change. Omitted settings stay as they are; null clears one to
    the runtime default. subAgents replaces every speaker, model configs included,
    and must include `main`; in a model config, omitted fields use the runtime
    default.
    """

    background_noise: Annotated[
        Optional[
            Literal[
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
            ]
        ],
        PropertyInfo(alias="backgroundNoise"),
    ]

    background_noise_url: Annotated[Optional[str], PropertyInfo(alias="backgroundNoiseUrl")]

    background_noise_volume: Annotated[Optional[float], PropertyInfo(alias="backgroundNoiseVolume")]

    call_max_duration_seconds: Annotated[Optional[int], PropertyInfo(alias="callMaxDurationSeconds")]

    call_silence_timeout_seconds: Annotated[Optional[int], PropertyInfo(alias="callSilenceTimeoutSeconds")]

    chat_inactivity_timeout_seconds: Annotated[Optional[int], PropertyInfo(alias="chatInactivityTimeoutSeconds")]

    chat_max_duration_seconds: Annotated[Optional[int], PropertyInfo(alias="chatMaxDurationSeconds")]

    end_call_goodbye_message: Annotated[Optional[str], PropertyInfo(alias="endCallGoodbyeMessage")]

    end_detection_phrases: Annotated[SequenceNotStr[str], PropertyInfo(alias="endDetectionPhrases")]

    end_detection_reasons: Annotated[SequenceNotStr[str], PropertyInfo(alias="endDetectionReasons")]

    first_message: Annotated[Optional[str], PropertyInfo(alias="firstMessage")]

    first_message_audio_url: Annotated[Optional[str], PropertyInfo(alias="firstMessageAudioUrl")]

    first_message_mode: Annotated[
        Optional[Literal["SPEAK_TEXT", "PLAY_AUDIO", "WAIT_FOR_CALLER"]], PropertyInfo(alias="firstMessageMode")
    ]

    idle_max_count: Annotated[Optional[int], PropertyInfo(alias="idleMaxCount")]

    idle_messages: Annotated[SequenceNotStr[str], PropertyInfo(alias="idleMessages")]

    idle_timeout_seconds: Annotated[Optional[int], PropertyInfo(alias="idleTimeoutSeconds")]

    interruption_mode: Annotated[Optional[Literal["ALLOW", "BLOCK"]], PropertyInfo(alias="interruptionMode")]

    language: Optional[str]

    modalities: List[Literal["call", "chat"]]

    sub_agents: Annotated[Iterable[SettingSubAgent], PropertyInfo(alias="subAgents")]

    vad_start_secs: Annotated[Optional[float], PropertyInfo(alias="vadStartSecs")]

    vad_stop_secs: Annotated[Optional[float], PropertyInfo(alias="vadStopSecs")]


class AgentDraftUpdateParams(TypedDict, total=False):
    settings: Required[Setting]
    """
    The settings to change. Omitted settings stay as they are; null clears one to
    the runtime default. subAgents replaces every speaker, model configs included,
    and must include `main`; in a model config, omitted fields use the runtime
    default.
    """

    expected_revision: Annotated[int, PropertyInfo(alias="expectedRevision")]
    """
    The draft's revision when you read it. When sent, the edit is refused if the
    draft changed since; when omitted, it applies on top of the latest edit.
    """
