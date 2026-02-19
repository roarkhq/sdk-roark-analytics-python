# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanCreateParams", "AgentEndpoint", "Evaluator", "Persona", "Scenario"]


class SimulationRunPlanCreateParams(TypedDict, total=False):
    agent_endpoints: Required[Annotated[Iterable[AgentEndpoint], PropertyInfo(alias="agentEndpoints")]]
    """Agent endpoints to include in this run plan"""

    direction: Required[Literal["INBOUND", "OUTBOUND"]]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

    evaluators: Required[Iterable[Evaluator]]
    """Evaluators to include in this run plan"""

    max_simulation_duration_seconds: Required[Annotated[int, PropertyInfo(alias="maxSimulationDurationSeconds")]]
    """Maximum duration in seconds for each simulation"""

    name: Required[str]
    """Name of the run plan"""

    personas: Required[Iterable[Persona]]
    """Personas to include in this run plan"""

    scenarios: Required[Iterable[Scenario]]
    """Scenarios to include in this run plan"""

    auto_run: Annotated[bool, PropertyInfo(alias="autoRun")]
    """Whether to automatically trigger a job after creating the run plan"""

    description: str
    """Description of the run plan"""

    end_call_phrases: Annotated[SequenceNotStr[str], PropertyInfo(alias="endCallPhrases")]
    """Phrases that trigger end of call. Empty array disables the feature."""

    execution_mode: Annotated[
        Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"], PropertyInfo(alias="executionMode")
    ]
    """Execution mode (PARALLEL or SEQUENTIAL)"""

    iteration_count: Annotated[int, PropertyInfo(alias="iterationCount")]
    """Number of iterations to run for each test case.

    Must be 1 for OUTBOUND direction.
    """

    max_concurrent_jobs: Annotated[int, PropertyInfo(alias="maxConcurrentJobs")]
    """Maximum number of concurrent simulation jobs"""

    silence_timeout_seconds: Annotated[int, PropertyInfo(alias="silenceTimeoutSeconds")]
    """Timeout in seconds for silence detection"""


class AgentEndpoint(TypedDict, total=False):
    id: Required[str]


class Evaluator(TypedDict, total=False):
    id: Required[str]


class Persona(TypedDict, total=False):
    id: Required[str]


class Scenario(TypedDict, total=False):
    id: Required[str]
