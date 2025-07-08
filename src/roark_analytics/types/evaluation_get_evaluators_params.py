# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EvaluationGetEvaluatorsParams"]


class EvaluationGetEvaluatorsParams(TypedDict, total=False):
    after: str
    """Cursor for pagination - evaluator ID to start after"""

    limit: str
    """Maximum number of evaluators to return (default: 20, max: 50)"""
