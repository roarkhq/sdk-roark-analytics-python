# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["HTTPRequestDefinitionCreateParams"]


class HTTPRequestDefinitionCreateParams(TypedDict, total=False):
    scope: Required[Literal["AGENT_OUTBOUND_DIAL"]]
    """Scope: AGENT_OUTBOUND_DIAL"""

    url: Required[str]
    """URL for the HTTP request"""

    body: Union[str, Dict[str, object], None]
    """
    Request body template. Accepts a JSON object or a string with placeholders like
    {{phoneNumberToDial}}. Objects are serialized to JSON for storage.
    """

    description: Optional[str]
    """Description of the HTTP request definition"""

    headers: Dict[str, str]
    """Request headers as key-value pairs"""

    max_attempts: Annotated[Optional[int], PropertyInfo(alias="maxAttempts")]
    """
    How many times to send the request, from 1 to 5. Set 1 so a slow answer is never
    sent again, which would start a second call. Null or omitted is the default, 3.
    """

    method: Literal["POST", "PUT", "PATCH", "GET"]
    """HTTP method (default: POST)"""

    timeout_ms: Annotated[Optional[int], PropertyInfo(alias="timeoutMs")]
    """
    How long to wait for each attempt, in milliseconds, from 1000 to 300000. Raise
    it while you debug your endpoint. Null or omitted is the default, 30000.
    """
