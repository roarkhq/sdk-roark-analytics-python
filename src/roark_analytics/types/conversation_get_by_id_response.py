# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ConversationGetByIDResponse", "Data"]


class Data(BaseModel):
    id: str
    """
    The conversation id: its call id or chat id. `modality` says which, and where to
    read its transcript and metrics (`/v1/call/{callId}` or `/v1/chat/{id}`).
    """

    created_at: str = FieldInfo(alias="createdAt")

    duration_ms: Optional[int] = FieldInfo(alias="durationMs")
    """How long it ran. Null until it ends."""

    ended_at: Optional[str] = FieldInfo(alias="endedAt")
    """When it ended (ISO 8601). Null until it ends."""

    external_id: Optional[str] = FieldInfo(alias="externalId")
    """Your own id for it, if one was given."""

    modality: Literal["voice", "chat"]
    """
    `voice` or `chat`. A voice conversation is recorded as a call
    (`/v1/call/{callId}`), a chat as a chat (`/v1/chat/{id}`).
    """

    project_id: str = FieldInfo(alias="projectId")

    started_at: str = FieldInfo(alias="startedAt")
    """When it started, or was created while pending (ISO 8601)."""

    status: Literal["PENDING", "IN_PROGRESS", "ENDED"]
    """
    `PENDING` until it starts (a call ringing, a chat nobody has joined yet),
    `IN_PROGRESS`, then `ENDED`.
    """

    summary: Optional[str]

    title: Optional[str]


class ConversationGetByIDResponse(BaseModel):
    data: Data
