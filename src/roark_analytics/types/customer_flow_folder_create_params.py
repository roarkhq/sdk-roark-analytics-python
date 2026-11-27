# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerFlowFolderCreateParams"]


class CustomerFlowFolderCreateParams(TypedDict, total=False):
    name: Required[str]
    """The folder name. Must be unique within its parent folder, ignoring case."""

    color: Literal[
        "GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"
    ]
    """
    The color the folder is shown with in the app. Folders share the palette labels
    use. Defaults to GREY.
    """

    description: Optional[str]
    """What belongs in this folder."""

    parent_id: Annotated[Optional[str], PropertyInfo(alias="parentId")]
    """
    Create the folder inside this folder. Omit it, or send null, for a top-level
    folder.
    """
