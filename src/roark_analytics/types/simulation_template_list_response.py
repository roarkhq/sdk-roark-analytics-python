# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationTemplateListResponse", "Data", "DataFlow", "DataFlowEdgeCase", "DataFlowHappyPath", "DataMetric"]


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


class Data(BaseModel):
    """
    A built-in simulation template, resolved against this project: what it measures
    and what it runs.
    """

    category: str
    """Grouping used in the dashboard library"""

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

    thresholds: List[DataMetric]
    """The Pass/Fail checks this template attaches alongside its metrics."""

    title: str
    """Display name"""


class SimulationTemplateListResponse(BaseModel):
    """The built-in simulation templates."""

    data: List[Data]
