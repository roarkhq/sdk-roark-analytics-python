# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["CustomerFlowDuplicateParams"]


class CustomerFlowDuplicateParams(TypedDict, total=False):
    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]
    """
    Agents to link on the copy. Omit to carry the source flow's agents over.
    Required when the source is a Roark-managed flow with no agents of its own.
    """

    title: str
    """Title for the copy. Defaults to "Copy of" the source flow."""
