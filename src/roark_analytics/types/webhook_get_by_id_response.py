# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookGetByIDResponse", "Data"]


class Data(BaseModel):
    """Webhook with its subscribed event types"""

    id: str
    """Webhook ID"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    description: Optional[str] = None
    """Webhook description"""

    events: List[
        Literal[
            "CALL_ANALYSIS_COMPLETED",
            "CALL_ANALYSIS_FAILED",
            "CALL_EVALUATION_COMPLETED",
            "CALL_EVALUATION_FAILED",
            "SIMULATION_RUN_PLAN_JOB_STARTED",
            "SIMULATION_RUN_PLAN_JOB_COMPLETED",
            "SIMULATION_RUN_PLAN_JOB_FAILED",
            "SIMULATION_RUN_PLAN_JOB_CANCELLED",
            "SIMULATION_JOB_STARTED",
            "SIMULATION_JOB_COMPLETED",
            "SIMULATION_JOB_FAILED",
            "SIMULATION_JOB_CANCELLED",
        ]
    ]
    """Event types this webhook is subscribed to"""

    headers: Dict[str, str]
    """Request headers"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    url: str
    """Webhook URL"""


class WebhookGetByIDResponse(BaseModel):
    data: Data
    """Webhook with its subscribed event types"""
