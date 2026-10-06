# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MeCreateAPIKeyParams"]


class MeCreateAPIKeyParams(TypedDict, total=False):
    name: Required[str]
    """
    A label you will recognise later. It is the only thing that tells two
    credentials apart in the list you revoke from.
    """

    expires_at: Annotated[str, PropertyInfo(alias="expiresAt")]
    """
    ISO 8601 expiry. Defaults to the calling credential's own expiry (no expiry, for
    a `roark auth login` credential) and may not outlive it, so a short-lived
    connector credential cannot mint a permanent one.
    """

    permissions: SequenceNotStr[str]
    """
    Granular 'resource:action' permissions. Defaults to the calling credential's own
    set, and can never exceed it. A ceiling, not an entitlement: the holder still
    only reaches what their project membership allows.
    """

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """
    Project the credential assumes when a request sends no X-Roark-Project-Id
    header. Defaults to the calling credential's own default project. You must be an
    admin of whichever project is used.
    """

    scopes: List[Literal["READ", "WRITE"]]
    """
    Coarse tier. Defaults to the calling credential's own tier, and can never exceed
    it: a READ credential cannot mint a WRITE one.
    """
