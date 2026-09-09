# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MetricVariantCreateParams"]


class MetricVariantCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    Name for the new variant. Must be unique for this metric within your
    organization and cannot be `Default`.
    """
