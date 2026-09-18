# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .autoimprove_fix import AutoimproveFix

__all__ = ["AutoimproveFixDismissResponse"]


class AutoimproveFixDismissResponse(BaseModel):
    data: AutoimproveFix
    """
    One Autoimprove engagement: Roark autonomously improving one agent toward one
    objective metric. Roark only ever changes the staging agent (a shadow clone by
    default); production changes exactly once, when a verified fix is promoted.
    """
