# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetricPolicyListResponse", "Data", "DataCondition", "DataConditionCondition", "DataMetric", "Pagination"]


class DataConditionCondition(BaseModel):
    condition_key: str = FieldInfo(alias="conditionKey")
    """Key to match against.

    For AGENT: the agent ID. For CALL_SOURCE: the source name. For CALL_PROPERTY:
    the property key.
    """

    condition_operator: Optional[
        Literal[
            "EQUALS",
            "NOT_EQUALS",
            "CONTAINS",
            "STARTS_WITH",
            "GREATER_THAN",
            "LESS_THAN",
            "GREATER_THAN_OR_EQUALS",
            "LESS_THAN_OR_EQUALS",
        ]
    ] = FieldInfo(alias="conditionOperator", default=None)
    """Comparison operator. Required for CALL_PROPERTY conditions."""

    condition_type: Literal["AGENT", "CALL_SOURCE", "CALL_PROPERTY", "INTEGRATION"] = FieldInfo(alias="conditionType")
    """Type of condition: AGENT (match by agent ID), CALL_SOURCE (match by source e.g.

    VAPI, RETELL), CALL_PROPERTY (match by call property key/value)
    """

    condition_value: Optional[str] = FieldInfo(alias="conditionValue", default=None)
    """Value to compare against. Required for CALL_PROPERTY conditions."""


class DataCondition(BaseModel):
    conditions: List[DataConditionCondition]


class DataMetric(BaseModel):
    id: str


class Data(BaseModel):
    """A metric policy defining when metrics should be collected"""

    id: str
    """Unique identifier of the metric policy"""

    conditions: Optional[List[DataCondition]] = None
    """Condition groups for this policy. Null means the policy matches all calls."""

    created_at: str = FieldInfo(alias="createdAt")
    """When the policy was created"""

    metrics: List[DataMetric]
    """Metric definitions associated with this policy"""

    name: str
    """Name of the metric policy"""

    status: Literal["ACTIVE", "INACTIVE"]
    """Status of the metric policy (ACTIVE or INACTIVE)"""

    type: Literal["SYSTEM", "USER"]
    """Type of the metric policy (SYSTEM or USER)"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the policy was last updated"""


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """Whether there are more items to fetch"""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page of items"""

    total: float
    """Total number of items"""


class MetricPolicyListResponse(BaseModel):
    """Paginated list of metric policies"""

    data: List[Data]

    pagination: Pagination
