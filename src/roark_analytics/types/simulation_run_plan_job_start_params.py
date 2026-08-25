# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanJobStartParams", "VariableUnionMember1", "VariableUnionMember2"]


class VariableUnionMember1(TypedDict, total=False):
    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]
    """A customer flow this plan runs."""

    variables: Required[Dict[str, str]]
    """The values to apply."""

    edge_case_id: Annotated[str, PropertyInfo(alias="edgeCaseId")]
    """Narrow to one edge case of that flow."""

    happy_path: Annotated[Literal[True], PropertyInfo(alias="happyPath")]
    """Narrow to the flow's happy path."""


class VariableUnionMember2(TypedDict, total=False):
    scenario_id: Required[Annotated[str, PropertyInfo(alias="scenarioId")]]
    """ID of the scenario to apply variables to"""

    variables: Required[Dict[str, str]]
    """Key-value pairs for this scenario"""


class SimulationRunPlanJobStartParams(TypedDict, total=False):
    variables: Union[Dict[str, str], Iterable[VariableUnionMember1], Iterable[VariableUnionMember2]]
    """
    Values for the {{variables}} the run resolves, overriding whatever the plan has
    pinned.
    An object applies them to the whole run:
    { "orderNumber": "12345", "tier": "gold" }
    An array applies them per flow, or to just its happy path or one of its edge
    cases, when a single set will not do. Each entry carries what it applies to:
    [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
    "flowId": "550e8400-...", "happyPath": true, "variables": { "orderNumber":
    "55555" } }, { "flowId": "550e8400-...", "edgeCaseId": "7a3d2e1f-...",
    "variables": { "orderNumber": "67890" } } ]
    An entry that narrows to neither covers everything that flow resolves. A flow
    this plan does not attach, or an edge case that does not belong to the flow, is
    rejected rather than ignored.
    A plan built on scenarios rather than customer flows targets them the same way,
    with `scenarioId` in place of `flowId`. That form is deprecated alongside
    scenarios themselves, and still accepted so runs against those plans keep
    working.
    """
