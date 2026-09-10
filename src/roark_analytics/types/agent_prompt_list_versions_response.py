# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentPromptListVersionsResponse", "Data"]


class Data(BaseModel):
    created_at: str = FieldInfo(alias="createdAt")
    """When this version was recorded (ISO 8601)."""

    prompt: str
    """Prompt content at this version."""

    version_number: int = FieldInfo(alias="versionNumber")
    """Version number: 1-based and increasing."""


class AgentPromptListVersionsResponse(BaseModel):
    data: List[Data]
