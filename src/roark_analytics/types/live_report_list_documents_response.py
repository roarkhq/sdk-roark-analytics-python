# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "LiveReportListDocumentsResponse",
    "Data",
    "DataItem",
    "DataItemDefinition",
    "DataItemDefinitionFilter",
    "DataItemDefinitionTarget",
    "DataItemDocument",
    "DataItemDocumentAgent",
    "DataItemDocumentAgentTarget",
    "DataItemDocumentAppendix",
    "DataItemDocumentChart",
    "DataItemDocumentChartSery",
    "DataItemDocumentChartSeryBucket",
    "DataItemDocumentCheck",
    "DataItemDocumentEvidence",
    "DataItemDocumentExecutiveSummary",
    "DataItemDocumentExecutiveSummaryKeyFinding",
    "DataItemDocumentExecutiveSummaryKeyFindingCall",
    "DataItemDocumentExecutiveSummarySection",
    "DataItemDocumentHeadline",
    "DataItemDocumentHeadlineStatTile",
    "DataItemDocumentRecommendation",
    "DataItemDocumentTarget",
    "DataItemDocumentTargetSery",
    "DataItemDocumentTheme",
    "DataItemDocumentThemeCollectorQuote",
    "DataItemDocumentThemeExcerpt",
    "DataItemDocumentThemeExcerptTurn",
    "DataItemDocumentThemeIssue",
    "DataItemDocumentVolume",
    "DataItemDocumentVolumeEnding",
]


class DataItemDefinitionFilter(BaseModel):
    type: Literal[
        "METRIC_PROPERTY", "CALL_PROPERTY", "AGENT_PROPERTY", "CALL_ID", "MODALITY", "DATASET", "METRIC_VALUE"
    ]
    """What the filter narrows on. GET /v1/analytics/schema lists each type."""

    operator: Optional[
        Literal[
            "EQUALS",
            "NOT_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "CONTAINS",
            "STARTS_WITH",
            "IS_SET",
            "IS_NOT_SET",
        ]
    ] = None
    """
    Defaults to EQUALS. IS_SET / IS_NOT_SET (CALL_PROPERTY only) keep conversations
    where the property is set, whatever the value, or missing (never sent, sent as
    null, or removed); they take no value.
    """

    property: Optional[str] = None
    """
    The property to compare. Required for CALL_PROPERTY and METRIC_PROPERTY; may be
    omitted for AGENT_PROPERTY, DATASET, MODALITY and CALL_ID.
    """

    value: Optional[Union[str, float, bool]] = None
    """
    The value to compare against (an agent id, "call" / "chat", a property value).
    Required except with IS_SET / IS_NOT_SET.
    """


class DataItemDefinitionTarget(BaseModel):
    metric: str
    """The metric's slug (e.g. `task_completion`) or id."""

    value: float
    """The bar, in display units. A PASS_RATE bar is a percentage, 0-100."""

    aggregation: Optional[Literal["PASS_RATE", "AVG", "MEDIAN", "PERCENTILE", "MIN", "MAX"]] = None
    """Defaults to PASS_RATE for thresholds and booleans, AVG for anything numeric."""

    comparator: Optional[Literal["AT_LEAST", "AT_MOST"]] = None
    """
    AT_LEAST (default for PASS_RATE) or AT_MOST (default for every other
    aggregation).
    """

    label: Optional[str] = None
    """Shown instead of the metric's name."""

    pass_operator: Optional[
        Literal[
            "EQUALS", "NOT_EQUALS", "GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO", "LESS_THAN", "LESS_THAN_OR_EQUAL_TO"
        ]
    ] = FieldInfo(alias="passOperator", default=None)
    """
    PASS_RATE on a metric that isn't a threshold: the per-call condition a call
    passes on.
    """

    pass_value: Optional[Union[str, float, bool]] = FieldInfo(alias="passValue", default=None)

    percentile: Optional[int] = None
    """Required with PERCENTILE, e.g. 95."""


class DataItemDefinition(BaseModel):
    agent_id: Optional[str] = FieldInfo(alias="agentId")

    agent_name: Optional[str] = FieldInfo(alias="agentName")

    dashboard_id: Optional[str] = FieldInfo(alias="dashboardId")

    description: Optional[str]

    filters: List[DataItemDefinitionFilter]

    include_transcript_excerpts: bool = FieldInfo(alias="includeTranscriptExcerpts")

    name: str

    targets: List[DataItemDefinitionTarget]


