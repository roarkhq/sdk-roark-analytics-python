# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentUpdateResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier of the agent"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    custom_id: Optional[str] = FieldInfo(alias="customId")
    """Custom identifier for the agent"""

    description: Optional[str]
    """Description of the agent"""

    industry: Optional[
        Literal[
            "HEALTHCARE",
            "FINANCIAL_SERVICES",
            "INSURANCE",
            "DEBT_COLLECTION",
            "RETAIL",
            "TRAVEL_AND_HOSPITALITY",
            "TELECOMMUNICATIONS",
            "TECHNOLOGY",
            "PUBLIC_SECTOR",
            "UTILITIES",
            "LOGISTICS",
            "AUTOMOTIVE",
            "HOME_SERVICES",
            "RESTAURANTS",
            "EDUCATION",
            "OTHER",
        ]
    ]
    """The industry the agent serves"""

    name: str
    """Name of the agent"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class AgentUpdateResponse(BaseModel):
    data: Data
