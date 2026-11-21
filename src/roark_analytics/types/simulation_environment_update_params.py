# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationEnvironmentUpdateParams", "LineCustom", "LineCustomFromAgent"]


class LineCustomFromAgent(TypedDict, total=False):
    packet_loss_percent: Required[Annotated[float, PropertyInfo(alias="packetLossPercent")]]
    """Share of packets lost, 0 to 20 in steps of 0.5."""

    mean_burst_packets: Annotated[int, PropertyInfo(alias="meanBurstPackets")]
    """Mean length of a loss gap in 20 ms packets, 2 to 10. Omit for random loss."""


class LineCustom(TypedDict, total=False):
    """The per-direction loss of a CUSTOM line."""

    from_agent: Annotated[LineCustomFromAgent, PropertyInfo(alias="fromAgent")]
    """
    The agent's audio on its way to the caller: what the caller hears. Omit for no
    loss.
    """

    to_agent: Annotated[LineCustomFromAgent, PropertyInfo(alias="toAgent")]
    """
    The caller's audio on its way to the agent: what the agent hears. Omit for no
    loss.
    """


class SimulationEnvironmentUpdateParams(TypedDict, total=False):
    background_noise: Annotated[
        Literal[
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
        ],
        PropertyInfo(alias="backgroundNoise"),
    ]
    """The noise bed played underneath the simulated caller. NONE plays nothing."""

    background_noise_volume: Annotated[float, PropertyInfo(alias="backgroundNoiseVolume")]
    """
    How loud the bed plays, as a gain from 0 (silent) to 1 (as loud as the caller).
    Defaults to 0.1, which sits well under the caller. Ignored on Vapi endpoints,
    which have no level control.
    """

    description: Optional[str]
    """Optional note on when to use this environment"""

    line_custom: Annotated[Optional[LineCustom], PropertyInfo(alias="lineCustom")]
    """Required with lineQuality CUSTOM, and refused with any other line."""

    line_quality: Annotated[
        Literal["CLEAR", "MINOR_LOSS", "CELL_EDGE", "POOR_CONNECTION", "ONE_WAY_DEGRADED", "CUSTOM"],
        PropertyInfo(alias="lineQuality"),
    ]
    """
    The phone line the simulated caller is on: packet loss applied to its 20 ms
    audio packets, per direction. The loss pattern is seeded per call, so a redial
    loses the same packets. CLEAR: No loss. MINOR_LOSS: 1% random, both ways.
    CELL_EDGE: 5% in 80 ms gaps, both ways. POOR_CONNECTION: 10% in 120 ms gaps,
    both ways. ONE_WAY_DEGRADED: 8% in 80 ms gaps, toward the agent only. CUSTOM:
    the per-direction loss in `lineCustom`, up to 20% in 0.5 steps, with a mean
    burst of up to 10 packets (omit it for random loss). Defaults to CLEAR.
    """

    name: str
    """Display name, shown wherever a flow variant references the environment"""
