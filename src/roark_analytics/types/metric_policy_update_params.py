# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetricPolicyUpdateParams", "Condition", "ConditionCondition", "Metric"]


class MetricPolicyUpdateParams(TypedDict, total=False):
    conditions: Iterable[Condition]
    """Condition groups.

    Omit to keep existing, provide empty array to remove all conditions.
    """

    metrics: Iterable[Metric]
    """Metric definitions to collect when this policy matches"""

    name: str
    """Name of the metric policy"""

    status: Literal["ACTIVE", "INACTIVE"]
    """Status of the policy"""


class ConditionCondition(TypedDict, total=False):
    condition_key: Required[Annotated[str, PropertyInfo(alias="conditionKey")]]
    """Key to match against.

    For AGENT: the agent ID. For CALL_SOURCE: the source name. For CALL_PROPERTY:
    the property key.
    """

    condition_type: Required[
        Annotated[Literal["AGENT", "CALL_SOURCE", "CALL_PROPERTY", "INTEGRATION"], PropertyInfo(alias="conditionType")]
    ]
    """Type of condition: AGENT (match by agent ID), CALL_SOURCE (match by source e.g.

    VAPI, RETELL), CALL_PROPERTY (match by call property key/value)
    """

    condition_operator: Annotated[
        Optional[
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
        ],
        PropertyInfo(alias="conditionOperator"),
    ]
    """Comparison operator. Required for CALL_PROPERTY conditions."""

    condition_value: Annotated[Optional[str], PropertyInfo(alias="conditionValue")]
    """Value to compare against. Required for CALL_PROPERTY conditions."""


class Condition(TypedDict, total=False):
    conditions: Required[Iterable[ConditionCondition]]


class Metric(TypedDict, total=False):
    id: Required[str]