class DataItemDocumentAgentTarget(BaseModel):
    actual: Optional[float]

    actual_label: Optional[str] = FieldInfo(alias="actualLabel")

    key: str

    status: Literal["MET", "MISSED", "NO_DATA"]


class DataItemDocumentAgent(BaseModel):
    agent_id: str = FieldInfo(alias="agentId")

    agent_name: str = FieldInfo(alias="agentName")

    conversation_count: int = FieldInfo(alias="conversationCount")

    share_pct: float = FieldInfo(alias="sharePct")

    targets: List[DataItemDocumentAgentTarget]


class DataItemDocumentAppendix(BaseModel):
    methodology: str

    notes: List[str]


class DataItemDocumentChartSeryBucket(BaseModel):
    date: str

    value: float

    comparison_date: Optional[str] = FieldInfo(alias="comparisonDate", default=None)

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue", default=None)

    passed: Optional[float] = None

    percentage_of_baseline: Optional[float] = FieldInfo(alias="percentageOfBaseline", default=None)

    sample_size: Optional[float] = FieldInfo(alias="sampleSize", default=None)


class DataItemDocumentChartSery(BaseModel):
    aggregation: Literal["COUNT", "AVG", "MIN", "MAX", "SUM", "MEDIAN", "PERCENTILE", "PASS_RATE"]

    breakdown_value: Optional[str] = FieldInfo(alias="breakdownValue")

    buckets: List[DataItemDocumentChartSeryBucket]

    comparison_group: Optional[str] = FieldInfo(alias="comparisonGroup")

    comparison_value: Optional[float] = FieldInfo(alias="comparisonValue")

    measure_index: int = FieldInfo(alias="measureIndex")

    metric: Optional[str]

    percentage_of_baseline: Optional[float] = FieldInfo(alias="percentageOfBaseline")

    sample_size: Optional[float] = FieldInfo(alias="sampleSize")

    type: Literal["METRIC", "CONVERSATION", "UPTIME"]

    value: float


class DataItemDocumentChart(BaseModel):
    blocked: bool

    description: Optional[str]

    display: Literal["LINE", "NUMBER", "RADAR", "STACKED_BAR", "TABLE"]

    error: Optional[str]

    interval: Literal["HOUR", "DAY", "WEEK", "MONTH"]

    name: str

    omitted_series: int = FieldInfo(alias="omittedSeries")

    series: List[DataItemDocumentChartSery]


class DataItemDocumentCheck(BaseModel):
    check_name: str = FieldInfo(alias="checkName")

    comparable: bool

    delta_pts: Optional[float] = FieldInfo(alias="deltaPts")

    evaluated_count: int = FieldInfo(alias="evaluatedCount")

    failed_count: int = FieldInfo(alias="failedCount")

    is_target: bool = FieldInfo(alias="isTarget")

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    metric_slug: str = FieldInfo(alias="metricSlug")

    pass_rate_pct: Optional[float] = FieldInfo(alias="passRatePct")

    previous_pass_rate_pct: Optional[float] = FieldInfo(alias="previousPassRatePct")


class DataItemDocumentEvidence(BaseModel):
    failing_conversation_count: int = FieldInfo(alias="failingConversationCount")

    failing_count_is_lower_bound: bool = FieldInfo(alias="failingCountIsLowerBound")

    read_conversation_count: int = FieldInfo(alias="readConversationCount")

    sampled: bool


