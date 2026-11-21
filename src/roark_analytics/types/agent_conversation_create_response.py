# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentConversationCreateResponse", "Data", "DataWeb"]


class DataWeb(BaseModel):
    """What a browser needs to join the conversation."""

    allowed_origins: List[str] = FieldInfo(alias="allowedOrigins")
    """The origins the browser may join from, normalized."""

    client_token: str = FieldInfo(alias="clientToken")
    """
    A single-use token for the browser, and the only thing your page should get. The
    web SDK spends it to join from one of `allowedOrigins` before
    `clientTokenExpiresAt`, and runs the connection itself. It is not an API key.
    """

    client_token_expires_at: str = FieldInfo(alias="clientTokenExpiresAt")
    """When the browser can no longer join (ISO 8601)."""


class Data(BaseModel):
    id: str
    """
    The conversation id. Read it with `GET /v1/conversation/{conversationId}`; once
    it is recorded it is also its call or chat id, and a call's tools get it as
    `{{conversation.id}}`.
    """

    agent_id: str = FieldInfo(alias="agentId")

    channel: Literal["web"]

    created_at: str = FieldInfo(alias="createdAt")
    """When it was created (ISO 8601)."""

    modality: Literal["voice", "chat"]

    status: Literal["PENDING"]
    """Waiting for the browser to join."""

    web: DataWeb
    """What a browser needs to join the conversation."""


class AgentConversationCreateResponse(BaseModel):
    data: Data
