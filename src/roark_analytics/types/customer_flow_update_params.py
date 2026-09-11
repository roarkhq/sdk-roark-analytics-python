# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["CustomerFlowUpdateParams", "AgentExpectation", "OffScriptPolicy"]


class AgentExpectation(TypedDict, total=False):
    prompt: Required[str]
    """What the agent under test is graded against."""


class OffScriptPolicy(TypedDict, total=False):
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

    off_script_policy: Annotated[Optional[OffScriptPolicy], PropertyInfo(alias="offScriptPolicy")]

    script_adherence: Annotated[Literal["LOOSE", "STRICT"], PropertyInfo(alias="scriptAdherence")]
    """
    Scripted flows only. How closely a run follows the script. LOOSE (default) hands
    the whole script to the simulated customer as one prompt; it keeps the call
    moving whatever your agent says. STRICT runs the script as a state machine on
    the agent service: at every agent step the simulated customer waits, silent,
    until your agent has said the expected line, and only then moves on. Scripted
    flows only; STRICT needs the agent-service transport and is not available on
    realtime models.
    """

    title: str
