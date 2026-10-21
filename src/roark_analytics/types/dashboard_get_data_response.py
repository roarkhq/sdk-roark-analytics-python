# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DashboardGetDataResponse", "Data", "DataWidget", "DataWidgetSery", "DataWidgetSeryBucket"]


class DataWidgetSeryBucket(BaseModel):
    date: str

    value: float

    comparison_date: Optional[str] = FieldInfo(alias="comparisonDate", default=None)

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)

    passed: Optional[float] = None

    percentage_of_baseline: Optional[float] = FieldInfo(alias="percentageOfBaseline", default=None)

    sample_size: Optional[float] = FieldInfo(alias="sampleSize", default=None)


class DataWidgetSery(BaseModel):
    aggregation: Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"]

    breakdown_value: Optional[str] = FieldInfo(alias="breakdownValue")

    buckets: List[DataWidgetSeryBucket]

    comparison_group: Optional[str] = FieldInfo(alias="comparisonGroup")

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue")

    measure_index: int = FieldInfo(alias="measureIndex")

    metric: Optional[str]

    percentage_of_baseline: Optional[float] = FieldInfo(alias="percentageOfBaseline")

    sample_size: Optional[float] = FieldInfo(alias="sampleSize")

    type: Literal["METRIC", "CONVERSATION", "UPTIME"]

    value: float


class DataWidget(BaseModel):
    blocked: bool

    error: Optional[str]

    interval: Literal["HOUR", "DAY", "WEEK", "MONTH"]

    name: str

    omitted_series: int = FieldInfo(alias="omittedSeries")

    series: List[DataWidgetSery]

    widget_id: str = FieldInfo(alias="widgetId")


class Data(BaseModel):
    """
    Every widget's series over the window, top to bottom. A widget that fails on its
    own (say its metric was deleted) carries `error` and no series; the others still
    return.
    """

    dashboard_id: str = FieldInfo(alias="dashboardId")

    from_: str = FieldInfo(alias="from")

    timezone: str

    to: str

    widgets: List[DataWidget]


class DashboardGetDataResponse(BaseModel):
    data: Data
    """
    Every widget's series over the window, top to bottom. A widget that fails on its
    own (say its metric was deleted) carries `error` and no series; the others still
    return.
    """
