# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentEndpointGetByIDResponse", "Data"]


class Data(BaseModel):
    """Detailed agent endpoint response"""

    id: str
    """Agent endpoint ID"""

    agent_id: str = FieldInfo(alias="agentId")
    """Agent ID this endpoint belongs to"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    direction: Literal["INCOMING", "OUTGOING", "INCOMING_AND_OUTGOING"]
    """Agent endpoint direction (INCOMING, OUTGOING, INCOMING_AND_OUTGOING)"""

    environment: str
    """Agent endpoint environment"""

    outbound_dial_http_request_definition_id: Optional[str] = FieldInfo(
        alias="outboundDialHttpRequestDefinitionId", default=None
    )
    """ID of the linked HTTP request definition for outbound dialing"""

    outbound_dial_type: Literal["NONE", "HTTP_REQUEST"] = FieldInfo(alias="outboundDialType")
    """Outbound dial type (NONE or HTTP_REQUEST)"""

    type: Literal["PHONE", "WEBSOCKET"]
    """Agent endpoint type (PHONE or WEBSOCKET)"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    value: str
    """Agent endpoint value (phone number or websocket URL)"""


class AgentEndpointGetByIDResponse(BaseModel):
    data: Data
    """Detailed agent endpoint response"""
