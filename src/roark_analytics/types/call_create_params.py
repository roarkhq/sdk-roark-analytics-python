# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CallCreateParams",
    "Variant0",
    "Variant0Agent",
    "Variant0AgentUnionMember0",
    "Variant0AgentUnionMember0Endpoint",
    "Variant0AgentUnionMember0EndpointID",
    "Variant0AgentUnionMember0EndpointUnionMember1",
    "Variant0AgentUnionMember0Prompt",
    "Variant0AgentUnionMember1",
    "Variant0AgentUnionMember1Endpoint",
    "Variant0AgentUnionMember1EndpointID",
    "Variant0AgentUnionMember1EndpointUnionMember1",
    "Variant0AgentUnionMember1Prompt",
    "Variant0AgentUnionMember2",
    "Variant0AgentUnionMember2Endpoint",
    "Variant0AgentUnionMember2EndpointID",
    "Variant0AgentUnionMember2EndpointUnionMember1",
    "Variant0AgentUnionMember2Prompt",
    "Variant0Customer",
    "Variant0ToolInvocation",
    "Variant0ToolInvocationParameters",
    "Variant0ToolInvocationParametersUnionMember0",
    "Variant0Transcript",
    "Variant0TranscriptUnionMember0",
    "Variant0TranscriptUnionMember0Agent",
    "Variant0TranscriptUnionMember1",
    "Variant0TranscriptUnionMember1Customer",
    "Variant1",
    "Variant1Agent",
    "Variant1AgentUnionMember0",
    "Variant1AgentUnionMember0Endpoint",
    "Variant1AgentUnionMember0EndpointID",
    "Variant1AgentUnionMember0EndpointUnionMember1",
    "Variant1AgentUnionMember0Prompt",
    "Variant1AgentUnionMember1",
    "Variant1AgentUnionMember1Endpoint",
    "Variant1AgentUnionMember1EndpointID",
    "Variant1AgentUnionMember1EndpointUnionMember1",
    "Variant1AgentUnionMember1Prompt",
    "Variant1AgentUnionMember2",
    "Variant1AgentUnionMember2Endpoint",
    "Variant1AgentUnionMember2EndpointID",
    "Variant1AgentUnionMember2EndpointUnionMember1",
    "Variant1AgentUnionMember2Prompt",
    "Variant1Customer",
    "Variant1ToolInvocation",
    "Variant1ToolInvocationParameters",
    "Variant1ToolInvocationParametersUnionMember0",
    "Variant1Transcript",
    "Variant1TranscriptUnionMember0",
    "Variant1TranscriptUnionMember0Agent",
    "Variant1TranscriptUnionMember1",
    "Variant1TranscriptUnionMember1Customer",
]


class Variant0(TypedDict, total=False):
    agent: Required[Variant0Agent]
    """Single agent participating in the call.

    Use this for simpler API when you have only one agent.
    """

    call_direction: Required[Annotated[Literal["INBOUND", "OUTBOUND"], PropertyInfo(alias="callDirection")]]
    """Direction of the call (INBOUND or OUTBOUND)"""

    interface_type: Required[Annotated[Literal["PHONE", "WEB"], PropertyInfo(alias="interfaceType")]]
    """Interface type of the call (PHONE or WEB)"""

    recording_url: Required[Annotated[str, PropertyInfo(alias="recordingUrl")]]
    """URL of source recording (must be an accessible WAV, MP3, or MP4 file).

    Can be a signed URL.
    """

    started_at: Required[Annotated[str, PropertyInfo(alias="startedAt")]]
    """When the call started (ISO 8601 format)"""

    customer: Variant0Customer
    """Single customer participating in the call.

    Use this for simpler API when you have only one customer.
    """

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

    properties: Dict[str, object]
    """Custom properties to include with the call.

    These can be used for filtering and will show in the call details page
    """

    stereo_recording_url: Annotated[str, PropertyInfo(alias="stereoRecordingUrl")]
    """URL of source stereo recording.

    Must be accessible. Can be a signed URL. Supported formats: WAV, MP3, MP4.
    """

    tool_invocations: Annotated[Iterable[Variant0ToolInvocation], PropertyInfo(alias="toolInvocations")]
    """List of tool invocations made during the call"""

    transcript: Iterable[Variant0Transcript]
    """List of transcript entries made during the call"""


