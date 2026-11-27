# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerFlowEdgeCaseUpdateParams", "AdditionalExpectation"]


class AdditionalExpectation(TypedDict, total=False):
    prompt: Required[str]
    """What the agent under test is graded against."""


class CustomerFlowEdgeCaseUpdateParams(TypedDict, total=False):
    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]

    additional_expectations: Annotated[Iterable[AdditionalExpectation], PropertyInfo(alias="additionalExpectations")]
    """
    The expectations graded on this variant only, on top of the flow's own. Sent as
    the complete set: it replaces whatever the variant had, so omit it to leave the
    set alone and send [] to clear it. Improv flows only: a scripted variant's
    expectations come from the agent turns on its path and are rewritten on every
    graph edit.
    """

    environment_id: Annotated[Optional[str], PropertyInfo(alias="environmentId")]

    hold_instructions: Annotated[Optional[str], PropertyInfo(alias="holdInstructions")]
    """
    CUSTOM only: when the simulated customer waits quietly, written as instructions
    it follows. It stays silent until the agent speaks again or the longest wait
    runs out, then takes the turn back. Required when holdMode is CUSTOM. Up to 4000
    characters.
    """

    hold_max_seconds: Annotated[Optional[int], PropertyInfo(alias="holdMaxSeconds")]
    """
    The longest one wait on hold can run, in seconds, from 5 to 600. When it runs
    out the simulated customer takes the turn back. Null uses the default, 180.
    Ignored when holdMode is NEVER.
    """

    hold_mode: Annotated[Optional[Literal["DEFAULT", "CUSTOM", "NEVER"]], PropertyInfo(alias="holdMode")]
    """
    How the simulated customer waits quietly on hold while your agent is busy.
    DEFAULT follows Roark's built-in rules: wait when the agent asks for a moment
    ("bear with me", "let me pull that up"), and never in place of answering a
    question. CUSTOM follows holdInstructions. NEVER means this customer never
    holds. Null on an edge case uses the happy path's mode, instructions and longest
    wait together; null on the happy path is DEFAULT. Applies to improv variants and
    to the improvised turns of scripted ones.
    """

    include_flow_expectations: Annotated[bool, PropertyInfo(alias="includeFlowExpectations")]
    """
    Whether this edge case is graded on the flow's agentExpectations as well as its
    own additionalExpectations. Defaults to true; false grades it on its
    additionalExpectations only.
    """

    opening_line: Annotated[Optional[str], PropertyInfo(alias="openingLine")]

    persona_override_id: Annotated[Optional[str], PropertyInfo(alias="personaOverrideId")]
    """The persona this runs as. Null on an edge case inherits the happy path's."""

    preceded_by_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="precededByCustomerFlowId")]

    preceded_by_customer_flow_variant_id: Annotated[
        Optional[str], PropertyInfo(alias="precededByCustomerFlowVariantId")
    ]

    prompt: Optional[str]
    """
    Improv flows only. The brief the simulated customer improvises from. Caller cues
    steer the caller from that point in the brief: `#{emotion:<emotion>}`,
    `#{language:<ISO 639-1 code>}`, `#{noise:<environmentId>}`, and `#{interrupt}`,
    whose sentence says when to cut in on your agent. Cues are voice only. See
    "Caller cues" in the customer flows concept.
    """

    title: str
