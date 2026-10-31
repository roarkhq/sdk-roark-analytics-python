# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    agent_id: Annotated[Optional[str], PropertyInfo(alias="agentId")]
    """Agent to assign the number to; null unassigns, omit to leave it alone"""

    name: Optional[str]
    """New label; null clears it, omit to leave it alone"""
