# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ConfigFlowStep"]


class ConfigFlowStep(BaseModel):
    type: Literal[
        "AGENT_TURN",
        "CUSTOMER_TURN",
        "CUSTOMER_FIRST_MESSAGE",
        "CUSTOMER_SILENCE",
        "CUSTOMER_DTMF",
        "VOICEMAIL",
        "SCENARIO_LINK",
    ]

    content: Optional[str] = None

    dtmf_digits: Optional[str] = FieldInfo(alias="dtmfDigits", default=None)

    flow: Optional[str] = None

    merge_into: Optional[List[str]] = FieldInfo(alias="mergeInto", default=None)

    ref: Optional[str] = None

    silence_duration_seconds: Optional[int] = FieldInfo(alias="silenceDurationSeconds", default=None)

    steps: Optional[List["ConfigFlowStep"]] = None
