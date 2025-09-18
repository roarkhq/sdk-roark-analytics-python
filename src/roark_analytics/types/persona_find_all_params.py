# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonaFindAllParams"]


class PersonaFindAllParams(TypedDict, total=False):
    after: str

    limit: int

    search_text: Annotated[str, PropertyInfo(alias="searchText")]
