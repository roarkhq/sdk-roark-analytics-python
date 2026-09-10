# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentPromptUpdateResponse", "Data"]


class Data(BaseModel):
    changed: bool
    """
    True if a new version was appended; false if the content matched the current
    version (no-op).
    """

    prompt_id: str = FieldInfo(alias="promptId")
    """The ID of the API-managed prompt lineage."""

    version_number: int = FieldInfo(alias="versionNumber")
    """The current version number after the set."""


class AgentPromptUpdateResponse(BaseModel):
    data: Data
