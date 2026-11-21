# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["McpServerUpdateParams", "AuthUnionMember0", "AuthUnionMember1", "AuthUnionMember2"]


class AuthUnionMember0(TypedDict, total=False):
    type: Required[Literal["NONE"]]


class AuthUnionMember1(TypedDict, total=False):
    token: Required[str]

    type: Required[Literal["BEARER"]]


class AuthUnionMember2(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["HEADER"]]

    value: Required[str]


class McpServerUpdateParams(TypedDict, total=False):
    auth: Union[AuthUnionMember0, AuthUnionMember1, AuthUnionMember2]
    """How the server authenticates. Stored encrypted; never returned."""

    label: str
