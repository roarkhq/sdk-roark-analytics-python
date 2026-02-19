# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    after: str
    """Cursor for pagination - webhook ID to start after"""

    limit: int
    """Maximum number of webhooks to return (default: 20, max: 50)"""