class DataItemDocumentExecutiveSummaryKeyFindingCall(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId")

    conversation_id: str = FieldInfo(alias="conversationId")

    cue_ms: Optional[int] = FieldInfo(alias="cueMs")

    persona_name: Optional[str] = FieldInfo(alias="personaName")


class DataItemDocumentExecutiveSummaryKeyFinding(BaseModel):
    body: str

    title: str

    calls: Optional[List[DataItemDocumentExecutiveSummaryKeyFindingCall]] = None


class DataItemDocumentExecutiveSummarySection(BaseModel):
    body: str

    heading: Optional[str]


class DataItemDocumentExecutiveSummary(BaseModel):
    key_findings: List[DataItemDocumentExecutiveSummaryKeyFinding] = FieldInfo(alias="keyFindings")

    paragraphs: List[str]

    sections: Optional[List[DataItemDocumentExecutiveSummarySection]] = None


class DataItemDocumentHeadlineStatTile(BaseModel):
    delta_direction: Optional[Literal["POSITIVE", "NEGATIVE", "NEUTRAL"]] = FieldInfo(alias="deltaDirection")

    label: str

    sub: Optional[str]

    value: str


class DataItemDocumentHeadline(BaseModel):
    agent_name: Optional[str] = FieldInfo(alias="agentName")

    cadence: Optional[Literal["DAILY", "WEEKLY", "MONTHLY"]]

    period_end_iso: str = FieldInfo(alias="periodEndIso")

    period_label: str = FieldInfo(alias="periodLabel")

    period_start_iso: str = FieldInfo(alias="periodStartIso")

    report_name: str = FieldInfo(alias="reportName")

    stat_tiles: List[DataItemDocumentHeadlineStatTile] = FieldInfo(alias="statTiles")

    timezone: str

    verdict: Literal["ON_TARGET", "OFF_TARGET", "NO_TARGETS", "NO_DATA"]

    verdict_prose: str = FieldInfo(alias="verdictProse")


class DataItemDocumentRecommendation(BaseModel):
    after_text: Optional[str] = FieldInfo(alias="afterText")

    before_text: Optional[str] = FieldInfo(alias="beforeText")

    body: str

    channel: Optional[Literal["PROMPT", "VOICE_CONFIG", "STT", "SPEECH_MODEL", "LLM_MODEL", "INFRA", "EXTERNAL"]]

    order: int

    prompt_optimization_finding_id: Optional[str] = FieldInfo(alias="promptOptimizationFindingId")

    severity: Optional[Literal["HIGH", "MEDIUM", "LOW"]]

    source: Literal["PROMPT_OPTIMIZER", "DEBRIEF"]

    theme_slugs: List[str] = FieldInfo(alias="themeSlugs")

    title: str


class DataItemDocumentTargetSery(BaseModel):
    date: str

    sample_size: Optional[int] = FieldInfo(alias="sampleSize")

    value: Optional[float]


class DataItemDocumentTarget(BaseModel):
    actual: Optional[float]

    actual_label: Optional[str] = FieldInfo(alias="actualLabel")

    aggregation: Literal["PASS_RATE", "AVG", "MEDIAN", "PERCENTILE", "MIN", "MAX"]

    comparator: Literal["AT_LEAST", "AT_MOST"]

    delta_direction: Optional[Literal["POSITIVE", "NEGATIVE", "NEUTRAL"]] = FieldInfo(alias="deltaDirection")

    delta_label: Optional[str] = FieldInfo(alias="deltaLabel")

    error: Optional[str]

    failing_conversation_count: Optional[int] = FieldInfo(alias="failingConversationCount")

    key: str

    label: str

    lifecycle: Optional[Literal["NEW_MISS", "STILL_MISSED", "RECOVERED", "HOLDING"]]

    metric_definition_id: Optional[str] = FieldInfo(alias="metricDefinitionId")

    metric_name: str = FieldInfo(alias="metricName")

    metric_slug: str = FieldInfo(alias="metricSlug")

    percentile: Optional[int]

    previous: Optional[float]

    previous_label: Optional[str] = FieldInfo(alias="previousLabel")

    sample_size: int = FieldInfo(alias="sampleSize")

    series: List[DataItemDocumentTargetSery]

    status: Literal["MET", "MISSED", "NO_DATA"]

    target_label: str = FieldInfo(alias="targetLabel")

    target_value: float = FieldInfo(alias="targetValue")

    unit: Literal["PERCENT", "VALUE"]


class DataItemDocumentThemeCollectorQuote(BaseModel):
    conversation_id: str = FieldInfo(alias="conversationId")

    metric_name: str = FieldInfo(alias="metricName")

    quote: str


class DataItemDocumentThemeExcerptTurn(BaseModel):
    flag_note: Optional[str] = FieldInfo(alias="flagNote")

    flagged: bool

    offset_ms: Optional[int] = FieldInfo(alias="offsetMs")

    role: Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"]

    text: str


class DataItemDocumentThemeExcerpt(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId")

    caption: Optional[str]

    conversation_id: str = FieldInfo(alias="conversationId")

    persona_name: Optional[str] = FieldInfo(alias="personaName")

    scenario_name: Optional[str] = FieldInfo(alias="scenarioName")

    turns: List[DataItemDocumentThemeExcerptTurn]


class DataItemDocumentThemeIssue(BaseModel):
    id: str

    first_seen_at_iso: Optional[str] = FieldInfo(alias="firstSeenAtIso")

    status: str

    title: str


class DataItemDocumentTheme(BaseModel):
    affected_conversation_count: int = FieldInfo(alias="affectedConversationCount")

    analysis: str

    check_names: List[str] = FieldInfo(alias="checkNames")

    collector_quote: Optional[DataItemDocumentThemeCollectorQuote] = FieldInfo(alias="collectorQuote")

    estimated_affected_conversation_count: Optional[int] = FieldInfo(alias="estimatedAffectedConversationCount")

    excerpts: List[DataItemDocumentThemeExcerpt]

    flagged_for_impact: bool = FieldInfo(alias="flaggedForImpact")

    impact: Optional[Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"]]

    impact_reason: Optional[str] = FieldInfo(alias="impactReason")

    issue: Optional[DataItemDocumentThemeIssue]

    lifecycle: Optional[Literal["NEW", "PERSISTENT", "IMPROVING", "FIXED"]]

    member_conversation_ids: List[str] = FieldInfo(alias="memberConversationIds")

    metric_definition_ids: List[str] = FieldInfo(alias="metricDefinitionIds")

    prevalence: Optional[Literal["WIDESPREAD", "RECURRING", "ISOLATED"]]

    root_cause_channel: Optional[
        Literal["PROMPT", "VOICE_CONFIG", "STT", "SPEECH_MODEL", "LLM_MODEL", "INFRA", "EXTERNAL"]
    ] = FieldInfo(alias="rootCauseChannel")

    severity: Literal["HIGH", "MEDIUM", "LOW"]

    slug: str

    title: str

    total_conversation_count: int = FieldInfo(alias="totalConversationCount")

    member_calls: Optional[List[DataItemDocumentExecutiveSummaryKeyFindingCall]] = FieldInfo(
        alias="memberCalls", default=None
    )


class DataItemDocumentVolumeEnding(BaseModel):
    count: int

    label: str

    share_pct: float = FieldInfo(alias="sharePct")

    value: str


class DataItemDocumentVolume(BaseModel):
    conversation_count: int = FieldInfo(alias="conversationCount")

    delta_pct: Optional[float] = FieldInfo(alias="deltaPct")

    endings: List[DataItemDocumentVolumeEnding]

    previous_conversation_count: Optional[int] = FieldInfo(alias="previousConversationCount")

    series: List[DataItemDocumentTargetSery]


class DataItemDocument(BaseModel):
    agents: List[DataItemDocumentAgent]

    appendix: DataItemDocumentAppendix

    charts: List[DataItemDocumentChart]

    checks: List[DataItemDocumentCheck]

    evidence: DataItemDocumentEvidence

    executive_summary: DataItemDocumentExecutiveSummary = FieldInfo(alias="executiveSummary")

    generated_at_iso: str = FieldInfo(alias="generatedAtIso")

    headline: DataItemDocumentHeadline

    live_report_id: Optional[str] = FieldInfo(alias="liveReportId")

    model: str

    recommendations: List[DataItemDocumentRecommendation]

    targets: List[DataItemDocumentTarget]

    themes: List[DataItemDocumentTheme]

    version: Literal[1]

    volume: DataItemDocumentVolume


class DataItem(BaseModel):
    """
    One written report over one period. `document` is null until `status` is READY;
    every number in it comes from the analytics engine (the same reads GET
    /v1/dashboard/{dashboardId}/data makes over the same window and filters).
    """

    id: str

    announced_at: Optional[str] = FieldInfo(alias="announcedAt")

    cadence: Optional[Literal["DAILY", "WEEKLY", "MONTHLY"]]

    completed_at: Optional[str] = FieldInfo(alias="completedAt")

    created_at: str = FieldInfo(alias="createdAt")

    definition: DataItemDefinition

    document: Optional[DataItemDocument]

    error_message: Optional[str] = FieldInfo(alias="errorMessage")

    live_report_id: Optional[str] = FieldInfo(alias="liveReportId")

    period_end: str = FieldInfo(alias="periodEnd")

    period_start: str = FieldInfo(alias="periodStart")

    project_id: str = FieldInfo(alias="projectId")

    status: Literal["PENDING", "GENERATING", "READY", "FAILED"]

    timezone: str

    trigger: Literal["SCHEDULED", "MANUAL"]


class Data(BaseModel):
    items: List[DataItem]

    total_count: int = FieldInfo(alias="totalCount")


class LiveReportListDocumentsResponse(BaseModel):
    data: Data
