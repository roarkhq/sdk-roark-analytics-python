# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpServerListResponse", "Data", "DataBoundTool", "DataTool"]


class DataBoundTool(BaseModel):
    name: str

    offered: bool
    """False when the server stopped offering it: agents lose the tool"""

    remote_tool_name: str = FieldInfo(alias="remoteToolName")
    """The tool it calls, as the server names it"""

    tool_definition_id: str = FieldInfo(alias="toolDefinitionId")


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
    id: str
    """The id a tool names the server by"""

    auth_header_name: Optional[str] = FieldInfo(alias="authHeaderName")
    """The header a HEADER credential is sent in"""

    auth_type: Literal["NONE", "BEARER", "HEADER"] = FieldInfo(alias="authType")
    """How the server authenticates. The credential is never returned."""

    bound_tools: List[DataBoundTool] = FieldInfo(alias="boundTools")
    """The tools calling on this server, and whether it still offers each"""

    catalog_hash: str = FieldInfo(alias="catalogHash")
    """Changes when the server changes the tools it offers"""

    created_at: str = FieldInfo(alias="createdAt")

    directory_key: Optional[str] = FieldInfo(alias="directoryKey")
    """The MCP registry entry it was connected from"""

    instructions: Optional[str]
    """The server's own advice on using it, for you to read. Never shown to the agent."""

    label: str

    last_discovered_at: str = FieldInfo(alias="lastDiscoveredAt")

    server_name: Optional[str] = FieldInfo(alias="serverName")
    """The name the server gives itself"""

    server_version: Optional[str] = FieldInfo(alias="serverVersion")

    tools: List[DataTool]

    transport: Literal["STREAMABLE_HTTP", "SSE"]

    updated_at: str = FieldInfo(alias="updatedAt")

    url: str


class McpServerListResponse(BaseModel):
    data: List[Data]
