# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "AgentConnectionCreateParams",
    "AgentConnectionCreateBland",
    "AgentConnectionCreateElevenLabs",
    "AgentConnectionCreateGoogleCes",
    "AgentConnectionCreateGoogleCesWifConfig",
    "AgentConnectionCreateGoogleCesWifConfigCredentialSource",
    "AgentConnectionCreateKore",
    "AgentConnectionCreateLeaping",
    "AgentConnectionCreateLivekit",
    "AgentConnectionCreateLivekitEndpoint",
    "AgentConnectionCreateLivekitSelfHosted",
    "AgentConnectionCreatePipecatCloud",
    "AgentConnectionCreatePipecatSelfHosted",
    "AgentConnectionCreateRetell",
    "AgentConnectionCreateVapi",
]


class AgentConnectionCreateRetell(TypedDict, total=False):
    """Retell. Agents and calls are pulled from your account on a schedule."""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["RETELL"]]

    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]
    """
    The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
    `POST /v1/connections/agent/discover` lists them.
    """

    agent_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentNames")]
    """
    Agents to create by name rather than by id, for agents the platform does not
    list. On LiveKit Cloud this is the agent name your worker dispatches as.
    """

    agent_scope: Annotated[Literal["ALL", "SELECTED"], PropertyInfo(alias="agentScope")]
    """
    ALL brings in every agent on the account. SELECTED brings in only `agentIds` and
    `agentNames`.
    """

    capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]]
    """
    What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
    PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.
    """

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """


class AgentConnectionCreateVapi(TypedDict, total=False):
    """Vapi. Assistants and calls are pulled from your account on a schedule."""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["VAPI"]]

    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]
    """
    The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
    `POST /v1/connections/agent/discover` lists them.
    """

    agent_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentNames")]
    """
    Agents to create by name rather than by id, for agents the platform does not
    list. On LiveKit Cloud this is the agent name your worker dispatches as.
    """

    agent_scope: Annotated[Literal["ALL", "SELECTED"], PropertyInfo(alias="agentScope")]
    """
    ALL brings in every agent on the account. SELECTED brings in only `agentIds` and
    `agentNames`.
    """

    capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]]
    """
    What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
    PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.
    """

    outbound_request_body_template: Annotated[
        Optional[Dict[str, object]], PropertyInfo(alias="outboundRequestBodyTemplate")
    ]
    """
    Assistant overrides Roark merges into the request when it asks Vapi to place an
    outbound test call.
    """

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """


class AgentConnectionCreateElevenLabs(TypedDict, total=False):
    """
    ElevenLabs Conversational AI. Agents and conversations are pulled from your
    account on a schedule.
    """

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["ELEVEN_LABS"]]

    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]
    """
    The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
    `POST /v1/connections/agent/discover` lists them.
    """

    agent_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentNames")]
    """
    Agents to create by name rather than by id, for agents the platform does not
    list. On LiveKit Cloud this is the agent name your worker dispatches as.
    """

    agent_scope: Annotated[Literal["ALL", "SELECTED"], PropertyInfo(alias="agentScope")]
    """
    ALL brings in every agent on the account. SELECTED brings in only `agentIds` and
    `agentNames`.
    """

    capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]]
    """
    What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
    PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.
    """

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """


class AgentConnectionCreateBland(TypedDict, total=False):
    """Bland. Agents and calls are pulled from your account on a schedule."""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["BLAND"]]

    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]
    """
    The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
    `POST /v1/connections/agent/discover` lists them.
    """

    agent_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentNames")]
    """
    Agents to create by name rather than by id, for agents the platform does not
    list. On LiveKit Cloud this is the agent name your worker dispatches as.
    """

    agent_scope: Annotated[Literal["ALL", "SELECTED"], PropertyInfo(alias="agentScope")]
    """
    ALL brings in every agent on the account. SELECTED brings in only `agentIds` and
    `agentNames`.
    """

    capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]]
    """
    What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
    PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.
    """

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """


