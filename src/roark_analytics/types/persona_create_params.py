# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonaCreateParams"]


class PersonaCreateParams(TypedDict, total=False):
    accent: Required[Literal["US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU"]]
    """Accent of the persona"""

    background_noise: Required[Annotated[Literal["NONE", "OFFICE"], PropertyInfo(alias="backgroundNoise")]]
    """Background noise setting"""

    base_emotion: Required[
        Annotated[
            Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"],
            PropertyInfo(alias="baseEmotion"),
        ]
    ]
    """Base emotional state of the persona"""

    confirmation_style: Required[Annotated[Literal["EXPLICIT", "VAGUE"], PropertyInfo(alias="confirmationStyle")]]
    """How the persona confirms information"""

    gender: Required[Literal["MALE", "FEMALE", "NEUTRAL"]]
    """Gender of the persona"""

    has_disfluencies: Required[Annotated[bool, PropertyInfo(alias="hasDisfluencies")]]
    """Whether the persona uses filler words like "um" and "uh" """

    intent_clarity: Required[Annotated[Literal["CLEAR", "INDIRECT", "VAGUE"], PropertyInfo(alias="intentClarity")]]
    """How clearly the persona expresses their intentions"""

    language: Required[Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL"]]
    """Primary language for the persona"""

    memory_reliability: Required[Annotated[Literal["HIGH", "LOW"], PropertyInfo(alias="memoryReliability")]]
    """How reliable the persona's memory is"""

    name: Required[str]
    """The name the agent will identify as during conversations"""

    speech_clarity: Required[Annotated[Literal["CLEAR", "VAGUE", "RAMBLING"], PropertyInfo(alias="speechClarity")]]
    """Speech clarity of the persona"""

    speech_pace: Required[Annotated[Literal["SLOW", "NORMAL", "FAST"], PropertyInfo(alias="speechPace")]]
    """Speech pace of the persona"""

    backstory_prompt: Annotated[Optional[str], PropertyInfo(alias="backstoryPrompt")]
    """Background story and behavioral patterns for the persona"""

    properties: Dict[str, object]
    """Additional custom properties about the persona"""

    secondary_language: Annotated[Optional[Literal["EN"]], PropertyInfo(alias="secondaryLanguage")]
    """Secondary language for code-switching (e.g., Hinglish, Spanglish)"""
