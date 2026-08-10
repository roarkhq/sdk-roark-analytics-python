# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationCustomerFlowUpdateParams", "AgentExpectation"]


class SimulationCustomerFlowUpdateParams(TypedDict, total=False):
    agent_expectations: Annotated[Iterable[AgentExpectation], PropertyInfo(alias="agentExpectations")]
    """Replaces the flow-level expectations. Omit to leave them unchanged."""

    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]
    """Replaces the linked agents. Omit to leave them unchanged."""

    description: Optional[str]

    scripted_branching_mode: Annotated[
        Literal["DETERMINISTIC", "ADAPTIVE"], PropertyInfo(alias="scriptedBranchingMode")
    ]

    title: str


class AgentExpectation(TypedDict, total=False):
    llm_prompt: Required[Annotated[str, PropertyInfo(alias="llmPrompt")]]
