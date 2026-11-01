# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentDraftPublishParams"]


class AgentDraftPublishParams(TypedDict, total=False):
    expected_revision: Required[Annotated[int, PropertyInfo(alias="expectedRevision")]]
    """The draft revision you reviewed."""

    summary: str
    """What changed."""
