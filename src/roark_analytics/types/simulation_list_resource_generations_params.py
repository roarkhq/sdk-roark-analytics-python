# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationListResourceGenerationsParams"]


class SimulationListResourceGenerationsParams(TypedDict, total=False):
    agent_ids: Annotated[str, PropertyInfo(alias="agentIds")]
    """
    Only generations for these agents, comma-separated, at most 100. Omit for every
    agent.
    """

    limit: int
    """How many to return, newest first. Default 20, max 50."""
