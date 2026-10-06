# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MeCreateAPIKeyResponse", "Data"]


class Data(BaseModel):
    """The created credential, with its key"""

    id: str
    """Roark ID of the credential. Pass it to DELETE to revoke."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601 timestamp"""

    default_project_id: Optional[str] = FieldInfo(alias="defaultProjectId")
    """
    The project a request acts on when it sends no X-Roark-Project-Id header. Null
    once that project is deleted.
    """

    expires_at: Optional[str] = FieldInfo(alias="expiresAt")
    """ISO 8601 timestamp, null if it never expires"""

    key: str
    """The credential value. Returned only here, only once."""

    last_used_at: Optional[str] = FieldInfo(alias="lastUsedAt")
    """ISO 8601 timestamp, null if never used"""

    name: str
    """The label chosen when it was created"""

    organization_id: Optional[str] = FieldInfo(alias="organizationId")
    """The organization this credential is pinned to"""

    permissions: List[str]
    """Granted 'resource:action' permissions"""

    scopes: List[str]
    """Coarse tier: READ, or WRITE for read and write"""

    status: Optional[Literal["ACTIVE", "REVOKED"]]


class MeCreateAPIKeyResponse(BaseModel):
    data: Data
    """The created credential, with its key"""
