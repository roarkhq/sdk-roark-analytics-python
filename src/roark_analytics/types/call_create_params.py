# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CallCreateParams",
    "Agent",
    "AgentAgentIdentificationByRoarkID",
    "AgentAgentIdentificationByRoarkIDEndpoint",
    "AgentAgentIdentificationByRoarkIDEndpointAgentEndpointByID",
    "AgentAgentIdentificationByRoarkIDEndpointAgentEndpointByValue",
    "AgentAgentIdentificationByRoarkIDPrompt",
    "AgentAgentIdentificationByName",
    "AgentAgentIdentificationByNameEndpoint",
    "AgentAgentIdentificationByNameEndpointAgentEndpointByID",
    "AgentAgentIdentificationByNameEndpointAgentEndpointByValue",
    "AgentAgentIdentificationByNamePrompt",
    "AgentAgentIdentificationByCustomID",
    "AgentAgentIdentificationByCustomIDEndpoint",
    "AgentAgentIdentificationByCustomIDEndpointAgentEndpointByID",
    "AgentAgentIdentificationByCustomIDEndpointAgentEndpointByValue",
    "AgentAgentIdentificationByCustomIDPrompt",
    "Customer",
    "ToolInvocation",
    "ToolInvocationParameters",
    "ToolInvocationParametersUnionMember0",
    "ToolInvocationAgent",
    "Transcript",
    "TranscriptTranscriptEntryAgent",
    "TranscriptTranscriptEntryAgentAgent",
    "TranscriptTranscriptEntryCustomer",
    "TranscriptTranscriptEntryCustomerCustomer",
]


class CallCreateParams(TypedDict, total=False):
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

    agent: Agent
    """Single agent participating in the call.

    Use this for simpler API when you have only one agent.
    """

    agents: Iterable[Agent]
    """Agents participating in the call.

    Each agent requires identification and prompt information.
    """

    customer: Customer
    """Single customer participating in the call.

    Use this for simpler API when you have only one customer.
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

    properties: Dict[str, object]
    """Custom properties to include with the call.

    These can be used for filtering and will show in the call details page
    """

    stereo_recording_url: Annotated[str, PropertyInfo(alias="stereoRecordingUrl")]
    """URL of source stereo recording.

    Must be accessible. Can be a signed URL. Supported formats: WAV, MP3, MP4.
    """

    tool_invocations: Annotated[Iterable[ToolInvocation], PropertyInfo(alias="toolInvocations")]
    """List of tool invocations made during the call"""

    transcript: Iterable[Transcript]
    """List of transcript entries made during the call"""


class AgentAgentIdentificationByRoarkIDEndpointAgentEndpointByID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class AgentAgentIdentificationByRoarkIDEndpointAgentEndpointByValue(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


AgentAgentIdentificationByRoarkIDEndpoint: TypeAlias = Union[
    AgentAgentIdentificationByRoarkIDEndpointAgentEndpointByID,
    AgentAgentIdentificationByRoarkIDEndpointAgentEndpointByValue,
]


class AgentAgentIdentificationByRoarkIDPrompt(TypedDict, total=False):
    """Agent's prompt configuration (optional)"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class AgentAgentIdentificationByRoarkID(TypedDict, total=False):
    roark_id: Required[Annotated[str, PropertyInfo(alias="roarkId")]]
    """Existing Roark agent ID"""

    endpoint: AgentAgentIdentificationByRoarkIDEndpoint
    """Endpoint configuration for this agent (optional)"""

    prompt: AgentAgentIdentificationByRoarkIDPrompt
    """Agent's prompt configuration (optional)"""


