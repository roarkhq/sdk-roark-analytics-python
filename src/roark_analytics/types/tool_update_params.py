# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ToolUpdateParams", "Input", "Runtime", "RuntimeMessage", "RuntimeRequest", "RuntimeRequestHeader"]


class Input(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["string", "number", "boolean"]]

    description: str

    required: bool


class RuntimeRequestHeader(TypedDict, total=False):
    name: Required[str]

    value: Required[str]


class RuntimeRequest(TypedDict, total=False):
    url: Required[str]

    body: Optional[str]

    headers: Iterable[RuntimeRequestHeader]

    method: Literal["POST", "PUT", "PATCH", "GET", "DELETE"]

    timeout_ms: Annotated[Optional[int], PropertyInfo(alias="timeoutMs")]


class RuntimeMessage(TypedDict, total=False):
    before: Optional[str]

    failure: Optional[str]

    slow: Optional[str]


class Runtime(TypedDict, total=False):
    """Omit or null for a tool that is only graded"""

    request: Required[RuntimeRequest]

    changes_data: Annotated[bool, PropertyInfo(alias="changesData")]

    messages: RuntimeMessage

    response_fields: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="responseFields")]


class ToolUpdateParams(TypedDict, total=False):
    description: Required[str]
    """When the agent should use the tool"""

    name: Required[str]

    agent_id: Annotated[Optional[str], PropertyInfo(alias="agentId")]

    expected_result: Annotated[Optional[str], PropertyInfo(alias="expectedResult")]

    inputs: Iterable[Input]

    invocation_criteria: Annotated[Optional[str], PropertyInfo(alias="invocationCriteria")]

    runtime: Optional[Runtime]
    """Omit or null for a tool that is only graded"""