class AgentConnectionCreateLeaping(TypedDict, total=False):
    """Leaping. Calls for the named agents are pulled on a schedule."""

    agent_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]]
    """
    The Leaping agent ids to import calls for. Leaping does not list agents, so name
    each one.
    """

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["LEAPING"]]

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """


class AgentConnectionCreateLivekitEndpoint(TypedDict, total=False):
    """
    Creates a LiveKit endpoint for each agent the connection brings in, so Roark can
    place test calls to it. Omit to create none; endpoints can be added later on the
    agent.
    """

    auto_create_room: Required[Annotated[bool, PropertyInfo(alias="autoCreateRoom")]]
    """
    True to let Roark create the LiveKit room for each test call. False to have
    Roark call `roomCreationUrl`, which creates the room and returns its connection
    details.
    """

    auto_create_room_metadata: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="autoCreateRoomMetadata")]
    """
    Room metadata Roark sets when it creates the room. Only used with
    `autoCreateRoom`.
    """

    environment: str
    """Environment label for the endpoints."""

    room_creation_url: Annotated[Optional[str], PropertyInfo(alias="roomCreationUrl")]
    """
    Your endpoint that creates a room for a test call. Required when
    `autoCreateRoom` is false.
    """


class AgentConnectionCreateLivekit(TypedDict, total=False):
    """LiveKit Cloud. Rooms are recorded through LiveKit egress and imported as calls."""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """LiveKit API key. Stored encrypted and never returned."""

    api_secret: Required[Annotated[str, PropertyInfo(alias="apiSecret")]]
    """LiveKit API secret. Stored encrypted and never returned."""

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["LIVEKIT"]]

    url: Required[str]
    """Your LiveKit server URL."""

    agent_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentNames")]
    """
    Agents to create by name rather than by id, for agents the platform does not
    list. On LiveKit Cloud this is the agent name your worker dispatches as.
    """

    agent_scope: Annotated[Literal["ALL", "SELECTED"], PropertyInfo(alias="agentScope")]
    """
    ALL brings in every agent on the account. SELECTED brings in only `agentIds` and
    `agentNames`.
    """

    endpoint: AgentConnectionCreateLivekitEndpoint
    """
    Creates a LiveKit endpoint for each agent the connection brings in, so Roark can
    place test calls to it. Omit to create none; endpoints can be added later on the
    agent.
    """

    metadata_egress_strategy: Annotated[Literal["EAGER", "DEFERRED"], PropertyInfo(alias="metadataEgressStrategy")]
    """
    When the recording starts for a marked room. EAGER starts it at room creation;
    DEFERRED waits for the metadata. Needs `metadataFilteringEnabled`. Defaults to
    DEFERRED.
    """

    metadata_filtering_enabled: Annotated[bool, PropertyInfo(alias="metadataFilteringEnabled")]
    """Only import rooms whose metadata marks them for Roark. Defaults to false."""

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """


class AgentConnectionCreateLivekitSelfHosted(TypedDict, total=False):
    """
    LiveKit Agents SDK. Your worker reports calls through the Roark plugin with the
    API key this returns.
    """

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["LIVEKIT_SELF_HOSTED"]]

    observer_api_key_name: Annotated[str, PropertyInfo(alias="observerApiKeyName")]
    """
    Name for the Roark API key minted for your SDK to report calls with. Defaults to
    the connection name plus "SDK".
    """

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """


class AgentConnectionCreatePipecatSelfHosted(TypedDict, total=False):
    """
    A self-hosted Pipecat bot. It reports calls through the Roark observer with the
    API key this returns.
    """

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["PIPECAT_SELF_HOSTED_INTEGRATION"]]

    append_agent_id: Annotated[bool, PropertyInfo(alias="appendAgentId")]
    """
    Append the agent's name to the signaling URL, for one server hosting several
    bots. Defaults to true.
    """

    auth_token: Annotated[Optional[str], PropertyInfo(alias="authToken")]
    """
    Bearer token Roark sends to the signaling URL. Stored encrypted and never
    returned. Null clears it.
    """

    base_signaling_url: Annotated[str, PropertyInfo(alias="baseSignalingUrl")]
    """
    Your bot's SmallWebRTC signaling URL. Set it to let Roark place test calls to
    the bot; omit for call import only.
    """

    observer_api_key_name: Annotated[str, PropertyInfo(alias="observerApiKeyName")]
    """
    Name for the Roark API key minted for your SDK to report calls with. Defaults to
    the connection name plus "SDK".
    """

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """


