# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

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

    type: Required[
        Literal[
            "AGENT_TURN",
            "CUSTOMER_TURN",
            "CUSTOMER_FIRST_MESSAGE",
            "CUSTOMER_SILENCE",
            "CUSTOMER_DTMF",
            "VOICEMAIL",
            "SCENARIO_LINK",
        ]
    ]
    """The type of this step"""

    dtmf_digits: Annotated[str, PropertyInfo(alias="dtmfDigits")]
    """DTMF digits to send (for CUSTOMER_DTMF type steps, e.g.

    1w2w3#). Valid characters: 0-9, \\**, #, w/W for pauses.
    """

    linked_scenario_id: Annotated[str, PropertyInfo(alias="linkedScenarioId")]
    """ID of the scenario to link to (required for SCENARIO_LINK type steps)"""

    silence_duration_seconds: Annotated[int, PropertyInfo(alias="silenceDurationSeconds")]
    """Duration of silence in seconds (for CUSTOMER_SILENCE type steps)"""
