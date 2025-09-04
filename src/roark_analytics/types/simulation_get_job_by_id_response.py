# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationGetJobByIDResponse", "Data", "DataAgentEndpoint", "DataPersona", "DataScenario"]


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
    """Persona ID"""

    accent: str
    """Accent of the persona"""

    background_noise: str = FieldInfo(alias="backgroundNoise")
    """Background noise setting"""

    base_emotion: str = FieldInfo(alias="baseEmotion")
    """Base emotion of the persona"""

    confirmation_style: str = FieldInfo(alias="confirmationStyle")
    """How the persona confirms information"""

    disfluencies: bool
    """Whether persona has speech disfluencies"""

    gender: str
    """Gender of the persona"""

    intent_clarity: str = FieldInfo(alias="intentClarity")
    """How clearly the persona expresses intent"""

    language: str
    """Language of the persona"""

    memory_reliability: str = FieldInfo(alias="memoryReliability")
    """Reliability of persona memory"""

    name: str
    """Persona name"""

    speech_clarity: str = FieldInfo(alias="speechClarity")
    """Speech clarity"""

    speech_pace: str = FieldInfo(alias="speechPace")
    """Speech pace"""


class DataScenario(BaseModel):
    id: str
    """Scenario ID"""

    description: Optional[str] = None
    """Scenario description"""


class Data(BaseModel):
    agent_endpoint: DataAgentEndpoint = FieldInfo(alias="agentEndpoint")
    """Agent endpoint used in the simulation"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    persona: DataPersona
    """Persona used in the simulation"""

    processing_status: str = FieldInfo(alias="processingStatus")
    """Processing status"""

    scenario: DataScenario
    """Scenario used in the simulation"""

    simulation_job_id: str = FieldInfo(alias="simulationJobId")
    """Simulation job ID"""

    status: str
    """Job status"""

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)
    """When the job completed"""

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)
    """When the job started"""


class SimulationGetJobByIDResponse(BaseModel):
    data: Data
    """Simulation job with related entities"""
