# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanCreateParams", "AgentEndpoint", "Metric", "Flow", "FlowVariant", "Persona", "Scenario"]


class SimulationRunPlanCreateParams(TypedDict, total=False):
    agent_endpoints: Required[Annotated[Iterable[AgentEndpoint], PropertyInfo(alias="agentEndpoints")]]
    """Agent endpoints to include in this run plan"""

    direction: Required[Literal["INBOUND", "OUTBOUND"]]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

    max_simulation_duration_seconds: Required[Annotated[int, PropertyInfo(alias="maxSimulationDurationSeconds")]]
    """Maximum duration in seconds for each simulation"""

    metrics: Required[Iterable[Metric]]
    """Metric definitions to include in this run plan.

    Reference each by `id` (UUID) or `slug`.
    """

    name: Required[str]
    """Name of the run plan"""

    auto_run: Annotated[bool, PropertyInfo(alias="autoRun")]
    """Whether to automatically trigger a job after creating the run plan"""

    description: str
    """Description of the run plan"""

    end_call_phrases: Annotated[SequenceNotStr[str], PropertyInfo(alias="endCallPhrases")]
    """Phrases that trigger end of call. Empty array disables the feature."""

    end_call_reasons: Annotated[SequenceNotStr[str], PropertyInfo(alias="endCallReasons")]
    """Semantic conditions that trigger end of call.

    The LLM evaluates the conversation against these conditions. Empty array
    disables the feature.
    """

    execution_mode: Annotated[
        Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"], PropertyInfo(alias="executionMode")
    ]
    """Execution mode (PARALLEL or SEQUENTIAL)"""

    flows: Iterable[Flow]
    """Customer flows to include in this run plan.

    The same flow can appear more than once with a different persona override or
    different variables.
    """

    iteration_count: Annotated[int, PropertyInfo(alias="iterationCount")]
    """Number of iterations to run for each test case (1-10000)"""

    max_concurrent_jobs: Annotated[int, PropertyInfo(alias="maxConcurrentJobs")]
    """Maximum number of concurrent simulation jobs"""

    personas: Iterable[Persona]
    """Personas to include in this run plan.

    Required with `scenarios`; ignored with `flows`, where each variant carries its
    own persona.
    """

    scenarios: Iterable[Scenario]
    """Deprecated: use `flows` instead.

    Scenarios to include in this run plan. The same scenario ID can appear multiple
    times with different variables.
    """

    silence_timeout_seconds: Annotated[int, PropertyInfo(alias="silenceTimeoutSeconds")]
    """Timeout in seconds for silence detection"""


class AgentEndpoint(TypedDict, total=False):
    id: Required[str]


class Metric(TypedDict, total=False):
    id: str
    """Metric definition UUID. Provide either this or `slug`, not both."""

    metric_id: Annotated[str, PropertyInfo(alias="metricId")]
    """Alias of `slug` accepted for backwards compatibility.

    Use `slug` for new integrations.
    """

    slug: str
    """Stable metric slug (e.g.

    `customer_satisfaction`). Provide either this or `id`, not both.
    """


class FlowVariant(TypedDict, total=False):
    id: Required[str]

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]

    variables: Dict[str, str]


class Flow(TypedDict, total=False):
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

    customer_flow_id: Required[Annotated[str, PropertyInfo(alias="customerFlowId")]]

    variants: Required[Iterable[FlowVariant]]

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]

    variables: Dict[str, str]

    variant_selection_mode: Annotated[
        Literal["ALL_VARIANTS", "DEFAULT_VARIANT", "SPECIFIC_VARIANT"], PropertyInfo(alias="variantSelectionMode")
    ]


class Persona(TypedDict, total=False):
    id: Required[str]


class Scenario(TypedDict, total=False):
    id: Required[str]
    """Scenario ID"""

    variables: Dict[str, str]
    """Template variables for this scenario instance.

    The same scenario can appear multiple times with different variables.
    """
