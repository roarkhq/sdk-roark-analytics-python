# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EvaluationCreateJobResponse", "Data"]


class Data(BaseModel):
    job_id: str = FieldInfo(alias="jobId")
    """ID of the evaluation job"""

    status: Literal["PENDING", "PROCESSING", "SUCCESS", "FAILURE"]
    """Status of the evaluation job"""


class EvaluationCreateJobResponse(BaseModel):
    data: Data
