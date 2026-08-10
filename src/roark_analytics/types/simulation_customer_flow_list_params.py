# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationCustomerFlowListParams"]


class SimulationCustomerFlowListParams(TypedDict, total=False):
    after: str

    include_system: Annotated[Literal["true", "false"], PropertyInfo(alias="includeSystem")]

    limit: int

    mode: Literal["UNSCRIPTED", "SCRIPTED", "VOICEMAIL"]

    search_text: Annotated[str, PropertyInfo(alias="searchText")]
