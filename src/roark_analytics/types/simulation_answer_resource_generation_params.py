# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SimulationAnswerResourceGenerationParams"]


class SimulationAnswerResourceGenerationParams(TypedDict, total=False):
    text: Required[str]
    """What you want the generation to know"""
