# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CallGetTranscriptResponse",
    "Data",
    "DataEntry",
    "DataParticipant",
    "DataParticipantUnionMember0",
    "DataParticipantUnionMember1",
    "DataParticipantUnionMember2",
    "DataParticipantUnionMember3",
]


class DataEntry(BaseModel):
    """A single transcript entry"""

    end_offset_ms: int = FieldInfo(alias="endOffsetMs")
    """End time offset in milliseconds from the start of the call"""

    participant_id: Optional[str] = FieldInfo(alias="participantId", default=None)
    """ID of the conversation participant who spoke this entry.

    References participants[].id.
    """

    role: Optional[Literal["AGENT", "CUSTOMER"]] = None
    """Convenience role derived from participant type"""

    start_offset_ms: int = FieldInfo(alias="startOffsetMs")
    """Start time offset in milliseconds from the start of the call"""

    text: str
    """Transcript text for this entry"""


class DataParticipantUnionMember0(BaseModel):
    """An agent participant"""

    id: str
    """Conversation participant ID"""

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)
    """ID of the agent entity"""

    type: Literal["AGENT"]


class DataParticipantUnionMember1(BaseModel):
    """A customer participant"""

    id: str
    """Conversation participant ID"""

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)
    """ID of the conversation customer record"""

    type: Literal["CUSTOMER"]


class DataParticipantUnionMember2(BaseModel):
    """A simulated customer participant"""

    id: str
    """Conversation participant ID"""

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)
    """ID of the conversation customer record"""

    type: Literal["SIMULATED_CUSTOMER"]


class DataParticipantUnionMember3(BaseModel):
    """A background speaker participant"""

    id: str
    """Conversation participant ID"""

    type: Literal["BACKGROUND_SPEAKER"]


DataParticipant: TypeAlias = Union[
    DataParticipantUnionMember0, DataParticipantUnionMember1, DataParticipantUnionMember2, DataParticipantUnionMember3
]


class Data(BaseModel):
    """Call transcript response"""

    entries: List[DataEntry]
    """Ordered list of transcript entries from the call"""

    participants: List[DataParticipant]
    """All participants in this transcript, referenced by participantId on each entry"""

    transcription_source: Optional[
        Literal["ROARK_POST_CALL", "SIMULATION_AGENT_REALTIME", "CUSTOMER_AGENT_REALTIME"]
    ] = FieldInfo(alias="transcriptionSource", default=None)
    """The transcription source used for this transcript.

    Null if no transcript is available.
    """


class CallGetTranscriptResponse(BaseModel):
    data: Data
    """Call transcript response"""
