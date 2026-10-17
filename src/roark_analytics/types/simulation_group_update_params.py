# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationGroupUpdateParams", "Notification", "NotificationEmail", "NotificationSlack"]


class NotificationEmail(TypedDict, total=False):
    enabled: Required[bool]
    """Whether the group report of each run is emailed when it is ready."""

    recipients: SequenceNotStr[str]
    """
    Addresses to email (at most 50), Roark users or not: the email attaches the
    report PDF. Empty emails every member of the project.
    """


class NotificationSlack(TypedDict, total=False):
    channel_id: Required[Annotated[str, PropertyInfo(alias="channelId")]]
    """The Slack channel id"""

    channel_name: Required[Annotated[str, PropertyInfo(alias="channelName")]]
    """The channel name, shown in Roark"""


class Notification(TypedDict, total=False):
    """Where each run's group report announces itself once it is ready."""

    email: NotificationEmail

    slack: Iterable[NotificationSlack]
    """
    Channels in the project's connected Slack workspace to post the report to (at
    most 10). Slack must be connected to the project first.
    """


class SimulationGroupUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Send null to clear it."""

    name: str

    notifications: Notification
    """Replaces the notification settings as a whole."""

    simulation_run_plan_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="simulationRunPlanIds")]
    """Replaces the plans, in run order."""
