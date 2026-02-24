# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationRunPlanUpdateResponse",
    "Data",
    "DataAgentEndpoint",
    "DataEvaluator",
    "DataPersona",
    "DataScenario",
]


class DataAgentEndpoint(BaseModel):
    id: str


class DataEvaluator(BaseModel):
    id: str


class DataPersona(BaseModel):
    id: str


class DataScenario(BaseModel):
    id: str


class Data(BaseModel):
    """A simulation run plan defining the test matrix"""

    id: str
    """Unique identifier of the run plan"""

    agent_endpoints: List[DataAgentEndpoint] = FieldInfo(alias="agentEndpoints")
    """Agent endpoints included in this run plan"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the run plan was created"""

    direction: Literal["INBOUND", "OUTBOUND"]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

    end_call_phrases: List[str] = FieldInfo(alias="endCallPhrases")
    """Phrases that trigger end of call. Empty array means disabled."""

    evaluators: List[DataEvaluator]
    """Evaluators included in this run plan"""

    execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] = FieldInfo(
        alias="executionMode"
    )
    """Execution mode (PARALLEL or SEQUENTIAL)"""

    iteration_count: int = FieldInfo(alias="iterationCount")
    """Number of iterations to run for each test case"""

    max_concurrent_jobs: int = FieldInfo(alias="maxConcurrentJobs")
    """Maximum number of concurrent simulation jobs"""

    max_simulation_duration_seconds: int = FieldInfo(alias="maxSimulationDurationSeconds")
    """Maximum duration in seconds for each simulation"""

    name: str
    """Name of the run plan"""

    personas: List[DataPersona]
    """Personas included in this run plan"""

    scenarios: List[DataScenario]
    """Scenarios included in this run plan"""

    silence_timeout_seconds: int = FieldInfo(alias="silenceTimeoutSeconds")
    """Timeout in seconds for silence detection"""

    test_case_count: int = FieldInfo(alias="testCaseCount")
    """Total number of test cases generated from the plan configuration"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the run plan was last updated"""

    description: Optional[str] = None
    """Description of the run plan"""


class SimulationRunPlanUpdateResponse(BaseModel):
    data: Data
    """A simulation run plan defining the test matrix"""
