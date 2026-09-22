# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ManagedAgentConfigRevision"]


class ManagedAgentConfigRevision(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601."""

    created_by_type: Literal["CUSTOMER", "AUTOIMPROVE"] = FieldInfo(alias="createdByType")
    """Who wrote it: your own pushes, or the Autoimprove loop staging a candidate."""

    document: Dict[str, object]
    """The config JSON, verbatim."""

    parent_revision_id: Optional[str] = FieldInfo(alias="parentRevisionId")

    summary: Optional[str]
    """One-line story of the change."""
