# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
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
    """What the agent handles. Simulation setup tests each one."""

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
    """The industry the agent serves."""

    industry_description: Annotated[Optional[str], PropertyInfo(alias="industryDescription")]
    """
    The industry in your own words, when none of the listed ones fits. Use it with
    industry OTHER.
    """

    name: str
    """Name of the agent"""

    website_url: Annotated[Optional[str], PropertyInfo(alias="websiteUrl")]
    """The business's website. Simulation setup reads it."""
