# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DashboardListResponse",
    "Data",
    "DataTimeRangeUnionMember0",
    "DataTimeRangeUnionMember1",
    "DataTimeRangeUnionMember2",
    "DataTimeRangeUnionMember3",
]


class DataTimeRangeUnionMember0(BaseModel):
    type: Literal["LAST"]

    unit: Literal["DAYS", "WEEKS", "MONTHS"]

    value: int


class DataTimeRangeUnionMember1(BaseModel):
    period: Literal[
        "TODAY", "YESTERDAY", "THIS_WEEK", "LAST_WEEK", "THIS_MONTH", "LAST_MONTH", "THIS_YEAR", "LAST_YEAR"
    ]

    type: Literal["CALENDAR_ALIGNED"]


class DataTimeRangeUnionMember2(BaseModel):
    from_: str = FieldInfo(alias="from")

    to: str

    type: Literal["FIXED"]


class DataTimeRangeUnionMember3(BaseModel):
    from_: str = FieldInfo(alias="from")

    type: Literal["SINCE"]


class Data(BaseModel):
    id: str

    config_managed: bool = FieldInfo(alias="configManaged")
    """
    Managed by config as code (`kind: dashboard`). A managed dashboard is read-only
    here: edits return 409; change it in the config file.
    """

    created_at: str = FieldInfo(alias="createdAt")

    description: Optional[str]

    is_default: bool = FieldInfo(alias="isDefault")

    name: str

    time_range: Union[
        DataTimeRangeUnionMember0, DataTimeRangeUnionMember1, DataTimeRangeUnionMember2, DataTimeRangeUnionMember3, None
    ] = FieldInfo(alias="timeRange")
    """
    The window: LAST n DAYS/WEEKS/MONTHS up to now, a CALENDAR_ALIGNED period
    (TODAY, YESTERDAY, THIS_WEEK, LAST_WEEK, THIS_MONTH, LAST_MONTH, THIS_YEAR,
    LAST_YEAR), FIXED from/to, or SINCE a date. At most 731 days (two years).
    """

    updated_at: str = FieldInfo(alias="updatedAt")


class DashboardListResponse(BaseModel):
    data: List[Data]
