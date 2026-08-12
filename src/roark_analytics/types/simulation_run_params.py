# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SimulationRunParams",
    "RunSimulationFromConfig",
    "RunSimulationFromConfigPlan",
    "RunSimulationFromConfigPlanAgentEndpoint",
    "RunSimulationFromConfigPlanMetric",
    "RunSimulationFromConfigPlanFlow",
    "RunSimulationFromConfigPlanFlowEdgeCasesUnionMember1",
    "RunSimulationFromConfigPlanPersona",
    "RunSimulationFromConfigPlanScenario",
    "RunSimulationFromConfigVariablesUnionMember1",
    "RunSimulationFromConfigVariablesUnionMember2",
    "RunSimulationFromPlanID",
    "RunSimulationFromPlanIDVariablesUnionMember1",
    "RunSimulationFromPlanIDVariablesUnionMember2",
]


class RunSimulationFromConfig(TypedDict, total=False):
    plan: Required[RunSimulationFromConfigPlan]
    """The simulation to run: what to call, who calls it, and what to measure."""

    save_as_plan: Annotated[bool, PropertyInfo(alias="saveAsPlan")]
    """
    Keeps this configuration as a run plan, listed by GET /v1/simulation/plan and
    re-runnable with `planId`. Requires `plan.name`, since a plan you meant to keep
    should not be filed under a generated one.

    Omitted or false gives a one-off. The run still needs a plan to execute, so one
    is created either way, but it is hidden: it carries this run and nothing else.
    """

    variables: Union[
        Dict[str, str],
        Iterable[RunSimulationFromConfigVariablesUnionMember1],
        Iterable[RunSimulationFromConfigVariablesUnionMember2],
    ]
    """
    Values for the {{variables}} the run resolves, overriding whatever the plan has
    pinned.

    An object applies them to the whole run:

    { "orderNumber": "12345", "tier": "gold" }

    An array applies them per flow, or to just its happy path or one of its edge
    cases, when a single set will not do. Each entry carries what it applies to:

    [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
    "flowId": "550e8400-...", "happyPath": true, "variables": { "orderNumber":
    "55555" } }, { "flowId": "550e8400-...", "edgeCaseId": "7a3d2e1f-...",
    "variables": { "orderNumber": "67890" } } ]

    An entry that narrows to neither covers everything that flow resolves. A flow
    this plan does not attach, or an edge case that does not belong to the flow, is
    rejected rather than ignored.

    A plan built on scenarios rather than customer flows targets them the same way,
    with `scenarioId` in place of `flowId`. That form is deprecated alongside
    scenarios themselves, and still accepted so runs against those plans keep
    working.
    """


class RunSimulationFromConfigPlanAgentEndpoint(TypedDict, total=False):
    id: Required[str]


class RunSimulationFromConfigPlanMetric(TypedDict, total=False):
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


class RunSimulationFromConfigPlanFlowEdgeCasesUnionMember1(TypedDict, total=False):
    id: Required[str]
    """The edge case to run."""

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """Run this one as that persona instead of its own."""

    variables: Dict[str, str]
    """Values for this one only."""


class RunSimulationFromConfigPlanFlow(TypedDict, total=False):
    """
    One customer flow attached to a run plan, and which of its ways of running you cover.

    Attaching the same flow more than once with different overrides is how you fan it out across
    personas or values.
    """

    id: Required[str]
    """The customer flow to run."""

    edge_cases: Annotated[
        Union[Literal["ALL"], Iterable[RunSimulationFromConfigPlanFlowEdgeCasesUnionMember1]],
        PropertyInfo(alias="edgeCases"),
    ]
    """
    `"ALL"` runs every edge case the flow has when the run starts, so one added
    later is covered. An array runs only the ones you name, each able to carry its
    own persona override and values.
    """

    happy_path: Annotated[bool, PropertyInfo(alias="happyPath")]
    """Run the flow's happy path.

    Resolved when the run starts, so it follows the flow.
    """

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """Runs everything this attachment resolves as that persona instead of its own."""

    variables: Dict[str, str]
    """Values for everything it resolves."""


class RunSimulationFromConfigPlanPersona(TypedDict, total=False):
    id: Required[str]


class RunSimulationFromConfigPlanScenario(TypedDict, total=False):
    id: Required[str]
    """Scenario ID"""

    variables: Dict[str, str]
    """Template variables for this scenario instance.

    The same scenario can appear multiple times with different variables.
    """


