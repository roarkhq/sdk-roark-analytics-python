# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentEndpointCreateParams"]


class AgentEndpointCreateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]
    """Agent ID to associate this endpoint with"""

    direction: Required[Literal["INCOMING", "OUTGOING", "INCOMING_AND_OUTGOING"]]
    """Call direction: INCOMING, OUTGOING, or INCOMING_AND_OUTGOING"""

    value: Required[str]
    """Phone number in E.164 format (e.g., +12345678900)"""

    environment: str
    """Environment name (default: production)"""

    outbound_dial_http_request_definition_id: Annotated[
        Optional[str], PropertyInfo(alias="outboundDialHttpRequestDefinitionId")
    ]
    """
    ID of the HTTP request definition for outbound dialing (required when
    outboundDialType is HTTP_REQUEST)
    """

    outbound_dial_type: Annotated[Literal["NONE", "HTTP_REQUEST"], PropertyInfo(alias="outboundDialType")]
    """Outbound dial type: NONE or HTTP_REQUEST (default: NONE)"""
