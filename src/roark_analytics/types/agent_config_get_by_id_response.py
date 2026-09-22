# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .managed_agent_config_revision import ManagedAgentConfigRevision

__all__ = ["AgentConfigGetByIDResponse", "Data"]


class Data(BaseModel):
    """
    A managed config for a code-first agent (LiveKit, Pipecat, or any stack using
    the SDK): your agent fetches its tunable surface from Roark at session start.
    Two channels: production for real traffic, staging for candidates under test.
    """

    id: str

    agent_id: Optional[str] = FieldInfo(alias="agentId")
    """The linked Roark agent, when one exists."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601."""

    key: str
    """The stable handle your code fetches by."""

    production_revision_id: Optional[str] = FieldInfo(alias="productionRevisionId")
    """The revision real traffic reads."""

    revisions: List[ManagedAgentConfigRevision]
    """Recent revisions, newest first."""

    staging_revision_id: Optional[str] = FieldInfo(alias="stagingRevisionId")
    """The candidate revision Roark test calls read. Null when nothing is staged."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """ISO 8601."""


class AgentConfigGetByIDResponse(BaseModel):
    data: Data
