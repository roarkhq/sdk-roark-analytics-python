# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerCreateFieldParams"]


class CustomerCreateFieldParams(TypedDict, total=False):
    extract: Required[bool]
    """Whether conversations fill this field"""

    key: Required[str]
    """Starts with a letter; letters, numbers and underscores only. Fixed once created."""

    label: Required[str]

    value_type: Required[
        Annotated[
            Literal["TEXT", "NUMBER", "BOOLEAN", "DATE", "PHONE_NUMBER", "EMAIL", "CURRENCY"],
            PropertyInfo(alias="valueType"),
        ]
    ]

    description: Optional[str]
    """What the agent listens for in a conversation. Required when extract is true."""
