# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentPromptListResponse", "Data"]


class Data(BaseModel):
    """A prompt lineage on an agent."""

    id: str
    """Prompt lineage ID (its own version history)."""

    created_at: str = FieldInfo(alias="createdAt")
    """When this prompt lineage was first created (ISO 8601)."""

    prompt: str
    """Current prompt content (the latest version)."""

    source: Literal[
        "USER",
        "RETELL_INTEGRATION",
        "VAPI_INTEGRATION",
        "ELEVEN_LABS_INTEGRATION",
        "BLAND_INTEGRATION",
        "PIPECAT_CLOUD_INTEGRATION",
        "PIPECAT_SELF_HOSTED_INTEGRATION",
        "LIVEKIT_SELF_HOSTED_INTEGRATION",
        "API",
        "CONFIG",
        "API_MANAGED",
    ]
    """
    Where this prompt came from: USER (edited in the app), API (provided via the API
    or on calls), CONFIG (managed by config-as-code), or a provider integration.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the current version was recorded (ISO 8601)."""


class AgentPromptListResponse(BaseModel):
    data: List[Data]
