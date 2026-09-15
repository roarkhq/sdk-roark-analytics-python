# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ConfigFlowStep", "OffScript"]


class OffScript(BaseModel):
    max_attempts: Optional[int] = FieldInfo(alias="maxAttempts", default=None)

    reaction: Optional[Literal["STAY_SILENT", "REPEAT", "RESPOND", "SAY"]] = None

    say_line: Optional[str] = FieldInfo(alias="sayLine", default=None)

    then: Optional[Literal["HANG_UP", "MOVE_ON", "ADAPT", "HANG_UP_INVALIDATE"]] = None

    wait_seconds: Optional[int] = FieldInfo(alias="waitSeconds", default=None)


class ConfigFlowStep(BaseModel):
    type: Literal[
        "AGENT_TURN",
        "CUSTOMER_TURN",
        "CUSTOMER_FIRST_MESSAGE",
        "CUSTOMER_VERBATIM_TURN",
        "CUSTOMER_SILENCE",
        "CUSTOMER_DTMF",
        "AGENT_DTMF",
        "VOICEMAIL",
        "SCENARIO_LINK",
    ]

    content: Optional[str] = None

    dtmf_digits: Optional[str] = FieldInfo(alias="dtmfDigits", default=None)

    flow: Optional[str] = None

    merge_into: Optional[List[str]] = FieldInfo(alias="mergeInto", default=None)

    off_script: Optional[OffScript] = FieldInfo(alias="offScript", default=None)

    ref: Optional[str] = None

    silence_duration_seconds: Optional[int] = FieldInfo(alias="silenceDurationSeconds", default=None)

    steps: Optional[List["ConfigFlowStep"]] = None
