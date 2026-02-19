# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SimulationScenarioUpdateParams",
    "StepChange",
    "StepChangeCreateStepChange",
    "StepChangeUpdateStepChange",
    "StepChangeDeleteStepChange",
]


class SimulationScenarioUpdateParams(TypedDict, total=False):
    step_changes: Required[Annotated[Iterable[StepChange], PropertyInfo(alias="stepChanges")]]
    """List of step changes to apply to the scenario"""

    name: str
    """New name for the scenario (updates the START node content)"""


class StepChangeCreateStepChange(TypedDict, total=False):
    """Create a new step in the scenario"""

    action: Required[Literal["create"]]
    """Create a new step"""

    content: Required[str]
    """The content/text of the new step"""

    type: Required[Literal["AGENT_TURN", "CUSTOMER_TURN", "CUSTOMER_FIRST_MESSAGE", "CUSTOMER_SILENCE", "VOICEMAIL"]]
    """The type of the new step"""


class StepChangeUpdateStepChange(TypedDict, total=False):
    """Update an existing step in the scenario"""

    action: Required[Literal["update"]]
    """Update an existing step"""

    node_id: Required[Annotated[str, PropertyInfo(alias="nodeId")]]
    """The ID of the step node to update"""

    content: str
    """The new content/text of the step (optional)"""

    type: Literal["AGENT_TURN", "CUSTOMER_TURN", "CUSTOMER_FIRST_MESSAGE", "CUSTOMER_SILENCE", "VOICEMAIL"]
    """The new type of the step (optional)"""


class StepChangeDeleteStepChange(TypedDict, total=False):
    """Delete a step from the scenario"""

    action: Required[Literal["delete"]]
    """Delete an existing step"""

    node_id: Required[Annotated[str, PropertyInfo(alias="nodeId")]]
    """The ID of the step node to delete"""


StepChange: TypeAlias = Union[StepChangeCreateStepChange, StepChangeUpdateStepChange, StepChangeDeleteStepChange]
