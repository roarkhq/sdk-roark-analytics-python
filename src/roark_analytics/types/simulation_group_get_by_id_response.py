# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationGroupGetByIDResponse",
    "Data",
    "DataNotification",
    "DataNotificationEmail",
    "DataNotificationSlack",
    "DataPlan",
]


class DataNotificationEmail(BaseModel):
    enabled: bool

    recipients: List[str]


class DataNotificationSlack(BaseModel):
    channel_id: str = FieldInfo(alias="channelId")

    channel_name: str = FieldInfo(alias="channelName")


class DataNotification(BaseModel):
    """Where each run's group report announces itself once it is ready."""

    email: DataNotificationEmail

    slack: List[DataNotificationSlack]


class DataPlan(BaseModel):
    id: str
    """The plan, readable at GET /v1/simulation/plan/{planId}"""

    name: str


class Data(BaseModel):
    """
    A saved, repeatable set of plans that run together. Each run starts one run of
    every plan and groups them into a run group with one combined report.
    """

    id: str

    config_managed: bool = FieldInfo(alias="configManaged")
    """
    Whether this group is managed by config as code. A managed group can be run
    here, but PUT and DELETE on it return 409: change it in the config file.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    description: Optional[str]

    last_run_at: Optional[str] = FieldInfo(alias="lastRunAt")
    """ISO 8601. Null when it has never run."""

    latest_run_group_id: Optional[str] = FieldInfo(alias="latestRunGroupId")
    """
    The most recent run group it started, readable at GET
    /v1/simulation/run-group/{groupId}. Null when it has never run.
    """

    name: str

    notifications: DataNotification
    """Where each run's group report announces itself once it is ready."""

    plans: List[DataPlan]
    """The plans in run order. A plan deleted since it was added is left out."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """ISO 8601"""


class SimulationGroupGetByIDResponse(BaseModel):
    data: Data
    """
    A saved, repeatable set of plans that run together. Each run starts one run of
    every plan and groups them into a run group with one combined report.
    """
