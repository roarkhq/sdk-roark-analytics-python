# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["HTTPRequestDefinitionCreateParams"]


class HTTPRequestDefinitionCreateParams(TypedDict, total=False):
    scope: Required[Literal["AGENT_OUTBOUND_DIAL"]]
    """Scope: AGENT_OUTBOUND_DIAL"""

    url: Required[str]
    """URL for the HTTP request"""

    body: Union[str, Dict[str, object], None]
    """Request body template.

    Accepts a JSON object or a string with placeholders like {{phoneNumberToDial}}.
    Objects are serialized to JSON for storage.
    """

    description: Optional[str]
    """Description of the HTTP request definition"""

    headers: Dict[str, str]
    """Request headers as key-value pairs"""

    method: Literal["POST", "PUT", "PATCH", "GET"]
    """HTTP method (default: POST)"""
