# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SimulationRunGroupListParams"]


class SimulationRunGroupListParams(TypedDict, total=False):
    limit: int
    """Maximum number of run groups to return (default: 20, max: 100)"""

    offset: int
    """Pagination offset"""
