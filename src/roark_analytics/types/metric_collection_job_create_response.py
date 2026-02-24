# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetricCollectionJobCreateResponse", "Data"]


class Data(BaseModel):
    """A metric collection job that processes metrics for calls"""

    id: str
    """Unique identifier of the metric collection job"""

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)
    """When the job completed"""

    completed_items: int = FieldInfo(alias="completedItems")
    """Number of successfully completed items"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Error message if the job failed"""

    failed_items: int = FieldInfo(alias="failedItems")
    """Number of failed items"""

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)
    """When the job started processing"""

    status: Literal["PENDING", "PROCESSING", "COMPLETED", "FAILED", "CANCELED"]
    """Current status of the job"""

    total_items: int = FieldInfo(alias="totalItems")
    """Total number of call-metric pairs to process"""

    triggered_by: Literal["USER_MANUAL", "USER_API", "METRIC_POLICY", "SIMULATION"] = FieldInfo(alias="triggeredBy")
    """What triggered this job"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the job was last updated"""


class MetricCollectionJobCreateResponse(BaseModel):
    data: Data
    """A metric collection job that processes metrics for calls"""
