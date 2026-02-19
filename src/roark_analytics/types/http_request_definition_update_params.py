# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["HTTPRequestDefinitionUpdateParams"]


class HTTPRequestDefinitionUpdateParams(TypedDict, total=False):
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
    """HTTP method: POST, PUT, PATCH, or GET"""

    url: str
    """URL for the HTTP request"""
