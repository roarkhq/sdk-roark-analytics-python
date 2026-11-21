# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AgentConnectionListParams"]


class AgentConnectionListParams(TypedDict, total=False):
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
