# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EvaluationGetJobRunsResponse",
    "Data",
    "DataData",
    "DataDataBlockRun",
    "DataDataEvaluator",
    "DataDataEvidence",
    "DataDataMetric",
    "DataPagination",
]


class DataDataBlockRun(BaseModel):
    block_definition_id: str = FieldInfo(alias="blockDefinitionId")
    """ID of the block definition"""

    block_name: str = FieldInfo(alias="blockName")
    """Name of the evaluation block"""

    block_run_id: str = FieldInfo(alias="blockRunId")
    """ID of the block run instance"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the block run was created"""

    reason: Optional[str] = None
    """Reason for the outcome (pass/fail explanation or skip reason)"""

    result: Optional[Literal["PASSED", "FAILED", "SKIPPED"]] = None
    """Result of the block run"""

    score: Optional[float] = None
    """Score of the block run (0-1)"""

    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"]
    """Status of the block run"""


class DataDataEvaluator(BaseModel):
    id: str
    """ID of the evaluator"""

    name: str
    """Name of the evaluator"""

    weight: Optional[float] = None
    """Weight of the evaluator"""


class DataDataEvidence(BaseModel):
    comment_text: Optional[str] = FieldInfo(alias="commentText", default=None)
    """Comment text of the evidence"""

    created_at: str = FieldInfo(alias="createdAt")
    """Created at of the evidence"""

    is_positive: bool = FieldInfo(alias="isPositive")
    """Is positive of the evidence"""

    snippet_text: str = FieldInfo(alias="snippetText")
    """Snippet text of the evidence"""


class DataDataMetric(BaseModel):
    boolean_value: Optional[bool] = FieldInfo(alias="booleanValue", default=None)
    """Boolean value of the metric"""

    confidence: Optional[float] = None
    """Confidence level of the metric (0-1)"""

    created_at: str = FieldInfo(alias="createdAt")
    """Created at of the metric"""

    name: str
    """Name of the metric"""

    numeric_value: Optional[float] = FieldInfo(alias="numericValue", default=None)
    """Numeric value of the metric"""

    reasoning: Optional[str] = None
    """Reasoning of the metric"""

    role: str
    """Role of the metric"""

    text_value: Optional[str] = FieldInfo(alias="textValue", default=None)
    """Text value of the metric"""

    value_type: str = FieldInfo(alias="valueType")
    """Value type of the metric"""


class DataData(BaseModel):
    block_runs: List[DataDataBlockRun] = FieldInfo(alias="blockRuns")
    """All block runs for this evaluator, including skipped ones"""

    evaluator: DataDataEvaluator

    evidence: List[DataDataEvidence]

    metrics: List[DataDataMetric]

    status: Literal["PENDING", "IN_PROGRESS", "COMPLETED", "FAILED"]
    """Status of the evaluator run"""

    id: Optional[str] = None
    """ID of the evaluator run"""

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)
    """When the evaluator run completed"""

    result: Optional[Literal["SUCCESS", "FAILURE", "SKIPPED"]] = None
    """
    Result of the evaluator run based on score threshold (IRRELEVANT is mapped to
    SKIPPED)
    """

    score: Optional[float] = None
    """Score of the evaluation run (0-1)"""

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)
    """When the evaluator run started"""

    summary: Optional[str] = None
    """Summary of the evaluation run"""


class DataPagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """Whether there are more items to fetch"""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page of items"""

    total: float
    """Total number of items"""


class Data(BaseModel):
    data: Optional[List[DataData]] = None
    """Evaluator runs of the evaluation job"""

    pagination: Optional[DataPagination] = None
    """Pagination information"""


class EvaluationGetJobRunsResponse(BaseModel):
    data: Data
    """Evaluation job runs response payload"""
