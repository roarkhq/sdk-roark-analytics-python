# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["McpServerDiscoverParams"]


class McpServerDiscoverParams(TypedDict, total=False):
    url: Required[str]

    auth: Dict[str, object]

    transport: Literal["STREAMABLE_HTTP", "SSE"]
