# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    after: str
    """The `nextCursor` of the previous page."""

    limit: int
    """How many to return (default 20, max 100)."""

    modality: Literal["voice", "chat", "call"]
    """Only `voice`, or only `chat`. Both by default."""

    started_from: Annotated[str, PropertyInfo(alias="startedFrom")]
    """Only conversations that started at or after this time."""

    started_to: Annotated[str, PropertyInfo(alias="startedTo")]
    """Only conversations that started at or before this time."""
