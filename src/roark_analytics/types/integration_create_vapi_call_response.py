# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationCreateVapiCallResponse", "Data"]


class Data(BaseModel):
    call_id: str = FieldInfo(alias="callId")
    """ID of the uploaded call"""


class IntegrationCreateVapiCallResponse(BaseModel):
    data: Data
    """Vapi call upload response"""
