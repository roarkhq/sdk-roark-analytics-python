# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentVersionRollbackParams"]


class AgentVersionRollbackParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    expected_live_version_id: Annotated[str, PropertyInfo(alias="expectedLiveVersionId")]
    """
    The live version when you decided to roll back. When sent, the rollback is
    refused with 409 if another version went live since.
    """

    summary: str