class RunSimulationFromConfigPlan(TypedDict, total=False):
    """The simulation to run: what to call, who calls it, and what to measure."""

    agent_endpoints: Required[
        Annotated[Iterable[RunSimulationFromConfigPlanAgentEndpoint], PropertyInfo(alias="agentEndpoints")]
    ]
    """Agent endpoints to include in this run plan"""

    direction: Required[Literal["INBOUND", "OUTBOUND"]]
    """Direction of the simulation (INBOUND or OUTBOUND)"""

    max_simulation_duration_seconds: Required[Annotated[int, PropertyInfo(alias="maxSimulationDurationSeconds")]]
    """Maximum duration in seconds for each simulation"""

    metrics: Required[Iterable[RunSimulationFromConfigPlanMetric]]
    """Metric definitions to include in this run plan.

    Reference each by `id` (UUID) or `slug`.
    """

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

    flows: Iterable[RunSimulationFromConfigPlanFlow]
    """Customer flows to include in this run plan.

    The same flow can appear more than once with a different persona override or
    different variables.
    """

    iteration_count: Annotated[int, PropertyInfo(alias="iterationCount")]
    """Number of iterations to run for each test case (1-10000)"""

    max_concurrent_jobs: Annotated[int, PropertyInfo(alias="maxConcurrentJobs")]
    """Maximum number of concurrent simulation jobs"""

    name: str
    """What to call this.

    Generated from the date when omitted, and required with `saveAsPlan`.
    """

    personas: Iterable[RunSimulationFromConfigPlanPersona]
    """Personas to include in this run plan.

    Required with `scenarios`; ignored with `flows`, where each variant carries its
    own persona.
    """

    scenarios: Iterable[RunSimulationFromConfigPlanScenario]
    """Deprecated: use `flows` instead.

    Scenarios to include in this run plan. The same scenario ID can appear multiple
    times with different variables.
    """

    silence_timeout_seconds: Annotated[int, PropertyInfo(alias="silenceTimeoutSeconds")]
    """Timeout in seconds for silence detection"""


class RunSimulationFromConfigVariablesUnionMember1(TypedDict, total=False):
    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]
    """A customer flow this plan runs."""

    variables: Required[Dict[str, str]]
    """The values to apply."""

    edge_case_id: Annotated[str, PropertyInfo(alias="edgeCaseId")]
    """Narrow to one edge case of that flow."""

    happy_path: Annotated[Literal[True], PropertyInfo(alias="happyPath")]
    """Narrow to the flow's happy path."""


class RunSimulationFromConfigVariablesUnionMember2(TypedDict, total=False):
    scenario_id: Required[Annotated[str, PropertyInfo(alias="scenarioId")]]
    """ID of the scenario to apply variables to"""

    variables: Required[Dict[str, str]]
    """Key-value pairs for this scenario"""


class RunSimulationFromPlanID(TypedDict, total=False):
    plan_id: Required[Annotated[str, PropertyInfo(alias="planId")]]
    """The run plan to run, saved or hidden.

    Rename or unhide it with PUT /v1/simulation/plan/{planId}.
    """

    variables: Union[
        Dict[str, str],
        Iterable[RunSimulationFromPlanIDVariablesUnionMember1],
        Iterable[RunSimulationFromPlanIDVariablesUnionMember2],
    ]
    """
    Values for the {{variables}} the run resolves, overriding whatever the plan has
    pinned.

    An object applies them to the whole run:

    { "orderNumber": "12345", "tier": "gold" }

    An array applies them per flow, or to just its happy path or one of its edge
    cases, when a single set will not do. Each entry carries what it applies to:

    [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
    "flowId": "550e8400-...", "happyPath": true, "variables": { "orderNumber":
    "55555" } }, { "flowId": "550e8400-...", "edgeCaseId": "7a3d2e1f-...",
    "variables": { "orderNumber": "67890" } } ]

    An entry that narrows to neither covers everything that flow resolves. A flow
    this plan does not attach, or an edge case that does not belong to the flow, is
    rejected rather than ignored.

    A plan built on scenarios rather than customer flows targets them the same way,
    with `scenarioId` in place of `flowId`. That form is deprecated alongside
    scenarios themselves, and still accepted so runs against those plans keep
    working.
    """


class RunSimulationFromPlanIDVariablesUnionMember1(TypedDict, total=False):
    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]
    """A customer flow this plan runs."""

    variables: Required[Dict[str, str]]
    """The values to apply."""

    edge_case_id: Annotated[str, PropertyInfo(alias="edgeCaseId")]
    """Narrow to one edge case of that flow."""

    happy_path: Annotated[Literal[True], PropertyInfo(alias="happyPath")]
    """Narrow to the flow's happy path."""


class RunSimulationFromPlanIDVariablesUnionMember2(TypedDict, total=False):
    scenario_id: Required[Annotated[str, PropertyInfo(alias="scenarioId")]]
    """ID of the scenario to apply variables to"""

    variables: Required[Dict[str, str]]
    """Key-value pairs for this scenario"""


SimulationRunParams: TypeAlias = Union[RunSimulationFromConfig, RunSimulationFromPlanID]
