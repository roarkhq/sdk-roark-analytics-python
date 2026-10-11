# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SimulationRunPlanJobCreateDebriefParams"]


class SimulationRunPlanJobCreateDebriefParams(TypedDict, total=False):
    regenerate: bool
    """
    Generate a new debrief even when a ready one exists. Without it, an existing
    ready or in-progress debrief is returned as-is.
    """
