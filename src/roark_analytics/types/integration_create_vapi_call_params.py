# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IntegrationCreateVapiCallParams"]


class IntegrationCreateVapiCallParams(TypedDict, total=False):
    vapi_end_of_call_report_payload: Required[
        Annotated[Dict[str, object], PropertyInfo(alias="vapiEndOfCallReportPayload")]
    ]
    """Raw Vapi data forwarded directly from the Vapi end-of-call-report webhook"""

    properties: Dict[str, object]
    """Optional metadata (key-value pairs) to include with the call.

    Useful for filtering and display in call details.
    """

    skip_already_imported: Annotated[bool, PropertyInfo(alias="skipAlreadyImported")]
    """Skip already imported Vapi calls with the same Vapi call id."""
