# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "LiveReportUpdateResponse",
    "Data",
    "DataFilter",
    "DataNotification",
    "DataNotificationEmail",
    "DataNotificationSlack",
    "DataTarget",
]


class DataFilter(BaseModel):
    type: Literal[
        "METRIC_PROPERTY", "CALL_PROPERTY", "AGENT_PROPERTY", "CALL_ID", "MODALITY", "DATASET", "METRIC_VALUE"
    ]
    """What the filter narrows on. GET /v1/analytics/schema lists each type."""

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
            "IS_SET",
            "IS_NOT_SET",
        ]
    ] = None
    """
    Defaults to EQUALS. IS_SET / IS_NOT_SET (CALL_PROPERTY only) keep conversations
    where the property is set, whatever the value, or missing (never sent, sent as
    null, or removed); they take no value.
    """

    property: Optional[str] = None
    """
    The property to compare. Required for CALL_PROPERTY and METRIC_PROPERTY; may be
    omitted for AGENT_PROPERTY, DATASET, MODALITY and CALL_ID.
    """

    value: Optional[Union[str, float, bool]] = None
    """
    The value to compare against (an agent id, "call" / "chat", a property value).
    Required except with IS_SET / IS_NOT_SET.
    """


class DataNotificationEmail(BaseModel):
    enabled: bool

    recipients: List[str]


class DataNotificationSlack(BaseModel):
    channel_id: str = FieldInfo(alias="channelId")

    channel_name: str = FieldInfo(alias="channelName")

    notification_config_id: str = FieldInfo(alias="notificationConfigId")


class DataNotification(BaseModel):
    email: DataNotificationEmail

    slack: List[DataNotificationSlack]

    from_config: Optional[bool] = FieldInfo(alias="fromConfig", default=None)


class DataTarget(BaseModel):
    metric: str
    """The metric's slug (e.g. `task_completion`) or id."""

    value: float
    """The bar, in display units. A PASS_RATE bar is a percentage, 0-100."""

    aggregation: Optional[Literal["PASS_RATE", "AVG", "MEDIAN", "PERCENTILE", "MIN", "MAX"]] = None
    """Defaults to PASS_RATE for thresholds and booleans, AVG for anything numeric."""

    comparator: Optional[Literal["AT_LEAST", "AT_MOST"]] = None
    """
    AT_LEAST (default for PASS_RATE) or AT_MOST (default for every other
    aggregation).
    """

    label: Optional[str] = None
    """Shown instead of the metric's name."""

    pass_operator: Optional[
        Literal[
            "EQUALS", "NOT_EQUALS", "GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO", "LESS_THAN", "LESS_THAN_OR_EQUAL_TO"
        ]
    ] = FieldInfo(alias="passOperator", default=None)
    """
    PASS_RATE on a metric that isn't a threshold: the per-call condition a call
    passes on.
    """

    pass_value: Optional[Union[str, float, bool]] = FieldInfo(alias="passValue", default=None)

    percentile: Optional[int] = None
    """Required with PERCENTILE, e.g. 95."""


class Data(BaseModel):
    id: str

    agent_id: Optional[str] = FieldInfo(alias="agentId")

    cadence: Literal["DAILY", "WEEKLY", "MONTHLY"]

    config_key: Optional[str] = FieldInfo(alias="configKey")

    config_managed: bool = FieldInfo(alias="configManaged")
    """Managed by config as code: read-only here (edits return 409)."""

    created_at: str = FieldInfo(alias="createdAt")

    dashboard_id: Optional[str] = FieldInfo(alias="dashboardId")

    delivery_hour: int = FieldInfo(alias="deliveryHour")

    description: Optional[str]

    filters: List[DataFilter]

    include_transcript_excerpts: bool = FieldInfo(alias="includeTranscriptExcerpts")

    name: str

    next_delivery_at: Optional[str] = FieldInfo(alias="nextDeliveryAt")
    """When the next scheduled report is written. Null while the report is paused."""

    notifications: DataNotification

    project_id: str = FieldInfo(alias="projectId")

    status: Literal["ACTIVE", "PAUSED"]

    targets: List[DataTarget]

    timezone: str

    updated_at: str = FieldInfo(alias="updatedAt")


class LiveReportUpdateResponse(BaseModel):
    data: Data
