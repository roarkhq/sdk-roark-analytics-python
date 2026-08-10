# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationRunPlanCreateResponse",
    "Data",
    "DataRunPlan",
    "DataRunPlanAgentEndpoint",
    "DataRunPlanEvaluator",
    "DataRunPlanFlow",
    "DataRunPlanFlowVariant",
    "DataRunPlanMetric",
    "DataRunPlanPersona",
    "DataRunPlanScenario",
    "DataRunPlanJob",
]


class DataRunPlanAgentEndpoint(BaseModel):
    id: str


class DataRunPlanEvaluator(BaseModel):
    id: str


class DataRunPlanFlowVariant(BaseModel):
    id: str

    persona_override_id: Optional[str] = FieldInfo(alias="personaOverrideId", default=None)

    variables: Optional[Dict[str, str]] = None


class DataRunPlanFlow(BaseModel):
    """One customer flow attached to a run plan.

    To run specific variants, list them in `variants`. Each entry may carry its own
    `personaOverrideId` and `variables`, so pinning two variants of one flow at different
    values is a single attachment.

    To let the run resolve the variants instead, leave `variants` out and set
    `variantSelectionMode`:
      ALL_VARIANTS: every variant the flow has when the run starts
      DEFAULT_VARIANT: only its default, so it follows the flow as the default moves

    There is no default mode. Each variant is a separate simulated call, so a forgotten
    field would quietly change how many calls a run places.

    `personaOverrideId` runs a variant as that persona instead of its own. Set it on the
    attachment to apply to every variant it resolves, or on a `variants` entry for one.
    The entry wins. Attaching the same flow more than once with different overrides is how
    you fan it out across personas.

    `variables` pins {{variable}} values the same way. Anything left unset is asked for
    when the run starts.
    """

    customer_flow_id: str = FieldInfo(alias="customerFlowId")

    variants: List[DataRunPlanFlowVariant]

    persona_override_id: Optional[str] = FieldInfo(alias="personaOverrideId", default=None)

    variables: Optional[Dict[str, str]] = None

    variant_selection_mode: Optional[Literal["ALL_VARIANTS", "DEFAULT_VARIANT", "SPECIFIC_VARIANT"]] = FieldInfo(
        alias="variantSelectionMode", default=None
    )


class DataRunPlanMetric(BaseModel):
    id: str


class DataRunPlanPersona(BaseModel):
    id: str


class DataRunPlanScenario(BaseModel):
    id: str

    variables: Optional[Dict[str, str]] = None
    """Template variables for this scenario instance.

    Absent when no variables are set. The same scenario can appear multiple times
    with different variables.
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
    """Semantic conditions that trigger end of call.

    The LLM evaluates the conversation against these conditions. Empty array means
    disabled.
    """

    evaluators: List[DataRunPlanEvaluator]
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

    metrics: List[DataRunPlanMetric]
    """Metric definitions included in this run plan"""

    name: str
    """Name of the run plan"""

    personas: List[DataRunPlanPersona]
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
    """Response when triggering a simulation run plan"""


class SimulationRunPlanCreateResponse(BaseModel):
    data: Data
    """Response when creating a run plan, optionally including a triggered job"""
