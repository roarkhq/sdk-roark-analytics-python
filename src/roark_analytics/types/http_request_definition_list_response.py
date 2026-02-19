# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["HTTPRequestDefinitionListResponse", "Data", "Pagination"]


class Data(BaseModel):
    """HTTP request definition"""

    id: str
    """HTTP request definition ID"""

    body: Optional[str] = None
    """Request body as a string"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    description: Optional[str] = None
    """Description of the HTTP request definition"""

    headers: Dict[str, str]
    """Request headers as key-value pairs"""

    method: Literal["POST", "PUT", "PATCH", "GET"]
    """HTTP method: POST, PUT, PATCH, or GET"""

    parsed_body: Union[Dict[str, object], str, None] = FieldInfo(alias="parsedBody", default=None)
    """Parsed body as a JSON object if valid JSON, otherwise the raw string"""

    scope: Literal["AGENT_OUTBOUND_DIAL"]
    """Scope of the HTTP request definition"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    url: str
    """URL for the HTTP request"""


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """Whether there are more items to fetch"""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page of items"""

    total: float
    """Total number of items"""


class HTTPRequestDefinitionListResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
