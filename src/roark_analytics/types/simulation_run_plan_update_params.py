# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanUpdateParams", "AgentEndpoint", "Metric", "Persona", "Scenario"]


class SimulationRunPlanUpdateParams(TypedDict, total=False):
    agent_endpoints: Annotated[Iterable[AgentEndpoint], PropertyInfo(alias="agentEndpoints")]
    """Agent endpoints to include in this run plan"""

    description: str
    """Description of the run plan"""

    direction: Literal["INBOUND", "OUTBOUND"]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

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

    max_simulation_duration_seconds: Annotated[int, PropertyInfo(alias="maxSimulationDurationSeconds")]
    """Maximum duration in seconds for each simulation"""

    metrics: Iterable[Metric]
    """Metric definitions to include in this run plan"""

    name: str
    """Name of the run plan"""

    personas: Iterable[Persona]
    """Personas to include in this run plan"""

    scenarios: Iterable[Scenario]
    """Scenarios to include in this run plan.

    The same scenario ID can appear multiple times with different variables.
    """

    silence_timeout_seconds: Annotated[int, PropertyInfo(alias="silenceTimeoutSeconds")]
    """Timeout in seconds for silence detection"""


class AgentEndpoint(TypedDict, total=False):
    id: Required[str]


class Metric(TypedDict, total=False):
    id: Required[str]


class Persona(TypedDict, total=False):
    id: Required[str]


class Scenario(TypedDict, total=False):
    id: Required[str]
    """Scenario ID"""

    variables: Dict[str, str]
    """Template variables for this scenario instance.

    The same scenario can appear multiple times with different variables.
    """
