# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CallCreateParams",
    "AgentEndpointByID",
    "AgentEndpointByValue",
    "AgentIdentificationByCustomID",
    "AgentIdentificationByName",
    "AgentIdentificationByRoarkID",
    "AgentIdentificationByRoarkIDPrompt",
    "Customer",
    "ToolInvocation",
    "ToolInvocationAgent",
    "ToolInvocationParameterUnionMember0",
    "TranscriptEntryAgent",
    "TranscriptEntryCustomer",
    "TranscriptEntryCustomerCustomer",
]


class AgentEndpointByID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class AgentEndpointByValue(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


class AgentIdentificationByRoarkIDPrompt(TypedDict, total=False):
    """Agent's prompt configuration (optional)"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class AgentIdentificationByRoarkID(TypedDict, total=False):
    roark_id: Required[Annotated[str, PropertyInfo(alias="roarkId")]]
    """Existing Roark agent ID"""

    endpoint: Union[AgentEndpointByID, AgentEndpointByValue]
    """Endpoint configuration for this agent (optional)"""

    prompt: AgentIdentificationByRoarkIDPrompt
    """Agent's prompt configuration (optional)"""


class AgentIdentificationByName(TypedDict, total=False):
    """
    Find existing by customId if provided, otherwise reuse exact project name match
    before creating
    """

    name: Required[str]
    """Agent name"""

    custom_id: Annotated[str, PropertyInfo(alias="customId")]
    """Agent custom ID"""

    description: str
    """Agent description"""

    endpoint: Union[AgentEndpointByID, AgentEndpointByValue]
    """Endpoint configuration for this agent (optional)"""

    prompt: AgentIdentificationByRoarkIDPrompt
    """Agent's prompt configuration (optional)"""


class AgentIdentificationByCustomID(TypedDict, total=False):
    custom_id: Required[Annotated[str, PropertyInfo(alias="customId")]]
    """Existing custom ID for a Roark agent"""

    endpoint: Union[AgentEndpointByID, AgentEndpointByValue]
    """Endpoint configuration for this agent (optional)"""

    prompt: AgentIdentificationByRoarkIDPrompt
    """Agent's prompt configuration (optional)"""


class Customer(TypedDict, total=False):
    """
    Single customer participating in the call. Use this for simpler API when you
    have only one customer.
    """

    phone_number_e164: Required[Annotated[Optional[str], PropertyInfo(alias="phoneNumberE164")]]
    """Customer phone number in E.164 format (e.g., +14155551234)"""

    label: Optional[str]
    """
    Label to identify this customer in the transcript (e.g., "speaker-01",
    "speaker-02")
    """


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


class TranscriptEntryAgent(TypedDict, total=False):
    end_offset_ms: Required[Annotated[int, PropertyInfo(alias="endOffsetMs")]]

    role: Required[Literal["AGENT"]]

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]

    text: Required[str]

    agent: ToolInvocationAgent
    """
    Metadata about the agent that spoke this turn - used to match which agent from
    the `agents` array this transcript entry belongs to
    """

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]

    payload: Optional[Dict[str, object]]


class TranscriptEntryCustomerCustomer(TypedDict, total=False):
    """
    Metadata about the customer that spoke this turn - used to match which customer
    from the `customers` array this transcript entry belongs to
    """

    label: str
    """Label matching the `label` field on the `customers` array when creating the call"""

    phone_number_e164: Annotated[str, PropertyInfo(alias="phoneNumberE164")]
    """
    The phone number of the customer in E.164 format, matching the `phoneNumberE164`
    field on the `customers` array when creating the call
    """


class TranscriptEntryCustomer(TypedDict, total=False):
    end_offset_ms: Required[Annotated[int, PropertyInfo(alias="endOffsetMs")]]

    role: Required[Literal["CUSTOMER"]]

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]

    text: Required[str]

    customer: TranscriptEntryCustomerCustomer
    """
    Metadata about the customer that spoke this turn - used to match which customer
    from the `customers` array this transcript entry belongs to
    """

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]

    payload: Optional[Dict[str, object]]


