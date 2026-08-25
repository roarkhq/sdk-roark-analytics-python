# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["CustomerFlowUpdateParams", "AgentExpectation"]


class AgentExpectation(TypedDict, total=False):
    prompt: Required[str]
    """What the agent under test is graded against."""


class CustomerFlowUpdateParams(TypedDict, total=False):
    agent_expectations: Annotated[Iterable[AgentExpectation], PropertyInfo(alias="agentExpectations")]
    """Replaces the flow-level expectations. Omit to leave them unchanged."""

    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]
    """
    Replaces the linked agents. Omit to leave them unchanged. An improv flow must
    keep at least one; a scripted flow can be left with none.
    """

    branching_mode: Annotated[Literal["DETERMINISTIC", "ADAPTIVE"], PropertyInfo(alias="branchingMode")]
    """Scripted flows only."""

    description: Optional[str]

    title: str
