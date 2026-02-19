# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "EvaluationUpdateEvaluatorParams",
    "Block",
    "BlockCreateCustomPromptBlockInput",
    "BlockCreateDatafieldCheckBlockInput",
    "BlockCreateEmotionBlockInput",
    "BlockCreateLatencyBlockInput",
    "BlockCreatePolitenessBlockInput",
    "BlockCreateSentimentBlockInput",
    "BlockCreateToolCallsBlockInput",
    "BlockCreateToxicityBlockInput",
    "BlockCreateVocalCueBlockInput",
]


class EvaluationUpdateEvaluatorParams(TypedDict, total=False):
    blocks: Iterable[Block]
    """Updated array of evaluation blocks.

    Include id to update, omit id to create. Existing blocks not in the array will
    be deleted.
    """

    description: Optional[str]
    """New description for the evaluator"""

    name: str
    """New name for the evaluator"""


class BlockCreateCustomPromptBlockInput(TypedDict, total=False):
    block_type: Required[Annotated[Literal["CUSTOM_PROMPT"], PropertyInfo(alias="blockType")]]

    metric_name: Required[Annotated[str, PropertyInfo(alias="metricName")]]
    """Name of the metric this prompt evaluates"""

    name: Required[str]
    """Display name of the evaluation block"""

    prompt: Required[str]
    """The prompt to evaluate the call against"""

    id: str
    """ID of an existing block to update.

    Omit to create a new block. Existing blocks not included will be deleted.
    """

    description: Optional[str]
    """Optional description of what this block evaluates"""

    input_dimensions: Annotated[SequenceNotStr[str], PropertyInfo(alias="inputDimensions")]
    """Input dimensions for the block (auto-assigned if not provided)"""

    order_index: Annotated[int, PropertyInfo(alias="orderIndex")]
    """Order in which this block is executed (defaults to array position)"""

    skip_condition: Annotated[Optional[str], PropertyInfo(alias="skipCondition")]
    """Condition to skip this block evaluation"""

    threshold: float
    """Minimum score threshold to pass evaluation (0-1, default: 0.7)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100, default: 50)"""


class BlockCreateDatafieldCheckBlockInput(TypedDict, total=False):
    block_type: Required[Annotated[Literal["DATAFIELD_CHECK"], PropertyInfo(alias="blockType")]]

    evaluation_criteria: Required[Annotated[str, PropertyInfo(alias="evaluationCriteria")]]
    """Criteria for evaluating the property"""

    name: Required[str]
    """Display name of the evaluation block"""

    property_name: Required[Annotated[str, PropertyInfo(alias="propertyName")]]
    """Name of the property to check"""

    id: str
    """ID of an existing block to update.

    Omit to create a new block. Existing blocks not included will be deleted.
    """

    description: Optional[str]
    """Optional description of what this block evaluates"""

    input_dimensions: Annotated[SequenceNotStr[str], PropertyInfo(alias="inputDimensions")]
    """Input dimensions for the block (auto-assigned if not provided)"""

    is_required: Annotated[bool, PropertyInfo(alias="isRequired")]
    """Whether this property must be present"""

    order_index: Annotated[int, PropertyInfo(alias="orderIndex")]
    """Order in which this block is executed (defaults to array position)"""

    skip_condition: Annotated[Optional[str], PropertyInfo(alias="skipCondition")]
    """Condition to skip this block evaluation"""

    threshold: float
    """Minimum score threshold to pass evaluation (0-1, default: 0.8)"""

    value_type: Annotated[str, PropertyInfo(alias="valueType")]
    """Expected type of the property value"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100, default: 50)"""


