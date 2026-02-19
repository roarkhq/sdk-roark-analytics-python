# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SimulationScenarioCreateParams", "Step"]


class SimulationScenarioCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the scenario (used as the START node content)"""

    steps: Required[Iterable[Step]]
    """Ordered list of steps for the scenario (at least one step is required)"""


class Step(TypedDict, total=False):
    """A step to include when creating a scenario"""

    content: Required[str]
    """The content/text of the step"""

    type: Required[Literal["AGENT_TURN", "CUSTOMER_TURN", "CUSTOMER_FIRST_MESSAGE", "CUSTOMER_SILENCE", "VOICEMAIL"]]
    """The type of this step"""
