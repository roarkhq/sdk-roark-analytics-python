# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentConfigResolveParams", "Session"]


class Session(TypedDict, total=False):
    """
    Session context. When the call was originated by a Roark simulation, Roark
    recognizes it here and serves the staging revision for this session only; real
    traffic always gets production.
    """

    called_number: Annotated[str, PropertyInfo(alias="calledNumber")]
    """The number your agent was reached on (E.164)."""

    caller_number: Annotated[str, PropertyInfo(alias="callerNumber")]
    """The number calling your agent (E.164). Required for simulation recognition."""

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Your session or room identifier, for correlation."""


class AgentConfigResolveParams(TypedDict, total=False):
    defaults: Dict[str, object]
    """
    Your baked-in config. On the first fetch of an unknown key this registers the
    config and becomes revision 1, so integration is a single call. Ignored once the
    key exists.
    """

    session: Session
    """
    Session context. When the call was originated by a Roark simulation, Roark
    recognizes it here and serves the staging revision for this session only; real
    traffic always gets production.
    """
