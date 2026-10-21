# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DashboardGetWidgetDataResponse", "Data", "DataSery", "DataSeryBucket"]


class DataSeryBucket(BaseModel):
    date: str

    value: float

    comparison_date: Optional[str] = FieldInfo(alias="comparisonDate", default=None)

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)

    passed: Optional[float] = None

    percentage_of_baseline: Optional[float] = FieldInfo(alias="percentageOfBaseline", default=None)

    sample_size: Optional[float] = FieldInfo(alias="sampleSize", default=None)


class DataSery(BaseModel):
    aggregation: Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"]

    breakdown_value: Optional[str] = FieldInfo(alias="breakdownValue")

    buckets: List[DataSeryBucket]

    comparison_group: Optional[str] = FieldInfo(alias="comparisonGroup")

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue")

    measure_index: int = FieldInfo(alias="measureIndex")

    metric: Optional[str]

    percentage_of_baseline: Optional[float] = FieldInfo(alias="percentageOfBaseline")

    sample_size: Optional[float] = FieldInfo(alias="sampleSize")

    type: Literal["METRIC", "CONVERSATION", "UPTIME"]

    value: float


class Data(BaseModel):
    blocked: bool

    error: Optional[str]

    from_: str = FieldInfo(alias="from")

    interval: Literal["HOUR", "DAY", "WEEK", "MONTH"]

    name: str

    omitted_series: int = FieldInfo(alias="omittedSeries")

    series: List[DataSery]

    timezone: str

    to: str

    widget_id: str = FieldInfo(alias="widgetId")


class DashboardGetWidgetDataResponse(BaseModel):
    data: Data
