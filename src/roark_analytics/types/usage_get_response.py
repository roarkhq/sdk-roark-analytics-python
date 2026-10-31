# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UsageGetResponse", "Data", "DataProject", "DataProjectBreakdown"]


class DataProjectBreakdown(BaseModel):
    amount_usd: float = FieldInfo(alias="amountUsd")
    """The same figure in US dollars."""

    amount_usd_micros: int = FieldInfo(alias="amountUsdMicros")
    """Billable spend for this type, in micro-dollars."""

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
    """
    The cost source, e.g. SIM_PLATFORM_FEE, SIM_LLM, SIM_TTS, SIM_STT,
    SIM_TELEPHONY, METRIC, or TRANSCRIPTION. These are the granular sources behind
    the Billing screen categories (SIM_* roll up into "Simulation").
    """

    surface: Literal["SIMULATION", "POST_CALL"]
    """Whether this cost came from a SIMULATION or a production call (POST_CALL)."""


class DataProject(BaseModel):
    amount_usd: float = FieldInfo(alias="amountUsd")
    """
    The same billable spend in US dollars. For display; use amountUsdMicros to
    reconcile.
    """

    amount_usd_micros: int = FieldInfo(alias="amountUsdMicros")
    """Billable spend in integer micro-dollars (1,000,000 = $1). The exact value."""

    breakdown: List[DataProjectBreakdown]
    """This project's spend split by cost type, highest first. Sums to amountUsdMicros."""

    project_id: str = FieldInfo(alias="projectId")

    project_name: Optional[str] = FieldInfo(alias="projectName")
    """Null only if the project no longer exists in this organization."""


class Data(BaseModel):
    currency: Literal["usd"]

    from_: str = FieldInfo(alias="from")
    """The resolved window start, echoed back as ISO 8601."""

    projects: List[DataProject]
    """
    Per-project billable spend, highest first. Only projects with spend in the
    window appear.
    """

    to: str
    """The resolved window end, echoed back as ISO 8601."""

    total_usd: float = FieldInfo(alias="totalUsd")
    """The same total in US dollars."""

    total_usd_micros: int = FieldInfo(alias="totalUsdMicros")
    """
    Total billable spend across the organization (or the single project) in
    micro-dollars.
    """


class UsageGetResponse(BaseModel):
    data: Data
