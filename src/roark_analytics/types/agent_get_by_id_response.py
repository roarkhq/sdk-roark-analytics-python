# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentGetByIDResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier of the agent"""

    capabilities: Optional[
        List[
            Literal[
                "APPOINTMENT_BOOKING",
                "FAQ",
                "IDENTITY_VERIFICATION",
                "ACCOUNT_MANAGEMENT",
                "BILLING_AND_PAYMENTS",
                "ORDER_MANAGEMENT",
                "TROUBLESHOOTING",
                "CALL_ROUTING",
                "LEAD_QUALIFICATION",
                "COLLECTIONS",
                "OUTBOUND_CALLING",
            ]
        ]
    ]
    """What the agent handles. Null until it has been said."""

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
            "RECRUITING_AND_STAFFING",
            "OTHER",
        ]
    ]
    """The industry the agent serves"""

    industry_description: Optional[str] = FieldInfo(alias="industryDescription")
    """
    The industry in the customer's own words, when none of the listed ones fits
    (industry OTHER)
    """

    name: str
    """Name of the agent"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    website_url: Optional[str] = FieldInfo(alias="websiteUrl")
    """The business's website, which simulation setup reads"""


class AgentGetByIDResponse(BaseModel):
    data: Data
