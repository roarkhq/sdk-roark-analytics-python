# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerUpdateFieldParams"]


class CustomerUpdateFieldParams(TypedDict, total=False):
    description: Optional[str]

    extract: bool

    label: str

    value_type: Annotated[
        Literal["TEXT", "NUMBER", "BOOLEAN", "DATE", "PHONE_NUMBER", "EMAIL", "CURRENCY"],
        PropertyInfo(alias="valueType"),
    ]
