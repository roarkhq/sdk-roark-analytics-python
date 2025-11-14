# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationLookupJobResponse", "Data", "DataAgentEndpoint", "DataPersona", "DataScenario"]


class DataAgentEndpoint(BaseModel):
    id: str
    """Agent endpoint ID"""

    endpoint_type: str = FieldInfo(alias="endpointType")
    """Agent endpoint type"""

    name: str
    """Agent endpoint name"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """Agent endpoint phone number"""


class DataPersona(BaseModel):
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


class DataScenario(BaseModel):
    id: str
    """Scenario ID"""

    description: Optional[str] = None
    """Scenario description"""


class Data(BaseModel):
    agent_endpoint: DataAgentEndpoint = FieldInfo(alias="agentEndpoint")
    """Agent endpoint used in a simulation"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    persona: DataPersona

    processing_status: str = FieldInfo(alias="processingStatus")
    """Processing status"""

    scenario: DataScenario
    """Scenario used in a simulation"""

    simulation_job_id: str = FieldInfo(alias="simulationJobId")
    """Simulation job ID"""

    status: str
    """Job status"""

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)
    """When the job completed"""

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)
    """When the job started"""


class SimulationLookupJobResponse(BaseModel):
    data: Data
    """Simulation job with related entities"""
