# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["LiveReportCreateParams", "Filter", "Notification", "NotificationEmail", "NotificationSlack", "Target"]


class Filter(TypedDict, total=False):
    type: Required[
        Literal["METRIC_PROPERTY", "CALL_PROPERTY", "AGENT_PROPERTY", "CALL_ID", "MODALITY", "DATASET", "METRIC_VALUE"]
    ]
    """What the filter narrows on. GET /v1/analytics/schema lists each type."""

    operator: Literal[
        "EQUALS",
        "NOT_EQUALS",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL_TO",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL_TO",
        "CONTAINS",
        "STARTS_WITH",
        "IS_SET",
        "IS_NOT_SET",
    ]
    """
    Defaults to EQUALS. IS_SET / IS_NOT_SET (CALL_PROPERTY only) keep conversations
    where the property is set, whatever the value, or missing (never sent, sent as
    null, or removed); they take no value.
    """

    property: str
    """
    The property to compare. Required for CALL_PROPERTY and METRIC_PROPERTY; may be
    omitted for AGENT_PROPERTY, DATASET, MODALITY and CALL_ID.
    """

    value: Union[str, float, bool]
    """
    The value to compare against (an agent id, "call" / "chat", a property value).
    Required except with IS_SET / IS_NOT_SET.
    """


class NotificationEmail(TypedDict, total=False):
    enabled: Required[bool]

    recipients: Required[SequenceNotStr[str]]


class NotificationSlack(TypedDict, total=False):
    channel_id: Required[Annotated[str, PropertyInfo(alias="channelId")]]

    channel_name: Required[Annotated[str, PropertyInfo(alias="channelName")]]


class Notification(TypedDict, total=False):
    email: Required[NotificationEmail]

    slack: Required[Iterable[NotificationSlack]]


class Target(TypedDict, total=False):
    metric: Required[str]
    """The metric's slug (e.g. `task_completion`) or id."""

    value: Required[float]
    """The bar, in display units. A PASS_RATE bar is a percentage, 0-100."""

    aggregation: Literal["PASS_RATE", "AVG", "MEDIAN", "PERCENTILE", "MIN", "MAX"]
    """Defaults to PASS_RATE for thresholds and booleans, AVG for anything numeric."""

    comparator: Literal["AT_LEAST", "AT_MOST"]
    """
    AT_LEAST (default for PASS_RATE) or AT_MOST (default for every other
    aggregation).
    """

    label: str
    """Shown instead of the metric's name."""

    pass_operator: Annotated[
        Literal[
            "EQUALS", "NOT_EQUALS", "GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO", "LESS_THAN", "LESS_THAN_OR_EQUAL_TO"
        ],
        PropertyInfo(alias="passOperator"),
    ]
    """
    PASS_RATE on a metric that isn't a threshold: the per-call condition a call
    passes on.
    """

    pass_value: Annotated[Union[str, float, bool], PropertyInfo(alias="passValue")]

    percentile: int
    """Required with PERCENTILE, e.g. 95."""


class LiveReportCreateParams(TypedDict, total=False):
    name: Required[str]

    agent_id: Annotated[Optional[str], PropertyInfo(alias="agentId")]

    cadence: Literal["DAILY", "WEEKLY", "MONTHLY"]

    dashboard_id: Annotated[Optional[str], PropertyInfo(alias="dashboardId")]

    delivery_hour: Annotated[int, PropertyInfo(alias="deliveryHour")]

    description: Optional[str]

    filters: Iterable[Filter]

    generate_now: Annotated[bool, PropertyInfo(alias="generateNow")]
    """Write the report for the latest closed period right away. Default true."""

    include_transcript_excerpts: Annotated[bool, PropertyInfo(alias="includeTranscriptExcerpts")]

    notifications: Notification

    status: Literal["ACTIVE", "PAUSED"]

    targets: Iterable[Target]

    timezone: str