class CallCreateParams(TypedDict, total=False):
    call_direction: Required[Annotated[Literal["INBOUND", "OUTBOUND"], PropertyInfo(alias="callDirection")]]
    """Direction of the call (INBOUND or OUTBOUND)"""

    interface_type: Required[Annotated[Literal["PHONE", "WEB"], PropertyInfo(alias="interfaceType")]]
    """Interface type of the call (PHONE or WEB)"""

    recording_url: Required[Annotated[str, PropertyInfo(alias="recordingUrl")]]
    """
    URL of source recording (must be an accessible WAV, MP3, MP4, or OGG file). Can
    be a signed URL.
    """

    started_at: Required[Annotated[str, PropertyInfo(alias="startedAt")]]
    """When the call started (ISO 8601 format)"""

    agent: Union[AgentIdentificationByRoarkID, AgentIdentificationByName, AgentIdentificationByCustomID]
    """
    Single agent participating in the call. Use this for simpler API when you have
    only one agent.
    """

    agents: List[Union[AgentIdentificationByRoarkID, AgentIdentificationByName, AgentIdentificationByCustomID]]
    """
    Agents participating in the call. Each agent requires identification and prompt
    information.
    """

    customer: Customer
    """
    Single customer participating in the call. Use this for simpler API when you
    have only one customer.
    """

    customers: Iterable[Customer]
    """Customers participating in the call."""

    ended_status: Annotated[
        Literal[
            "PARTICIPANTS_DID_NOT_SPEAK",
            "AGENT_DID_NOT_ANSWER",
            "AGENT_DID_NOT_SPEAK",
            "AGENT_STOPPED_SPEAKING",
            "AGENT_ENDED_CALL",
            "AGENT_TRANSFERRED_CALL",
            "AGENT_BUSY",
            "AGENT_ERROR",
            "CUSTOMER_ENDED_CALL",
            "VOICE_MAIL_REACHED",
            "SILENCE_TIME_OUT",
            "PHONE_CALL_PROVIDER_CONNECTION_ERROR",
            "CUSTOMER_DID_NOT_ANSWER",
            "CUSTOMER_DID_NOT_SPEAK",
            "CUSTOMER_STOPPED_SPEAKING",
            "CUSTOMER_BUSY",
            "DIAL_ERROR",
            "MAX_DURATION_REACHED",
            "UNKNOWN",
        ],
        PropertyInfo(alias="endedStatus"),
    ]
    """High-level call end status, indicating how the call terminated"""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A stable identifier from your own system (e.g. session ID, conversation ID) used
    to correlate this call with OpenTelemetry traces. Set the same value as a
    `roark.external_id` span or resource attribute on your traces and the matching
    trace will be linked automatically. Must be unique within a project.
    """

    livekit_room_id: Annotated[str, PropertyInfo(alias="livekitRoomId")]
    """
    The LiveKit Cloud room ID to link this call with OpenTelemetry trace data from
    LiveKit. Used for matching calls with OTEL traces.
    """

    properties: Dict[str, object]
    """
    Custom properties to include with the call. These can be used for filtering and
    will show in the call details page
    """

    stereo_recording_url: Annotated[str, PropertyInfo(alias="stereoRecordingUrl")]
    """
    URL of source stereo recording. Must be accessible. Can be a signed URL.
    Supported formats: WAV, MP3, MP4, OGG.
    """

    tool_invocations: Annotated[Iterable[ToolInvocation], PropertyInfo(alias="toolInvocations")]
    """List of tool invocations made during the call"""

    transcript: List[Union[TranscriptEntryAgent, TranscriptEntryCustomer]]
    """List of transcript entries made during the call"""

    vapi_call_id: Annotated[str, PropertyInfo(alias="vapiCallId")]
    """
    The Vapi call ID (UUID) to link this call with OpenTelemetry trace data from
    Vapi. Used for matching calls with OTEL traces.
    """
