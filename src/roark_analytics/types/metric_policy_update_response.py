# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MetricPolicyUpdateResponse",
    "Data",
    "DataCondition",
    "DataConditionCondition",
    "DataMetric",
    "DataMetricSetting",
]


class DataConditionCondition(BaseModel):
    condition_key: str = FieldInfo(alias="conditionKey")
    """
    Key to match against. For AGENT: the agent ID. For CALL_SOURCE: the source name.
    For CALL_PROPERTY: the property key.
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
    ] = FieldInfo(alias="conditionOperator")
    """Comparison operator. Required for CALL_PROPERTY conditions."""

    condition_type: Literal["AGENT", "CALL_SOURCE", "CALL_PROPERTY", "INTEGRATION"] = FieldInfo(alias="conditionType")
    """
    Type of condition: AGENT (match by agent ID), CALL_SOURCE (match by source e.g.
    VAPI, RETELL), CALL_PROPERTY (match by call property key/value)
    """

    condition_value: Optional[str] = FieldInfo(alias="conditionValue")
    """Value to compare against. Required for CALL_PROPERTY conditions."""


class DataCondition(BaseModel):
    conditions: List[DataConditionCondition]


class DataMetricSetting(BaseModel):
    """
    The metric's per-collector setting. A metric takes at most one field, and which
    one depends on the metric: verifiedProperties for Property Verification,
    excludedPhrases for voice consistency, voicemailScript for voicemail,
    screeningBrief for call screening, toolDefinitionIds for tool invocation,
    knowledgeBaseDocumentIds for knowledge grounding. A field the metric doesn't
    take is rejected with a 400.
    """

    excluded_phrases: Optional[List[str]] = FieldInfo(alias="excludedPhrases", default=None)
    """
    Voice consistency metrics: phrases whose agent lines are not judged, such as a
    recorded prompt in a different voice.
    """

    knowledge_base_document_ids: Optional[List[str]] = FieldInfo(alias="knowledgeBaseDocumentIds", default=None)
    """
    Knowledge grounding metrics: the knowledge base documents to ground against, in
    priority order. Empty or omitted uses every knowledge base in the project.
    """

    screening_brief: Optional[str] = FieldInfo(alias="screeningBrief", default=None)
    """
    Call screening metrics: what the agent should say when a screener asks who is
    calling and why.
    """

    tool_definition_ids: Optional[List[str]] = FieldInfo(alias="toolDefinitionIds", default=None)
    """
    Tool invocation metrics: the tool definitions to score. Empty or omitted scores
    every tool the agent has.
    """

    verified_properties: Optional[List[str]] = FieldInfo(alias="verifiedProperties", default=None)
    """
    Property Verification metrics: the conversation properties to check against the
    transcript. Empty or omitted checks every custom property.
    """

    voicemail_script: Optional[str] = FieldInfo(alias="voicemailScript", default=None)
    """Voicemail metrics: the message the agent is expected to leave on voicemail."""


class DataMetric(BaseModel):
    id: str

    settings: Optional[DataMetricSetting]
    """The metric's per-collector setting, or null when it runs with its default"""


class Data(BaseModel):
    """A metric policy defining when metrics should be collected"""

    id: str
    """Unique identifier of the metric policy"""

    conditions: Optional[List[DataCondition]]
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


class MetricPolicyUpdateResponse(BaseModel):
    data: Data
    """A metric policy defining when metrics should be collected"""
