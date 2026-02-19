# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentEndpointUpdateParams"]


class AgentEndpointUpdateParams(TypedDict, total=False):
    environment: str
    """Environment name"""

    outbound_dial_http_request_definition_id: Annotated[
        Optional[str], PropertyInfo(alias="outboundDialHttpRequestDefinitionId")
    ]
    """ID of the HTTP request definition for outbound dialing"""

    outbound_dial_type: Annotated[Literal["NONE", "HTTP_REQUEST"], PropertyInfo(alias="outboundDialType")]
    """Outbound dial type: NONE or HTTP_REQUEST"""
