# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationRunPlanJobCreateDebriefResponse",
    "Data",
    "DataReport",
    "DataReportExecutiveSummary",
    "DataReportExecutiveSummarySection",
    "DataReportKeyFinding",
    "DataReportRecommendation",
    "DataReportTheme",
    "DataReportTrend",
    "DataReportTrendRow",
]


class DataReportExecutiveSummarySection(BaseModel):
    body: str

    heading: Optional[str]


class DataReportExecutiveSummary(BaseModel):
    paragraphs: List[str]

    sections: List[DataReportExecutiveSummarySection]


class DataReportKeyFinding(BaseModel):
    body: str

    call_ids: List[str] = FieldInfo(alias="callIds")
    """The calls the finding is about."""

    title: str


class DataReportRecommendation(BaseModel):
    body: str

    channel: Optional[Literal["PROMPT", "VOICE_CONFIG", "STT", "SPEECH_MODEL", "LLM_MODEL", "INFRA", "EXTERNAL"]]

    current_text: Optional[str] = FieldInfo(alias="currentText")
    """For a prompt fix: the text to replace."""

    order: int

    severity: Optional[Literal["HIGH", "MEDIUM", "LOW"]]

    suggested_text: Optional[str] = FieldInfo(alias="suggestedText")
    """For a prompt fix: the replacement."""

    theme_slugs: List[str] = FieldInfo(alias="themeSlugs")

    title: str


class DataReportTheme(BaseModel):
    affected_call_count: int = FieldInfo(alias="affectedCallCount")

    analysis: str

    call_ids: List[str] = FieldInfo(alias="callIds")

    check_names: List[str] = FieldInfo(alias="checkNames")

    impact: Optional[Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"]]

    lifecycle: Optional[Literal["NEW", "PERSISTENT", "IMPROVING", "FIXED"]]

    prevalence: Optional[Literal["WIDESPREAD", "RECURRING", "ISOLATED"]]

    root_cause_channel: Optional[
        Literal["PROMPT", "VOICE_CONFIG", "STT", "SPEECH_MODEL", "LLM_MODEL", "INFRA", "EXTERNAL"]
    ] = FieldInfo(alias="rootCauseChannel")

    severity: Literal["HIGH", "MEDIUM", "LOW"]

    slug: str

    title: str

    total_call_count: int = FieldInfo(alias="totalCallCount")


class DataReportTrendRow(BaseModel):
    check_name: str = FieldInfo(alias="checkName")

    current_pass_rate: Optional[float] = FieldInfo(alias="currentPassRate")

    lifecycle: Optional[Literal["NEW", "PERSISTENT", "IMPROVING", "FIXED"]]

    previous_pass_rate: Optional[float] = FieldInfo(alias="previousPassRate")


class DataReportTrend(BaseModel):
    """The checks against the previous run, as of generation."""

    baseline_run_number: Optional[int] = FieldInfo(alias="baselineRunNumber")

    baseline_run_plan_job_id: str = FieldInfo(alias="baselineRunPlanJobId")

    rows: List[DataReportTrendRow]


class DataReport(BaseModel):
    executive_summary: DataReportExecutiveSummary = FieldInfo(alias="executiveSummary")

    generated_at: str = FieldInfo(alias="generatedAt")

    key_findings: List[DataReportKeyFinding] = FieldInfo(alias="keyFindings")

    recommendations: List[DataReportRecommendation]

    themes: List[DataReportTheme]
    """Failure themes, clustered across the run’s failing calls."""

    trend: Optional[DataReportTrend]
    """The checks against the previous run, as of generation."""

    verdict: Literal["PASSED", "THRESHOLD_FAILED"]

    verdict_summary: str = FieldInfo(alias="verdictSummary")
    """
    One-paragraph verdict, e.g. "Not ready to promote. ..."
    """

    went_well: List[DataReportKeyFinding] = FieldInfo(alias="wentWell")


class Data(BaseModel):
    """
    The run’s written debrief: executive summary, failure themes and
    recommendations. Generated automatically when a run with graded calls settles.
    """

    completed_at: Optional[str] = FieldInfo(alias="completedAt")

    created_at: str = FieldInfo(alias="createdAt")

    debrief_id: str = FieldInfo(alias="debriefId")

    error_message: Optional[str] = FieldInfo(alias="errorMessage")

    report: Optional[DataReport]
    """Present once READY."""

    status: Literal["PENDING", "GENERATING", "READY", "FAILED"]
    """
    PENDING and GENERATING while it is written (usually a few minutes), then READY
    or FAILED.
    """


class SimulationRunPlanJobCreateDebriefResponse(BaseModel):
    data: Data
    """
    The run’s written debrief: executive summary, failure themes and
    recommendations. Generated automatically when a run with graded calls settles.
    """
