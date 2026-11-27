# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationGenerateResourcesParams", "Explore"]


class Explore(TypedDict, total=False):
    """Exploration settings"""

    enabled: bool
    """
    Whether Roark calls the agent to discover what it does before finishing the
    generation. Exploration calls are billed.
    """

    max_conversation_minutes: Annotated[int, PropertyInfo(alias="maxConversationMinutes")]
    """The longest a single exploration call may last, in minutes."""

    max_conversations: Annotated[int, PropertyInfo(alias="maxConversations")]
    """The most exploration calls Roark places."""


class SimulationGenerateResourcesParams(TypedDict, total=False):
    agent_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]]
    """
    The agents to generate simulation resources for. One agent per generation for
    now.
    """

    agent_endpoint_id: Annotated[str, PropertyInfo(alias="agentEndpointId")]
    """The endpoint the run plan calls. Defaults to the agent's newest endpoint."""

    capabilities: List[
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
    """The capabilities to test. Omit to let Roark work them out from the agent."""

    explore: Explore
    """Exploration settings"""

    industry: Literal[
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
    """The industry the agent serves."""

    industry_description: Annotated[str, PropertyInfo(alias="industryDescription")]
    """
    The industry in your own words, when none of the listed ones fits. Use it with
    industry OTHER.
    """

    testing_instructions: Annotated[str, PropertyInfo(alias="testingInstructions")]
    """
    What you want tested, in your own words. Each scenario you describe becomes a
    flow.
    """

    website_url: Annotated[str, PropertyInfo(alias="websiteUrl")]
    """A page Roark reads to learn about the business."""
