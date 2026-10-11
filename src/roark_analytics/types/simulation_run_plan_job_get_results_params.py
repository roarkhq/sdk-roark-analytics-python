# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimulationRunPlanJobGetResultsParams"]


class SimulationRunPlanJobGetResultsParams(TypedDict, total=False):
    compare_to_job_id: Annotated[str, PropertyInfo(alias="compareToJobId")]
    """
    Simulation run plan job to compare this run against, e.g. the last run on your
    main branch. Defaults to the plan's previous settled run. Any run in the project
    works, including another plan's: checks are matched by metric, and a check only
    one run graded reads null on the other side.
    """