class Variant0AgentUnionMember0EndpointID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class Variant0AgentUnionMember0EndpointUnionMember1(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


Variant0AgentUnionMember0Endpoint: TypeAlias = Union[
    Variant0AgentUnionMember0EndpointID, Variant0AgentUnionMember0EndpointUnionMember1
]


class Variant0AgentUnionMember0Prompt(TypedDict, total=False):
    """Agent's prompt configuration"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class Variant0AgentUnionMember0(TypedDict, total=False):
    roark_id: Required[Annotated[str, PropertyInfo(alias="roarkId")]]
    """Existing Roark agent ID"""

    endpoint: Variant0AgentUnionMember0Endpoint
    """Endpoint configuration for this agent (optional)"""

    prompt: Variant0AgentUnionMember0Prompt
    """Agent's prompt configuration"""


class Variant0AgentUnionMember1EndpointID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class Variant0AgentUnionMember1EndpointUnionMember1(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


Variant0AgentUnionMember1Endpoint: TypeAlias = Union[
    Variant0AgentUnionMember1EndpointID, Variant0AgentUnionMember1EndpointUnionMember1
]


class Variant0AgentUnionMember1Prompt(TypedDict, total=False):
    """Agent's prompt configuration"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class Variant0AgentUnionMember1(TypedDict, total=False):
    custom_id: Required[Annotated[str, PropertyInfo(alias="customId")]]
    """Existing custom ID for a Roark agent"""

    endpoint: Variant0AgentUnionMember1Endpoint
    """Endpoint configuration for this agent (optional)"""

    prompt: Variant0AgentUnionMember1Prompt
    """Agent's prompt configuration"""


class Variant0AgentUnionMember2EndpointID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class Variant0AgentUnionMember2EndpointUnionMember1(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


Variant0AgentUnionMember2Endpoint: TypeAlias = Union[
    Variant0AgentUnionMember2EndpointID, Variant0AgentUnionMember2EndpointUnionMember1
]


class Variant0AgentUnionMember2Prompt(TypedDict, total=False):
    """Agent's prompt configuration"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class Variant0AgentUnionMember2(TypedDict, total=False):
    """
    Match existing agent by name, description, and custom ID, or create a new one if no match is found
    """

    name: Required[str]
    """Agent name"""

    custom_id: Annotated[str, PropertyInfo(alias="customId")]
    """Agent custom ID"""

    description: str
    """Agent description"""

    endpoint: Variant0AgentUnionMember2Endpoint
    """Endpoint configuration for this agent (optional)"""

    prompt: Variant0AgentUnionMember2Prompt
    """Agent's prompt configuration"""


Variant0Agent: TypeAlias = Union[Variant0AgentUnionMember0, Variant0AgentUnionMember1, Variant0AgentUnionMember2]


class Variant0Customer(TypedDict, total=False):
    """Single customer participating in the call.

    Use this for simpler API when you have only one customer.
    """

    phone_number_e164: Required[Annotated[Optional[str], PropertyInfo(alias="phoneNumberE164")]]
    """Customer phone number in E.164 format (e.g., +14155551234)"""

    label: Optional[str]
    """
    Label to identify this customer in the transcript (e.g., "speaker-01",
    "speaker-02")
    """


class Variant0ToolInvocationParametersUnionMember0(TypedDict, total=False):
    description: str

    type: Literal["string", "number", "boolean"]

    value: object


Variant0ToolInvocationParameters: TypeAlias = Union[Variant0ToolInvocationParametersUnionMember0, object]


class Variant0ToolInvocation(TypedDict, total=False):
    name: Required[str]
    """Name of the tool that was invoked"""

    parameters: Required[Dict[str, Variant0ToolInvocationParameters]]
    """Parameters provided to the tool during invocation"""

    result: Required[Union[str, Dict[str, object]]]
    """Result returned by the tool after execution. Can be a string or a JSON object"""

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]
    """Offset in milliseconds from the start of the call when the tool was invoked"""

    description: str
    """Description of when the tool should be invoked"""

    end_offset_ms: Annotated[int, PropertyInfo(alias="endOffsetMs")]
    """
    Offset in milliseconds from the start of the call when the tool execution
    completed. Used to calculate duration of the tool execution
    """


class Variant0TranscriptUnionMember0Agent(TypedDict, total=False):
    custom_id: Annotated[str, PropertyInfo(alias="customId")]

    roark_id: Annotated[str, PropertyInfo(alias="roarkId")]


class Variant0TranscriptUnionMember0(TypedDict, total=False):
    end_offset_ms: Required[Annotated[int, PropertyInfo(alias="endOffsetMs")]]

    role: Required[Literal["AGENT"]]

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]

    text: Required[str]

    agent: Variant0TranscriptUnionMember0Agent

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]


