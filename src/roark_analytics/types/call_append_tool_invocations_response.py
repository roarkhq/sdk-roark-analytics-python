# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallAppendToolInvocationsResponse", "Data", "DataMetricCollectionJob"]


class DataMetricCollectionJob(BaseModel):
    """A metric collection job that processes metrics for calls or chats"""

    id: str
    """Unique identifier of the metric collection job"""

    completed_at: Optional[str] = FieldInfo(alias="completedAt")
    """When the job completed"""

    completed_items: int = FieldInfo(alias="completedItems")
    """Number of successfully completed items"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    error_message: Optional[str] = FieldInfo(alias="errorMessage")
    """Error message if the job failed"""

    failed_items: int = FieldInfo(alias="failedItems")
    """Number of failed items"""

    policy_ids: List[str] = FieldInfo(alias="policyIds")
    """IDs of the metric policies that triggered this job"""

    started_at: Optional[str] = FieldInfo(alias="startedAt")
    """When the job started processing"""

    status: Literal["PENDING", "PROCESSING", "COMPLETED", "FAILED", "CANCELED"]
    """Current status of the job"""

    total_items: int = FieldInfo(alias="totalItems")
    """Total number of call-metric pairs to process"""

    triggered_by: Literal["USER_MANUAL", "USER_API", "METRIC_POLICY", "SIMULATION"] = FieldInfo(alias="triggeredBy")
    """What triggered this job"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the job was last updated"""


class Data(BaseModel):
    """Result of appending tool invocations to a call."""

    added: int
    """Number of tool invocations newly written"""

    call_id: str = FieldInfo(alias="callId")
    """The call the tool invocations were attached to"""

    metric_collection_error: Optional[str] = FieldInfo(alias="metricCollectionError")
    """
    Present (non-null) only when `metrics` were requested but the collection job
    could not be started (e.g. insufficient credits, or an unknown metric id). The
    tool invocations were still attached — retry scoring via POST
    /v1/metric/collection-jobs, or re-send this request (attaching is idempotent).
    Null on success or when no metrics were requested.
    """

    metric_collection_job: Optional[DataMetricCollectionJob] = FieldInfo(alias="metricCollectionJob")
    """
    The metric collection job triggered to (re)score the requested metrics, or null
    when no metrics were requested (or when scoring failed, see
    metricCollectionError). Track its id to fetch results from GET
    /v1/metric/collection-jobs/:jobId.
    """

    skipped: int
    """
    Number of tool invocations skipped because an identical one (same tool and
    timing) already existed on the call
    """


class CallAppendToolInvocationsResponse(BaseModel):
    data: Data
    """Result of appending tool invocations to a call."""
