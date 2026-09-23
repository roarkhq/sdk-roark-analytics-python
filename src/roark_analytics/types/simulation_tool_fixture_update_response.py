# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimulationToolFixtureUpdateResponse", "Data"]


class Data(BaseModel):
    """
    A deterministic tool response for Roark test calls: where the scenario-aware
    model makes mocked tools plausible, a fixture makes one exact, so a simulation
    can force the branch under test. Never applies to real callers.
    """

    id: str

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601."""

    customer_flow_variant_id: Optional[str] = FieldInfo(alias="customerFlowVariantId")
    """The flow variant this fixture is pinned to. Null = project-wide."""

    description: Optional[str]
    """Why this fixture exists."""

    enabled: bool

    tool_name: str = FieldInfo(alias="toolName")

    updated_at: str = FieldInfo(alias="updatedAt")
    """ISO 8601."""

    response: Optional[object] = None
    """The exact JSON the tool returns during Roark test calls."""


class SimulationToolFixtureUpdateResponse(BaseModel):
    data: Data
    """
    A deterministic tool response for Roark test calls: where the scenario-aware
    model makes mocked tools plausible, a fixture makes one exact, so a simulation
    can force the branch under test. Never applies to real callers.
    """
