# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentCreateParams", "Endpoint"]


class Endpoint(TypedDict, total=False):
    """The phone number or connection Roark calls to test the agent"""

    direction: Required[Literal["INCOMING", "OUTGOING", "INCOMING_AND_OUTGOING"]]
    """Call direction: INCOMING, OUTGOING, or INCOMING_AND_OUTGOING"""

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

    value: Optional[str]
    """
    Phone number in E.164 format (e.g., +12345678900). Optional when direction is
    OUTGOING, for an agent that calls from numbers you do not know up front.
    """


class AgentCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the agent"""

    custom_id: Annotated[Optional[str], PropertyInfo(alias="customId")]
    """Custom identifier for the agent. Must be unique in the project."""

    description: Optional[str]
    """Description of the agent"""

    endpoint: Optional[Endpoint]
    """The phone number Roark calls to test the agent."""

    industry: Optional[
        Literal[
            "HEALTHCARE",
            "FINANCIAL_SERVICES",
            "INSURANCE",
            "DEBT_COLLECTION",
            "RETAIL",
            "TRAVEL_AND_HOSPITALITY",
            "TELECOMMUNICATIONS",
            "TECHNOLOGY",
            "PUBLIC_SECTOR",
            "UTILITIES",
            "LOGISTICS",
            "AUTOMOTIVE",
            "HOME_SERVICES",
            "RESTAURANTS",
            "EDUCATION",
            "OTHER",
        ]
    ]
    """The industry the agent serves."""

    prompt: Optional[str]
    """The agent's system prompt."""
