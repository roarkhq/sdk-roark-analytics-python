# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EvaluationCreateJobResponse", "Data"]


class Data(BaseModel):
    job_id: str = FieldInfo(alias="jobId")
    """ID of the evaluation job"""

    status: Literal["PENDING", "PROCESSING", "SUCCESS", "FAILURE"]
    """Status of the evaluation job"""

    call_id: Optional[str] = FieldInfo(alias="callId", default=None)
    """ID of the call being evaluated (only present for single call evaluations)"""


class EvaluationCreateJobResponse(BaseModel):
    data: Data
