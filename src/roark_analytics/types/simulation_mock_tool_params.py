# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationMockToolParams"]


class SimulationMockToolParams(TypedDict, total=False):
    simulation_job_id: Required[Annotated[str, PropertyInfo(alias="simulationJobId")]]
    """
    The simulation this session belongs to, from the agent-config resolve response
    (`simulationJobId`). Roark re-validates it against the live simulation before
    answering.
    """

    tool_name: Required[Annotated[str, PropertyInfo(alias="toolName")]]
    """The tool the agent invoked."""

    arguments: Dict[str, object]
    """The arguments the agent called the tool with, verbatim."""

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Your session or room identifier, echoed back in logs for correlation."""

    tool_description: Annotated[str, PropertyInfo(alias="toolDescription")]
    """
    The tool's contract: its description and, ideally, its parameter and return
    shape. The more contract you pass, the more faithful the simulated response.
    """
