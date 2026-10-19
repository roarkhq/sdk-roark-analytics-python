# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MetricCollectionJobCreateParams", "Metric"]


class Metric(TypedDict, total=False):
    id: Required[str]


class MetricCollectionJobCreateParams(TypedDict, total=False):
    call_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="callIds")]
    """
    Call IDs to collect metrics for. Mutually exclusive with chatIds. Max 500 per
    request.
    """

    chat_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="chatIds")]
    """
    Chat IDs to collect metrics for. Mutually exclusive with callIds. Max 500 per
    request.
    """

    metrics: Iterable[Metric]
    """
    Metric definitions to collect. Max 20 per request. Required unless policyId is
    given; with policyId, defaults to every metric that policy collects, and each
    one listed must be in it.
    """

    policy_id: Annotated[str, PropertyInfo(alias="policyId")]
    """
    Optional. A metric policy (collector) whose settings to score with: each metric
    runs at the version that policy runs it at, with its per-collector setting (such
    as the properties Property Verification checks), instead of the metric's
    default. A metric the policy runs at its default runs at its default here too.
    The policy's conditions are not applied: the listed conversations are scored as
    given. Use it to re-score past conversations after changing a policy's settings.
    """
