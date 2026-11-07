# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FlowStep",
    "FlowStepUnionMember0",
    "FlowStepUnionMember0OffScriptPolicy",
    "FlowStepUnionMember0Stage",
    "FlowStepUnionMember1",
    "FlowStepUnionMember10",
    "FlowStepUnionMember2",
    "FlowStepUnionMember3",
    "FlowStepUnionMember4",
    "FlowStepUnionMember5",
    "FlowStepUnionMember6",
    "FlowStepUnionMember7",
    "FlowStepUnionMember8",
    "FlowStepUnionMember9",
]


class FlowStepUnionMember0OffScriptPolicy(BaseModel):
    max_attempts: int = FieldInfo(alias="maxAttempts")

    reaction: Literal["STAY_SILENT", "REPEAT", "RESPOND", "SAY"]

    then: Literal["HANG_UP", "MOVE_ON", "ADAPT", "HANG_UP_INVALIDATE"]

    say_line: Optional[str] = FieldInfo(alias="sayLine", default=None)

    wait_seconds: Optional[int] = FieldInfo(alias="waitSeconds", default=None)


class FlowStepUnionMember0Stage(BaseModel):
    name: str

    analyze: Optional[bool] = None

    required: Optional[bool] = None


class FlowStepUnionMember0(BaseModel):
    type: Literal["AGENT_TURN"]

    content: Optional[str] = None

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    off_script_policy: Optional[FlowStepUnionMember0OffScriptPolicy] = FieldInfo(alias="offScriptPolicy", default=None)

    ref: Optional[str] = None

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember1(BaseModel):
    type: Literal["CUSTOMER_TURN"]

    content: Optional[str] = None

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember2(BaseModel):
    type: Literal["CUSTOMER_FIRST_MESSAGE"]

    content: Optional[str] = None

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember3(BaseModel):
    type: Literal["CUSTOMER_VERBATIM_TURN"]

    content: Optional[str] = None

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember4(BaseModel):
    type: Literal["CUSTOMER_SILENCE"]

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    silence_duration_seconds: Optional[int] = FieldInfo(alias="silenceDurationSeconds", default=None)

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember5(BaseModel):
    type: Literal["CUSTOMER_AUDIO"]

    audio_clip: Optional[
        Literal[
            "HOLD_MUSIC_CLASSICAL_PIANO",
            "HOLD_MUSIC_CLASSICAL_ORCHESTRA",
            "HOLD_MUSIC_STRING_QUARTET",
            "HOLD_MUSIC_AMBIENT",
            "HOLD_MUSIC_SMOOTH_JAZZ",
            "HOLD_MUSIC_SOFT_SYNTH",
            "HOLD_BEEP",
            "RINGBACK_US",
            "RINGBACK_UK",
        ]
    ] = FieldInfo(alias="audioClip", default=None)

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    silence_duration_seconds: Optional[int] = FieldInfo(alias="silenceDurationSeconds", default=None)

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember6(BaseModel):
    type: Literal["CUSTOMER_DTMF"]

    dtmf_digits: Optional[str] = FieldInfo(alias="dtmfDigits", default=None)

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember7(BaseModel):
    type: Literal["AGENT_DTMF"]

    dtmf_digits: Optional[str] = FieldInfo(alias="dtmfDigits", default=None)

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    off_script_policy: Optional[FlowStepUnionMember0OffScriptPolicy] = FieldInfo(alias="offScriptPolicy", default=None)

    ref: Optional[str] = None

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember8(BaseModel):
    type: Literal["VOICEMAIL"]

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember9(BaseModel):
    type: Literal["CUSTOMER_HANDOFF"]

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    handoff_persona_id: Optional[str] = FieldInfo(alias="handoffPersonaId", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


class FlowStepUnionMember10(BaseModel):
    type: Literal["SCENARIO_LINK"]

    ends_call: Optional[bool] = FieldInfo(alias="endsCall", default=None)

    linked_customer_flow_id: Optional[str] = FieldInfo(alias="linkedCustomerFlowId", default=None)

    linked_customer_flow_variant_id: Optional[str] = FieldInfo(alias="linkedCustomerFlowVariantId", default=None)

    merge_into_node_ids: Optional[List[str]] = FieldInfo(alias="mergeIntoNodeIds", default=None)

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    ref: Optional[str] = None

    stage: Optional[FlowStepUnionMember0Stage] = None

    steps: Optional[List["FlowStep"]] = None


FlowStep: TypeAlias = Union[
    FlowStepUnionMember0,
    FlowStepUnionMember1,
    FlowStepUnionMember2,
    FlowStepUnionMember3,
    FlowStepUnionMember4,
    FlowStepUnionMember5,
    FlowStepUnionMember6,
    FlowStepUnionMember7,
    FlowStepUnionMember8,
    FlowStepUnionMember9,
    FlowStepUnionMember10,
]