class Variant0TranscriptUnionMember1Customer(TypedDict, total=False):
    label: str

    phone_number_e164: Annotated[str, PropertyInfo(alias="phoneNumberE164")]


class Variant0TranscriptUnionMember1(TypedDict, total=False):
    end_offset_ms: Required[Annotated[int, PropertyInfo(alias="endOffsetMs")]]

    role: Required[Literal["CUSTOMER"]]

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]

    text: Required[str]

    customer: Variant0TranscriptUnionMember1Customer

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]


Variant0Transcript: TypeAlias = Union[Variant0TranscriptUnionMember0, Variant0TranscriptUnionMember1]


class Variant1(TypedDict, total=False):
    agents: Required[Iterable[Variant1Agent]]
    """Agents participating in the call.

    Each agent requires identification and prompt information.
    """

    call_direction: Required[Annotated[Literal["INBOUND", "OUTBOUND"], PropertyInfo(alias="callDirection")]]
    """Direction of the call (INBOUND or OUTBOUND)"""

    interface_type: Required[Annotated[Literal["PHONE", "WEB"], PropertyInfo(alias="interfaceType")]]
    """Interface type of the call (PHONE or WEB)"""

    recording_url: Required[Annotated[str, PropertyInfo(alias="recordingUrl")]]
    """URL of source recording (must be an accessible WAV, MP3, or MP4 file).

    Can be a signed URL.
    """

    started_at: Required[Annotated[str, PropertyInfo(alias="startedAt")]]
    """When the call started (ISO 8601 format)"""

    customers: Iterable[Variant1Customer]
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

    properties: Dict[str, object]
    """Custom properties to include with the call.

    These can be used for filtering and will show in the call details page
    """

    stereo_recording_url: Annotated[str, PropertyInfo(alias="stereoRecordingUrl")]
    """URL of source stereo recording.

    Must be accessible. Can be a signed URL. Supported formats: WAV, MP3, MP4.
    """

    tool_invocations: Annotated[Iterable[Variant1ToolInvocation], PropertyInfo(alias="toolInvocations")]
    """List of tool invocations made during the call"""

    transcript: Iterable[Variant1Transcript]
    """List of transcript entries made during the call"""


