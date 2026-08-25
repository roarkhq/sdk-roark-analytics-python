# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ConfigApplyResponse", "Data", "DataChange", "DataSummary"]


class DataChange(BaseModel):
    config_key: str = FieldInfo(alias="configKey")

    kind: Literal["agent", "persona", "flow", "collector", "metric"]

    name: str

    op: Literal["create", "update", "delete", "noop"]

    status: Literal["applied", "skipped", "failed"]

    id: Optional[str] = None

    detail: Optional[str] = None

    error: Optional[str] = None


class DataSummary(BaseModel):
    create: int

    delete: int

    failed: int

    noop: int

    update: int


class Data(BaseModel):
    changes: List[DataChange]

    summary: DataSummary


class ConfigApplyResponse(BaseModel):
    data: Data
