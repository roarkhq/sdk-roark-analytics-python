# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EvaluationGetJobRunsResponse",
    "Data",
    "DataData",
    "DataDataEvaluator",
    "DataDataEvidence",
    "DataDataMetric",
    "DataPagination",
]


class DataDataEvaluator(BaseModel):
    id: Optional[str] = None
    """ID of the evaluator"""

    name: Optional[str] = None
    """Name of the evaluator"""


class DataDataEvidence(BaseModel):
    id: Optional[str] = None
    """ID of the evidence"""

    comment_text: Optional[str] = FieldInfo(alias="commentText", default=None)
    """Comment on the evidence"""

    is_positive: Optional[bool] = FieldInfo(alias="isPositive", default=None)
    """Whether this is a positive example of the metric"""

    snippet_text: Optional[str] = FieldInfo(alias="snippetText", default=None)
    """Snippet of the evidence"""


class DataDataMetric(BaseModel):
    id: Optional[str] = None
    """ID of the metric"""

    boolean_value: Optional[bool] = FieldInfo(alias="booleanValue", default=None)
    """Boolean value of the metric"""

    confidence: Optional[float] = None
    """Confidence of the metric"""

    name: Optional[str] = None
    """Name of the metric"""

    numeric_value: Optional[float] = FieldInfo(alias="numericValue", default=None)
    """Numeric value of the metric"""

    reasoning: Optional[str] = None
    """Reasoning for the metric"""

    role: Optional[Literal["PRIMARY", "SECONDARY"]] = None
    """Role of the metric"""

    text_value: Optional[str] = FieldInfo(alias="textValue", default=None)
    """Text value of the metric"""

    value_type: Optional[Literal["NUMERIC", "BOOLEAN", "TEXT"]] = FieldInfo(alias="valueType", default=None)
    """Value type of the metric"""


class DataData(BaseModel):
    id: str
    """ID of the evaluator run"""

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)
    """When the evaluator run completed"""

    evaluator: Optional[DataDataEvaluator] = None
    """Evaluator of the evaluator run"""

    evidence: Optional[List[DataDataEvidence]] = None
    """Evidence of the evaluator run"""

    metrics: Optional[List[DataDataMetric]] = None
    """Metrics of the evaluator run"""

    score: Optional[float] = None
    """Score of the evaluator run"""

    score_classification: Optional[Literal["SUCCESS", "FAILURE", "IRRELEVANT"]] = FieldInfo(
        alias="scoreClassification", default=None
    )
    """Score classification of the evaluator run"""

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)
    """When the evaluator run started"""

    status: Literal["PENDING", "IN_PROGRESS", "COMPLETED", "FAILED"]
    """Status of the evaluator run"""

    summary: Optional[str] = None
    """Summary of the evaluator run"""


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
