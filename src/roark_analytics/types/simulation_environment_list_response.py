# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationEnvironmentListResponse", "Data", "DataLineCustom", "DataLineCustomFromAgent", "Pagination"]


class DataLineCustomFromAgent(BaseModel):
    packet_loss_percent: float = FieldInfo(alias="packetLossPercent")
    """Share of packets lost, 0 to 20 in steps of 0.5."""

    mean_burst_packets: Optional[int] = FieldInfo(alias="meanBurstPackets", default=None)
    """Mean length of a loss gap in 20 ms packets, 2 to 10. Omit for random loss."""


class DataLineCustom(BaseModel):
    """The per-direction loss of a CUSTOM line."""

    from_agent: Optional[DataLineCustomFromAgent] = FieldInfo(alias="fromAgent", default=None)
    """
    The agent's audio on its way to the caller: what the caller hears. Omit for no
    loss.
    """

    to_agent: Optional[DataLineCustomFromAgent] = FieldInfo(alias="toAgent", default=None)
    """
    The caller's audio on its way to the agent: what the agent hears. Omit for no
    loss.
    """


class Data(BaseModel):
    """
    A simulation environment: the ambient conditions a customer flow variant runs
    under. The list includes both your own and the ones Roark curates for every
    project.
    """

    id: str

    background_noise: Literal[
        "NONE",
        "AIRPORT",
        "CHILDREN_PLAYING",
        "CITY",
        "COFFEE_SHOP",
        "CONSTRUCTION",
        "CRYING_BABY",
        "DRIVING",
        "LIBRARY",
        "OFFICE",
        "THUNDERSTORM",
        "TRAIN",
    ] = FieldInfo(alias="backgroundNoise")

    background_noise_volume: float = FieldInfo(alias="backgroundNoiseVolume")

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    line_custom: Optional[DataLineCustom] = FieldInfo(alias="lineCustom")
    """The loss of a CUSTOM line; null on every other."""

    line_noise: float = FieldInfo(alias="lineNoise")
    """
    Hiss on the line, both ways, from 0 (none) to 1 (heavy, about 10 dB under phone
    speech). Combines with the phone and lineQuality.
    """

    line_quality: Literal["CLEAR", "MINOR_LOSS", "CELL_EDGE", "POOR_CONNECTION", "ONE_WAY_DEGRADED", "CUSTOM"] = (
        FieldInfo(alias="lineQuality")
    )
    """
    The phone line the simulated caller is on: packet loss applied to its 20 ms
    audio packets, per direction. The loss pattern is seeded per call, so a redial
    loses the same packets. CLEAR: No loss. MINOR_LOSS: 1% random, both ways.
    CELL_EDGE: 5% in 80 ms gaps, both ways. POOR_CONNECTION: 10% in 120 ms gaps,
    both ways. ONE_WAY_DEGRADED: 8% in 80 ms gaps, toward the agent only. CUSTOM:
    the per-direction loss in `lineCustom`, up to 20% in 0.5 steps, with a mean
    burst of up to 10 packets (omit it for random loss).
    """

    name: str

    phone: Optional[Literal["LANDLINE", "MOBILE", "BLUETOOTH"]]
    """
    The phone the simulated caller is on: the codecs the call passes through, both
    ways, on top of any loss in lineQuality. Null is no phone. LANDLINE: The narrow
    band of a phone handset and the codec of the phone network. MOBILE: The narrow
    band and the compressed voice codec of a mobile call. BLUETOOTH: A mobile on a
    car kit or headset: the Bluetooth link adds fizz under the voice, then the
    mobile codec.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""

    description: Optional[str] = None


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """Whether there are more items to fetch"""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor")
    """Cursor for the next page of items"""

    total: float
    """Total number of items"""


class SimulationEnvironmentListResponse(BaseModel):
    """
    Paginated list of environments: the project's own plus the shared Roark-curated
    ones
    """

    data: List[Data]

    pagination: Pagination
