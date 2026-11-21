# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "AgentConnectionUpdateParams",
    "AgentConnectionUpdateBland",
    "AgentConnectionUpdateElevenLabs",
    "AgentConnectionUpdateGoogleCes",
    "AgentConnectionUpdateGoogleCesWifConfig",
    "AgentConnectionUpdateGoogleCesWifConfigCredentialSource",
    "AgentConnectionUpdateKore",
    "AgentConnectionUpdateLeaping",
    "AgentConnectionUpdateLivekit",
    "AgentConnectionUpdateLivekitSelfHosted",
    "AgentConnectionUpdatePipecatCloud",
    "AgentConnectionUpdatePipecatSelfHosted",
    "AgentConnectionUpdateRetell",
    "AgentConnectionUpdateVapi",
]


class AgentConnectionUpdateRetell(TypedDict, total=False):
    provider: Required[Literal["RETELL"]]
    """The connection's provider. It cannot change."""

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

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]]
    """
    What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
    PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.
    """

    name: str
    """What the connection is called in Roark. At least 3 characters."""

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""


class AgentConnectionUpdateVapi(TypedDict, total=False):
    provider: Required[Literal["VAPI"]]
    """The connection's provider. It cannot change."""

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

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]]
    """
    What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
    PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.
    """

    name: str
    """What the connection is called in Roark. At least 3 characters."""

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

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""


class AgentConnectionUpdateElevenLabs(TypedDict, total=False):
    provider: Required[Literal["ELEVEN_LABS"]]
    """The connection's provider. It cannot change."""

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

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]]
    """
    What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
    PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.
    """

    name: str
    """What the connection is called in Roark. At least 3 characters."""

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""


class AgentConnectionUpdateBland(TypedDict, total=False):
    provider: Required[Literal["BLAND"]]
    """The connection's provider. It cannot change."""

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

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]]
    """
    What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
    PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.
    """

    name: str
    """What the connection is called in Roark. At least 3 characters."""

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""


class AgentConnectionUpdateLeaping(TypedDict, total=False):
    provider: Required[Literal["LEAPING"]]
    """The connection's provider. It cannot change."""

    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]
    """
    The Leaping agent ids to import calls for. Leaping does not list agents, so name
    each one.
    """

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """
    The platform's API key. Checked against the platform before anything is stored.
    Stored encrypted and never returned.
    """

    name: str
    """What the connection is called in Roark. At least 3 characters."""

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""


class AgentConnectionUpdateLivekit(TypedDict, total=False):
    provider: Required[Literal["LIVEKIT"]]
    """The connection's provider. It cannot change."""

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

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """LiveKit API key. Stored encrypted and never returned."""

    api_secret: Annotated[str, PropertyInfo(alias="apiSecret")]
    """LiveKit API secret. Stored encrypted and never returned."""

    metadata_egress_strategy: Annotated[Literal["EAGER", "DEFERRED"], PropertyInfo(alias="metadataEgressStrategy")]
    """
    When the recording starts for a marked room. EAGER starts it at room creation;
    DEFERRED waits for the metadata. Needs `metadataFilteringEnabled`. Defaults to
    DEFERRED.
    """

    metadata_filtering_enabled: Annotated[bool, PropertyInfo(alias="metadataFilteringEnabled")]
    """Only import rooms whose metadata marks them for Roark. Defaults to false."""

    name: str
    """What the connection is called in Roark. At least 3 characters."""

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""

    url: str
    """Your LiveKit server URL."""


class AgentConnectionUpdateLivekitSelfHosted(TypedDict, total=False):
    provider: Required[Literal["LIVEKIT_SELF_HOSTED"]]
    """The connection's provider. It cannot change."""

    name: str
    """What the connection is called in Roark. At least 3 characters."""

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""


class AgentConnectionUpdatePipecatSelfHosted(TypedDict, total=False):
    provider: Required[Literal["PIPECAT_SELF_HOSTED_INTEGRATION"]]
    """The connection's provider. It cannot change."""

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

    name: str
    """What the connection is called in Roark. At least 3 characters."""

    sampling_rate: Annotated[float, PropertyInfo(alias="samplingRate")]
    """
    Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
    (every call).
    """

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""


class AgentConnectionUpdatePipecatCloud(TypedDict, total=False):
    provider: Required[Literal["PIPECAT_CLOUD_INTEGRATION"]]
    """The connection's provider. It cannot change."""

    name: str
    """What the connection is called in Roark. At least 3 characters."""

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

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""


class AgentConnectionUpdateKore(TypedDict, total=False):
    provider: Required[Literal["KORE"]]
    """The connection's provider. It cannot change."""

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """Kore AI API key. Stored encrypted and never returned."""

    app_id: Annotated[str, PropertyInfo(alias="appId")]

    base_url: Annotated[Optional[str], PropertyInfo(alias="baseUrl")]
    """Kore AI platform URL, when not the default."""

    env_name: Annotated[str, PropertyInfo(alias="envName")]

    name: str
    """What the connection is called in Roark. At least 3 characters."""

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""


class AgentConnectionUpdateGoogleCesWifConfigCredentialSource(TypedDict, total=False):
    environment_id: Required[str]

    region_url: Required[str]

    regional_cred_verification_url: Required[str]

    url: Required[str]


class AgentConnectionUpdateGoogleCesWifConfig(TypedDict, total=False):
    """
    The Workload Identity Federation credential file (`type: external_account`)
    exactly as Google generates it. Stored encrypted and never returned.
    """

    audience: Required[str]

    credential_source: Required[AgentConnectionUpdateGoogleCesWifConfigCredentialSource]

    service_account_impersonation_url: Required[str]

    subject_token_type: Required[str]

    token_url: Required[str]

    type: Required[Literal["external_account"]]

    universe_domain: str


class AgentConnectionUpdateGoogleCes(TypedDict, total=False):
    provider: Required[Literal["GOOGLE_CES"]]
    """The connection's provider. It cannot change."""

    app_id: Annotated[str, PropertyInfo(alias="appId")]

    deployment_id: Annotated[str, PropertyInfo(alias="deploymentId")]

    location: str

    name: str
    """What the connection is called in Roark. At least 3 characters."""

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""

    version_id: Annotated[Optional[str], PropertyInfo(alias="versionId")]
    """Pin a version. Omit to use whatever version the deployment serves."""

    wif_config: Annotated[AgentConnectionUpdateGoogleCesWifConfig, PropertyInfo(alias="wifConfig")]
    """
    The Workload Identity Federation credential file (`type: external_account`)
    exactly as Google generates it. Stored encrypted and never returned.
    """


AgentConnectionUpdateParams: TypeAlias = Union[
    AgentConnectionUpdateRetell,
    AgentConnectionUpdateVapi,
    AgentConnectionUpdateElevenLabs,
    AgentConnectionUpdateBland,
    AgentConnectionUpdateLeaping,
    AgentConnectionUpdateLivekit,
    AgentConnectionUpdateLivekitSelfHosted,
    AgentConnectionUpdatePipecatSelfHosted,
    AgentConnectionUpdatePipecatCloud,
    AgentConnectionUpdateKore,
    AgentConnectionUpdateGoogleCes,
]
