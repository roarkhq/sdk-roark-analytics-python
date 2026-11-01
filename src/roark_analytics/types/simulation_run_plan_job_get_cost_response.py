# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationRunPlanJobGetCostResponse", "Data", "DataBreakdown", "DataCall"]


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


class DataCall(BaseModel):
    amount_usd: float = FieldInfo(alias="amountUsd")

    amount_usd_micros: int = FieldInfo(alias="amountUsdMicros")

    breakdown: List[DataBreakdown]

    conversation_id: Optional[str] = FieldInfo(alias="conversationId")
    """
    The call (voice runs) or chat (chat runs) the spend is attributed to. Null for
    costs incurred before the conversation existed; use simulationJobId to join
    those.
    """

    simulation_job_id: Optional[str] = FieldInfo(alias="simulationJobId")


class Data(BaseModel):
    breakdown: List[DataBreakdown]
    """Spend by cost type. Sums to totalUsdMicros."""

    calls: List[DataCall]
    """Spend per simulated call in the run."""

    currency: Literal["usd"]

    job_id: str = FieldInfo(alias="jobId")

    total_usd: float = FieldInfo(alias="totalUsd")

    total_usd_micros: int = FieldInfo(alias="totalUsdMicros")
    """Total billable spend for the run, in micro-dollars."""


class SimulationRunPlanJobGetCostResponse(BaseModel):
    data: Data
