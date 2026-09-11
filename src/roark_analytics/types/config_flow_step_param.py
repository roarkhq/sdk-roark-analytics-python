# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ConfigFlowStepParam", "OffScript"]


class OffScript(TypedDict, total=False):
    max_attempts: Annotated[int, PropertyInfo(alias="maxAttempts")]

    reaction: Literal["STAY_SILENT", "REPEAT", "RESPOND", "SAY"]

    say_line: Annotated[str, PropertyInfo(alias="sayLine")]

    then: Literal["HANG_UP", "MOVE_ON", "ADAPT", "HANG_UP_INVALIDATE"]

    wait_seconds: Annotated[int, PropertyInfo(alias="waitSeconds")]


class ConfigFlowStepParam(TypedDict, total=False):
    type: Required[
        Literal[
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
    ]

    content: str

    dtmf_digits: Annotated[str, PropertyInfo(alias="dtmfDigits")]

    flow: str

    merge_into: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeInto")]

    off_script: Annotated[OffScript, PropertyInfo(alias="offScript")]

    ref: str

    silence_duration_seconds: Annotated[int, PropertyInfo(alias="silenceDurationSeconds")]

    steps: List["ConfigFlowStepParam"]