class BlockCreateEmotionBlockInput(TypedDict, total=False):
    block_type: Required[Annotated[Literal["EMOTION"], PropertyInfo(alias="blockType")]]

    name: Required[str]
    """Display name of the evaluation block"""

    id: str
    """ID of an existing block to update.

    Omit to create a new block. Existing blocks not included will be deleted.
    """

    description: Optional[str]
    """Optional description of what this block evaluates"""

    input_dimensions: Annotated[SequenceNotStr[str], PropertyInfo(alias="inputDimensions")]
    """Input dimensions for the block (auto-assigned if not provided)"""

    order_index: Annotated[int, PropertyInfo(alias="orderIndex")]
    """Order in which this block is executed (defaults to array position)"""

    selected_emotion: Annotated[str, PropertyInfo(alias="selectedEmotion")]
    """The emotion to detect (e.g., "joy", "anger", "sadness")"""

    skip_condition: Annotated[Optional[str], PropertyInfo(alias="skipCondition")]
    """Condition to skip this block evaluation"""

    threshold: float
    """Minimum confidence threshold for emotion detection (0-1, default: 0.7)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100, default: 50)"""


class BlockCreateLatencyBlockInput(TypedDict, total=False):
    block_type: Required[Annotated[Literal["LATENCY"], PropertyInfo(alias="blockType")]]

    name: Required[str]
    """Display name of the evaluation block"""

    id: str
    """ID of an existing block to update.

    Omit to create a new block. Existing blocks not included will be deleted.
    """

    description: Optional[str]
    """Optional description of what this block evaluates"""

    input_dimensions: Annotated[SequenceNotStr[str], PropertyInfo(alias="inputDimensions")]
    """Input dimensions for the block (auto-assigned if not provided)"""

    max_allowed_silences: Annotated[float, PropertyInfo(alias="maxAllowedSilences")]
    """Maximum number of silence periods allowed"""

    min_silence_duration: Annotated[float, PropertyInfo(alias="minSilenceDuration")]
    """Minimum duration of silence in milliseconds to be considered"""

    order_index: Annotated[int, PropertyInfo(alias="orderIndex")]
    """Order in which this block is executed (defaults to array position)"""

    skip_condition: Annotated[Optional[str], PropertyInfo(alias="skipCondition")]
    """Condition to skip this block evaluation"""

    threshold: float
    """Maximum allowed latency score"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100, default: 50)"""


class BlockCreatePolitenessBlockInput(TypedDict, total=False):
    block_type: Required[Annotated[Literal["POLITENESS"], PropertyInfo(alias="blockType")]]

    name: Required[str]
    """Display name of the evaluation block"""

    id: str
    """ID of an existing block to update.

    Omit to create a new block. Existing blocks not included will be deleted.
    """

    description: Optional[str]
    """Optional description of what this block evaluates"""

    input_dimensions: Annotated[SequenceNotStr[str], PropertyInfo(alias="inputDimensions")]
    """Input dimensions for the block (auto-assigned if not provided)"""

    order_index: Annotated[int, PropertyInfo(alias="orderIndex")]
    """Order in which this block is executed (defaults to array position)"""

    skip_condition: Annotated[Optional[str], PropertyInfo(alias="skipCondition")]
    """Condition to skip this block evaluation"""

    threshold: float
    """Minimum politeness score threshold (0-1, default: 0.7)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100, default: 50)"""


class BlockCreateSentimentBlockInput(TypedDict, total=False):
    block_type: Required[Annotated[Literal["SENTIMENT"], PropertyInfo(alias="blockType")]]

    name: Required[str]
    """Display name of the evaluation block"""

    id: str
    """ID of an existing block to update.

    Omit to create a new block. Existing blocks not included will be deleted.
    """

    description: Optional[str]
    """Optional description of what this block evaluates"""

    input_dimensions: Annotated[SequenceNotStr[str], PropertyInfo(alias="inputDimensions")]
    """Input dimensions for the block (auto-assigned if not provided)"""

    order_index: Annotated[int, PropertyInfo(alias="orderIndex")]
    """Order in which this block is executed (defaults to array position)"""

    skip_condition: Annotated[Optional[str], PropertyInfo(alias="skipCondition")]
    """Condition to skip this block evaluation"""

    threshold: float
    """Minimum sentiment score threshold (0-1, default: 0.7)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100, default: 50)"""


