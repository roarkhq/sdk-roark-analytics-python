# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AgentConnectionListResponse",
    "Data",
    "DataGoogleCe",
    "DataKore",
    "DataLivekit",
    "DataPipecat",
    "DataSync",
    "DataSyncProblem",
    "DataVapi",
]


class DataGoogleCe(BaseModel):
    """Set for GOOGLE_CES only."""

    app_id: str = FieldInfo(alias="appId")

    deployment_id: str = FieldInfo(alias="deploymentId")

    gcp_project_id: str = FieldInfo(alias="gcpProjectId")

    location: str

    service_account_email: str = FieldInfo(alias="serviceAccountEmail")

    version_id: Optional[str] = FieldInfo(alias="versionId")


class DataKore(BaseModel):
    """Set for KORE only."""

    app_id: str = FieldInfo(alias="appId")

    base_url: Optional[str] = FieldInfo(alias="baseUrl")

    env_name: str = FieldInfo(alias="envName")


class DataLivekit(BaseModel):
    """Set for LIVEKIT only."""

    metadata_egress_strategy: Literal["EAGER", "DEFERRED"] = FieldInfo(alias="metadataEgressStrategy")

    metadata_filtering_enabled: bool = FieldInfo(alias="metadataFilteringEnabled")

    url: str


class DataPipecat(BaseModel):
    """
    Set for the Pipecat providers only. Secrets are reported only as present or
    absent.
    """

    append_agent_id: bool = FieldInfo(alias="appendAgentId")

    base_signaling_url: Optional[str] = FieldInfo(alias="baseSignalingUrl")

    has_auth_token: bool = FieldInfo(alias="hasAuthToken")

    has_pcc_public_key: bool = FieldInfo(alias="hasPccPublicKey")

    pcc_room_properties: Optional[Dict[str, object]] = FieldInfo(alias="pccRoomProperties")

    pcc_start_body: Optional[Dict[str, object]] = FieldInfo(alias="pccStartBody")


class DataSync(BaseModel):
    """
    The latest scheduled sync. Null for platforms that report calls themselves
    rather than being pulled.
    """

    created_agent_count: Optional[int] = FieldInfo(alias="createdAgentCount")
    """Agents the latest run brought in."""

    ended_at: Optional[str] = FieldInfo(alias="endedAt")
    """ISO 8601"""

    interval_minutes: Optional[int] = FieldInfo(alias="intervalMinutes")
    """How often the connection syncs."""

    is_up_to_date: Optional[bool] = FieldInfo(alias="isUpToDate")

    started_at: Optional[str] = FieldInfo(alias="startedAt")
    """ISO 8601"""

    status: Optional[Literal["IN_PROGRESS", "COMPLETED", "FAILED"]]
    """How the latest sync run went."""


class DataSyncProblem(BaseModel):
    agent_id: Optional[str] = FieldInfo(alias="agentId")
    """The platform's id of the agent the problem is with"""

    agent_name: Optional[str] = FieldInfo(alias="agentName")

    at: str
    """ISO 8601"""

    reason: Optional[str]
    """Why the sync failed for it, such as INVALID_API_KEY or AGENT_NOT_FOUND."""


class DataVapi(BaseModel):
    """Set for VAPI only."""

    outbound_request_body_template: Optional[Dict[str, object]] = FieldInfo(alias="outboundRequestBodyTemplate")


class Data(BaseModel):
    """
    A connection to the platform a project’s agents run on. Credentials are never
    returned; the API key Roark mints for an SDK-driven platform is returned once,
    on create.
    """

    id: str

    agent_ids: List[str] = FieldInfo(alias="agentIds")
    """The platform's ids of the SELECTED agents."""

    agent_names: List[str] = FieldInfo(alias="agentNames")
    """Agents created by name."""

    agent_scope: Optional[Literal["ALL", "SELECTED"]] = FieldInfo(alias="agentScope")
    """Null for platforms that do not scope by agent."""

    capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]]

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    google_ces: Optional[DataGoogleCe] = FieldInfo(alias="googleCes")
    """Set for GOOGLE_CES only."""

    kore: Optional[DataKore]
    """Set for KORE only."""

    livekit: Optional[DataLivekit]
    """Set for LIVEKIT only."""

    name: str

    pipecat: Optional[DataPipecat]
    """
    Set for the Pipecat providers only. Secrets are reported only as present or
    absent.
    """

    provider: Literal[
        "RETELL",
        "VAPI",
        "ELEVEN_LABS",
        "BLAND",
        "LEAPING",
        "LIVEKIT",
        "LIVEKIT_SELF_HOSTED",
        "PIPECAT_CLOUD_INTEGRATION",
        "PIPECAT_SELF_HOSTED_INTEGRATION",
        "KORE",
        "GOOGLE_CES",
    ]
    """
    The platform the agents run on. LIVEKIT is LiveKit Cloud; LIVEKIT_SELF_HOSTED is
    the LiveKit Agents SDK reporting through the Roark plugin.
    PIPECAT_CLOUD_INTEGRATION and PIPECAT_SELF_HOSTED_INTEGRATION are Pipecat Cloud
    and a self-hosted Pipecat bot. `GET /v1/connections/agent/providers` describes
    what each one needs.
    """

    sampling_rate: float = FieldInfo(alias="samplingRate")

    status: Literal["ACTIVE", "INACTIVE"]
    """INACTIVE pauses syncing and call import without deleting anything."""

    sync: Optional[DataSync]

    sync_problems: List[DataSyncProblem] = FieldInfo(alias="syncProblems")
    """
    Agents the latest sync could not bring in, and why. Empty when the sync is
    healthy.
    """

    updated_at: Optional[str] = FieldInfo(alias="updatedAt")
    """ISO 8601"""

    vapi: Optional[DataVapi]
    """Set for VAPI only."""


class AgentConnectionListResponse(BaseModel):
    data: List[Data]
