# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationRunGroupGetByIDResponse",
    "Data",
    "DataLatestReport",
    "DataLatestReportDocument",
    "DataLatestReportDocumentAggregate",
    "DataLatestReportDocumentExecutiveSummary",
    "DataLatestReportDocumentHeadline",
    "DataLatestReportDocumentHeadlineStatTile",
    "DataLatestReportDocumentIssue",
    "DataLatestReportDocumentIssueCall",
    "DataLatestReportDocumentIssueEvidence",
    "DataLatestReportDocumentIssueSourceTheme",
    "DataLatestReportDocumentRecommendation",
    "DataLatestReportDocumentRun",
    "DataLatestReportDocumentScorecard",
    "DataLatestReportDocumentWentWell",
    "DataRun",
]


class DataLatestReportDocumentAggregate(BaseModel):
    average_label: Optional[str] = FieldInfo(alias="averageLabel")

    evaluated_count: int = FieldInfo(alias="evaluatedCount")

    median_label: Optional[str] = FieldInfo(alias="medianLabel")

    metric_name: str = FieldInfo(alias="metricName")

    p95_label: Optional[str] = FieldInfo(alias="p95Label")


class DataLatestReportDocumentExecutiveSummary(BaseModel):
    body: str

    heading: str


class DataLatestReportDocumentHeadlineStatTile(BaseModel):
    delta_direction: Optional[Literal["POSITIVE", "NEGATIVE", "NEUTRAL"]] = FieldInfo(alias="deltaDirection")

    label: str

    sub: Optional[str]

    value: str


class DataLatestReportDocumentHeadline(BaseModel):
    call_count: int = FieldInfo(alias="callCount")

    completed_at_iso: Optional[str] = FieldInfo(alias="completedAtIso")

    group_name: str = FieldInfo(alias="groupName")

    passed_run_count: int = FieldInfo(alias="passedRunCount")

    reported_run_count: int = FieldInfo(alias="reportedRunCount")

    run_count: int = FieldInfo(alias="runCount")

    stat_tiles: List[DataLatestReportDocumentHeadlineStatTile] = FieldInfo(alias="statTiles")

    verdict: Literal["PASSED", "THRESHOLD_FAILED"]

    verdict_prose: str = FieldInfo(alias="verdictProse")


class DataLatestReportDocumentIssueCall(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId")

    conversation_id: str = FieldInfo(alias="conversationId")

    cue_ms: Optional[int] = FieldInfo(alias="cueMs")

    persona_name: Optional[str] = FieldInfo(alias="personaName")

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")


class DataLatestReportDocumentIssueEvidence(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId")

    conversation_id: str = FieldInfo(alias="conversationId")

    cue_ms: Optional[int] = FieldInfo(alias="cueMs")

    persona_name: Optional[str] = FieldInfo(alias="personaName")

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")

    text: str


class DataLatestReportDocumentIssueSourceTheme(BaseModel):
    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")

    slug: str


class DataLatestReportDocumentIssue(BaseModel):
    affected_call_count: int = FieldInfo(alias="affectedCallCount")

    body: str

    calls: List[DataLatestReportDocumentIssueCall]

    check_names: List[str] = FieldInfo(alias="checkNames")

    evidence: List[DataLatestReportDocumentIssueEvidence]

    order: int

    root_cause_channel: Optional[
        Literal["PROMPT", "VOICE_CONFIG", "STT", "SPEECH_MODEL", "LLM_MODEL", "INFRA", "EXTERNAL"]
    ] = FieldInfo(alias="rootCauseChannel")

    run_labels: List[str] = FieldInfo(alias="runLabels")

    severity: Literal["HIGH", "MEDIUM", "LOW"]

    source_themes: List[DataLatestReportDocumentIssueSourceTheme] = FieldInfo(alias="sourceThemes")

    title: str


class DataLatestReportDocumentRecommendation(BaseModel):
    body: str

    channel: Optional[Literal["PROMPT", "VOICE_CONFIG", "STT", "SPEECH_MODEL", "LLM_MODEL", "INFRA", "EXTERNAL"]]

    issue_orders: List[int] = FieldInfo(alias="issueOrders")

    order: int

    title: str


class DataLatestReportDocumentRun(BaseModel):
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


class DataLatestReportDocumentScorecard(BaseModel):
    check_name: str = FieldInfo(alias="checkName")

    evaluated_count: int = FieldInfo(alias="evaluatedCount")

    failed_count: int = FieldInfo(alias="failedCount")

    failed_run_count: int = FieldInfo(alias="failedRunCount")

    pass_rate_pct: Optional[float] = FieldInfo(alias="passRatePct")

    run_count: int = FieldInfo(alias="runCount")


class DataLatestReportDocumentWentWell(BaseModel):
    body: str

    evidence: List[DataLatestReportDocumentIssueEvidence]

    title: str


class DataLatestReportDocument(BaseModel):
    """
    The group report: the runs it covers, a scorecard summed across them, what went
    well, and the issues found, each merged from the per-run debriefs with
    call-level evidence. Every figure is computed from the runs; the prose is
    AI-written around those facts.
    """

    aggregates: List[DataLatestReportDocumentAggregate]

    executive_summary: List[DataLatestReportDocumentExecutiveSummary] = FieldInfo(alias="executiveSummary")

    generated_at_iso: str = FieldInfo(alias="generatedAtIso")

    headline: DataLatestReportDocumentHeadline

    issues: List[DataLatestReportDocumentIssue]

    methodology: str

    model: str

    recommendations: List[DataLatestReportDocumentRecommendation]

    runs: List[DataLatestReportDocumentRun]

    scorecard: List[DataLatestReportDocumentScorecard]

    simulation_run_group_id: str = FieldInfo(alias="simulationRunGroupId")

    smaller_items: List[DataLatestReportDocumentIssue] = FieldInfo(alias="smallerItems")

    version: Literal[1]

    went_well: List[DataLatestReportDocumentWentWell] = FieldInfo(alias="wentWell")


class DataLatestReport(BaseModel):
    """One generation of the group report."""

    id: str

    completed_at: Optional[str] = FieldInfo(alias="completedAt")
    """ISO 8601. Null until the report settles."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    document: Optional[DataLatestReportDocument]
    """Null until the report is READY."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage")

    status: Literal["PENDING", "GENERATING", "READY", "FAILED"]
    """
    PENDING and GENERATING are in flight; READY carries the document; FAILED carries
    errorMessage.
    """


class DataRun(BaseModel):
    """One run in the group, in group order."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    ended_at: Optional[str] = FieldInfo(alias="endedAt")

    plan_name: Optional[str] = FieldInfo(alias="planName")
    """The name of the plan the run ran. Null when the plan was deleted."""

    run_number: Optional[int] = FieldInfo(alias="runNumber")
    """Per-project run number, shown as SR-42 in the app."""

    simulation_run_plan_id: str = FieldInfo(alias="simulationRunPlanId")

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")
    """The run, readable at GET /v1/simulation/plan/job/{jobId}"""

    started_at: Optional[str] = FieldInfo(alias="startedAt")

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


class Data(BaseModel):
    """Several simulation runs read as one."""

    id: str

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601"""

    latest_report: Optional[DataLatestReport] = FieldInfo(alias="latestReport")
    """The latest group report in any status. Null when none has been requested."""

    name: str

    run_count: int = FieldInfo(alias="runCount")

    runs: List[DataRun]


class SimulationRunGroupGetByIDResponse(BaseModel):
    data: Data
    """Several simulation runs read as one."""
