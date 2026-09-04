# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CallAppendToolInvocationsParams",
    "Metric",
    "ToolInvocation",
    "ToolInvocationAgent",
    "ToolInvocationParameterUnionMember0",
]


class ToolInvocationParameterUnionMember0(TypedDict, total=False):
    description: str

    type: Literal["string", "number", "boolean"]

    value: object


class ToolInvocationAgent(TypedDict, total=False):
    """
    Metadata about the agent that invoked this tool - used to match which agent from
    the agents array this tool invocation belongs to
    """

    custom_id: Annotated[str, PropertyInfo(alias="customId")]
    """The custom ID set on the agent"""

    roark_id: Annotated[str, PropertyInfo(alias="roarkId")]
    """The Roark ID of the agent"""


class ToolInvocation(TypedDict, total=False):
    name: Required[str]
    """Name of the tool that was invoked"""

    parameters: Required[Dict[str, Union[ToolInvocationParameterUnionMember0, object]]]
    """Parameters provided to the tool during invocation"""

    result: Required[Union[str, Dict[str, object]]]
    """Result returned by the tool after execution. Can be a string or a JSON object"""

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]
    """Offset in milliseconds from the start of the call when the tool was invoked"""

    agent: ToolInvocationAgent
    """
    Metadata about the agent that invoked this tool - used to match which agent from
    the agents array this tool invocation belongs to
    """

    description: str
    """Description of when the tool should be invoked"""

    end_offset_ms: Annotated[int, PropertyInfo(alias="endOffsetMs")]
    """
    Offset in milliseconds from the start of the call when the tool execution
    completed. Used to calculate duration of the tool execution
    """


class Metric(TypedDict, total=False):
    id: Required[str]


class CallAppendToolInvocationsParams(TypedDict, total=False):
    tool_invocations: Required[Annotated[Iterable[ToolInvocation], PropertyInfo(alias="toolInvocations")]]
    """
    Tool invocations that fired during the call, to attach to it. Max 500 per
    request. Re-sending an invocation already present on the call (same tool name
    and timing) is skipped, so retries are safe.
    """

    metrics: Iterable[Metric]
    """
    Optional. Metric definitions to (re)score on this call after the tool
    invocations are attached, e.g. the Tool Invocation Analysis metrics. Triggers a
    metric collection job (billed, credit-gated) and requires the 'metric:create'
    permission. Omit to attach tools without scoring. Max 20.
    """
