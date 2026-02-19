# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentCreateResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier of the agent"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    custom_id: Optional[str] = FieldInfo(alias="customId", default=None)
    """Custom identifier for the agent"""

    description: Optional[str] = None
    """Description of the agent"""

    name: str
    """Name of the agent"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class AgentCreateResponse(BaseModel):
    data: Data
