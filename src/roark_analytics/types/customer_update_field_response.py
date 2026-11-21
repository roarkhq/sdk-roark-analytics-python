# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CustomerUpdateFieldResponse", "Data"]


class Data(BaseModel):
    description: Optional[str]
    """What extraction looks for in a conversation"""

    extract: bool
    """
    Whether conversations fill this field on this project: the project's own setting
    where it made one
    """

    key: str
    """What filters, sorts and attribute routes name the field by"""

    label: str

    redacted_by: Optional[
        Literal[
            "redactName", "redactEmail", "redactPhone", "redactDateOfBirth", "redactAddress", "redactBankAccountNumber"
        ]
    ] = FieldInfo(alias="redactedBy")
    """
    The project redaction setting that, when on, keeps conversations from filling
    this field
    """

    source: Literal["SYSTEM", "CUSTOM"]
    """SYSTEM for a built-in field, CUSTOM for one your project defined"""

    value_type: Literal["TEXT", "NUMBER", "BOOLEAN", "DATE", "PHONE_NUMBER", "EMAIL", "CURRENCY"] = FieldInfo(
        alias="valueType"
    )


class CustomerUpdateFieldResponse(BaseModel):
    data: Data
