# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationTemplateListResponse",
    "Data",
    "DataFlow",
    "DataFlowEdgeCase",
    "DataFlowHappyPath",
    "DataMetric",
    "DataSweep",
]


class DataFlowEdgeCase(BaseModel):
    id: str
    """Customer flow variant ID"""

    slug: Optional[str]
    """
    The stable slug of a Roark-curated edge case, null for one of your own.
    Prefer this over `id` in a run you keep in version control. A curated edge case
    is a global row, so its id differs between deployments, and renaming one
    replaces the row and its id outright. The slug survives both.
    """

    title: str
    """What this way of running the flow is called"""


class DataFlowHappyPath(BaseModel):
    """
    The flow's default way of running, when this template covers it. Null when it
    does not, or the flow has none.
    """

    title: str


class DataFlow(BaseModel):
    id: str
    """Customer flow ID"""

    edge_cases: List[DataFlowEdgeCase] = FieldInfo(alias="edgeCases")
    """The other ways of running this flow that this template covers."""

    happy_path: Optional[DataFlowHappyPath] = FieldInfo(alias="happyPath")
    """
    The flow's default way of running, when this template covers it. Null when it
    does not, or the flow has none.
    """

    slug: Optional[str]
    """
    The stable slug of a Roark-curated flow, null for one of your own.
    Prefer this over `id` when you are storing a run in version control: a curated
    flow is a global row, so its id is the same for every project but differs
    between deployments, while the slug is stable wherever the flow exists. Both are
    accepted by a run request.
    """

    title: str
    """Flow title"""


class DataMetric(BaseModel):
    id: str
    """Metric definition ID"""

    slug: str
    """
    Stable metric slug, e.g. "response_time"
    """


class DataSweep(BaseModel):
    baseline: Optional[str]
    """
    The reference value, shown first in the results, resolved to what a plan built
    from this template will actually record. `null` when the property has no obvious
    norm. It does not change the verdict: each value is compared with every other
    value combined.
    """

    property: Literal[
        "ACCENT",
        "AGE",
        "BACKGROUND_NOISE",
        "BACKGROUND_NOISE_VOLUME",
        "BASE_EMOTION",
        "CONFIRMATION_STYLE",
        "GENDER",
        "INTENT_CLARITY",
        "LANGUAGE",
        "INTERRUPTION",
        "MEMORY_RELIABILITY",
        "RESPONSE_TIMING",
        "SPEECH_CLARITY",
        "SPEECH_PACE",
    ]
    """The property this template varies across the flow it runs."""

    values: List[str]
    """Every value the template sweeps, in the order the plan attaches them."""


class Data(BaseModel):
    """
    A built-in simulation template, resolved against this project: what it measures
    and what it runs.
    """

    category: str
    """Grouping used in the dashboard library"""

    default_end_call_reasons: List[str] = FieldInfo(alias="defaultEndCallReasons")
    """
    The end-call conditions a run from this template uses unless the request sets
    its own.
    Empty for templates whose calls end when the agent says goodbye. Non-empty where
    the template runs scripted flows that finish on a verdict: the simulated caller
    hangs up on an end-call phrase or one of these, so a run that discards them
    would stay on the line until the duration cap.
    """

    default_max_simulation_duration_seconds: int = FieldInfo(alias="defaultMaxSimulationDurationSeconds")
    """
    The per-simulation cap a run from this template uses unless the request sets its
    own.
    """

    description: str
    """What this template tests"""

    flows: List[DataFlow]
    """
    The flows this template runs, and which of their ways of running it covers.
    Empty means the template presets only what to measure, and a run has to say what
    to measure it on: pass `flows` to POST /v1/simulation/run. When it is not empty
    you can still pass `flows` to narrow it, naming a subset of the ids listed here.
    """

    include_flow_metrics: bool = FieldInfo(alias="includeFlowMetrics")
    """
    Whether runs from this template also collect each attached flow's own metrics,
    on top of the template's set.
    """

    metrics: List[DataMetric]
    """The metrics this template collects, resolved to this project's definitions."""

    slug: str
    """Stable identifier. Name this in a run request."""

    sweep: Optional[DataSweep]
    """
    Set when this template is a property sweep: it runs ONE flow once per value of a
    single caller or environment property, and the report compares the values
    against `baseline`.
    This is what decides the size of the run. A sweep attaches the flow once per
    entry in `values`, so a plan built from it costs `values.length` times the calls
    a normal template would, before iterations. Read it before creating a plan you
    have to pay for.
    `null` for every other template.
    """

    thresholds: List[DataMetric]
    """The Pass/Fail checks this template attaches alongside its metrics."""

    title: str
    """Display name"""


class SimulationTemplateListResponse(BaseModel):
    """The built-in simulation templates."""

    data: List[Data]
