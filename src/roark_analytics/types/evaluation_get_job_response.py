# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EvaluationGetJobResponse", "Data", "DataCall", "DataDataset", "DataDatasetCall"]


class DataCall(BaseModel):
    id: Optional[str] = None
    """ID of the call being evaluated"""


class DataDatasetCall(BaseModel):
    id: Optional[str] = None
    """ID of the call"""


class DataDataset(BaseModel):
    id: Optional[str] = None
    """ID of the dataset"""

    calls: List[DataDatasetCall]
    """Calls in the dataset"""


class Data(BaseModel):
    id: str
    """ID of the evaluation job"""

    status: Literal["PENDING", "PROCESSING", "SUCCESS", "FAILURE"]
    """Status of the evaluation job"""

    call: Optional[DataCall] = None
    """Call being evaluated"""

    dataset: Optional[DataDataset] = None
    """Dataset being evaluated"""


class EvaluationGetJobResponse(BaseModel):
    data: Data
    """Evaluation job response payload"""
