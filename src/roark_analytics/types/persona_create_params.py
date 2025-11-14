# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonaCreateParams"]


class PersonaCreateParams(TypedDict, total=False):
    accent: Required[Literal["US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT"]]
    """
    Accent of the persona, defined using ISO 3166-1 alpha-2 country codes with
    optional variants
    """

    gender: Required[Literal["MALE", "FEMALE", "NEUTRAL"]]
    """Gender of the persona"""

    language: Required[Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT"]]
    """Primary language ISO 639-1 code for the persona"""

    name: Required[str]
    """The name the agent will identify as during conversations"""

    background_noise: Annotated[
        Literal["NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"],
        PropertyInfo(alias="backgroundNoise"),
    ]
    """Background noise setting"""

    backstory_prompt: Annotated[Optional[str], PropertyInfo(alias="backstoryPrompt")]
    """Background story and behavioral patterns for the persona"""

    base_emotion: Annotated[
        Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"],
        PropertyInfo(alias="baseEmotion"),
    ]
    """Base emotional state of the persona"""

    confirmation_style: Annotated[Literal["EXPLICIT", "VAGUE"], PropertyInfo(alias="confirmationStyle")]
    """How the persona confirms information"""

    has_disfluencies: Annotated[bool, PropertyInfo(alias="hasDisfluencies")]
    """Whether the persona uses filler words like "um" and "uh" """

    intent_clarity: Annotated[Literal["CLEAR", "INDIRECT", "VAGUE"], PropertyInfo(alias="intentClarity")]
    """How clearly the persona expresses their intentions"""

    memory_reliability: Annotated[Literal["HIGH", "LOW"], PropertyInfo(alias="memoryReliability")]
    """How reliable the persona's memory is"""

    properties: Dict[str, object]
    """Additional custom properties about the persona"""

    secondary_language: Annotated[Optional[Literal["EN"]], PropertyInfo(alias="secondaryLanguage")]
    """
    Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)
    """

    speech_clarity: Annotated[Literal["CLEAR", "VAGUE", "RAMBLING"], PropertyInfo(alias="speechClarity")]
    """Speech clarity of the persona"""

    speech_pace: Annotated[Literal["SLOW", "NORMAL", "FAST"], PropertyInfo(alias="speechPace")]
    """Speech pace of the persona"""
