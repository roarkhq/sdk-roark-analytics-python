# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationCustomerFlowReplaceStepsParams"]


class SimulationCustomerFlowReplaceStepsParams(TypedDict, total=False):
    steps: Required[Iterable["FlowStepParam"]]
    """The complete set of steps.

    This replaces the flow's existing steps rather than merging into them.
    """

    allow_unmerge: Annotated[bool, PropertyInfo(alias="allowUnmerge")]
    """Confirms a write that drops branches which currently rejoin.

    Only needed when the request omits mergeIntoNodeIds references the flow already
    had; a faithful round trip never needs it.
    """


from .flow_step_param import FlowStepParam
