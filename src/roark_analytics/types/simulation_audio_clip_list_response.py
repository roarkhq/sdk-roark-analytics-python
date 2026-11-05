# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SimulationAudioClipListResponse", "Data"]


class Data(BaseModel):
    category: Literal["HOLD_MUSIC", "HOLD_TONE", "RINGBACK"]
    """The kind of audio this is"""

    clip: Literal[
        "HOLD_MUSIC_CLASSICAL_PIANO",
        "HOLD_MUSIC_CLASSICAL_ORCHESTRA",
        "HOLD_MUSIC_STRING_QUARTET",
        "HOLD_MUSIC_AMBIENT",
        "HOLD_MUSIC_SMOOTH_JAZZ",
        "HOLD_MUSIC_SOFT_SYNTH",
        "HOLD_BEEP",
        "RINGBACK_US",
        "RINGBACK_UK",
    ]
    """What a CUSTOMER_AUDIO step names as its `audioClip`"""

    description: str
    """What it sounds like"""

    name: str
    """What the clip is called"""


class SimulationAudioClipListResponse(BaseModel):
    data: List[Data]
