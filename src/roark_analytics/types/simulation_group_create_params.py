# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SimulationGroupCreateParams", "Notification", "NotificationEmail", "NotificationSlack"]


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


class SimulationGroupCreateParams(TypedDict, total=False):
    name: Required[str]
    """What to call the group."""

    simulation_run_plan_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="simulationRunPlanIds")]]
    """The plans to run together, in run order (2 to 20). Duplicates are dropped."""

    description: Optional[str]
    """What the group is for."""

    notifications: Notification
    """Defaults to email on (to the default audience) and no Slack."""
