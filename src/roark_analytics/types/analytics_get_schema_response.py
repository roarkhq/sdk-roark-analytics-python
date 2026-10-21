# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AnalyticsGetSchemaResponse",
    "Data",
    "DataBreakdown",
    "DataCallProperty",
    "DataFilter",
    "DataFilterProperty",
    "DataMeasureType",
    "DataMetric",
]


class DataBreakdown(BaseModel):
    description: str

    type: Literal["METRIC_PROPERTY", "CALL_PROPERTY", "AGENT_PROPERTY", "DATASET"]


class DataCallProperty(BaseModel):
    is_system: bool = FieldInfo(alias="isSystem")

    name: str

    value_type: str = FieldInfo(alias="valueType")


class DataFilterProperty(BaseModel):
    description: str

    property: str


class DataFilter(BaseModel):
    description: str

    properties: List[DataFilterProperty]

    type: Literal[
        "METRIC_PROPERTY", "CALL_PROPERTY", "AGENT_PROPERTY", "CALL_ID", "MODALITY", "DATASET", "METRIC_VALUE"
    ]


class DataMeasureType(BaseModel):
    aggregations: List[Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"]]

    description: str

    type: Literal["METRIC", "CONVERSATION", "UPTIME"]


class DataMetric(BaseModel):
    id: str

    aggregations: List[Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"]]

    default_aggregation: Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"] = FieldInfo(
        alias="defaultAggregation"
    )

    is_threshold: bool = FieldInfo(alias="isThreshold")

    name: str

    output_type: str = FieldInfo(alias="outputType")

    slug: str


class Data(BaseModel):
    """
    What can be queried in this project: metrics (by slug), measure types, filters,
    breakdowns.
    """

    breakdowns: List[DataBreakdown]

    call_properties: List[DataCallProperty] = FieldInfo(alias="callProperties")

    display_types: List[Literal["LINE", "NUMBER", "RADAR", "STACKED_BAR", "TABLE"]] = FieldInfo(alias="displayTypes")

    filters: List[DataFilter]

    intervals: List[Literal["HOUR", "DAY", "WEEK", "MONTH"]]

    measure_types: List[DataMeasureType] = FieldInfo(alias="measureTypes")

    metrics: List[DataMetric]

    operators: List[
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
    ]


class AnalyticsGetSchemaResponse(BaseModel):
    data: Data
    """
    What can be queried in this project: metrics (by slug), measure types, filters,
    breakdowns.
    """
