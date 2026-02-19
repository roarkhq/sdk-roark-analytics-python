# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CallGetTranscriptParams"]


class CallGetTranscriptParams(TypedDict, total=False):
    source: Literal["ROARK_POST_CALL", "SIMULATION_AGENT_REALTIME", "CUSTOMER_AGENT_REALTIME"]
    """Transcription source to fetch.

    When omitted, uses the preferred source based on availability:
    CUSTOMER_AGENT_REALTIME > SIMULATION_AGENT_REALTIME > ROARK_POST_CALL
    """
