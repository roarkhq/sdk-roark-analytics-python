# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookDeleteResponse", "Data"]


class Data(BaseModel):
    success: bool
    """Whether the deletion was successful"""


class WebhookDeleteResponse(BaseModel):
    data: Data
