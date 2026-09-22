# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ManagedAgentConfigRevisionParam"]


class ManagedAgentConfigRevisionParam(TypedDict, total=False):
    id: Required[str]

    created_at: Required[Annotated[str, PropertyInfo(alias="createdAt")]]
    """ISO 8601."""

    created_by_type: Required[Annotated[Literal["CUSTOMER", "AUTOIMPROVE"], PropertyInfo(alias="createdByType")]]
    """Who wrote it: your own pushes, or the Autoimprove loop staging a candidate."""

    document: Required[Dict[str, object]]
    """The config JSON, verbatim."""

    parent_revision_id: Required[Annotated[Optional[str], PropertyInfo(alias="parentRevisionId")]]

    summary: Required[Optional[str]]
    """One-line story of the change."""
