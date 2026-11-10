# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CustomerListConversationsResponse", "Data", "DataItem"]


class DataItem(BaseModel):
    id: str

    conversation_type: Literal["voice", "chat"] = FieldInfo(alias="conversationType")
    """`voice` or `chat`."""

    duration_ms: Optional[int] = FieldInfo(alias="durationMs")

    started_at: str = FieldInfo(alias="startedAt")

    summary: Optional[str]

    title: Optional[str]


class Data(BaseModel):
    items: List[DataItem]

    page: int

    total_count: int = FieldInfo(alias="totalCount")


class CustomerListConversationsResponse(BaseModel):
    data: Data
