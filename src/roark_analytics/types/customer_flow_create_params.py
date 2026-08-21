# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "CustomerFlowCreateParams",
    "CreateScriptedCustomerFlowInput",
    "CreateScriptedCustomerFlowInputAgentExpectation",
    "CreateImprovCustomerFlowInput",
    "CreateImprovCustomerFlowInputHappyPath",
    "CreateImprovCustomerFlowInputAgentExpectation",
    "CreateImprovCustomerFlowInputEdgeCase",
]


class CreateScriptedCustomerFlowInput(TypedDict, total=False):
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

    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]
    """Agents this flow exercises. Optional for scripted flows."""

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
    """Agents this flow exercises. At least one is required for improv flows."""

    happy_path: Required[Annotated[CreateImprovCustomerFlowInputHappyPath, PropertyInfo(alias="happyPath")]]
    """The way this flow is meant to go."""

    title: Required[str]

    type: Required[Literal["IMPROV"]]

    agent_expectations: Annotated[
        Iterable[CreateImprovCustomerFlowInputAgentExpectation], PropertyInfo(alias="agentExpectations")
    ]

    description: Optional[str]

    edge_cases: Annotated[Iterable[CreateImprovCustomerFlowInputEdgeCase], PropertyInfo(alias="edgeCases")]
    """
    Other ways of running it, each inheriting from the happy path what it does not
    name.
    """


class CreateImprovCustomerFlowInputHappyPath(TypedDict, total=False):
    """The way this flow is meant to go."""

    environment_id: Required[Annotated[str, PropertyInfo(alias="environmentId")]]
    """The conditions this flow runs under.

    Edge cases inherit them unless they name their own.
    """

    persona_override_id: Required[Annotated[str, PropertyInfo(alias="personaOverrideId")]]
    """The persona this flow runs as.

    Edge cases inherit it unless they name their own.
    """

    title: Required[str]

    preceded_by_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="precededByCustomerFlowId")]

    preceded_by_customer_flow_variant_id: Annotated[
        Optional[str], PropertyInfo(alias="precededByCustomerFlowVariantId")
    ]

    prompt: Optional[str]


class CreateImprovCustomerFlowInputAgentExpectation(TypedDict, total=False):
    prompt: Required[str]
    """What the agent under test is graded against."""


class CreateImprovCustomerFlowInputEdgeCase(TypedDict, total=False):
    title: Required[str]

    environment_id: Annotated[Optional[str], PropertyInfo(alias="environmentId")]

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """The persona this runs as. Omit to inherit the happy path's."""

    preceded_by_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="precededByCustomerFlowId")]

    preceded_by_customer_flow_variant_id: Annotated[
        Optional[str], PropertyInfo(alias="precededByCustomerFlowVariantId")
    ]

    prompt: Optional[str]


CustomerFlowCreateParams: TypeAlias = Union[CreateScriptedCustomerFlowInput, CreateImprovCustomerFlowInput]

from .flow_step_param import FlowStepParam