class Variant1AgentUnionMember0EndpointID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class Variant1AgentUnionMember0EndpointUnionMember1(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


Variant1AgentUnionMember0Endpoint: TypeAlias = Union[
    Variant1AgentUnionMember0EndpointID, Variant1AgentUnionMember0EndpointUnionMember1
]


class Variant1AgentUnionMember0Prompt(TypedDict, total=False):
    """Agent's prompt configuration"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class Variant1AgentUnionMember0(TypedDict, total=False):
    roark_id: Required[Annotated[str, PropertyInfo(alias="roarkId")]]
    """Existing Roark agent ID"""

    endpoint: Variant1AgentUnionMember0Endpoint
    """Endpoint configuration for this agent (optional)"""

    prompt: Variant1AgentUnionMember0Prompt
    """Agent's prompt configuration"""


class Variant1AgentUnionMember1EndpointID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class Variant1AgentUnionMember1EndpointUnionMember1(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


Variant1AgentUnionMember1Endpoint: TypeAlias = Union[
    Variant1AgentUnionMember1EndpointID, Variant1AgentUnionMember1EndpointUnionMember1
]


class Variant1AgentUnionMember1Prompt(TypedDict, total=False):
    """Agent's prompt configuration"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class Variant1AgentUnionMember1(TypedDict, total=False):
    custom_id: Required[Annotated[str, PropertyInfo(alias="customId")]]
    """Existing custom ID for a Roark agent"""

    endpoint: Variant1AgentUnionMember1Endpoint
    """Endpoint configuration for this agent (optional)"""

    prompt: Variant1AgentUnionMember1Prompt
    """Agent's prompt configuration"""


class Variant1AgentUnionMember2EndpointID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class Variant1AgentUnionMember2EndpointUnionMember1(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


Variant1AgentUnionMember2Endpoint: TypeAlias = Union[
    Variant1AgentUnionMember2EndpointID, Variant1AgentUnionMember2EndpointUnionMember1
]


class Variant1AgentUnionMember2Prompt(TypedDict, total=False):
    """Agent's prompt configuration"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class Variant1AgentUnionMember2(TypedDict, total=False):
    """
    Match existing agent by name, description, and custom ID, or create a new one if no match is found
    """

    name: Required[str]
    """Agent name"""

    custom_id: Annotated[str, PropertyInfo(alias="customId")]
    """Agent custom ID"""

    description: str
    """Agent description"""

    endpoint: Variant1AgentUnionMember2Endpoint
    """Endpoint configuration for this agent (optional)"""

    prompt: Variant1AgentUnionMember2Prompt
    """Agent's prompt configuration"""


Variant1Agent: TypeAlias = Union[Variant1AgentUnionMember0, Variant1AgentUnionMember1, Variant1AgentUnionMember2]


class Variant1Customer(TypedDict, total=False):
    """Customer participating in the call"""

    phone_number_e164: Required[Annotated[Optional[str], PropertyInfo(alias="phoneNumberE164")]]
    """Customer phone number in E.164 format (e.g., +14155551234)"""

    label: Optional[str]
    """
    Label to identify this customer in the transcript (e.g., "speaker-01",
    "speaker-02")
    """


class Variant1ToolInvocationParametersUnionMember0(TypedDict, total=False):
    description: str

    type: Literal["string", "number", "boolean"]

    value: object


Variant1ToolInvocationParameters: TypeAlias = Union[Variant1ToolInvocationParametersUnionMember0, object]


class Variant1ToolInvocation(TypedDict, total=False):
    name: Required[str]
    """Name of the tool that was invoked"""

    parameters: Required[Dict[str, Variant1ToolInvocationParameters]]
    """Parameters provided to the tool during invocation"""

    result: Required[Union[str, Dict[str, object]]]
    """Result returned by the tool after execution. Can be a string or a JSON object"""

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]
    """Offset in milliseconds from the start of the call when the tool was invoked"""

    description: str
    """Description of when the tool should be invoked"""

    end_offset_ms: Annotated[int, PropertyInfo(alias="endOffsetMs")]
    """
    Offset in milliseconds from the start of the call when the tool execution
    completed. Used to calculate duration of the tool execution
    """


class Variant1TranscriptUnionMember0Agent(TypedDict, total=False):
    custom_id: Annotated[str, PropertyInfo(alias="customId")]

    roark_id: Annotated[str, PropertyInfo(alias="roarkId")]


class Variant1TranscriptUnionMember0(TypedDict, total=False):
    end_offset_ms: Required[Annotated[int, PropertyInfo(alias="endOffsetMs")]]

    role: Required[Literal["AGENT"]]

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]

    text: Required[str]

    agent: Variant1TranscriptUnionMember0Agent

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]


class Variant1TranscriptUnionMember1Customer(TypedDict, total=False):
    label: str

    phone_number_e164: Annotated[str, PropertyInfo(alias="phoneNumberE164")]


class Variant1TranscriptUnionMember1(TypedDict, total=False):
    end_offset_ms: Required[Annotated[int, PropertyInfo(alias="endOffsetMs")]]

    role: Required[Literal["CUSTOMER"]]

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]

    text: Required[str]

    customer: Variant1TranscriptUnionMember1Customer

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]


Variant1Transcript: TypeAlias = Union[Variant1TranscriptUnionMember0, Variant1TranscriptUnionMember1]

CallCreateParams: TypeAlias = Union[Variant0, Variant1]
