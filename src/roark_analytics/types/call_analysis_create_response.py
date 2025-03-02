# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallAnalysisCreateResponse", "Data", "DataCall", "DataCallParticipant"]


class DataCallParticipant(BaseModel):
    role: Literal["AGENT", "CUSTOMER"]

    is_simulated: Optional[bool] = FieldInfo(alias="isSimulated", default=None)

    name: Optional[str] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    spoke_first: Optional[bool] = FieldInfo(alias="spokeFirst", default=None)


class DataCall(BaseModel):
    id: str

    call_direction: Literal["INBOUND", "OUTBOUND"] = FieldInfo(alias="callDirection")

    is_test: bool = FieldInfo(alias="isTest")

    participants: List[DataCallParticipant]

    started_at: str = FieldInfo(alias="startedAt")

    status: Optional[Literal["RINGING", "IN_PROGRESS", "ENDED"]] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    ended_at: Optional[str] = FieldInfo(alias="endedAt", default=None)

    ended_reason: Optional[str] = FieldInfo(alias="endedReason", default=None)

    properties: Optional[Dict[str, object]] = None

    summary: Optional[str] = None


class Data(BaseModel):
    call: DataCall

    job_id: str = FieldInfo(alias="jobId")
    """Analysis job ID for tracking progress"""

    status: Literal["PENDING", "IN_PROGRESS", "COMPLETED", "FAILED"]


class CallAnalysisCreateResponse(BaseModel):
    data: Data
    """Analysis job with associated call context"""
