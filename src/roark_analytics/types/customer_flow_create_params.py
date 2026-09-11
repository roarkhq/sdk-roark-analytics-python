# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .flow_step_param import FlowStepParam

__all__ = [
    "CustomerFlowCreateParams",
    "CreateImprovCustomerFlowInput",
    "CreateImprovCustomerFlowInputEdgeCase",
    "CreateImprovCustomerFlowInputHappyPath",
    "CreateScriptedCustomerFlowInput",
    "CreateScriptedCustomerFlowInputAgentExpectation",
    "CreateScriptedCustomerFlowInputOffScriptPolicy",
]


class CreateScriptedCustomerFlowInputAgentExpectation(TypedDict, total=False):
    prompt: Required[str]
    """What the agent under test is graded against."""


class CreateScriptedCustomerFlowInputOffScriptPolicy(TypedDict, total=False):
    """
    STRICT only. What the simulated customer does when your agent does not say the
    expected line. Each unmatched agent utterance is an attempt: `reaction` runs per
    attempt (STAY_SILENT, REPEAT its last scripted line, RESPOND once in character
    without moving on, or SAY `sayLine`), and `then` runs when attempts reach
    `maxAttempts` or your agent stays silent for `waitSeconds` (HANG_UP ends the
    call with ended reason SCRIPT_DIVERGED, HANG_UP_INVALIDATE ends it the same way
    and invalidates the run so it is scored by nothing and counted nowhere, MOVE_ON
    advances anyway, ADAPT hands the rest of the call to loose behaviour). Null:
    stay silent, 3 attempts, hang up. The default for every agent step; an
    AGENT_TURN step can carry its own.
    """

    max_attempts: Required[Annotated[int, PropertyInfo(alias="maxAttempts")]]

    reaction: Required[Literal["STAY_SILENT", "REPEAT", "RESPOND", "SAY"]]

    then: Required[Literal["HANG_UP", "MOVE_ON", "ADAPT", "HANG_UP_INVALIDATE"]]

    say_line: Annotated[Optional[str], PropertyInfo(alias="sayLine")]

    wait_seconds: Annotated[Optional[int], PropertyInfo(alias="waitSeconds")]


class CreateScriptedCustomerFlowInput(TypedDict, total=False):
    graph: Required[List[FlowStepParam]]
    """
    The conversation, as a graph of steps. At most 100 steps across at most 25
    paths. The variants come from the graph: one per path, so they are not sent
    here. A CUSTOMER_TURN describes what the simulated customer says and the persona
    phrases it; a CUSTOMER_VERBATIM_TURN is said word for word.
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
    How a run walks the graph. DETERMINISTIC ("Simulate every path" in the app)
    places one call per variant, each following its path exactly whatever the agent
    says. ADAPTIVE ("Adapt to your agent") collapses the paths into one call PER
    PERSONA, on which the simulated customer picks a branch from what the agent
    actually said. Both modes speak the exact authored lines, and neither changes
    how metrics or expectations grade. (DETERMINISTIC is the default.)
    """

    description: Optional[str]

    off_script_policy: Annotated[
        Optional[CreateScriptedCustomerFlowInputOffScriptPolicy], PropertyInfo(alias="offScriptPolicy")
    ]

    script_adherence: Annotated[Literal["LOOSE", "STRICT"], PropertyInfo(alias="scriptAdherence")]
    """
    How closely a run follows the script. LOOSE (default) hands the whole script to
    the simulated customer as one prompt; it keeps the call moving whatever your
    agent says. STRICT runs the script as a state machine on the agent service: at
    every agent step the simulated customer waits, silent, until your agent has said
    the expected line, and only then moves on. Scripted flows only; STRICT needs the
    agent-service transport and is not available on realtime models. (LOOSE is the
    default.)
    """


class CreateImprovCustomerFlowInputHappyPath(TypedDict, total=False):
    """The way this flow is meant to go."""

    environment_id: Required[Annotated[str, PropertyInfo(alias="environmentId")]]
    """
    The conditions this flow runs under. Edge cases inherit them unless they name
    their own.
    """

    persona_override_id: Required[Annotated[str, PropertyInfo(alias="personaOverrideId")]]
    """The persona this flow runs as. Edge cases inherit it unless they name their own."""

    title: Required[str]

    preceded_by_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="precededByCustomerFlowId")]

    preceded_by_customer_flow_variant_id: Annotated[
        Optional[str], PropertyInfo(alias="precededByCustomerFlowVariantId")
    ]

    prompt: Optional[str]


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


class CreateImprovCustomerFlowInput(TypedDict, total=False):
    agent_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]]
    """Agents this flow exercises. At least one is required for improv flows."""

    happy_path: Required[Annotated[CreateImprovCustomerFlowInputHappyPath, PropertyInfo(alias="happyPath")]]
    """The way this flow is meant to go."""

    title: Required[str]

    type: Required[Literal["IMPROV"]]

    agent_expectations: Annotated[
        Iterable[CreateScriptedCustomerFlowInputAgentExpectation], PropertyInfo(alias="agentExpectations")
    ]

    description: Optional[str]

    edge_cases: Annotated[Iterable[CreateImprovCustomerFlowInputEdgeCase], PropertyInfo(alias="edgeCases")]
    """
    Other ways of running it, each inheriting from the happy path what it does not
    name.
    """


CustomerFlowCreateParams: TypeAlias = Union[CreateScriptedCustomerFlowInput, CreateImprovCustomerFlowInput]
