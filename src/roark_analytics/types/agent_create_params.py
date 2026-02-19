# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the agent"""

    custom_id: Annotated[Optional[str], PropertyInfo(alias="customId")]
    """Custom identifier for the agent"""

    description: Optional[str]
    """Description of the agent"""
