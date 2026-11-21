# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]

    field_key: Annotated[str, PropertyInfo(alias="fieldKey")]
    """
    Filter by this field, a key from GET /v1/customer/fields. Use with fieldOperator
    and, unless checking presence, fieldValue.
    """

    field_operator: Annotated[
        Literal["EQUALS", "NOT_EQUALS", "CONTAINS", "STARTS_WITH", "IS_SET", "IS_NOT_SET"],
        PropertyInfo(alias="fieldOperator"),
    ]
    """
    How fieldValue is compared, ignoring case. NOT_EQUALS includes customers without
    the field.
    """

    field_value: Annotated[str, PropertyInfo(alias="fieldValue")]

    include_no_data: Annotated[Literal["true", "false"], PropertyInfo(alias="includeNoData")]
    """
    Include customers we hold nothing about beyond their identifier. Defaults to
    false.
    """

    limit: int

    modality: Literal["voice", "chat", "call"]

    page: int

    search: str

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """
    lastSeenAt (the default), firstSeenAt, conversationCount, voiceCount, chatCount,
    talkTimeMs or displayName, or field.<key> (for example field.COMPANY) to sort by
    a field's value. Field keys come from GET /v1/customer/fields. Customers without
    a value sort last.
    """

    sort_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortDirection")]
