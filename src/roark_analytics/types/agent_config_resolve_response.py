# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentConfigResolveResponse", "Data"]


class Data(BaseModel):
    channel: Literal["production", "staging"]
    """Which channel this session resolved to."""

    document: Dict[str, object]
    """The config JSON to apply."""

    key: str

    revision_id: str = FieldInfo(alias="revisionId")

    simulation_job_id: Optional[str] = FieldInfo(alias="simulationJobId")
    """
    Set when this session is a Roark simulation call. Stamp it (and the revisionId)
    into your session metadata so analysis attributes the call correctly.
    """


class AgentConfigResolveResponse(BaseModel):
    data: Data
