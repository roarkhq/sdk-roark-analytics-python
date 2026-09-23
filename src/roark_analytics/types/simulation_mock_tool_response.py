# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationMockToolResponse", "Data"]


class Data(BaseModel):
    """
    A simulated backend response for a guarded tool during a Roark test call. The
    real tool was not, and must not be, executed.
    """

    reused: bool
    """
    True when this exact invocation (same tool, same arguments) was answered moments
    ago and the stored response was returned, e.g. on a retry.
    """

    simulation_job_id: str = FieldInfo(alias="simulationJobId")

    source: Literal["GENERATED", "FIXTURE"]
    """
    GENERATED = the scenario-aware model answered; FIXTURE = a pinned deterministic
    response you configured answered.
    """

    tool_name: str = FieldInfo(alias="toolName")

    result: Optional[object] = None
    """
    The simulated tool response: valid JSON, shaped by the tool contract, consistent
    with the test scenario and with earlier mocked responses in the same call.
    Return this from your tool instead of executing it.
    """


class SimulationMockToolResponse(BaseModel):
    data: Data
    """
    A simulated backend response for a guarded tool during a Roark test call. The
    real tool was not, and must not be, executed.
    """
