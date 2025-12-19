# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallCreateResponse", "Data", "DataAgent", "DataAgentEndpoint", "DataCustomer"]


class DataAgentEndpoint(BaseModel):
    id: str

    environment: str

    phone_number_e164: Optional[str] = FieldInfo(alias="phoneNumberE164", default=None)


class DataAgent(BaseModel):
    id: str

    endpoint: Optional[DataAgentEndpoint] = None


class DataCustomer(BaseModel):
    label: Optional[str] = None

    phone_number_e164: Optional[str] = FieldInfo(alias="phoneNumberE164", default=None)


class Data(BaseModel):
    """Response after creating a call"""

    id: str
    """Unique identifier for the call"""

    agents: Optional[List[DataAgent]] = None

    call_direction: Literal["INBOUND", "OUTBOUND"] = FieldInfo(alias="callDirection")
    """Direction of the call (inbound or outbound)"""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    customers: Optional[List[DataCustomer]] = None

    project_id: str = FieldInfo(alias="projectId")
    """ID of the project this call belongs to"""

    started_at: str = FieldInfo(alias="startedAt")
    """Timestamp when the call started"""

    status: Optional[Literal["RINGING", "IN_PROGRESS", "ENDED"]] = None


class CallCreateResponse(BaseModel):
    data: Data
    """Response after creating a call"""
