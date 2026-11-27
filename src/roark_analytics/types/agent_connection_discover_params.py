# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentConnectionDiscoverParams"]


class AgentConnectionDiscoverParams(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """The platform API key to list agents with. Stored nowhere."""

    provider: Required[Literal["RETELL", "VAPI", "ELEVEN_LABS", "BLAND"]]
    """Platforms whose agents can be listed with a key."""
