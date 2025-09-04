# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationLookupJobParams"]


class SimulationLookupJobParams(TypedDict, total=False):
    roark_phone_number: Required[Annotated[object, PropertyInfo(alias="roarkPhoneNumber")]]
    """Phone number provisioned by Roark for the simulation job in E.164 format.

    In the case of an inbound simulation, this is the number that calls your agent;
    in the case of an outbound simulation, this is the number you call from your
    agent.
    """

    call_received_at: Annotated[object, PropertyInfo(alias="callReceivedAt")]
    """ISO 8601 timestamp of when the call was received.

    Alternatively, any time between the start and end of the call is valid. Defaults
    to the current time, which fetches any jobs that are currently ongoing.
    """
