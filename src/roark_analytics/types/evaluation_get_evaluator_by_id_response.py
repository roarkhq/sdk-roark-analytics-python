# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EvaluationGetEvaluatorByIDResponse",
    "Block",
    "BlockUnionMember0",
    "BlockUnionMember1",
    "BlockUnionMember2",
    "BlockUnionMember3",
    "BlockUnionMember4",
    "BlockUnionMember5",
    "BlockUnionMember6",
    "BlockUnionMember7",
    "BlockUnionMember8",
]


class BlockUnionMember0(BaseModel):
    id: str
    """Unique identifier for the block"""

    block_type: Literal["CUSTOM_PROMPT"] = FieldInfo(alias="blockType")
    """Block type identifier"""

    description: Optional[str] = None
    """Optional description of what this block evaluates"""

    metric_name: str = FieldInfo(alias="metricName")
    """Name of the metric this prompt evaluates"""

    name: str
    """Display name of the evaluation block"""

    order_index: int = FieldInfo(alias="orderIndex")
    """Order in which this block is executed"""

    prompt: str
    """The prompt to evaluate the call against"""

    threshold: float
    """Minimum score threshold to pass evaluation (0-1)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100)"""


class BlockUnionMember1(BaseModel):
    id: str
    """Unique identifier for the block"""

    block_type: Literal["DATAFIELD_CHECK"] = FieldInfo(alias="blockType")
    """Block type identifier"""

    description: Optional[str] = None
    """Optional description of what this block evaluates"""

    evaluation_criteria: str = FieldInfo(alias="evaluationCriteria")
    """Criteria for evaluating the property"""

    is_required: bool = FieldInfo(alias="isRequired")
    """Whether this property must be present"""

    name: str
    """Display name of the evaluation block"""

    order_index: int = FieldInfo(alias="orderIndex")
    """Order in which this block is executed"""

    property_name: str = FieldInfo(alias="propertyName")
    """Name of the property to check"""

    threshold: float
    """Minimum score threshold to pass evaluation (0-1)"""

    value_type: str = FieldInfo(alias="valueType")
    """Expected type of the property value"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100)"""


class BlockUnionMember2(BaseModel):
    id: str
    """Unique identifier for the block"""

    block_type: Literal["EMOTION"] = FieldInfo(alias="blockType")
    """Block type identifier"""

    description: Optional[str] = None
    """Optional description of what this block evaluates"""

    name: str
    """Display name of the evaluation block"""

    order_index: int = FieldInfo(alias="orderIndex")
    """Order in which this block is executed"""

    selected_emotion: str = FieldInfo(alias="selectedEmotion")
    """The emotion to detect (e.g., "joy", "anger", "sadness")"""

    threshold: float
    """Minimum confidence threshold for emotion detection (0-1)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100)"""


class BlockUnionMember3(BaseModel):
    id: str
    """Unique identifier for the block"""

    block_type: Literal["LATENCY"] = FieldInfo(alias="blockType")
    """Block type identifier"""

    description: Optional[str] = None
    """Optional description of what this block evaluates"""

    max_allowed_silences: float = FieldInfo(alias="maxAllowedSilences")
    """Maximum number of silence periods allowed"""

    min_silence_duration: float = FieldInfo(alias="minSilenceDuration")
    """Minimum duration of silence in milliseconds to be considered"""

    name: str
    """Display name of the evaluation block"""

    order_index: int = FieldInfo(alias="orderIndex")
    """Order in which this block is executed"""

    threshold: float
    """Maximum allowed latency score"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100)"""


class BlockUnionMember4(BaseModel):
    id: str
    """Unique identifier for the block"""

    block_type: Literal["POLITENESS"] = FieldInfo(alias="blockType")
    """Block type identifier"""

    description: Optional[str] = None
    """Optional description of what this block evaluates"""

    name: str
    """Display name of the evaluation block"""

    order_index: int = FieldInfo(alias="orderIndex")
    """Order in which this block is executed"""

    threshold: float
    """Minimum politeness score threshold (0-1)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100)"""


class BlockUnionMember5(BaseModel):
    id: str
    """Unique identifier for the block"""

    block_type: Literal["SENTIMENT"] = FieldInfo(alias="blockType")
    """Block type identifier"""

    description: Optional[str] = None
    """Optional description of what this block evaluates"""

    name: str
    """Display name of the evaluation block"""

    order_index: int = FieldInfo(alias="orderIndex")
    """Order in which this block is executed"""

    threshold: float
    """Minimum sentiment score threshold (0-1)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100)"""


class BlockUnionMember6(BaseModel):
    id: str
    """Unique identifier for the block"""

    block_type: Literal["TOOL_CALLS"] = FieldInfo(alias="blockType")
    """Block type identifier"""

    description: Optional[str] = None
    """Optional description of what this block evaluates"""

    invocation_condition: Optional[str] = FieldInfo(alias="invocationCondition", default=None)
    """Condition that must be met for tool invocation"""

    min_invocation_count: Optional[float] = FieldInfo(alias="minInvocationCount", default=None)
    """Minimum number of times the tool should be invoked"""

    name: str
    """Display name of the evaluation block"""

    order_index: int = FieldInfo(alias="orderIndex")
    """Order in which this block is executed"""

    should_be_invoked: bool = FieldInfo(alias="shouldBeInvoked")
    """Whether the tool should be invoked"""

    tool_definition_id: str = FieldInfo(alias="toolDefinitionId")
    """ID of the tool definition"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100)"""


class BlockUnionMember7(BaseModel):
    id: str
    """Unique identifier for the block"""

    block_type: Literal["TOXICITY"] = FieldInfo(alias="blockType")
    """Block type identifier"""

    description: Optional[str] = None
    """Optional description of what this block evaluates"""

    name: str
    """Display name of the evaluation block"""

    order_index: int = FieldInfo(alias="orderIndex")
    """Order in which this block is executed"""

    threshold: float
    """Maximum allowed toxicity score (0-1)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100)"""


class BlockUnionMember8(BaseModel):
    id: str
    """Unique identifier for the block"""

    block_type: Literal["VOCAL_CUE"] = FieldInfo(alias="blockType")
    """Block type identifier"""

    description: Optional[str] = None
    """Optional description of what this block evaluates"""

    name: str
    """Display name of the evaluation block"""

    order_index: int = FieldInfo(alias="orderIndex")
    """Order in which this block is executed"""

    selected_cue: str = FieldInfo(alias="selectedCue")
    """The vocal cue to detect (e.g., "pace", "tone", "volume")"""

    threshold: float
    """Minimum confidence threshold for vocal cue detection (0-1)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100)"""


Block: TypeAlias = Union[
    BlockUnionMember0,
    BlockUnionMember1,
    BlockUnionMember2,
    BlockUnionMember3,
    BlockUnionMember4,
    BlockUnionMember5,
    BlockUnionMember6,
    BlockUnionMember7,
    BlockUnionMember8,
]


class EvaluationGetEvaluatorByIDResponse(BaseModel):
    id: str
    """Unique identifier for the evaluator"""

    blocks: List[Block]
    """Array of evaluation blocks configured for this evaluator"""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO timestamp when the evaluator was created"""

    description: Optional[str] = None
    """Optional description of the evaluator"""

    name: str
    """Name of the evaluator"""

    slug: str
    """Unique slug identifier for the evaluator"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """ISO timestamp when the evaluator was last updated"""
