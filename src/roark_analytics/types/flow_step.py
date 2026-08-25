# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FlowStep",
    "FlowStepUnionMember0",
    "FlowStepUnionMember1",
    "FlowStepUnionMember2",
    "FlowStepUnionMember3",
    "FlowStepUnionMember4",
    "FlowStepUnionMember5",
    "FlowStepUnionMember6",
]


class FlowStepUnionMember0(BaseModel):
    type: Literal["AGENT_TURN"]

    content: Optional[str] = None

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember1(BaseModel):
    type: Literal["CUSTOMER_TURN"]

    content: Optional[str] = None

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember2(BaseModel):
    type: Literal["CUSTOMER_FIRST_MESSAGE"]

    content: Optional[str] = None

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember3(BaseModel):
    type: Literal["CUSTOMER_SILENCE"]

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    silence_duration_seconds: Optional[int] = FieldInfo(alias="silenceDurationSeconds", default=None)

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember4(BaseModel):
    type: Literal["CUSTOMER_DTMF"]

    dtmf_digits: Optional[str] = FieldInfo(alias="dtmfDigits", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember5(BaseModel):
    type: Literal["VOICEMAIL"]

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember6(BaseModel):
    type: Literal["SCENARIO_LINK"]

    linked_customer_flow_id: Optional[str] = FieldInfo(alias="linkedCustomerFlowId", default=None)

    linked_customer_flow_variant_id: Optional[str] = FieldInfo(alias="linkedCustomerFlowVariantId", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


FlowStep: TypeAlias = Union[
    FlowStepUnionMember0,
    FlowStepUnionMember1,
    FlowStepUnionMember2,
    FlowStepUnionMember3,
    FlowStepUnionMember4,
    FlowStepUnionMember5,
    FlowStepUnionMember6,
]
