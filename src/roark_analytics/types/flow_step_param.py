# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["FlowStepParam"]


class FlowStepParam(TypedDict, total=False):
    """One step in a scripted flow's conversation.

    `nodeId` is the identity contract: include it to update the existing step, omit it to create a new one.
    A step continues into `steps` (more than one child is a branch point) and/or `mergeIntoNodeIds`, which
    names steps elsewhere in the same request that this step rejoins. Branches that come back together are
    represented that way rather than by repeating the shared step, so reading a flow, editing it and writing
    it back preserves it exactly.

    A merge target is named by its `nodeId` when it already exists, or by `ref` when it is being created in
    the same request. `ref` is a label you choose, it is request-local, and it is never stored or returned.
    Put the shared step inline under the first branch that reaches it and point the others at it: a top-level
    step is a root wired straight from the start of the flow, so a merge target parked there would also be
    reachable directly.
    """

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

    content: Optional[str]

    dtmf_digits: Annotated[Optional[str], PropertyInfo(alias="dtmfDigits")]

    linked_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="linkedCustomerFlowId")]

    linked_customer_flow_variant_id: Annotated[Optional[str], PropertyInfo(alias="linkedCustomerFlowVariantId")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    silence_duration_seconds: Annotated[Optional[int], PropertyInfo(alias="silenceDurationSeconds")]

    steps: Iterable["FlowStepParam"]
