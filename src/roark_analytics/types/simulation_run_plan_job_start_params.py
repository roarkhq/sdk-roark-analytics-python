# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanJobStartParams", "VariablesUnionMember1"]


class SimulationRunPlanJobStartParams(TypedDict, total=False):
    variables: Union[Dict[str, str], Iterable[VariablesUnionMember1]]
    """Runtime variables that override plan-defined scenario variables.

    Accepts one of two formats:

    Option 1 — Global (flat key-value object, applies to ALL scenarios): {
    "orderNumber": "12345", "environment": "staging" }

    Option 2 — Per-scenario (array of objects with scenarioId + variables): [ {
    "scenarioId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
    "scenarioId": "7a3d2e1f-...", "variables": { "orderNumber": "67890" } } ]
    """


class VariablesUnionMember1(TypedDict, total=False):
    scenario_id: Required[Annotated[str, PropertyInfo(alias="scenarioId")]]
    """ID of the scenario to apply variables to"""

    variables: Required[Dict[str, str]]
    """Key-value pairs for this scenario"""
