# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FlowStep"]


class FlowStep(BaseModel):
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

    type: Literal[
        "AGENT_TURN",
        "CUSTOMER_TURN",
        "CUSTOMER_FIRST_MESSAGE",
        "CUSTOMER_SILENCE",
        "CUSTOMER_DTMF",
        "VOICEMAIL",
        "SCENARIO_LINK",
    ]

    content: Optional[str] = None

    dtmf_digits: Optional[str] = FieldInfo(alias="dtmfDigits", default=None)

    linked_customer_flow_id: Optional[str] = FieldInfo(alias="linkedCustomerFlowId", default=None)

    linked_customer_flow_variant_id: Optional[str] = FieldInfo(alias="linkedCustomerFlowVariantId", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    silence_duration_seconds: Optional[int] = FieldInfo(alias="silenceDurationSeconds", default=None)

    steps: Optional[List["FlowStep"]] = None
