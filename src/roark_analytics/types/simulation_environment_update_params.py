# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationEnvironmentUpdateParams"]


class SimulationEnvironmentUpdateParams(TypedDict, total=False):
    background_noise: Annotated[
        Literal["NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"],
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

    name: str
    """Display name, shown wherever a flow variant references the environment"""
