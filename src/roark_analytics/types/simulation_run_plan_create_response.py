# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationRunPlanCreateResponse",
    "Data",
    "DataRunPlan",
    "DataRunPlanAgentEndpoint",
    "DataRunPlanFlow",
    "DataRunPlanFlowEdgeCaseUnionMember1",
    "DataRunPlanJob",
    "DataRunPlanScenario",
]


class DataRunPlanAgentEndpoint(BaseModel):
    id: str


class DataRunPlanFlowEdgeCaseUnionMember1(BaseModel):
    id: str
    """The edge case to run."""

    persona_override_id: Optional[str] = FieldInfo(alias="personaOverrideId", default=None)
    """Run this one as that persona instead of its own."""

    variables: Optional[Dict[str, str]] = None
    """Values for this one only."""


class DataRunPlanFlow(BaseModel):
    """
    One customer flow attached to a run plan, and which of its ways of running you
    cover.
    Attaching the same flow more than once with different overrides is how you fan
    it out across personas or values.
    """

    id: str
    """The customer flow to run."""

    edge_cases: Optional[Union[Literal["ALL"], List[DataRunPlanFlowEdgeCaseUnionMember1]]] = FieldInfo(
        alias="edgeCases", default=None
    )
    """
    `"ALL"` runs every edge case the flow has when the run starts, so one added
    later is covered. An array runs only the ones you name, each able to carry its
    own persona override and values.
    """

    happy_path: Optional[bool] = FieldInfo(alias="happyPath", default=None)
    """Run the flow's happy path. Resolved when the run starts, so it follows the flow."""

    persona_override_id: Optional[str] = FieldInfo(alias="personaOverrideId", default=None)
    """Runs everything this attachment resolves as that persona instead of its own."""

    variables: Optional[Dict[str, str]] = None
    """Values for everything it resolves."""


class DataRunPlanScenario(BaseModel):
    id: str

    variables: Optional[Dict[str, str]] = None
    """
    Template variables for this scenario instance. Absent when no variables are set.
    The same scenario can appear multiple times with different variables.
    """


class DataRunPlan(BaseModel):
    """A simulation run plan defining the test matrix"""

    id: str
    """Unique identifier of the run plan"""

    agent_endpoints: List[DataRunPlanAgentEndpoint] = FieldInfo(alias="agentEndpoints")
    """Agent endpoints included in this run plan"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the run plan was created"""

    direction: Literal["INBOUND", "OUTBOUND"]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

    end_call_phrases: List[str] = FieldInfo(alias="endCallPhrases")
    """Phrases that trigger end of call. Empty array means disabled."""

    end_call_reasons: List[str] = FieldInfo(alias="endCallReasons")
    """
    Semantic conditions that trigger end of call. The LLM evaluates the conversation
    against these conditions. Empty array means disabled.
    """

    evaluators: List[DataRunPlanAgentEndpoint]
    """Deprecated: Use metrics instead. Evaluators included in this run plan."""

    execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] = FieldInfo(
        alias="executionMode"
    )
    """Execution mode (PARALLEL or SEQUENTIAL)"""

    flows: List[DataRunPlanFlow]
    """Customer flows included in this run plan"""

    iteration_count: int = FieldInfo(alias="iterationCount")
    """Number of iterations to run for each test case"""

    max_concurrent_jobs: int = FieldInfo(alias="maxConcurrentJobs")
    """Maximum number of concurrent simulation jobs"""

    max_simulation_duration_seconds: int = FieldInfo(alias="maxSimulationDurationSeconds")
    """Maximum duration in seconds for each simulation"""

    metrics: List[DataRunPlanAgentEndpoint]
    """Metric definitions included in this run plan"""

    name: str
    """Name of the run plan"""

    personas: List[DataRunPlanAgentEndpoint]
    """Personas included in this run plan. Only meaningful alongside `scenarios`."""

    scenarios: List[DataRunPlanScenario]
    """Deprecated: use `flows` instead. Scenarios included in this run plan."""

    silence_timeout_seconds: int = FieldInfo(alias="silenceTimeoutSeconds")
    """Timeout in seconds for silence detection"""

    test_case_count: int = FieldInfo(alias="testCaseCount")
    """Total number of test cases generated from the plan configuration"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the run plan was last updated"""

    description: Optional[str] = None
    """Description of the run plan"""


class DataRunPlanJob(BaseModel):
    """Response when triggering a simulation run plan"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    simulation_run_plan_id: str = FieldInfo(alias="simulationRunPlanId")
    """ID of the simulation run plan that was executed"""

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")
    """ID of the simulation run plan job that was created"""

    status: Literal[
        "PENDING",
        "QUEUED",
        "CREATING_SNAPSHOTS",
        "CREATING_SIMULATIONS",
        "PREPARING_CAPACITY",
        "RUNNING_SIMULATIONS",
        "COMPLETED",
        "FAILED",
        "TIMED_OUT",
        "CANCELLED",
        "CANCELLING",
        "ENDING_SIMULATIONS",
    ]
    """Initial status of the job"""


class Data(BaseModel):
    """Response when creating a run plan, optionally including a triggered job"""

    run_plan: DataRunPlan = FieldInfo(alias="runPlan")
    """A simulation run plan defining the test matrix"""

    run_plan_job: Optional[DataRunPlanJob] = FieldInfo(alias="runPlanJob", default=None)
    """The triggered job, only present if autoRun was true"""


class SimulationRunPlanCreateResponse(BaseModel):
    data: Data
    """Response when creating a run plan, optionally including a triggered job"""
