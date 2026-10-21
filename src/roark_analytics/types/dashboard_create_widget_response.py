# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DashboardCreateWidgetResponse",
    "Data",
    "DataComparisonGroup",
    "DataMeasure",
    "DataMeasureBreakdown",
    "DataMeasureFilter",
]


class DataMeasureBreakdown(BaseModel):
    """
    Split the measure into one series per value of this dimension (the largest 50
    are returned). Ignored while comparisonGroups are set: each group is then one
    series.
    """

    type: Literal["METRIC_PROPERTY", "CALL_PROPERTY", "AGENT_PROPERTY", "DATASET"]

    property: Optional[str] = None
    """The property to split by. Required for CALL_PROPERTY and METRIC_PROPERTY."""


class DataMeasureFilter(BaseModel):
    type: Literal[
        "METRIC_PROPERTY", "CALL_PROPERTY", "AGENT_PROPERTY", "CALL_ID", "MODALITY", "DATASET", "METRIC_VALUE"
    ]
    """What the filter narrows on. GET /v1/analytics/schema lists each type."""

    value: Union[str, float, bool]
    """The value to compare against (an agent id, "call" / "chat", a property value)."""

    operator: Optional[
        Literal[
            "EQUALS",
            "NOT_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "CONTAINS",
            "STARTS_WITH",
        ]
    ] = None
    """Defaults to EQUALS."""

    property: Optional[str] = None
    """
    The property to compare. Required for CALL_PROPERTY and METRIC_PROPERTY; may be
    omitted for AGENT_PROPERTY, DATASET, MODALITY and CALL_ID.
    """


class DataMeasure(BaseModel):
    aggregation: Optional[Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"]] = None
    """
    Defaults by output type: AVG for numeric metrics, COUNT (split by value) for
    classification and text, PASS_RATE for thresholds and uptime, COUNT for
    conversations.
    """

    breakdown: Optional[DataMeasureBreakdown] = None
    """
    Split the measure into one series per value of this dimension (the largest 50
    are returned). Ignored while comparisonGroups are set: each group is then one
    series.
    """

    color: Optional[
        Literal["GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"]
    ] = None
    """Chart color on a dashboard."""

    distinct_by: Optional[Literal["NONE", "CALL"]] = FieldInfo(alias="distinctBy", default=None)
    """
    CALL (default for metrics) folds each conversation to one value first, so a long
    call does not outweigh a short one. NONE aggregates every value.
    """

    filters: Optional[List[DataMeasureFilter]] = None
    """Filters for this measure only, on top of the query's filters."""

    is_baseline: Optional[bool] = FieldInfo(alias="isBaseline", default=None)
    """
    Mark one measure as the baseline: every series also reports its value as a
    percentage of it.
    """

    metric: Optional[str] = None
    """The metric's slug (e.g. `task_completion`) or id. Required for METRIC."""

    nested_aggregation: Optional[Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"]] = (
        FieldInfo(alias="nestedAggregation", default=None)
    )
    """
    How each conversation is folded when distinctBy is CALL. Defaults to SUM under
    SUM, else AVG.
    """

    nested_aggregation_percentile: Optional[int] = FieldInfo(alias="nestedAggregationPercentile", default=None)

    pass_operator: Optional[
        Literal[
            "EQUALS",
            "NOT_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "CONTAINS",
            "STARTS_WITH",
        ]
    ] = FieldInfo(alias="passOperator", default=None)
    """
    PASS_RATE condition operator. Omit for a threshold metric: its own condition is
    used.
    """

    pass_value: Optional[Union[str, float, bool]] = FieldInfo(alias="passValue", default=None)
    """PASS_RATE condition value, e.g. 4 or "resolved"."""

    percentile: Optional[int] = None
    """Required with PERCENTILE, e.g. 95."""

    type: Optional[Literal["METRIC", "CONVERSATION", "UPTIME"]] = None
    """
    METRIC (default): a metric's values. CONVERSATION: conversation counts. UPTIME:
    health-check outcomes.
    """


class DataComparisonGroup(BaseModel):
    filters: List[DataMeasureFilter]

    name: str
    """The series label; unique within the query."""

    color: Optional[
        Literal["GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"]
    ] = None


class Data(BaseModel):
    id: str

    measures: List[DataMeasure]
    """What to aggregate: 1 to 10 measures."""

    name: str
    """Unique on the dashboard: how the widget is matched on update."""

    comparison_groups: Optional[List[DataComparisonGroup]] = FieldInfo(alias="comparisonGroups", default=None)
    """Run every measure once per named filter set, e.g. one group per agent."""

    comparison_mode: Optional[Literal["NONE", "PREVIOUS_PERIOD"]] = FieldInfo(alias="comparisonMode", default=None)
    """PREVIOUS_PERIOD adds the preceding window of the same length to every series."""

    description: Optional[str] = None

    display: Optional[Literal["LINE", "NUMBER", "RADAR", "STACKED_BAR", "TABLE"]] = None
    """Chart type. Defaults to LINE."""

    filters: Optional[List[DataMeasureFilter]] = None
    """Applied to every measure, on top of each measure's own filters."""

    interval: Optional[Literal["HOUR", "DAY", "WEEK", "MONTH"]] = None
    """
    Bucket size. Defaults from the window's length and steps coarser when the window
    would exceed 500 buckets.
    """

    size: Optional[Literal["SMALL", "MEDIUM", "LARGE", "EXTRA_LARGE"]] = None
    """Grid width. Defaults to MEDIUM."""


class DashboardCreateWidgetResponse(BaseModel):
    data: Data
