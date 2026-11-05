# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ConfigFlowStepParam", "OffScript", "StageUnionMember1"]


class OffScript(TypedDict, total=False):
    max_attempts: Annotated[int, PropertyInfo(alias="maxAttempts")]

    reaction: Literal["STAY_SILENT", "REPEAT", "RESPOND", "SAY"]

    say_line: Annotated[str, PropertyInfo(alias="sayLine")]

    then: Literal["HANG_UP", "MOVE_ON", "ADAPT", "HANG_UP_INVALIDATE"]

    wait_seconds: Annotated[int, PropertyInfo(alias="waitSeconds")]


class StageUnionMember1(TypedDict, total=False):
    name: Required[str]

    analyze: bool

    required: bool


class ConfigFlowStepParam(TypedDict, total=False):
    type: Required[
        Literal[
            "AGENT_TURN",
            "CUSTOMER_TURN",
            "CUSTOMER_FIRST_MESSAGE",
            "CUSTOMER_VERBATIM_TURN",
            "CUSTOMER_SILENCE",
            "CUSTOMER_AUDIO",
            "CUSTOMER_DTMF",
            "AGENT_DTMF",
            "VOICEMAIL",
            "SCENARIO_LINK",
            "CUSTOMER_HANDOFF",
        ]
    ]

    audio_clip: Annotated[
        Literal[
            "HOLD_MUSIC_CLASSICAL_PIANO",
            "HOLD_MUSIC_CLASSICAL_ORCHESTRA",
            "HOLD_MUSIC_STRING_QUARTET",
            "HOLD_MUSIC_AMBIENT",
            "HOLD_MUSIC_SMOOTH_JAZZ",
            "HOLD_MUSIC_SOFT_SYNTH",
            "HOLD_BEEP",
            "RINGBACK_US",
            "RINGBACK_UK",
        ],
        PropertyInfo(alias="audioClip"),
    ]

    content: str

    dtmf_digits: Annotated[str, PropertyInfo(alias="dtmfDigits")]

    flow: str

    handoff_persona: Annotated[str, PropertyInfo(alias="handoffPersona")]

    merge_into: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeInto")]

    off_script: Annotated[OffScript, PropertyInfo(alias="offScript")]

    ref: str

    required_for_valid_run: Annotated[bool, PropertyInfo(alias="requiredForValidRun")]
    """Removed. Use `stage` with `required: true`."""

    silence_duration_seconds: Annotated[int, PropertyInfo(alias="silenceDurationSeconds")]

    stage: Union[str, StageUnionMember1]

    steps: List["ConfigFlowStepParam"]
