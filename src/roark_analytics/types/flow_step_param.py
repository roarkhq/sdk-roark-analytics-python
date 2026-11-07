# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "FlowStepParam",
    "FlowStepParamUnionMember0",
    "FlowStepParamUnionMember0OffScriptPolicy",
    "FlowStepParamUnionMember0Stage",
    "FlowStepParamUnionMember1",
    "FlowStepParamUnionMember10",
    "FlowStepParamUnionMember2",
    "FlowStepParamUnionMember3",
    "FlowStepParamUnionMember4",
    "FlowStepParamUnionMember5",
    "FlowStepParamUnionMember6",
    "FlowStepParamUnionMember7",
    "FlowStepParamUnionMember8",
    "FlowStepParamUnionMember9",
]


class FlowStepParamUnionMember0OffScriptPolicy(TypedDict, total=False):
    max_attempts: Required[Annotated[int, PropertyInfo(alias="maxAttempts")]]

    reaction: Required[Literal["STAY_SILENT", "REPEAT", "RESPOND", "SAY"]]

    then: Required[Literal["HANG_UP", "MOVE_ON", "ADAPT", "HANG_UP_INVALIDATE"]]

    say_line: Annotated[Optional[str], PropertyInfo(alias="sayLine")]

    wait_seconds: Annotated[Optional[int], PropertyInfo(alias="waitSeconds")]


class FlowStepParamUnionMember0Stage(TypedDict, total=False):
    name: Required[str]

    analyze: bool

    required: bool


class FlowStepParamUnionMember0(TypedDict, total=False):
    type: Required[Literal["AGENT_TURN"]]

    content: Optional[str]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    off_script_policy: Annotated[
        Optional[FlowStepParamUnionMember0OffScriptPolicy], PropertyInfo(alias="offScriptPolicy")
    ]

    ref: str

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember1(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_TURN"]]

    content: Optional[str]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember2(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_FIRST_MESSAGE"]]

    content: Optional[str]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember3(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_VERBATIM_TURN"]]

    content: Optional[str]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember4(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_SILENCE"]]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    silence_duration_seconds: Annotated[Optional[int], PropertyInfo(alias="silenceDurationSeconds")]

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember5(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_AUDIO"]]

    audio_clip: Annotated[
        Optional[
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
        ],
        PropertyInfo(alias="audioClip"),
    ]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    silence_duration_seconds: Annotated[Optional[int], PropertyInfo(alias="silenceDurationSeconds")]

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember6(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_DTMF"]]

    dtmf_digits: Annotated[Optional[str], PropertyInfo(alias="dtmfDigits")]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember7(TypedDict, total=False):
    type: Required[Literal["AGENT_DTMF"]]

    dtmf_digits: Annotated[Optional[str], PropertyInfo(alias="dtmfDigits")]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    off_script_policy: Annotated[
        Optional[FlowStepParamUnionMember0OffScriptPolicy], PropertyInfo(alias="offScriptPolicy")
    ]

    ref: str

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember8(TypedDict, total=False):
    type: Required[Literal["VOICEMAIL"]]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember9(TypedDict, total=False):
    type: Required[Literal["CUSTOMER_HANDOFF"]]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    handoff_persona_id: Annotated[Optional[str], PropertyInfo(alias="handoffPersonaId")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    stage: Optional[FlowStepParamUnionMember0Stage]

    steps: List["FlowStepParam"]


class FlowStepParamUnionMember10(TypedDict, total=False):
    type: Required[Literal["SCENARIO_LINK"]]

    ends_call: Annotated[bool, PropertyInfo(alias="endsCall")]

    linked_customer_flow_id: Annotated[Optional[str], PropertyInfo(alias="linkedCustomerFlowId")]

    linked_customer_flow_variant_id: Annotated[Optional[str], PropertyInfo(alias="linkedCustomerFlowVariantId")]

    merge_into_node_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergeIntoNodeIds")]

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    ref: str

    stage: Optional[FlowStepParamUnionMember0Stage]

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
    FlowStepParamUnionMember8,
    FlowStepParamUnionMember9,
    FlowStepParamUnionMember10,
]
