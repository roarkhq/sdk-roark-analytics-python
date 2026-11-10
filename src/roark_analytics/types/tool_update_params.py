# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ToolUpdateParams",
    "Calendar",
    "CalendarAppointmentType",
    "CalendarMessage",
    "Input",
    "Mcp",
    "Runtime",
    "RuntimeRequest",
    "RuntimeRequestHeader",
]


class CalendarAppointmentType(TypedDict, total=False):
    event_type_id: Required[Annotated[int, PropertyInfo(alias="eventTypeId")]]
    """For Cal.com: the event type to book"""

    name: Required[str]

    duration_minutes: Annotated[Optional[int], PropertyInfo(alias="durationMinutes")]

    when_to_use: Annotated[Optional[str], PropertyInfo(alias="whenToUse")]


class CalendarMessage(TypedDict, total=False):
    before: Optional[str]

    failure: Optional[str]

    slow: Optional[str]


class Calendar(TypedDict, total=False):
    """
    Makes this a calendar tool, which Roark runs against a connected calendar: it
    takes no runtime and no inputs. Omit or null for any other tool; on update,
    omitting it makes the tool an ordinary one.
    """

    appointment_types: Required[Annotated[Iterable[CalendarAppointmentType], PropertyInfo(alias="appointmentTypes")]]

    calendar_connection_id: Required[Annotated[str, PropertyInfo(alias="calendarConnectionId")]]

    operation: Required[
        Literal["CHECK_AVAILABILITY", "BOOK", "LOOKUP_BOOKING", "RESCHEDULE", "CANCEL", "LIST_BOOKINGS"]
    ]

    messages: CalendarMessage

    simulate: bool


class Input(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["string", "number", "boolean"]]

    description: str

    required: bool


class Mcp(TypedDict, total=False):
    """
    Makes this a tool on one of the project's MCP servers: it takes no runtime, no
    inputs and no calendar, and the description replaces the server's own. On
    update, omitting it makes the tool an ordinary one.
    """

    mcp_server_id: Required[Annotated[str, PropertyInfo(alias="mcpServerId")]]

    tool: Required[str]
    """The tool as the server names it"""

    messages: CalendarMessage


class RuntimeRequestHeader(TypedDict, total=False):
    name: Required[str]

    value: Required[str]


class RuntimeRequest(TypedDict, total=False):
    url: Required[str]

    body: Optional[str]

    headers: Iterable[RuntimeRequestHeader]

    method: Literal["POST", "PUT", "PATCH", "GET", "DELETE"]

    timeout_ms: Annotated[Optional[int], PropertyInfo(alias="timeoutMs")]


class Runtime(TypedDict, total=False):
    """Omit or null for a tool that is only graded"""

    request: Required[RuntimeRequest]

    changes_data: Annotated[bool, PropertyInfo(alias="changesData")]

    messages: CalendarMessage

    response_fields: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="responseFields")]


class ToolUpdateParams(TypedDict, total=False):
    description: Required[str]
    """When the agent should use the tool"""

    name: Required[str]

    agent_id: Annotated[Optional[str], PropertyInfo(alias="agentId")]

    calendar: Optional[Calendar]
    """
    Makes this a calendar tool, which Roark runs against a connected calendar: it
    takes no runtime and no inputs. Omit or null for any other tool; on update,
    omitting it makes the tool an ordinary one.
    """

    expected_result: Annotated[Optional[str], PropertyInfo(alias="expectedResult")]

    inputs: Iterable[Input]

    invocation_criteria: Annotated[Optional[str], PropertyInfo(alias="invocationCriteria")]

    mcp: Optional[Mcp]
    """
    Makes this a tool on one of the project's MCP servers: it takes no runtime, no
    inputs and no calendar, and the description replaces the server's own. On
    update, omitting it makes the tool an ordinary one.
    """

    runtime: Optional[Runtime]
    """Omit or null for a tool that is only graded"""
