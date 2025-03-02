# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallAnalysisCreateParams", "Participant"]


class CallAnalysisCreateParams(TypedDict, total=False):
    call_direction: Required[Annotated[Literal["INBOUND", "OUTBOUND"], PropertyInfo(alias="callDirection")]]
    """Direction of the call (INBOUND or OUTBOUND)"""

    interface_type: Required[Annotated[Literal["PHONE", "WEB"], PropertyInfo(alias="interfaceType")]]
    """Interface type of the call (PHONE or WEB)"""

    participants: Required[Iterable[Participant]]
    """Exactly two participants in the call"""

    recording_url: Required[Annotated[str, PropertyInfo(alias="recordingUrl")]]
    """URL of source recording (must be an accessible WAV file). Can be a signed URL."""

    started_at: Required[Annotated[str, PropertyInfo(alias="startedAt")]]
    """When the call started (ISO 8601 format)"""

    ended_reason: Annotated[str, PropertyInfo(alias="endedReason")]
    """Reason why the call ended (optional)"""

    is_test: Annotated[bool, PropertyInfo(alias="isTest")]
    """Whether this is a test call"""

    properties: Dict[str, object]
    """Custom properties to include with the call.

    These can be used for filtering and will show in the call details page
    """

    stereo_recording_url: Annotated[str, PropertyInfo(alias="stereoRecordingUrl")]
    """URL of source stereo recording in WAV format.

    Must be accessible. Can be a signed URL. While optional it allows for a richer
    audio player
    """


class Participant(TypedDict, total=False):
    role: Required[Literal["AGENT", "CUSTOMER"]]

    is_simulated: Annotated[bool, PropertyInfo(alias="isSimulated")]

    name: Optional[str]

    phone_number: Annotated[Optional[str], PropertyInfo(alias="phoneNumber")]

    spoke_first: Annotated[bool, PropertyInfo(alias="spokeFirst")]
