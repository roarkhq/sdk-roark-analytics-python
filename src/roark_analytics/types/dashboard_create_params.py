# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "DashboardCreateParams",
    "Filter",
    "TimeRangeUnionMember0",
    "TimeRangeUnionMember1",
    "TimeRangeUnionMember2",
    "TimeRangeUnionMember3",
    "Widget",
    "WidgetComparisonGroup",
    "WidgetMeasure",
    "WidgetMeasureBreakdown",
]


class Filter(TypedDict, total=False):
    type: Required[
        Literal["METRIC_PROPERTY", "CALL_PROPERTY", "AGENT_PROPERTY", "CALL_ID", "MODALITY", "DATASET", "METRIC_VALUE"]
    ]
    """What the filter narrows on. GET /v1/analytics/schema lists each type."""

    value: Required[Union[str, float, bool]]
    """The value to compare against (an agent id, "call" / "chat", a property value)."""

    operator: Literal[
        "EQUALS",
        "NOT_EQUALS",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL_TO",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL_TO",
        "CONTAINS",
        "STARTS_WITH",
    ]
    """Defaults to EQUALS."""

    property: str
    """
    The property to compare. Required for CALL_PROPERTY and METRIC_PROPERTY; may be
    omitted for AGENT_PROPERTY, DATASET, MODALITY and CALL_ID.
    """


class TimeRangeUnionMember0(TypedDict, total=False):
    type: Required[Literal["LAST"]]

    unit: Required[Literal["DAYS", "WEEKS", "MONTHS"]]

    value: Required[int]


class TimeRangeUnionMember1(TypedDict, total=False):
    period: Required[
        Literal["TODAY", "YESTERDAY", "THIS_WEEK", "LAST_WEEK", "THIS_MONTH", "LAST_MONTH", "THIS_YEAR", "LAST_YEAR"]
    ]

    type: Required[Literal["CALENDAR_ALIGNED"]]


class TimeRangeUnionMember2(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]

    to: Required[str]

    type: Required[Literal["FIXED"]]


class TimeRangeUnionMember3(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]

    type: Required[Literal["SINCE"]]


class WidgetMeasureBreakdown(TypedDict, total=False):
    """
    Split the measure into one series per value of this dimension (the largest 50
    are returned). Ignored while comparisonGroups are set: each group is then one
    series.
    """

    type: Required[Literal["METRIC_PROPERTY", "CALL_PROPERTY", "AGENT_PROPERTY", "DATASET"]]

    property: str
    """The property to split by. Required for CALL_PROPERTY and METRIC_PROPERTY."""


class WidgetMeasure(TypedDict, total=False):
    aggregation: Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"]
    """
    Defaults by output type: AVG for numeric metrics, COUNT (split by value) for
    classification and text, PASS_RATE for thresholds and uptime, COUNT for
    conversations.
    """

    breakdown: WidgetMeasureBreakdown
    """
    Split the measure into one series per value of this dimension (the largest 50
    are returned). Ignored while comparisonGroups are set: each group is then one
    series.
    """

    color: Literal[
        "GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"
    ]
    """Chart color on a dashboard."""

    distinct_by: Annotated[Literal["NONE", "CALL"], PropertyInfo(alias="distinctBy")]
    """
    CALL (default for metrics) folds each conversation to one value first, so a long
    call does not outweigh a short one. NONE aggregates every value.
    """

    filters: Iterable[Filter]
    """Filters for this measure only, on top of the query's filters."""

    is_baseline: Annotated[bool, PropertyInfo(alias="isBaseline")]
    """
    Mark one measure as the baseline: every series also reports its value as a
    percentage of it.
    """

    metric: str
    """The metric's slug (e.g. `task_completion`) or id. Required for METRIC."""

    nested_aggregation: Annotated[
        Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"],
        PropertyInfo(alias="nestedAggregation"),
    ]
    """
    How each conversation is folded when distinctBy is CALL. Defaults to SUM under
    SUM, else AVG.
    """

    nested_aggregation_percentile: Annotated[int, PropertyInfo(alias="nestedAggregationPercentile")]

    pass_operator: Annotated[
        Literal[
            "EQUALS",
            "NOT_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "CONTAINS",
            "STARTS_WITH",
        ],
        PropertyInfo(alias="passOperator"),
    ]
    """
    PASS_RATE condition operator. Omit for a threshold metric: its own condition is
    used.
    """

    pass_value: Annotated[Union[str, float, bool], PropertyInfo(alias="passValue")]
    """PASS_RATE condition value, e.g. 4 or "resolved"."""

    percentile: int
    """Required with PERCENTILE, e.g. 95."""

    type: Literal["METRIC", "CONVERSATION", "UPTIME"]
    """
    METRIC (default): a metric's values. CONVERSATION: conversation counts. UPTIME:
    health-check outcomes.
    """


class WidgetComparisonGroup(TypedDict, total=False):
    filters: Required[Iterable[Filter]]

    name: Required[str]
    """The series label; unique within the query."""

    color: Literal[
        "GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"
    ]


class Widget(TypedDict, total=False):
    measures: Required[Iterable[WidgetMeasure]]
    """What to aggregate: 1 to 10 measures."""

    name: Required[str]
    """Unique on the dashboard: how the widget is matched on update."""

    comparison_groups: Annotated[Iterable[WidgetComparisonGroup], PropertyInfo(alias="comparisonGroups")]
    """Run every measure once per named filter set, e.g. one group per agent."""

    comparison_mode: Annotated[Literal["NONE", "PREVIOUS_PERIOD"], PropertyInfo(alias="comparisonMode")]
    """PREVIOUS_PERIOD adds the preceding window of the same length to every series."""

    description: str

    display: Literal["LINE", "NUMBER", "RADAR", "STACKED_BAR", "TABLE"]
    """Chart type. Defaults to LINE."""

    filters: Iterable[Filter]
    """Applied to every measure, on top of each measure's own filters."""

    interval: Literal["HOUR", "DAY", "WEEK", "MONTH"]
    """
    Bucket size. Defaults from the window's length and steps coarser when the window
    would exceed 500 buckets.
    """

    size: Literal["SMALL", "MEDIUM", "LARGE", "EXTRA_LARGE"]
    """Grid width. Defaults to MEDIUM."""


class DashboardCreateParams(TypedDict, total=False):
    name: Required[str]

    description: str

    filters: Iterable[Filter]

    is_default: Annotated[bool, PropertyInfo(alias="isDefault")]

    time_range: Annotated[
        Union[TimeRangeUnionMember0, TimeRangeUnionMember1, TimeRangeUnionMember2, TimeRangeUnionMember3],
        PropertyInfo(alias="timeRange"),
    ]
    """
    The window: LAST n DAYS/WEEKS/MONTHS up to now, a CALENDAR_ALIGNED period
    (TODAY, YESTERDAY, THIS_WEEK, LAST_WEEK, THIS_MONTH, LAST_MONTH, THIS_YEAR,
    LAST_YEAR), FIXED from/to, or SINCE a date. At most 731 days (two years).
    """

    widgets: Iterable[Widget]
