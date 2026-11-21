# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpServerDiscoverResponse", "Data", "DataTool"]


class DataTool(BaseModel):
    description: Optional[str]

    name: str
    """The tool as the server names it"""

    read_only: Optional[bool] = FieldInfo(alias="readOnly")
    """The server's hint that the tool only reads"""

    suggested_name: Optional[str] = FieldInfo(alias="suggestedName")
    """
    What a tool for it is called by default: the name with unusable characters
    replaced
    """

    unavailable_reason: Optional[str] = FieldInfo(alias="unavailableReason")
    """Why an agent could not use this tool, such as a name a built-in tool already has"""


class Data(BaseModel):
    catalog_hash: str = FieldInfo(alias="catalogHash")
    """Changes when the server changes the tools it offers"""

    instructions: Optional[str]
    """The server's own advice on using it, for you to read. Never shown to the agent."""

    server_name: Optional[str] = FieldInfo(alias="serverName")
    """The name the server gives itself"""

    server_version: Optional[str] = FieldInfo(alias="serverVersion")

    tools: List[DataTool]


class McpServerDiscoverResponse(BaseModel):
    data: Data