class AgentAgentIdentificationByNameEndpointAgentEndpointByID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class AgentAgentIdentificationByNameEndpointAgentEndpointByValue(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


AgentAgentIdentificationByNameEndpoint: TypeAlias = Union[
    AgentAgentIdentificationByNameEndpointAgentEndpointByID, AgentAgentIdentificationByNameEndpointAgentEndpointByValue
]


class AgentAgentIdentificationByNamePrompt(TypedDict, total=False):
    """Agent's prompt configuration (optional)"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class AgentAgentIdentificationByName(TypedDict, total=False):
    """Create a new agent or find existing by customId if provided"""

    name: Required[str]
    """Agent name"""

    custom_id: Annotated[str, PropertyInfo(alias="customId")]
    """Agent custom ID"""

    description: str
    """Agent description"""

    endpoint: AgentAgentIdentificationByNameEndpoint
    """Endpoint configuration for this agent (optional)"""

    prompt: AgentAgentIdentificationByNamePrompt
    """Agent's prompt configuration (optional)"""


class AgentAgentIdentificationByCustomIDEndpointAgentEndpointByID(TypedDict, total=False):
    id: Required[str]
    """Existing Roark endpoint ID"""


class AgentAgentIdentificationByCustomIDEndpointAgentEndpointByValue(TypedDict, total=False):
    """Lookup or create endpoint if one with these values does not exist"""

    type: Required[str]
    """Type of endpoint (phone or websocket)"""

    value: Required[str]
    """Endpoint value (phone number in E.164 format or websocket URL)"""

    direction: str
    """Call direction for this endpoint"""


AgentAgentIdentificationByCustomIDEndpoint: TypeAlias = Union[
    AgentAgentIdentificationByCustomIDEndpointAgentEndpointByID,
    AgentAgentIdentificationByCustomIDEndpointAgentEndpointByValue,
]


class AgentAgentIdentificationByCustomIDPrompt(TypedDict, total=False):
    """Agent's prompt configuration (optional)"""

    resolved_prompt: Required[Annotated[str, PropertyInfo(alias="resolvedPrompt")]]
    """The agent's system prompt used during this call"""


class AgentAgentIdentificationByCustomID(TypedDict, total=False):
    custom_id: Required[Annotated[str, PropertyInfo(alias="customId")]]
    """Existing custom ID for a Roark agent"""

    endpoint: AgentAgentIdentificationByCustomIDEndpoint
    """Endpoint configuration for this agent (optional)"""

    prompt: AgentAgentIdentificationByCustomIDPrompt
    """Agent's prompt configuration (optional)"""


Agent: TypeAlias = Union[
    AgentAgentIdentificationByRoarkID, AgentAgentIdentificationByName, AgentAgentIdentificationByCustomID
]


class Customer(TypedDict, total=False):
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


class ToolInvocationParametersUnionMember0(TypedDict, total=False):
    description: str

    type: Literal["string", "number", "boolean"]

    value: object


ToolInvocationParameters: TypeAlias = Union[ToolInvocationParametersUnionMember0, object]


class ToolInvocationAgent(TypedDict, total=False):
    """
    Metadata about the agent that invoked this tool - used to match which agent from the agents array this tool invocation belongs to
    """

    custom_id: Annotated[str, PropertyInfo(alias="customId")]

    roark_id: Annotated[str, PropertyInfo(alias="roarkId")]


class ToolInvocation(TypedDict, total=False):
    name: Required[str]
    """Name of the tool that was invoked"""

    parameters: Required[Dict[str, ToolInvocationParameters]]
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


class TranscriptTranscriptEntryAgentAgent(TypedDict, total=False):
    custom_id: Annotated[str, PropertyInfo(alias="customId")]

    roark_id: Annotated[str, PropertyInfo(alias="roarkId")]


class TranscriptTranscriptEntryAgent(TypedDict, total=False):
    end_offset_ms: Required[Annotated[int, PropertyInfo(alias="endOffsetMs")]]

    role: Required[Literal["AGENT"]]

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]

    text: Required[str]

    agent: TranscriptTranscriptEntryAgentAgent

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]


class TranscriptTranscriptEntryCustomerCustomer(TypedDict, total=False):
    """
    Metadata about the customer that spoke this turn - used to match which customer from the `customers` array this transcript entry belongs to
    """

    label: str
    """
    Label matching the `label` field on the `customers` array when creating the call
    """

    phone_number_e164: Annotated[str, PropertyInfo(alias="phoneNumberE164")]
    """
    The phone number of the customer in E.164 format, matching the `phoneNumberE164`
    field on the `customers` array when creating the call
    """


class TranscriptTranscriptEntryCustomer(TypedDict, total=False):
    end_offset_ms: Required[Annotated[int, PropertyInfo(alias="endOffsetMs")]]

    role: Required[Literal["CUSTOMER"]]

    start_offset_ms: Required[Annotated[int, PropertyInfo(alias="startOffsetMs")]]

    text: Required[str]

    customer: TranscriptTranscriptEntryCustomerCustomer
    """
    Metadata about the customer that spoke this turn - used to match which customer
    from the `customers` array this transcript entry belongs to
    """

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]


Transcript: TypeAlias = Union[TranscriptTranscriptEntryAgent, TranscriptTranscriptEntryCustomer]