class BlockCreateToolCallsBlockInput(TypedDict, total=False):
    block_type: Required[Annotated[Literal["TOOL_CALLS"], PropertyInfo(alias="blockType")]]

    name: Required[str]
    """Display name of the evaluation block"""

    tool_definition_id: Required[Annotated[str, PropertyInfo(alias="toolDefinitionId")]]
    """ID of the tool definition"""

    id: str
    """ID of an existing block to update.

    Omit to create a new block. Existing blocks not included will be deleted.
    """

    description: Optional[str]
    """Optional description of what this block evaluates"""

    input_dimensions: Annotated[SequenceNotStr[str], PropertyInfo(alias="inputDimensions")]
    """Input dimensions for the block (auto-assigned if not provided)"""

    invocation_condition: Annotated[Optional[str], PropertyInfo(alias="invocationCondition")]
    """Condition that must be met for tool invocation"""

    min_invocation_count: Annotated[Optional[float], PropertyInfo(alias="minInvocationCount")]
    """Minimum number of times the tool should be invoked"""

    order_index: Annotated[int, PropertyInfo(alias="orderIndex")]
    """Order in which this block is executed (defaults to array position)"""

    should_be_invoked: Annotated[bool, PropertyInfo(alias="shouldBeInvoked")]
    """Whether the tool should be invoked"""

    skip_condition: Annotated[Optional[str], PropertyInfo(alias="skipCondition")]
    """Condition to skip this block evaluation"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100, default: 50)"""


class BlockCreateToxicityBlockInput(TypedDict, total=False):
    block_type: Required[Annotated[Literal["TOXICITY"], PropertyInfo(alias="blockType")]]

    name: Required[str]
    """Display name of the evaluation block"""

    id: str
    """ID of an existing block to update.

    Omit to create a new block. Existing blocks not included will be deleted.
    """

    description: Optional[str]
    """Optional description of what this block evaluates"""

    input_dimensions: Annotated[SequenceNotStr[str], PropertyInfo(alias="inputDimensions")]
    """Input dimensions for the block (auto-assigned if not provided)"""

    order_index: Annotated[int, PropertyInfo(alias="orderIndex")]
    """Order in which this block is executed (defaults to array position)"""

    skip_condition: Annotated[Optional[str], PropertyInfo(alias="skipCondition")]
    """Condition to skip this block evaluation"""

    threshold: float
    """Maximum allowed toxicity score (0-1, default: 0.7)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100, default: 50)"""


class BlockCreateVocalCueBlockInput(TypedDict, total=False):
    block_type: Required[Annotated[Literal["VOCAL_CUE"], PropertyInfo(alias="blockType")]]

    name: Required[str]
    """Display name of the evaluation block"""

    id: str
    """ID of an existing block to update.

    Omit to create a new block. Existing blocks not included will be deleted.
    """

    description: Optional[str]
    """Optional description of what this block evaluates"""

    input_dimensions: Annotated[SequenceNotStr[str], PropertyInfo(alias="inputDimensions")]
    """Input dimensions for the block (auto-assigned if not provided)"""

    order_index: Annotated[int, PropertyInfo(alias="orderIndex")]
    """Order in which this block is executed (defaults to array position)"""

    selected_cue: Annotated[str, PropertyInfo(alias="selectedCue")]
    """The vocal cue to detect (e.g., "pace", "tone", "volume")"""

    skip_condition: Annotated[Optional[str], PropertyInfo(alias="skipCondition")]
    """Condition to skip this block evaluation"""

    threshold: float
    """Minimum confidence threshold for vocal cue detection (0-1, default: 0.7)"""

    weight: int
    """Weight of this block in the overall evaluation score (0-100, default: 50)"""


Block: TypeAlias = Union[
    BlockCreateCustomPromptBlockInput,
    BlockCreateDatafieldCheckBlockInput,
    BlockCreateEmotionBlockInput,
    BlockCreateLatencyBlockInput,
    BlockCreatePolitenessBlockInput,
    BlockCreateSentimentBlockInput,
    BlockCreateToolCallsBlockInput,
    BlockCreateToxicityBlockInput,
    BlockCreateVocalCueBlockInput,
]
