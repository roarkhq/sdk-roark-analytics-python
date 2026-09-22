# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentConfigUpdateParams"]


class AgentConfigUpdateParams(TypedDict, total=False):
    channel: Required[Literal["production", "staging"]]
    """Which channel to write."""

    document: Required[Dict[str, object]]
    """The full config JSON for the new revision."""

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """
    Link this config to a Roark agent (the one your calls report). Required before
    Autoimprove can run on it: the link is how a fix finds the config channel.
    """

    summary: str
    """One-line story of the change."""
