# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SimulationGroupListParams"]


class SimulationGroupListParams(TypedDict, total=False):
    limit: int
    """Maximum number of groups to return (default: 20, max: 100)"""

    offset: int
    """Pagination offset"""
