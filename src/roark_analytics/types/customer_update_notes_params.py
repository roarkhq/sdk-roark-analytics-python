# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CustomerUpdateNotesParams"]


class CustomerUpdateNotesParams(TypedDict, total=False):
    notes: Required[Optional[str]]
    """Replaces the existing notes. Null or empty clears them."""
