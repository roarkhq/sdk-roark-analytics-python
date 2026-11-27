# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["McpServerCreateParams"]


class McpServerCreateParams(TypedDict, total=False):
    label: Required[str]

    url: Required[str]

    auth: Dict[str, object]

    directory_key: Annotated[Optional[str], PropertyInfo(alias="directoryKey")]

    transport: Literal["STREAMABLE_HTTP", "SSE"]
