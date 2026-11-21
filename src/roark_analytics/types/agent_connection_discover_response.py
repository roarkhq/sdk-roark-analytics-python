# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentConnectionDiscoverResponse", "Data"]


class Data(BaseModel):
    id: str
    """The platform's id, for `agentIds`"""

    hipaa_enabled: Optional[bool] = FieldInfo(alias="hipaaEnabled")
    """
    Vapi only: true when the assistant withholds recordings, so its calls cannot be
    analysed. Null elsewhere.
    """

    name: str


class AgentConnectionDiscoverResponse(BaseModel):
    data: List[Data]
