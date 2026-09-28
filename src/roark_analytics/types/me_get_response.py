# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MeGetResponse", "Data", "DataDefaultProject", "DataOrganization", "DataUser"]


class DataDefaultProject(BaseModel):
    id: str

    name: str

    slug: str


class DataOrganization(BaseModel):
    id: str

    name: str


class DataUser(BaseModel):
    id: str

    email: str

    name: Optional[str]


class Data(BaseModel):
    """The credential making this request, and what it is bound to"""

    default_project: Optional[DataDefaultProject] = FieldInfo(alias="defaultProject")

    granted_permissions: List[str] = FieldInfo(alias="grantedPermissions")

    organization: DataOrganization

    scopes: List[str]

    token_scope: Literal["PROJECT", "USER"] = FieldInfo(alias="tokenScope")

    user: Optional[DataUser]


class MeGetResponse(BaseModel):
    data: Data
    """The credential making this request, and what it is bound to"""
