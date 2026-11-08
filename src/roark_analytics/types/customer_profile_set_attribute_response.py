# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CustomerProfileSetAttributeResponse",
    "Data",
    "DataAttribute",
    "DataAttributeEvidence",
    "DataAttributeHistory",
]


class DataAttributeEvidence(BaseModel):
    """
    The moment the current value was heard. Null for a value set by a person or the
    API.
    """

    call_id: Optional[str] = FieldInfo(alias="callId")

    chat_id: Optional[str] = FieldInfo(alias="chatId")

    observed_at: str = FieldInfo(alias="observedAt")

    offset_ms: Optional[int] = FieldInfo(alias="offsetMs")
    """Where in the conversation this was said"""

    quote: Optional[str]
    """The customer's words. Null on a project with redaction on."""

    source: Literal["LIVE_EXTRACTION", "POST_CALL_EXTRACTION", "API", "USER"]

    value: str


class DataAttributeHistory(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId")

    chat_id: Optional[str] = FieldInfo(alias="chatId")

    observed_at: str = FieldInfo(alias="observedAt")

    offset_ms: Optional[int] = FieldInfo(alias="offsetMs")
    """Where in the conversation this was said"""

    quote: Optional[str]
    """The customer's words. Null on a project with redaction on."""

    source: Literal["LIVE_EXTRACTION", "POST_CALL_EXTRACTION", "API", "USER"]

    value: str


class DataAttribute(BaseModel):
    blocked_value: Optional[str] = FieldInfo(alias="blockedValue")
    """What a newer conversation said while this field was locked"""

    evidence: Optional[DataAttributeEvidence]
    """
    The moment the current value was heard. Null for a value set by a person or the
    API.
    """

    history: List[DataAttributeHistory]
    """Other values this field has held or been offered, newest first"""

    is_locked: bool = FieldInfo(alias="isLocked")
    """True when newer conversations cannot change this field"""

    key: Literal[
        "FULL_NAME",
        "PREFERRED_NAME",
        "ACCOUNT_ID",
        "COMPANY",
        "JOB_TITLE",
        "EMAIL",
        "ALTERNATE_PHONE",
        "AGE",
        "GENDER",
        "LANGUAGE",
        "LOCATION",
        "TIMEZONE",
        "BEST_TIME_TO_REACH",
        "PREFERRED_CHANNEL",
    ]

    observed_at: str = FieldInfo(alias="observedAt")

    source: Literal["LIVE_EXTRACTION", "POST_CALL_EXTRACTION", "API", "USER"]
    """
    Where the current value came from. LIVE and POST_CALL extraction are read from
    conversations.
    """

    value: str


class Data(BaseModel):
    id: str
    """Unique identifier of the customer profile"""

    agent_ids: List[str] = FieldInfo(alias="agentIds")

    attributes: List[DataAttribute]

    chat_count: int = FieldInfo(alias="chatCount")

    conversation_count: int = FieldInfo(alias="conversationCount")

    display_name: Optional[str] = FieldInfo(alias="displayName")
    """Null until a name is known, which is common"""

    external_id: Optional[str] = FieldInfo(alias="externalId")

    first_seen_at: Optional[str] = FieldInfo(alias="firstSeenAt")

    last_seen_at: Optional[str] = FieldInfo(alias="lastSeenAt")

    notes: Optional[str]
    """Your team's shared notes. Never sent to the agent."""

    notes_updated_at: Optional[str] = FieldInfo(alias="notesUpdatedAt")

    open_items: Optional[str] = FieldInfo(alias="openItems")

    phone_number_e164: Optional[str] = FieldInfo(alias="phoneNumberE164")

    summary: Optional[str]

    talk_time_ms: int = FieldInfo(alias="talkTimeMs")
    """Voice only. Chat time is not included."""

    voice_count: int = FieldInfo(alias="voiceCount")


class CustomerProfileSetAttributeResponse(BaseModel):
    data: Data