class AgentConnectionCreatePipecatCloud(TypedDict, total=False):
    """
    A bot on Pipecat Cloud. It reports calls through the Roark observer with the API
    key this returns.
    """

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["PIPECAT_CLOUD_INTEGRATION"]]

    observer_api_key_name: Annotated[str, PropertyInfo(alias="observerApiKeyName")]
    """
    Name for the Roark API key minted for your SDK to report calls with. Defaults to
    the connection name plus "SDK".
    """

    pcc_public_key: Annotated[str, PropertyInfo(alias="pccPublicKey")]
    """
    Pipecat Cloud public API key. Set it to let Roark place test calls through
    Pipecat Cloud; omit for call import only. Stored encrypted and never returned.
    """

    pcc_room_properties: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="pccRoomProperties")]
    """Daily room properties for test calls."""

    pcc_start_body: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="pccStartBody")]
    """Body Roark sends when starting a session."""

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """


class AgentConnectionCreateKore(TypedDict, total=False):
    """Kore AI Agent Platform. Creates one agent for the app, ready to test."""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """Kore AI API key. Stored encrypted and never returned."""

    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    env_name: Required[Annotated[str, PropertyInfo(alias="envName")]]

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["KORE"]]

    base_url: Annotated[Optional[str], PropertyInfo(alias="baseUrl")]
    """Kore AI platform URL, when not the default."""


class AgentConnectionCreateGoogleCesWifConfigCredentialSource(TypedDict, total=False):
    environment_id: Required[str]

    region_url: Required[str]

    regional_cred_verification_url: Required[str]

    url: Required[str]


class AgentConnectionCreateGoogleCesWifConfig(TypedDict, total=False):
    """
    The Workload Identity Federation credential file (`type: external_account`)
    exactly as Google generates it. Stored encrypted and never returned.
    """

    audience: Required[str]

    credential_source: Required[AgentConnectionCreateGoogleCesWifConfigCredentialSource]

    service_account_impersonation_url: Required[str]

    subject_token_type: Required[str]

    token_url: Required[str]

    type: Required[Literal["external_account"]]

    universe_domain: str


class AgentConnectionCreateGoogleCes(TypedDict, total=False):
    """
    Google Customer Engagement Suite. Creates one agent for the deployment, ready to
    test.
    """

    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    deployment_id: Required[Annotated[str, PropertyInfo(alias="deploymentId")]]

    location: Required[str]

    name: Required[str]
    """What the connection is called in Roark. At least 3 characters."""

    provider: Required[Literal["GOOGLE_CES"]]

    wif_config: Required[Annotated[AgentConnectionCreateGoogleCesWifConfig, PropertyInfo(alias="wifConfig")]]
    """
    The Workload Identity Federation credential file (`type: external_account`)
    exactly as Google generates it. Stored encrypted and never returned.
    """

    version_id: Annotated[Optional[str], PropertyInfo(alias="versionId")]
    """Pin a version. Omit to use whatever version the deployment serves."""


AgentConnectionCreateParams: TypeAlias = Union[
    AgentConnectionCreateRetell,
    AgentConnectionCreateVapi,
    AgentConnectionCreateElevenLabs,
    AgentConnectionCreateBland,
    AgentConnectionCreateLeaping,
    AgentConnectionCreateLivekit,
    AgentConnectionCreateLivekitSelfHosted,
    AgentConnectionCreatePipecatSelfHosted,
    AgentConnectionCreatePipecatCloud,
    AgentConnectionCreateKore,
    AgentConnectionCreateGoogleCes,
]
