# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationCustomerFlowCreateParams", "AgentExpectation", "Variant"]


class SimulationCustomerFlowCreateParams(TypedDict, total=False):
    agent_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]]
    """Agents this flow exercises. At least one is required."""

    mode: Required[Literal["UNSCRIPTED", "SCRIPTED"]]
    """
    SCRIPTED follows a step graph you author; UNSCRIPTED gives the simulated
    customer a brief and lets it improvise.
    """

    title: Required[str]

    agent_expectations: Annotated[Iterable[AgentExpectation], PropertyInfo(alias="agentExpectations")]

    description: Optional[str]

    scripted_branching_mode: Annotated[
        Literal["DETERMINISTIC", "ADAPTIVE"], PropertyInfo(alias="scriptedBranchingMode")
    ]
    """Scripted flows only.

    DETERMINISTIC runs one variant per path through the graph; ADAPTIVE collapses
    the paths into one call the customer adapts across.
    """

    steps: Iterable["FlowStepParam"]
    """Required for SCRIPTED flows. At most 100 steps across at most 25 paths."""

    variants: Iterable[Variant]
    """Required for UNSCRIPTED flows: the briefs to run.

    Scripted flows get one variant per path from the graph instead.
    """


class AgentExpectation(TypedDict, total=False):
    llm_prompt: Required[Annotated[str, PropertyInfo(alias="llmPrompt")]]


class Variant(TypedDict, total=False):
    title: Required[str]

    environment_id: Annotated[Optional[str], PropertyInfo(alias="environmentId")]

    is_default: Annotated[bool, PropertyInfo(alias="isDefault")]

    persona_id: Annotated[Optional[str], PropertyInfo(alias="personaId")]

    preceded_by_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="precededByCustomerFlowId")]

    preceded_by_customer_flow_variant_id: Annotated[
        Optional[str], PropertyInfo(alias="precededByCustomerFlowVariantId")
    ]

    prompt: Optional[str]


from .flow_step_param import FlowStepParam
