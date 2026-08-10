# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanJobStartParams", "FlowVariable", "VariablesUnionMember1"]


class SimulationRunPlanJobStartParams(TypedDict, total=False):
    flow_variables: Annotated[Iterable[FlowVariable], PropertyInfo(alias="flowVariables")]
    """
    Runtime variable overrides targeted at the plan’s customer flows, taking
    precedence over the values pinned on the flow attachment.

    An entry without `variantId` applies to every variant the attachment resolves. A
    flow that is not attached to this plan, or a variant that does not belong to the
    flow, is rejected rather than ignored.
    """

    variables: Union[Dict[str, str], Iterable[VariablesUnionMember1]]
    """Runtime variables that override the values defined on the plan.

    Accepts one of two formats:

    Option 1, global (a flat key-value object): { "orderNumber": "12345",
    "environment": "staging" }

    Option 2, per-scenario (an array of objects with scenarioId + variables): [ {
    "scenarioId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
    "scenarioId": "7a3d2e1f-...", "variables": { "orderNumber": "67890" } } ]

    On a flow-based plan the global format applies to every variant the run
    resolves. The per-scenario format targets scenarios, so use `flowVariables` to
    override a specific flow or variant instead.
    """


class FlowVariable(TypedDict, total=False):
    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]
    """ID of a customer flow attached to this plan"""

    variables: Required[Dict[str, str]]
    """Key-value pairs to apply"""

    variant_id: Annotated[str, PropertyInfo(alias="variantId")]
    """Target a single variant.

    Omit to apply to every variant this plan runs for the flow.
    """


class VariablesUnionMember1(TypedDict, total=False):
    scenario_id: Required[Annotated[str, PropertyInfo(alias="scenarioId")]]
    """ID of the scenario to apply variables to"""

    variables: Required[Dict[str, str]]
    """Key-value pairs for this scenario"""
