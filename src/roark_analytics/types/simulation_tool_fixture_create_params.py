# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationToolFixtureCreateParams"]


class SimulationToolFixtureCreateParams(TypedDict, total=False):
    tool_name: Required[Annotated[str, PropertyInfo(alias="toolName")]]
    """The tool this fixture answers for."""

    customer_flow_variant_id: Annotated[str, PropertyInfo(alias="customerFlowVariantId")]
    """
    Pin the fixture to one flow variant (scenario). Omit for a project-wide fixture.
    A variant-pinned fixture beats the project-wide one.
    """

    description: str
    """Why this fixture exists."""

    enabled: bool
    """Defaults to true."""

    response: object
    """The exact JSON to return."""
