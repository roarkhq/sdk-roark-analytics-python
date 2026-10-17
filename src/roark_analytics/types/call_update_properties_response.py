# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallUpdatePropertiesResponse", "Data", "DataMetricCollectionJob"]


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
    """Result of updating the properties of a call."""

    call_id: str = FieldInfo(alias="callId")
    """The call whose properties were updated"""

    metric_collection_error: Optional[str] = FieldInfo(alias="metricCollectionError")
    """
    Present (non-null) only when `metrics` were requested but the collection job
    could not be started (e.g. insufficient credits, or an unknown metric id). The
    properties were still written. Retry scoring via POST
    /v1/metric/collection-jobs, or re-send this request (writing the same values
    again is harmless). Null on success or when no metrics were requested.
    """

    metric_collection_job: Optional[DataMetricCollectionJob] = FieldInfo(alias="metricCollectionJob")
    """
    The metric collection job triggered to (re)score the requested metrics, or null
    when no metrics were requested (or when scoring failed, see
    metricCollectionError). Track its id to fetch results from GET
    /v1/metric/collection-jobs/:jobId.
    """

    properties: Dict[str, str]
    """
    All of the call's properties after the update, including the ones Roark sets,
    when the key also has the 'call:read' permission. A key without it gets back
    only the properties this request wrote. Values are returned as strings, as on
    GET /v1/call/:callId.
    """

    removed: List[str]
    """
    Stored names of the properties removed by this request. A property sent as null
    that was not on the call is not listed.
    """

    updated: List[str]
    """
    Stored (snake_case) names of the properties written by this request, including
    ones sent with the value they already had
    """


class CallUpdatePropertiesResponse(BaseModel):
    data: Data
    """Result of updating the properties of a call."""
