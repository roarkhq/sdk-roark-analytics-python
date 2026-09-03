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
    """
    Scripted flows only. How a run walks the graph. DETERMINISTIC ("Simulate every
    path" in the app) places one call per variant, each following its path exactly
    whatever the agent says. ADAPTIVE ("Adapt to your agent") collapses the paths
    into one call PER PERSONA, on which the simulated customer picks a branch from
    what the agent actually said. Both modes speak the exact authored lines, and
    neither changes how metrics or expectations grade.
    """

    description: Optional[str]

    title: str
