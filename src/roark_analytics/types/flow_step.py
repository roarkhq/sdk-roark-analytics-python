# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FlowStep",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
    "UnionMember5",
    "UnionMember6",
]


class UnionMember0(BaseModel):
    type: Literal["AGENT_TURN"]

    content: Optional[str] = None

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class UnionMember1(BaseModel):
    type: Literal["CUSTOMER_TURN"]

    content: Optional[str] = None

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class UnionMember2(BaseModel):
    type: Literal["CUSTOMER_FIRST_MESSAGE"]

    content: Optional[str] = None

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class UnionMember3(BaseModel):
    type: Literal["CUSTOMER_SILENCE"]

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    silence_duration_seconds: Optional[int] = FieldInfo(alias="silenceDurationSeconds", default=None)

    steps: Optional[List["FlowStep"]] = None


class UnionMember4(BaseModel):
    type: Literal["CUSTOMER_DTMF"]

    dtmf_digits: Optional[str] = FieldInfo(alias="dtmfDigits", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class UnionMember5(BaseModel):
    type: Literal["VOICEMAIL"]

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


class UnionMember6(BaseModel):
    type: Literal["SCENARIO_LINK"]

    linked_customer_flow_id: Optional[str] = FieldInfo(alias="linkedCustomerFlowId", default=None)

    linked_customer_flow_variant_id: Optional[str] = FieldInfo(alias="linkedCustomerFlowVariantId", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    steps: Optional[List["FlowStep"]] = None


FlowStep: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6
]
