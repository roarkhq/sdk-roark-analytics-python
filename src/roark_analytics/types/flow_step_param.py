# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "FlowStepParam",
    "FlowStepParamUnionMember0",
    "FlowStepParamUnionMember1",
    "FlowStepParamUnionMember2",
    "FlowStepParamUnionMember3",
    "FlowStepParamUnionMember4",
    "FlowStepParamUnionMember5",
    "FlowStepParamUnionMember6",
    "FlowStepParamUnionMember7",
]


class FlowStepParamUnionMember0(TypedDict, total=False):
    type: Required[Literal["AGENT_TURN"]]

    content: Optional[str]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember1(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_TURN"]]

    content: Optional[str]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember2(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_FIRST_MESSAGE"]]

    content: Optional[str]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember3(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_SILENCE"]]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    silence_duration_seconds: Annotated[Optional[int], PropertyInfo(alias="silenceDurationSeconds")]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember4(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_DTMF"]]

    dtmf_digits: Annotated[Optional[str], PropertyInfo(alias="dtmfDigits")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember5(TypedDict, total=False):
    type: Required[Literal["AGENT_DTMF"]]

    dtmf_digits: Annotated[Optional[str], PropertyInfo(alias="dtmfDigits")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember6(TypedDict, total=False):
    type: Required[Literal["VOICEMAIL"]]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember7(TypedDict, total=False):
    type: Required[Literal["SCENARIO_LINK"]]

    linked_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="linkedCustomerFlowId")]

    linked_customer_flow_variant_id: Annotated[Optional[str], PropertyInfo(alias="linkedCustomerFlowVariantId")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    steps: List["FlowStepParam"]


FlowStepParam: TypeAlias = Union[
    FlowStepParamUnionMember0,
    FlowStepParamUnionMember1,
    FlowStepParamUnionMember2,
    FlowStepParamUnionMember3,
    FlowStepParamUnionMember4,
    FlowStepParamUnionMember5,
    FlowStepParamUnionMember6,
    FlowStepParamUnionMember7,
]
