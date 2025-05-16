# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CallAnalysisCreateParams",
    "Participant",
    "ToolInvocation",
    "ToolInvocationParameters",
    "ToolInvocationParametersUnionMember0",
]


class CallAnalysisCreateParams(TypedDict, total=False):
    call_direction: Required[Annotated[Literal["INBOUND", "OUTBOUND"], PropertyInfo(alias="callDirection")]]
    """Direction of the call (INBOUND or OUTBOUND)"""

    interface_type: Required[Annotated[Literal["PHONE", "WEB"], PropertyInfo(alias="interfaceType")]]
    """Interface type of the call (PHONE or WEB)"""

    participants: Required[Iterable[Participant]]
    """Exactly two participants in the call"""

    recording_url: Required[Annotated[str, PropertyInfo(alias="recordingUrl")]]
    """URL of source recording (must be an accessible WAV or MP3 file).

    Can be a signed URL.
    """

    started_at: Required[Annotated[str, PropertyInfo(alias="startedAt")]]
    """When the call started (ISO 8601 format)"""

    ended_reason: Annotated[str, PropertyInfo(alias="endedReason")]
    """Additional context on why the call terminated with the endedStatus"""

    ended_status: Annotated[
        Literal[
            "AGENT_ENDED_CALL",
            "AGENT_TRANSFERRED_CALL",
            "AGENT_ERROR",
            "CUSTOMER_ENDED_CALL",
            "VOICE_MAIL_REACHED",
            "SILENCE_TIME_OUT",
            "PHONE_CALL_PROVIDER_CONNECTION_ERROR",
            "CUSTOMER_DID_NOT_ANSWER",
            "CUSTOMER_BUSY",
            "DIAL_ERROR",
            "MAX_DURATION_REACHED",
            "UNKNOWN",
        ],
        PropertyInfo(alias="endedStatus"),
    ]
    """High-level call end status, indicating how the call terminated"""

    is_test: Annotated[bool, PropertyInfo(alias="isTest")]
    """Whether this is a test call"""

    properties: Dict[str, object]
    """Custom properties to include with the call.

    These can be used for filtering and will show in the call details page
    """

    retell_call_id: Annotated[str, PropertyInfo(alias="retellCallId")]
    """Retell call ID if call is being imported from Retell"""

    stereo_recording_url: Annotated[str, PropertyInfo(alias="stereoRecordingUrl")]
    """URL of source stereo recording in WAV format.

    Must be accessible. Can be a signed URL. While optional it allows for a richer
    audio player
    """

    tool_invocations: Annotated[Iterable[ToolInvocation], PropertyInfo(alias="toolInvocations")]
    """List of tool invocations made during the call"""

    vapi_call_id: Annotated[str, PropertyInfo(alias="vapiCallId")]
    """Vapi call ID if call is being imported from Vapi"""


class Participant(TypedDict, total=False):
    role: Required[Literal["AGENT", "CUSTOMER"]]

    is_simulated: Annotated[bool, PropertyInfo(alias="isSimulated")]

    name: Optional[str]

    phone_number: Annotated[Optional[str], PropertyInfo(alias="phoneNumber")]

    spoke_first: Annotated[bool, PropertyInfo(alias="spokeFirst")]


class ToolInvocationParametersUnionMember0(TypedDict, total=False):
    description: str

    type: Literal["string", "number", "boolean"]

    value: object


ToolInvocationParameters: TypeAlias = Union[ToolInvocationParametersUnionMember0, object]


class ToolInvocation(TypedDict, total=False):
    name: Required[str]
    """Name of the tool that was invoked"""

    parameters: Required[Dict[str, ToolInvocationParameters]]
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
