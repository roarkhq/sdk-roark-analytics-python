# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AgentVersionRollbackResponse",
    "AgentCascadeModelConfig",
    "AgentCascadeModelConfigLlm",
    "AgentCascadeModelConfigStt",
    "AgentCascadeModelConfigTt",
    "AgentSpeechToSpeechModelConfig",
    "AgentSpeechToSpeechModelConfigSpeechToSpeech",
    "Data",
    "DataIssue",
    "DataSubAgent",
    "DataSubAgentHandoff",
    "DataSubAgentTool",
]


class DataSubAgentHandoff(BaseModel):
    description: str
    """When to hand off, in the words the model is given."""

    history: Literal["SHARED", "NONE"]
    """SHARED: the new speaker hears the conversation so far. NONE: it starts fresh."""

    note: Optional[str]
    """Added to the new speaker's prompt at the handoff, such as a warm-transfer brief."""

    once: bool
    """At most once per call."""

    to: str
    """The key of the sub-agent that takes over; `main` for the main agent."""


class AgentCascadeModelConfigLlm(BaseModel):
    """A text model. Null settings use the default."""

    max_tokens: Optional[int] = FieldInfo(alias="maxTokens")

    model: str
    """Any text model id the provider accepts."""

    provider: Literal["OPENAI", "ANTHROPIC", "GOOGLE", "XAI", "ULTRAVOX", "AWS", "ELEVENLABS"]

    temperature: Optional[float]
    """0 to 2."""


class AgentCascadeModelConfigStt(BaseModel):
    """A transcriber. Null settings use the default."""

    endpointing_ms: Optional[int] = FieldInfo(alias="endpointingMs")
    """How long the transcriber waits before it ends a turn."""

    keyterms: List[str]
    """Words and phrases the transcriber should listen for."""

    model: str
    """Any transcriber model id the provider accepts."""

    provider: Literal["DEEPGRAM", "OPENAI_WHISPER", "SPEECHMATICS", "ASSEMBLYAI", "ELEVENLABS"]

    smart_format: Optional[bool] = FieldInfo(alias="smartFormat")

    turn_detection: Optional[Literal["pipeline", "provider"]] = FieldInfo(alias="turnDetection")


class AgentCascadeModelConfigTt(BaseModel):
    """A voice. Null settings use the default."""

    model: str
    """Any voice model id the provider accepts."""

    provider: Literal["CARTESIA", "ELEVENLABS", "OPENAI", "RIME"]

    similarity_boost: Optional[float] = FieldInfo(alias="similarityBoost")
    """0 to 1, ElevenLabs."""

    speed: Optional[float]
    """0.5 to 2."""

    stability: Optional[float]
    """0 to 1, ElevenLabs."""

    voice_id: str = FieldInfo(alias="voiceId")
    """Any voice id the provider accepts, including your own voices."""


class AgentCascadeModelConfig(BaseModel):
    """
    A transcriber, a text model and a voice. A component that fails during a call
    moves to its next entry; the others stay.
    """

    llm: List[AgentCascadeModelConfigLlm]
    """One to three text models, in the order a call tries them."""

    stt: List[AgentCascadeModelConfigStt]
    """One to three transcribers, in the order a call tries them."""

    tts: List[AgentCascadeModelConfigTt]
    """One to three voices, in the order a call tries them."""

    type: Literal["CASCADE"]


class AgentSpeechToSpeechModelConfigSpeechToSpeech(BaseModel):
    """
    A model that hears the caller and speaks with its own voice. Null settings use
    the default.
    """

    backend_model: Optional[str] = FieldInfo(alias="backendModel")
    """OpenAI Live models only: the text model they delegate to."""

    max_output_tokens: Optional[int] = FieldInfo(alias="maxOutputTokens")

    model: str
    """Any speech-to-speech model id the provider accepts."""

    provider: Literal["OPENAI", "ANTHROPIC", "GOOGLE", "XAI", "ULTRAVOX", "AWS", "ELEVENLABS"]

    temperature: Optional[float]
    """0 to 2."""

    voice: Optional[str]
    """The model's own voice."""


class AgentSpeechToSpeechModelConfig(BaseModel):
    """One model that hears the caller and speaks with its own voice."""

    speech_to_speech: AgentSpeechToSpeechModelConfigSpeechToSpeech = FieldInfo(alias="speechToSpeech")
    """
    A model that hears the caller and speaks with its own voice. Null settings use
    the default.
    """

    type: Literal["SPEECH_TO_SPEECH"]


class DataSubAgentTool(BaseModel):
    pinned_version: Optional[int] = FieldInfo(alias="pinnedVersion")
    """The tool version the agent runs; null runs the tool's latest declared version."""

    tool_definition_id: str = FieldInfo(alias="toolDefinitionId")


