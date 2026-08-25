# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricPolicyDeleteResponse", "Data"]


class Data(BaseModel):
    deleted: bool
    """Whether the policy was deleted"""


class MetricPolicyDeleteResponse(BaseModel):
    data: Data
