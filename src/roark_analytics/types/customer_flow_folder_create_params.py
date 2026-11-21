# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomerFlowFolderCreateParams"]


class CustomerFlowFolderCreateParams(TypedDict, total=False):
    name: Required[str]
    """The folder name. Must be unique in the project."""

    color: Literal[
        "GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"
    ]
    """
    The color the folder is shown with in the app. Folders share the palette labels
    use. Defaults to GREY.
    """

    description: Optional[str]
    """What belongs in this folder."""
