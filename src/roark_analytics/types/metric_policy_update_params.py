# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MetricPolicyUpdateParams", "Condition", "ConditionCondition", "Metric", "MetricSetting"]


class ConditionCondition(TypedDict, total=False):
    condition_key: Required[Annotated[str, PropertyInfo(alias="conditionKey")]]
    """
    Key to match against. For AGENT: the agent ID. For CALL_SOURCE: the source name.
    For CALL_PROPERTY: the property key.
    """

    condition_type: Required[
        Annotated[Literal["AGENT", "CALL_SOURCE", "CALL_PROPERTY", "INTEGRATION"], PropertyInfo(alias="conditionType")]
    ]
    """
    Type of condition: AGENT (match by agent ID), CALL_SOURCE (match by source e.g.
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


class MetricSetting(TypedDict, total=False):
    """
    The metric's per-collector setting. A metric takes at most one field, and which
    one depends on the metric: verifiedProperties for Property Verification,
    excludedPhrases for voice consistency, voicemailScript for voicemail,
    screeningBrief for call screening, toolDefinitionIds for tool invocation,
    knowledgeBaseDocumentIds for knowledge grounding. A field the metric doesn't
    take is rejected with a 400.
    """

    excluded_phrases: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludedPhrases")]
    """
    Voice consistency metrics: phrases whose agent lines are not judged, such as a
    recorded prompt in a different voice.
    """

    knowledge_base_document_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="knowledgeBaseDocumentIds")]
    """
    Knowledge grounding metrics: the knowledge base documents to ground against, in
    priority order. Empty or omitted uses every knowledge base in the project.
    """

    screening_brief: Annotated[str, PropertyInfo(alias="screeningBrief")]
    """
    Call screening metrics: what the agent should say when a screener asks who is
    calling and why.
    """

    tool_definition_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="toolDefinitionIds")]
    """
    Tool invocation metrics: the tool definitions to score. Empty or omitted scores
    every tool the agent has.
    """

    verified_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="verifiedProperties")]
    """
    Property Verification metrics: the conversation properties to check against the
    transcript. Empty or omitted checks every custom property.
    """

    voicemail_script: Annotated[str, PropertyInfo(alias="voicemailScript")]
    """Voicemail metrics: the message the agent is expected to leave on voicemail."""


class Metric(TypedDict, total=False):
    id: Required[str]
    """The metric definition to collect"""

    settings: Optional[MetricSetting]
    """
    Optional. Omit, or send null, to collect the metric with its default (every
    property, every tool, no excluded phrases). Null is what a read returns for a
    metric on its default, so a fetched metrics list can be sent back as is.
    """


class MetricPolicyUpdateParams(TypedDict, total=False):
    conditions: Iterable[Condition]
    """
    Condition groups. Omit to keep existing, provide empty array to remove all
    conditions.
    """

    metrics: Iterable[Metric]
    """
    Metric definitions to collect when this policy matches. Replaces the policy's
    whole metric list: a metric sent without settings goes back to its default, so
    resend a metric's settings to keep them. Omit to keep the current metrics.
    """

    name: str
    """Name of the metric policy"""

    status: Literal["ACTIVE", "INACTIVE"]
    """Status of the policy"""
