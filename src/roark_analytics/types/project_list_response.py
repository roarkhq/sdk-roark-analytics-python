# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectListResponse", "Data", "DataProject", "DataProjectOrganization"]


class DataProjectOrganization(BaseModel):
    id: str

    name: str


class DataProject(BaseModel):
    id: str

    granted_permissions: List[str] = FieldInfo(alias="grantedPermissions")

    name: str

    organization: DataProjectOrganization

    slug: str


class Data(BaseModel):
    """Projects this credential may act on"""

    projects: List[DataProject]


class ProjectListResponse(BaseModel):
    data: Data
    """Projects this credential may act on"""
