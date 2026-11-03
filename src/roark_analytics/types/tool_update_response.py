# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ToolUpdateResponse",
    "Data",
    "DataInput",
    "DataRuntime",
    "DataRuntimeMessage",
    "DataRuntimeRequest",
    "DataRuntimeRequestHeader",
]


class DataInput(BaseModel):
    description: Optional[str]
    """What the input is, so the agent fills it in right"""

    name: str
    """The input name, as the agent passes it"""

    required: bool
    """The agent must pass it"""

    type: Literal["string", "number", "boolean"]
    """string, number or boolean"""


class DataRuntimeMessage(BaseModel):
    before: Optional[str]
    """Said as the request goes out"""

    failure: Optional[str]
    """Given to the agent to say when the request fails"""

    slow: Optional[str]
    """Said once if the request is slow"""


class DataRuntimeRequestHeader(BaseModel):
    name: str

    value: str


class DataRuntimeRequest(BaseModel):
    body: Optional[str]
    """
    JSON body template. Null sends the inputs as the body (POST, PUT, PATCH) or the
    query (GET, DELETE).
    """

    headers: List[DataRuntimeRequestHeader]

    method: Literal["POST", "PUT", "PATCH", "GET", "DELETE"]

    timeout_ms: Optional[int] = FieldInfo(alias="timeoutMs")
    """How long the agent waits, 1000 to 30000 ms"""

    url: str
    """
    https URL. Placeholders {{args.<input>}} and {{conversation.*}} (id, direction,
    modality, agentNumber, customerNumber, startedAt) may appear in the path and
    query.
    """


class DataRuntime(BaseModel):
    """What a hosted agent sends and says when it calls the tool"""

    changes_data: bool = FieldInfo(alias="changesData")
    """
    The tool books, cancels or sends something: its call is not abandoned when the
    caller interrupts, and each request carries an Idempotency-Key.
    """

    messages: DataRuntimeMessage

    request: DataRuntimeRequest

    response_fields: Optional[List[str]] = FieldInfo(alias="responseFields")
    """
    Dot paths into the JSON response the agent is given. Null gives it the whole
    response.
    """


class Data(BaseModel):
    id: str

    agent_id: Optional[str] = FieldInfo(alias="agentId")
    """The agent the tool is scoped to; null for the project"""

    created_at: str = FieldInfo(alias="createdAt")

    description: Optional[str]

    expected_result: Optional[str] = FieldInfo(alias="expectedResult")
    """How it should handle the result, for grading"""

    inputs: List[DataInput]

    invocation_criteria: Optional[str] = FieldInfo(alias="invocationCriteria")
    """When the agent should call it, for grading"""

    name: str

    runtime: Optional[DataRuntime]
    """Null for a tool that is only graded"""

    source: Literal["CUSTOM", "SYSTEM"]
    """SYSTEM for a built-in tool every project can attach"""

    system_key: Optional[str] = FieldInfo(alias="systemKey")
    """The stable key of a built-in tool, such as dtmf"""

    updated_at: str = FieldInfo(alias="updatedAt")

    version: Optional[int]
    """The latest version; null before any is declared"""


class ToolUpdateResponse(BaseModel):
    data: Data
