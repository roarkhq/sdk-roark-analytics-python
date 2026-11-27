# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CustomerFlowFolderUpdateResponse", "Data"]


class Data(BaseModel):
    """
    A folder that groups customer flows. A flow sits in at most one folder. Folders
    can sit inside other folders, up to 5 levels deep.
    """

    id: str

    built_in: bool = FieldInfo(alias="builtIn")
    """
    Whether Roark curates this folder. Built-in folders cannot be deleted or have
    your flows filed in them.
    """

    color: Literal[
        "GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"
    ]
    """
    The color the folder is shown with in the app. Folders share the palette labels
    use.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp in ISO 8601 format"""

    description: Optional[str]
    """What belongs in this folder."""

    name: str
    """The folder name, unique within its parent folder."""

    parent_id: Optional[str] = FieldInfo(alias="parentId")
    """The folder this one sits inside, or null when it is a top-level folder."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp in ISO 8601 format"""


class CustomerFlowFolderUpdateResponse(BaseModel):
    data: Data
    """
    A folder that groups customer flows. A flow sits in at most one folder. Folders
    can sit inside other folders, up to 5 levels deep.
    """
