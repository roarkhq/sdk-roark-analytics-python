# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import TypedDict

__all__ = ["SimulationRunPlanJobStartParams"]


class SimulationRunPlanJobStartParams(TypedDict, total=False):
    variables: Union[Dict[str, str], Dict[str, Dict[str, str]]]
    """Runtime variables that override plan-defined variables.

    Can be a flat key-value object (applies to all scenarios) or keyed by scenario
    ID for per-scenario overrides.
    """
