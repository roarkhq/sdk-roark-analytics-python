# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationAnswerResourceGenerationResponse",
    "Data",
    "DataActivity",
    "DataExplore",
    "DataItem",
    "DataItemSource",
    "DataLayer",
    "DataQuestion",
    "DataTestDataNeeded",
]


class DataActivity(BaseModel):
    """One thing the generation did or said, in order"""

    created_at: str = FieldInfo(alias="createdAt")

    kind: Literal["STATUS", "REASONING", "ACTION", "GUIDANCE", "QUESTION", "ANSWER", "EXPLORATION", "ERROR"]
    """STATUS, REASONING, ACTION, GUIDANCE, QUESTION, ANSWER, EXPLORATION or ERROR"""

    text: str


class DataExplore(BaseModel):
    conversations_used: int = FieldInfo(alias="conversationsUsed")

    enabled: bool

    max_conversation_minutes: int = FieldInfo(alias="maxConversationMinutes")

    max_conversations: int = FieldInfo(alias="maxConversations")


class DataItemSource(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId")
    """
    The call it came from: an exploration call Roark placed, or one of the agent’s
    production calls
    """

    offset_ms: Optional[int] = FieldInfo(alias="offsetMs")
    """Where in the call"""

    quote: Optional[str]
    """The words in the source that led to it"""

    type: Literal[
        "CATALOGUE", "PROMPT", "DESCRIPTION", "WEBSITE", "EXPLORATION_CALL", "INSTRUCTIONS", "PRODUCTION_CALL"
    ]

    url: Optional[str]
    """The page it came from, for website sources"""


class DataItem(BaseModel):
    """Something the generation created or chose to leave out, and why"""

    id: str

    action: Literal["CREATED", "SKIPPED", "UPDATED"]
    """
    CREATED, SKIPPED with the reason, or UPDATED when scenarios were added to a flow
    it built
    """

    capability: Optional[
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

    kind: Literal["FLOW", "METRIC", "CHECK", "LAYER"]
    """A flow, a metric, or a pass or fail check"""

    label: str

    layer: Literal[
        "CORE", "INDUSTRY", "CAPABILITY", "AGENT_CONTEXT", "EXPLORATION", "CUSTOMER_INSTRUCTIONS", "PRODUCTION_CALLS"
    ]
    """
    Why it exists: CORE (every agent), INDUSTRY, CAPABILITY, AGENT_CONTEXT (your
    prompt or website), EXPLORATION or CUSTOMER_INSTRUCTIONS
    """

    origin: Optional[Literal["DISCOVERED", "INFERRED"]]
    """
    Exploration only: DISCOVERED on a call, or INFERRED from a path the agent
    offered
    """

    reason: str

    resource_id: Optional[str] = FieldInfo(alias="resourceId")
    """The flow or metric it created"""

    source: DataItemSource


class DataLayer(BaseModel):
    """Where one part of testing the agent stands"""

    layer: Literal[
        "CORE", "INDUSTRY", "CAPABILITY", "AGENT_CONTEXT", "EXPLORATION", "CUSTOMER_INSTRUCTIONS", "PRODUCTION_CALLS"
    ]

    status: Literal["COVERED", "SKIPPED", "OPEN", "NOT_APPLICABLE"]
    """
    COVERED: tests exist for it, or are added when the generation finishes. SKIPPED:
    the generation could not test it and said why. OPEN: not covered yet; the
    generation does not finish while a layer is open. NOT_APPLICABLE: nothing to
    test it from.
    """

    summary: str


class DataQuestion(BaseModel):
    """The question the generation is waiting on, while NEEDS_INPUT"""

    default_option: str = FieldInfo(alias="defaultOption")

    options: List[str]

    question: str


class DataTestDataNeeded(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId")

    label: str

    reason: str


class Data(BaseModel):
    """
    The simulation resources Roark generated for agents: the flows, metrics, checks
    and run plan, and why
    """

    id: str
    """Simulation resource generation ID"""

    activity: List[DataActivity]
    """What the generation did and said, in order"""

    agent_ids: List[str] = FieldInfo(alias="agentIds")
    """The agents the inputs were generated for"""

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

    completed_at: Optional[str] = FieldInfo(alias="completedAt")

    created_at: str = FieldInfo(alias="createdAt")

    draft_run_plan_id: Optional[str] = FieldInfo(alias="draftRunPlanId")
    """
    The quick test: a smaller run plan built from the agent’s own material before
    Roark calls the agent. You can start it while the generation is still running.
    Null when the generation does not call the agent.
    """

    error_message: Optional[str] = FieldInfo(alias="errorMessage")

    explore: DataExplore

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

    industry_description: Optional[str] = FieldInfo(alias="industryDescription")
    """The industry in your own words, when none of the listed ones fits"""

    items: List[DataItem]

    layers: List[DataLayer]
    """The checklist the generation works through"""

    question: Optional[DataQuestion]
    """The question the generation is waiting on, while NEEDS_INPUT"""

    run_plan_id: Optional[str] = FieldInfo(alias="runPlanId")
    """The full suite: the run plan to start once the generation completes"""

    status: Literal["PENDING", "RUNNING", "NEEDS_INPUT", "COMPLETED", "FAILED", "CANCELLED"]
    """
    PENDING, RUNNING, NEEDS_INPUT (waiting on a question; it goes ahead with the
    default if nobody answers), COMPLETED, FAILED or CANCELLED
    """

    test_data_needed: List[DataTestDataNeeded] = FieldInfo(alias="testDataNeeded")
    """Test data the agent asked for that Roark did not have"""


class SimulationAnswerResourceGenerationResponse(BaseModel):
    data: Data
    """
    The simulation resources Roark generated for agents: the flows, metrics, checks
    and run plan, and why
    """