class DataSubAgent(BaseModel):
    """
    A speaker in the conversation. A sub-agent without model configs runs on the
    main agent's.
    """

    handoffs: List[DataSubAgentHandoff]

    is_initial: bool = FieldInfo(alias="isInitial")
    """The call opens as this sub-agent instead of the main agent."""

    key: str
    """`main` for the main agent; otherwise letters, digits, `_` or `-`."""

    model_configs: List[Union[AgentCascadeModelConfig, AgentSpeechToSpeechModelConfig]] = FieldInfo(
        alias="modelConfigs"
    )
    """
    Up to three, in the order a call tries them. Empty on a sub-agent: it runs on
    the main agent's. The main agent needs one.
    """

    name: Optional[str]
    """How the agent refers to this speaker."""

    system_prompt: Optional[str] = FieldInfo(alias="systemPrompt")
    """The speaker's prompt."""

    tools: List[DataSubAgentTool]


class DataIssue(BaseModel):
    """Something that stops a version from running."""

    field: str
    """The setting the issue is about."""

    message: str


class Data(BaseModel):
    """
    One version of a Roark-hosted agent's configuration. Null settings use the
    runtime default.
    """

    id: str

    agent_id: str = FieldInfo(alias="agentId")

    background_noise: Optional[
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
    ] = FieldInfo(alias="backgroundNoise")
    """A background preset."""

    background_noise_url: Optional[str] = FieldInfo(alias="backgroundNoiseUrl")
    """A custom background recording, instead of a preset."""

    background_noise_volume: Optional[float] = FieldInfo(alias="backgroundNoiseVolume")
    """0 to 1."""

    base_version_id: Optional[str] = FieldInfo(alias="baseVersionId")
    """The published version a draft started from."""

    call_max_duration_seconds: Optional[int] = FieldInfo(alias="callMaxDurationSeconds")

    call_silence_timeout_seconds: Optional[int] = FieldInfo(alias="callSilenceTimeoutSeconds")

    chat_inactivity_timeout_seconds: Optional[int] = FieldInfo(alias="chatInactivityTimeoutSeconds")

    chat_max_duration_seconds: Optional[int] = FieldInfo(alias="chatMaxDurationSeconds")

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601."""

    created_by_id: Optional[str] = FieldInfo(alias="createdById")

    created_by_type: Literal["USER", "API", "CONFIG", "AUTOIMPROVE", "INTEGRATION", "SYSTEM"] = FieldInfo(
        alias="createdByType"
    )

    end_call_goodbye_message: Optional[str] = FieldInfo(alias="endCallGoodbyeMessage")

    end_detection_phrases: List[str] = FieldInfo(alias="endDetectionPhrases")
    """
    Phrases that end the call when the caller says them, matched anywhere in what
    they say.
    """

    end_detection_reasons: List[str] = FieldInfo(alias="endDetectionReasons")
    """When the agent may decide to end the call itself."""

    first_message: Optional[str] = FieldInfo(alias="firstMessage")
    """What the agent says first, with firstMessageMode SPEAK_TEXT."""

    first_message_audio_url: Optional[str] = FieldInfo(alias="firstMessageAudioUrl")
    """The audio a call opens with, with firstMessageMode PLAY_AUDIO."""

    first_message_mode: Optional[Literal["SPEAK_TEXT", "PLAY_AUDIO", "WAIT_FOR_CALLER"]] = FieldInfo(
        alias="firstMessageMode"
    )

    idle_max_count: Optional[int] = FieldInfo(alias="idleMaxCount")

    idle_messages: List[str] = FieldInfo(alias="idleMessages")

    idle_timeout_seconds: Optional[int] = FieldInfo(alias="idleTimeoutSeconds")

    interruption_mode: Optional[Literal["ALLOW", "BLOCK"]] = FieldInfo(alias="interruptionMode")

    language: Optional[str]
    """ISO 639-1, e.g. en."""

    modalities: List[Literal["call", "chat"]]
    """Whether the agent takes calls, chats, or both."""

    published_at: Optional[str] = FieldInfo(alias="publishedAt")
    """ISO 8601."""

    published_by_id: Optional[str] = FieldInfo(alias="publishedById")

    published_by_type: Optional[Literal["USER", "API", "CONFIG", "AUTOIMPROVE", "INTEGRATION", "SYSTEM"]] = FieldInfo(
        alias="publishedByType"
    )

    revision: int
    """
    Increases with every edit to a draft. Send it back as expectedRevision when you
    publish.
    """

    rolled_back_from_version_id: Optional[str] = FieldInfo(alias="rolledBackFromVersionId")
    """Set when this version rolls the agent back to an older one."""

    status: Literal["DRAFT", "PUBLISHED", "DISCARDED"]
    """DRAFT while being edited, PUBLISHED once it has been live."""

    sub_agents: List[DataSubAgent] = FieldInfo(alias="subAgents")
    """The main agent (key `main`) first, then the sub-agents it can hand the call to."""

    summary: Optional[str]
    """What changed, written on publish."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """ISO 8601."""

    vad_start_secs: Optional[float] = FieldInfo(alias="vadStartSecs")

    vad_stop_secs: Optional[float] = FieldInfo(alias="vadStopSecs")

    version_number: Optional[int] = FieldInfo(alias="versionNumber")
    """v1, v2, ... assigned on publish; null on a draft."""

    issues: Optional[List[DataIssue]] = None
    """
    Why this version cannot run; empty when it can be published. Returned when
    reading one version.
    """


class AgentVersionRollbackResponse(BaseModel):
    data: Data
    """
    One version of a Roark-hosted agent's configuration. Null settings use the
    runtime default.
    """
