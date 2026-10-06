# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MeRevokeAPIKeyResponse", "Data"]


class Data(BaseModel):
    """Result of revoking one of your credentials"""

    id: str

    deleted: Literal[True]
    """Always true when the credential was revoked"""


class MeRevokeAPIKeyResponse(BaseModel):
    data: Data
    """Result of revoking one of your credentials"""
