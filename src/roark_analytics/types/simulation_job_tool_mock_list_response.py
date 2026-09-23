# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationJobToolMockListResponse", "Data"]


class Data(BaseModel):
    """
    One guarded tool invocation during a test call: what the agent tried to call,
    and what it got.
    """

    id: str

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601."""

    session_id: Optional[str] = FieldInfo(alias="sessionId")

    source: Literal["GENERATED", "FIXTURE"]
    """
    GENERATED = the scenario-aware model answered; FIXTURE = a pinned deterministic
    response.
    """

    tool_name: str = FieldInfo(alias="toolName")

    arguments: Optional[object] = None
    """What the agent called the tool with, verbatim."""

    result: Optional[object] = None
    """The simulated response the agent received."""


class SimulationJobToolMockListResponse(BaseModel):
    data: List[Data]
