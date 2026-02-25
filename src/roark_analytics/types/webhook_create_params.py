# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    events: Required[
        List[
            Literal[
                "CALL_ANALYSIS_COMPLETED",
                "CALL_ANALYSIS_FAILED",
                "CALL_ANALYSIS_CANCELLED",
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
    ]
    """Event types to subscribe to (at least one required)"""

    url: Required[str]
    """Webhook URL"""

    description: Optional[str]
    """Webhook description"""

    headers: Dict[str, str]
    """Request headers (e.g. authorization tokens)"""
