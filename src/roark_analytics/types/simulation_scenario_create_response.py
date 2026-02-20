# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationScenarioCreateResponse", "Data", "DataStep"]


class DataStep(BaseModel):
    content: Optional[str] = None
    """Content/text of the step"""

    node_id: str = FieldInfo(alias="nodeId")
    """Unique identifier of the step node (use this for update/delete operations)"""

    type: Literal[
        "START",
        "AGENT_TURN",
        "CUSTOMER_TURN",
        "CUSTOMER_FIRST_MESSAGE",
        "CUSTOMER_SILENCE",
        "CUSTOMER_DTMF",
        "VOICEMAIL",
    ]
    """Type of step in the scenario"""

    dtmf_digits: Optional[str] = FieldInfo(alias="dtmfDigits", default=None)
    """DTMF digits to send during this step (e.g.

    1w2w3#). Valid characters: 0-9, \\**, #, w/W for pauses.
    """


class Data(BaseModel):
    id: str
    """Unique identifier of the scenario"""

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    description: Optional[str] = None
    """Description of the scenario"""

    name: Optional[str] = None
    """Name of the scenario (from the start node content)"""

    steps: List[DataStep]
    """Ordered list of steps in the scenario (excludes the START node)"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class SimulationScenarioCreateResponse(BaseModel):
    data: Data
