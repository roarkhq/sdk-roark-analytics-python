# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentPromptUpdateParams"]


class AgentPromptUpdateParams(TypedDict, total=False):
    prompt: Required[str]
    """The prompt content to set."""
