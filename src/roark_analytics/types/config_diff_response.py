# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ConfigDiffResponse", "Data", "DataChange", "DataSummary"]


class DataChange(BaseModel):
    config_key: str = FieldInfo(alias="configKey")

    kind: Literal["agent", "persona", "flow", "collector", "metric"]

    name: str

    op: Literal["create", "update", "delete", "noop"]

    detail: Optional[str] = None


class DataSummary(BaseModel):
    create: int

    delete: int

    noop: int

    update: int


class Data(BaseModel):
    changes: List[DataChange]

    summary: DataSummary


class ConfigDiffResponse(BaseModel):
    data: Data
