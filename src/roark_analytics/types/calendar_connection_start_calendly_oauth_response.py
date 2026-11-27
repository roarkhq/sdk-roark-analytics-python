# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CalendarConnectionStartCalendlyOauthResponse", "Data"]


class Data(BaseModel):
    authorize_url: str = FieldInfo(alias="authorizeUrl")
    """
    Open this in a browser. After the customer consents, the provider returns to
    Roark, which exchanges the code, verifies the credential and stores the
    connection. Read the result with `GET /v1/connections/calendar?provider=…`.
    """

    expires_at: str = FieldInfo(alias="expiresAt")
    """When the link stops working, ISO 8601. Start again after that."""

    state: str
    """
    The opaque single-use value this flow is identified by, echoed so a caller can
    correlate its own UI. Not a credential and not accepted anywhere as one.
    """


class CalendarConnectionStartCalendlyOauthResponse(BaseModel):
    data: Data
