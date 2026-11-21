# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentConnectionListProvidersResponse", "Data"]


class Data(BaseModel):
    default_capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] = FieldInfo(
        alias="defaultCapabilities"
    )

    ingestion: Literal["SYNC", "WEBHOOK", "SDK", "NONE"]
    """
    How calls reach Roark. SYNC: Roark pulls them on a schedule. WEBHOOK: the
    platform sends them as rooms end. SDK: your code reports them with the returned
    `observerApiKey`. NONE: the connection is for testing only.
    """

    label: str

    multiple_connections: bool = FieldInfo(alias="multipleConnections")
    """
    Whether a project may connect more than one account. Otherwise a second create
    returns 409.
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

    required_fields: List[str] = FieldInfo(alias="requiredFields")
    """Create-body fields this provider requires."""

    supported_capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] = FieldInfo(
        alias="supportedCapabilities"
    )

    supports_agent_discovery: bool = FieldInfo(alias="supportsAgentDiscovery")
    """Whether `discover` can list its agents, so a connection can be scoped by id."""

    supports_backfill: bool = FieldInfo(alias="supportsBackfill")
    """Whether past calls can be imported with a backfill."""


class AgentConnectionListProvidersResponse(BaseModel):
    data: List[Data]
