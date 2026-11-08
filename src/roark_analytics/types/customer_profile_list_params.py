# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerProfileListParams"]


class CustomerProfileListParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]

    field_key: Annotated[
        Literal[
            "FULL_NAME",
            "PREFERRED_NAME",
            "ACCOUNT_ID",
            "COMPANY",
            "JOB_TITLE",
            "EMAIL",
            "ALTERNATE_PHONE",
            "AGE",
            "GENDER",
            "LANGUAGE",
            "LOCATION",
            "TIMEZONE",
            "BEST_TIME_TO_REACH",
            "PREFERRED_CHANNEL",
        ],
        PropertyInfo(alias="fieldKey"),
    ]
    """
    Filter by this field. Use with fieldOperator and, unless checking presence,
    fieldValue.
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

    modality: Literal["call", "chat"]

    page: int

    search: str

    sort_by: Annotated[
        Literal[
            "lastSeenAt",
            "firstSeenAt",
            "conversationCount",
            "voiceCount",
            "chatCount",
            "talkTimeMs",
            "displayName",
            "field.FULL_NAME",
            "field.PREFERRED_NAME",
            "field.ACCOUNT_ID",
            "field.COMPANY",
            "field.JOB_TITLE",
            "field.EMAIL",
            "field.ALTERNATE_PHONE",
            "field.AGE",
            "field.GENDER",
            "field.LANGUAGE",
            "field.LOCATION",
            "field.TIMEZONE",
            "field.BEST_TIME_TO_REACH",
            "field.PREFERRED_CHANNEL",
        ],
        PropertyInfo(alias="sortBy"),
    ]
    """
    A column, or field.<KEY> (for example field.COMPANY) to sort by a field's value.
    Customers without a value sort last.
    """

    sort_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortDirection")]
