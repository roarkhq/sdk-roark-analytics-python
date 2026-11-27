# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentConnectionListBackfillsResponse", "Data"]


class Data(BaseModel):
    """An import of past calls from the platform."""

    id: str

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    imported_call_count: Optional[int] = FieldInfo(alias="importedCallCount")
    """Past calls imported so far."""

    max_calls: int = FieldInfo(alias="maxCalls")

    status: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELLED"]


class AgentConnectionListBackfillsResponse(BaseModel):
    data: List[Data]
