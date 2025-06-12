# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IntegrationCreateRetellCallParams"]


class IntegrationCreateRetellCallParams(TypedDict, total=False):
    retell_call_ended_payload: Required[Annotated[Dict[str, object], PropertyInfo(alias="retellCallEndedPayload")]]
    """Raw Retell data forwarded directly from the Retell call_ended webhook"""

    properties: Dict[str, object]
    """Optional metadata (key-value pairs) to include with the call.

    Useful for filtering and display in call details.
    """

    skip_already_imported: Annotated[bool, PropertyInfo(alias="skipAlreadyImported")]
    """Skip already imported Retell calls with the same Retell call id."""
