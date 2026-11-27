# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerFlowFolderUpdateParams"]


class CustomerFlowFolderUpdateParams(TypedDict, total=False):
    color: Literal[
        "GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"
    ]
    """
    The color the folder is shown with in the app. Folders share the palette labels
    use.
    """

    description: Optional[str]
    """What belongs in this folder. Null clears it."""

    name: str
    """A new name. Must be unique within the parent folder, ignoring case."""

    parent_id: Annotated[Optional[str], PropertyInfo(alias="parentId")]
    """
    Moves the folder, with everything in it, inside this folder. Null moves it to
    the top level; omit it to leave it where it is.
    """
