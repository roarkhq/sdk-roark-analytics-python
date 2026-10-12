# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationRunGroupRegenerateReportResponse",
    "Data",
    "DataDocument",
    "DataDocumentAggregate",
    "DataDocumentExecutiveSummary",
    "DataDocumentHeadline",
    "DataDocumentHeadlineStatTile",
    "DataDocumentIssue",
    "DataDocumentIssueCall",
    "DataDocumentIssueEvidence",
    "DataDocumentIssueSourceTheme",
    "DataDocumentRecommendation",
    "DataDocumentRun",
    "DataDocumentScorecard",
    "DataDocumentWentWell",
]


class DataDocumentAggregate(BaseModel):
    average_label: Optional[str] = FieldInfo(alias="averageLabel")

    evaluated_count: int = FieldInfo(alias="evaluatedCount")

    median_label: Optional[str] = FieldInfo(alias="medianLabel")

    metric_name: str = FieldInfo(alias="metricName")

    p95_label: Optional[str] = FieldInfo(alias="p95Label")


class DataDocumentExecutiveSummary(BaseModel):
    body: str

    heading: str


class DataDocumentHeadlineStatTile(BaseModel):
    delta_direction: Optional[Literal["POSITIVE", "NEGATIVE", "NEUTRAL"]] = FieldInfo(alias="deltaDirection")

    label: str

    sub: Optional[str]

    value: str


class DataDocumentHeadline(BaseModel):
    call_count: int = FieldInfo(alias="callCount")

    completed_at_iso: Optional[str] = FieldInfo(alias="completedAtIso")

    group_name: str = FieldInfo(alias="groupName")

    passed_run_count: int = FieldInfo(alias="passedRunCount")

    reported_run_count: int = FieldInfo(alias="reportedRunCount")

    run_count: int = FieldInfo(alias="runCount")

    stat_tiles: List[DataDocumentHeadlineStatTile] = FieldInfo(alias="statTiles")

    verdict: Literal["PASSED", "THRESHOLD_FAILED"]

    verdict_prose: str = FieldInfo(alias="verdictProse")


class DataDocumentIssueCall(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId")

    conversation_id: str = FieldInfo(alias="conversationId")

    cue_ms: Optional[int] = FieldInfo(alias="cueMs")

    persona_name: Optional[str] = FieldInfo(alias="personaName")

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")


class DataDocumentIssueEvidence(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId")

    conversation_id: str = FieldInfo(alias="conversationId")

    cue_ms: Optional[int] = FieldInfo(alias="cueMs")

    persona_name: Optional[str] = FieldInfo(alias="personaName")

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")

    text: str


class DataDocumentIssueSourceTheme(BaseModel):
    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")

    slug: str


class DataDocumentIssue(BaseModel):
    affected_call_count: int = FieldInfo(alias="affectedCallCount")

    body: str

    calls: List[DataDocumentIssueCall]

    check_names: List[str] = FieldInfo(alias="checkNames")

    evidence: List[DataDocumentIssueEvidence]

    order: int

    root_cause_channel: Optional[
        Literal["PROMPT", "VOICE_CONFIG", "STT", "SPEECH_MODEL", "LLM_MODEL", "INFRA", "EXTERNAL"]
    ] = FieldInfo(alias="rootCauseChannel")

    run_labels: List[str] = FieldInfo(alias="runLabels")

    severity: Literal["HIGH", "MEDIUM", "LOW"]

    source_themes: List[DataDocumentIssueSourceTheme] = FieldInfo(alias="sourceThemes")

    title: str


class DataDocumentRecommendation(BaseModel):
    body: str

    channel: Optional[Literal["PROMPT", "VOICE_CONFIG", "STT", "SPEECH_MODEL", "LLM_MODEL", "INFRA", "EXTERNAL"]]

    issue_orders: List[int] = FieldInfo(alias="issueOrders")

    order: int

    title: str


class DataDocumentRun(BaseModel):
    call_count: int = FieldInfo(alias="callCount")

    checks_passed: int = FieldInfo(alias="checksPassed")

    checks_total: int = FieldInfo(alias="checksTotal")

    completed_at_iso: Optional[str] = FieldInfo(alias="completedAtIso")

    run_label: str = FieldInfo(alias="runLabel")

    run_number: Optional[int] = FieldInfo(alias="runNumber")

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")

    status: Literal[
        "PENDING",
        "QUEUED",
        "CREATING_SNAPSHOTS",
        "CREATING_SIMULATIONS",
        "PREPARING_CAPACITY",
        "RUNNING_SIMULATIONS",
        "COMPLETED",
        "FAILED",
        "TIMED_OUT",
        "CANCELLED",
        "CANCELLING",
        "ENDING_SIMULATIONS",
    ]

    summary: Optional[str]

    theme_count: int = FieldInfo(alias="themeCount")

    verdict: Optional[Literal["PASSED", "THRESHOLD_FAILED"]]


class DataDocumentScorecard(BaseModel):
    check_name: str = FieldInfo(alias="checkName")

    evaluated_count: int = FieldInfo(alias="evaluatedCount")

    failed_count: int = FieldInfo(alias="failedCount")

    failed_run_count: int = FieldInfo(alias="failedRunCount")

    pass_rate_pct: Optional[float] = FieldInfo(alias="passRatePct")

    run_count: int = FieldInfo(alias="runCount")


class DataDocumentWentWell(BaseModel):
    body: str

    evidence: List[DataDocumentIssueEvidence]

    title: str


class DataDocument(BaseModel):
    """
    The group report: the runs it covers, a scorecard summed across them, what went
    well, and the issues found, each merged from the per-run debriefs with
    call-level evidence. Every figure is computed from the runs; the prose is
    AI-written around those facts.
    """

    aggregates: List[DataDocumentAggregate]

    executive_summary: List[DataDocumentExecutiveSummary] = FieldInfo(alias="executiveSummary")

    generated_at_iso: str = FieldInfo(alias="generatedAtIso")

    headline: DataDocumentHeadline

    issues: List[DataDocumentIssue]

    methodology: str

    model: str

    recommendations: List[DataDocumentRecommendation]

    runs: List[DataDocumentRun]

    scorecard: List[DataDocumentScorecard]

    simulation_run_group_id: str = FieldInfo(alias="simulationRunGroupId")

    smaller_items: List[DataDocumentIssue] = FieldInfo(alias="smallerItems")

    version: Literal[1]

    went_well: List[DataDocumentWentWell] = FieldInfo(alias="wentWell")


class Data(BaseModel):
    """One generation of the group report."""

    id: str

    completed_at: Optional[str] = FieldInfo(alias="completedAt")
    """ISO 8601. Null until the report settles."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    document: Optional[DataDocument]
    """Null until the report is READY."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage")

    status: Literal["PENDING", "GENERATING", "READY", "FAILED"]
    """
    PENDING and GENERATING are in flight; READY carries the document; FAILED carries
    errorMessage.
    """


class SimulationRunGroupRegenerateReportResponse(BaseModel):
    data: Data
    """One generation of the group report."""
