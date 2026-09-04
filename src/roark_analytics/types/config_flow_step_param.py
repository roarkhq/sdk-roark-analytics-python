# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ConfigFlowStepParam"]


class ConfigFlowStepParam(TypedDict, total=False):
    type: Required[
        Literal[
            "AGENT_TURN",
            "CUSTOMER_TURN",
            "CUSTOMER_FIRST_MESSAGE",
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

    ref: str

    silence_duration_seconds: Annotated[int, PropertyInfo(alias="silenceDurationSeconds")]

    steps: List["ConfigFlowStepParam"]
