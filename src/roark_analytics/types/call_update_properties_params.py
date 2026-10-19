# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["CallUpdatePropertiesParams", "Metric"]


class Metric(TypedDict, total=False):
    id: Required[str]


class CallUpdatePropertiesParams(TypedDict, total=False):
    properties: Required[Dict[str, Union[str, float, bool, None]]]
    """
    Properties to change on the call. A string, number or boolean value adds the
    property or overwrites it; null removes it. Properties left out are untouched.
    Keys are stored in snake_case, as on POST /v1/call. A property keeps the value
    type it was first stored with in the project, so a value of another type is
    rejected. Properties Roark sets itself (direction, duration_seconds, agent_id,
    ...) can't be changed. Max 100 per request.
    """

    metrics: Iterable[Metric]
    """
    Optional. Metric definitions to (re)score on this call once the properties are
    written, e.g. metrics that read the call's properties. Triggers a metric
    collection job (billed, credit-gated) and requires the 'metric:create'
    permission. Omit to update properties without scoring. Max 20.
    """
