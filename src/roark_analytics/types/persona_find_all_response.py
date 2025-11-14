# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PersonaFindAllResponse", "Data", "Pagination"]


class Data(BaseModel):
    id: str
    """Unique identifier of the persona"""

    accent: Literal["US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT"]
    """
    Accent of the persona, defined using ISO 3166-1 alpha-2 country codes with
    optional variants
    """

    background_noise: Literal[
        "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
    ] = FieldInfo(alias="backgroundNoise")
    """Background noise setting"""

    base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"] = FieldInfo(
        alias="baseEmotion"
    )
    """Base emotional state of the persona"""

    confirmation_style: Literal["EXPLICIT", "VAGUE"] = FieldInfo(alias="confirmationStyle")
    """How the persona confirms information"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    gender: Literal["MALE", "FEMALE", "NEUTRAL"]
    """Gender of the persona"""

    has_disfluencies: bool = FieldInfo(alias="hasDisfluencies")
    """Whether the persona uses filler words like "um" and "uh" """

    intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] = FieldInfo(alias="intentClarity")
    """How clearly the persona expresses their intentions"""

    language: Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT"]
    """Primary language ISO 639-1 code for the persona"""

    memory_reliability: Literal["HIGH", "LOW"] = FieldInfo(alias="memoryReliability")
    """How reliable the persona's memory is"""

    name: str
    """The name the agent will identify as during conversations"""

    properties: Dict[str, object]
    """Additional custom properties about the persona"""

    speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] = FieldInfo(alias="speechClarity")
    """Speech clarity of the persona"""

    speech_pace: Literal["SLOW", "NORMAL", "FAST"] = FieldInfo(alias="speechPace")
    """Speech pace of the persona"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    backstory_prompt: Optional[str] = FieldInfo(alias="backstoryPrompt", default=None)
    """Background story and behavioral patterns for the persona"""

    secondary_language: Optional[Literal["EN"]] = FieldInfo(alias="secondaryLanguage", default=None)
    """
    Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)
    """


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """Whether there are more items to fetch"""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page of items"""

    total: float
    """Total number of items"""


class PersonaFindAllResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
