# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SimulationCustomerFlowCreateParams",
    "CreateScriptedCustomerFlowInput",
    "CreateScriptedCustomerFlowInputAgentExpectation",
    "CreateImprovCustomerFlowInput",
    "CreateImprovCustomerFlowInputVariant",
    "CreateImprovCustomerFlowInputAgentExpectation",
]


class CreateScriptedCustomerFlowInput(TypedDict, total=False):
    agent_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]]
    """Agents this flow exercises. At least one is required."""

    graph: Required[Iterable["FlowStepParam"]]
    """The conversation, as a graph of steps.

    At most 100 steps across at most 25 paths. The variants come from the graph: one
    per path, so they are not sent here.
    """

    title: Required[str]

    type: Required[Literal["SCRIPTED"]]

    agent_expectations: Annotated[
        Iterable[CreateScriptedCustomerFlowInputAgentExpectation], PropertyInfo(alias="agentExpectations")
    ]

    branching_mode: Annotated[Literal["DETERMINISTIC", "ADAPTIVE"], PropertyInfo(alias="branchingMode")]
    """
    DETERMINISTIC (the default) runs one variant per path through the graph;
    ADAPTIVE collapses the paths into one call the simulated customer adapts across.
    """

    description: Optional[str]


class CreateScriptedCustomerFlowInputAgentExpectation(TypedDict, total=False):
    prompt: Required[str]
    """What the agent under test is graded against."""


class CreateImprovCustomerFlowInput(TypedDict, total=False):
    agent_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]]
    """Agents this flow exercises. At least one is required."""

    title: Required[str]

    type: Required[Literal["IMPROV"]]

    variants: Required[Iterable[CreateImprovCustomerFlowInputVariant]]
    """The briefs to run. At least one, and one of them is the default."""

    agent_expectations: Annotated[
        Iterable[CreateImprovCustomerFlowInputAgentExpectation], PropertyInfo(alias="agentExpectations")
    ]

    description: Optional[str]


class CreateImprovCustomerFlowInputVariant(TypedDict, total=False):
    title: Required[str]

    environment_id: Annotated[Optional[str], PropertyInfo(alias="environmentId")]

    is_default: Annotated[bool, PropertyInfo(alias="isDefault")]

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """The persona this variant runs as.

    Omit on a non-default variant to inherit the default variant's.
    """

    preceded_by_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="precededByCustomerFlowId")]

    preceded_by_customer_flow_variant_id: Annotated[
        Optional[str], PropertyInfo(alias="precededByCustomerFlowVariantId")
    ]

    prompt: Optional[str]


class CreateImprovCustomerFlowInputAgentExpectation(TypedDict, total=False):
    prompt: Required[str]
    """What the agent under test is graded against."""


SimulationCustomerFlowCreateParams: TypeAlias = Union[CreateScriptedCustomerFlowInput, CreateImprovCustomerFlowInput]

from .flow_step_param import FlowStepParam
