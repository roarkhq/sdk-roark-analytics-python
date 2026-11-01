# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallGetCostResponse", "Data", "DataBreakdown", "DataItem"]


class DataBreakdown(BaseModel):
    amount_usd: float = FieldInfo(alias="amountUsd")
    """The same figure in US dollars."""

    amount_usd_micros: int = FieldInfo(alias="amountUsdMicros")
    """Billable spend for this type, in micro-dollars."""

    quantity: float
    """Units billed (see the line items for the unit)."""

    source: Literal[
        "SIM_PLATFORM_FEE",
        "SIM_TTS",
        "SIM_STT",
        "SIM_LLM",
        "SIM_TELEPHONY",
        "METRIC",
        "TRANSCRIPTION",
        "INTERNAL_LLM",
        "INTERNAL_STT",
        "PHONE_NUMBER",
    ]
    """The cost source, e.g. SIM_PLATFORM_FEE, SIM_LLM, METRIC."""

    surface: Literal["SIMULATION", "POST_CALL"]
    """SIMULATION or POST_CALL."""


class DataItem(BaseModel):
    amount_usd: float = FieldInfo(alias="amountUsd")

    amount_usd_micros: int = FieldInfo(alias="amountUsdMicros")

    event_id: str = FieldInfo(alias="eventId")
    """Stable id of the cost event. Use it to deduplicate."""

    metric_collection_job_id: Optional[str] = FieldInfo(alias="metricCollectionJobId")
    """
    The grading pass a METRIC line paid for. A call graded twice carries one line
    per pass.
    """

    metric_definition_id: Optional[str] = FieldInfo(alias="metricDefinitionId")
    """The metric a METRIC line was charged for."""

    model: Optional[str]

    occurred_at: str = FieldInfo(alias="occurredAt")
    """When the cost was incurred, ISO 8601."""

    provider: Optional[str]

    quantity: float

    quantity_unit: Literal["MINUTES", "INPUT_TOKENS", "OUTPUT_TOKENS", "CHARACTERS", "AUDIO_SECONDS", "UNITS"] = (
        FieldInfo(alias="quantityUnit")
    )

    simulation_job_id: Optional[str] = FieldInfo(alias="simulationJobId")

    source: Literal[
        "SIM_PLATFORM_FEE",
        "SIM_TTS",
        "SIM_STT",
        "SIM_LLM",
        "SIM_TELEPHONY",
        "METRIC",
        "TRANSCRIPTION",
        "INTERNAL_LLM",
        "INTERNAL_STT",
        "PHONE_NUMBER",
    ]

    surface: Literal["SIMULATION", "POST_CALL"]


class Data(BaseModel):
    breakdown: List[DataBreakdown]
    """Spend by cost type. Sums to totalUsdMicros."""

    call_id: str = FieldInfo(alias="callId")

    currency: Literal["usd"]

    items: List[DataItem]
    """Every billable cost line attributed to the call."""

    total_usd: float = FieldInfo(alias="totalUsd")

    total_usd_micros: int = FieldInfo(alias="totalUsdMicros")
    """Total billable spend for this call, in micro-dollars."""


class CallGetCostResponse(BaseModel):
    data: Data
