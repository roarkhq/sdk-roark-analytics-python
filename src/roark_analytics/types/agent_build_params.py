# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentBuildParams"]


class AgentBuildParams(TypedDict, total=False):
    job_description: Required[Annotated[str, PropertyInfo(alias="jobDescription")]]
    """
    One-line description of what the agent should do. Roark authors the system
    prompt from this.
    """

    name: Required[str]
    """Name of the agent"""

    voice: Optional[str]
    """Optional voice label for the hosted agent"""
