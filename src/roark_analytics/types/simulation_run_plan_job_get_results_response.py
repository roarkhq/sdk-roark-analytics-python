# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SimulationRunPlanJobGetResultsResponse",
    "Data",
    "DataAttemptSummary",
    "DataBreakdown",
    "DataBreakdownByAgent",
    "DataCall",
    "DataCallCheck",
    "DataCallValue",
    "DataComparison",
    "DataComparisonBaselineRun",
    "DataComparisonCheck",
    "DataDebrief",
    "DataDebriefReport",
    "DataDebriefReportExecutiveSummary",
    "DataDebriefReportExecutiveSummarySection",
    "DataDebriefReportKeyFinding",
    "DataDebriefReportRecommendation",
    "DataDebriefReportTheme",
    "DataDebriefReportTrend",
    "DataDebriefReportTrendRow",
    "DataMetric",
    "DataMetricCheck",
    "DataMetricDistribution",
    "DataMetricNumeric",
    "DataRun",
    "DataSummary",
    "DataSweepAttribution",
    "DataSweepAttributionCheck",
    "DataSweepAttributionCheckWorseValue",
    "DataSweepAttributionNeverSpokeValue",
    "DataSweepAttributionValue",
    "DataVerdict",
    "DataVerdictCheck",
    "DataVerdictFailureUnionMember0",
    "DataVerdictFailureUnionMember1",
    "DataVerdictFailureUnionMember2",
    "DataVerdictFailureUnionMember3",
    "DataVerdictFailureUnionMember4",
]


class DataAttemptSummary(BaseModel):
    """
    The run’s simulations against its test cases. Differs from a plain job count
    only when the plan retries simulations your agent never spoke on.
    """

    attempt_count: int = FieldInfo(alias="attemptCount")
    """Every simulation placed, retries included. Each is a separate, billed call."""

    retry_count: int = FieldInfo(alias="retryCount")
    """Simulations placed as a retry of one your agent never spoke on."""

    silent_attempt_count: int = FieldInfo(alias="silentAttemptCount")
    """Simulations your agent never spoke on, including the ones a retry replaced."""

    still_silent_test_case_count: int = FieldInfo(alias="stillSilentTestCaseCount")
    """
    Test cases whose final attempt your agent still never spoke on. This is what the
    `AGENT_NEVER_SPOKE` verdict failure counts.
    """

    test_case_count: int = FieldInfo(alias="testCaseCount")
    """
    Test cases in the run. Each one has a single final attempt that its result is
    read from.
    """


class DataBreakdownByAgent(BaseModel):
    call_pass_rate: Optional[float] = FieldInfo(alias="callPassRate")
    """0-100. Null when nothing was evaluated."""

    calls: int
    """Counted simulations in the group."""

    evaluated_calls: int = FieldInfo(alias="evaluatedCalls")

    key: str
    """The agent or persona ID."""

    label: str

    passed_calls: int = FieldInfo(alias="passedCalls")

    score: Optional[float]
    """The group’s own score. 0-100. Null when nothing was evaluated."""


class DataBreakdown(BaseModel):
    by_agent: List[DataBreakdownByAgent] = FieldInfo(alias="byAgent")

    by_persona: List[DataBreakdownByAgent] = FieldInfo(alias="byPersona")


class DataCallCheck(BaseModel):
    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    metric_name: str = FieldInfo(alias="metricName")

    passed: bool


class DataCallValue(BaseModel):
    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    metric_name: str = FieldInfo(alias="metricName")

    output_type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"] = FieldInfo(
        alias="outputType"
    )

    participant_role: Optional[Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"]] = FieldInfo(
        alias="participantRole"
    )

    reasoning: Optional[str]

    value: Union[float, bool, str, None]


class DataCall(BaseModel):
    agent_name: Optional[str] = FieldInfo(alias="agentName")

    attempt_number: int = FieldInfo(alias="attemptNumber")

    call_id: Optional[str] = FieldInfo(alias="callId")
    """
    Use with GET /v1/call/{callId} for the transcript, recording and every metric
    value.
    """

    checks: List[DataCallCheck]

    counted: bool
    """False for an invalidated simulation: listed, never scored."""

    duration_ms: Optional[int] = FieldInfo(alias="durationMs")

    passed: Optional[bool]
    """
    Passed every check that graded it. Null when no check graded it, or it does not
    count.
    """

    persona_name: Optional[str] = FieldInfo(alias="personaName")

    retry_of_simulation_job_id: Optional[str] = FieldInfo(alias="retryOfSimulationJobId")

    simulation_job_id: str = FieldInfo(alias="simulationJobId")

    status: Literal[
        "QUEUED",
        "CONNECTING",
        "IN_CALL",
        "PROCESSING",
        "COMPLETED",
        "ERROR",
        "TIMED_OUT",
        "CANCELLED",
        "INVALIDATED",
        "NOT_RUN",
    ]
    """
    QUEUED, CONNECTING, IN_CALL and PROCESSING while the simulation runs. Once
    settled: COMPLETED, TIMED_OUT (ran to the maximum duration, still graded), ERROR
    (failed on the agent’s side), NOT_RUN (failed on Roark’s side), CANCELLED, or
    INVALIDATED (ran, but does not count).
    """

    values: List[DataCallValue]
    """
    Call-level values of the run’s other metrics. Empty without the `metric:read`
    permission. Per-turn values are on GET /v1/call/{callId}/metrics.
    """


class DataComparisonBaselineRun(BaseModel):
    ended_at: Optional[str] = FieldInfo(alias="endedAt")

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


class DataComparisonCheck(BaseModel):
    baseline_pass_rate: Optional[float] = FieldInfo(alias="baselinePassRate")

    current_pass_rate: Optional[float] = FieldInfo(alias="currentPassRate")

    delta: Optional[float]

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    metric_name: str = FieldInfo(alias="metricName")


class DataComparison(BaseModel):
    baseline_call_pass_rate: Optional[float] = FieldInfo(alias="baselineCallPassRate")

    baseline_run: DataComparisonBaselineRun = FieldInfo(alias="baselineRun")

    baseline_score: Optional[float] = FieldInfo(alias="baselineScore")

    baseline_source: Literal["PREVIOUS_RUN", "REQUESTED"] = FieldInfo(alias="baselineSource")
    """REQUESTED when `compareToJobId` picked the baseline, PREVIOUS_RUN otherwise."""

    call_pass_rate_delta: Optional[float] = FieldInfo(alias="callPassRateDelta")

    checks: List[DataComparisonCheck]
    """Every check either run was graded on. A side that did not grade it reads null."""

    current_call_pass_rate: Optional[float] = FieldInfo(alias="currentCallPassRate")

    current_score: Optional[float] = FieldInfo(alias="currentScore")

    score_delta: Optional[float] = FieldInfo(alias="scoreDelta")
    """Current minus baseline, in points."""


class DataDebriefReportExecutiveSummarySection(BaseModel):
    body: str

    heading: Optional[str]


class DataDebriefReportExecutiveSummary(BaseModel):
    paragraphs: List[str]

    sections: List[DataDebriefReportExecutiveSummarySection]


class DataDebriefReportKeyFinding(BaseModel):
    body: str

    call_ids: List[str] = FieldInfo(alias="callIds")
    """The calls the finding is about."""

    title: str


class DataDebriefReportRecommendation(BaseModel):
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


class DataDebriefReportTheme(BaseModel):
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


class DataDebriefReportTrendRow(BaseModel):
    check_name: str = FieldInfo(alias="checkName")

    current_pass_rate: Optional[float] = FieldInfo(alias="currentPassRate")

    lifecycle: Optional[Literal["NEW", "PERSISTENT", "IMPROVING", "FIXED"]]

    previous_pass_rate: Optional[float] = FieldInfo(alias="previousPassRate")


class DataDebriefReportTrend(BaseModel):
    """The checks against the previous run, as of generation."""

    baseline_run_number: Optional[int] = FieldInfo(alias="baselineRunNumber")

    baseline_run_plan_job_id: str = FieldInfo(alias="baselineRunPlanJobId")

    rows: List[DataDebriefReportTrendRow]


class DataDebriefReport(BaseModel):
    executive_summary: DataDebriefReportExecutiveSummary = FieldInfo(alias="executiveSummary")

    generated_at: str = FieldInfo(alias="generatedAt")

    key_findings: List[DataDebriefReportKeyFinding] = FieldInfo(alias="keyFindings")

    recommendations: List[DataDebriefReportRecommendation]

    themes: List[DataDebriefReportTheme]
    """Failure themes, clustered across the run’s failing calls."""

    trend: Optional[DataDebriefReportTrend]
    """The checks against the previous run, as of generation."""

    verdict: Literal["PASSED", "THRESHOLD_FAILED"]

    verdict_summary: str = FieldInfo(alias="verdictSummary")
    """
    One-paragraph verdict, e.g. "Not ready to promote. ..."
    """

    went_well: List[DataDebriefReportKeyFinding] = FieldInfo(alias="wentWell")


class DataDebrief(BaseModel):
    """
    The run’s written debrief: executive summary, failure themes and
    recommendations. Generated automatically when a run with graded calls settles.
    """

    completed_at: Optional[str] = FieldInfo(alias="completedAt")

    created_at: str = FieldInfo(alias="createdAt")

    debrief_id: str = FieldInfo(alias="debriefId")

    error_message: Optional[str] = FieldInfo(alias="errorMessage")

    report: Optional[DataDebriefReport]
    """Present once READY."""

    status: Literal["PENDING", "GENERATING", "READY", "FAILED"]
    """
    PENDING and GENERATING while it is written (usually a few minutes), then READY
    or FAILED.
    """


class DataMetricCheck(BaseModel):
    """The check’s tally. Null for a metric that is not a check."""

    evaluated_calls: int = FieldInfo(alias="evaluatedCalls")

    failed_calls: int = FieldInfo(alias="failedCalls")

    pass_rate: Optional[float] = FieldInfo(alias="passRate")
    """0-100. Null when nothing was evaluated."""

    passed_calls: int = FieldInfo(alias="passedCalls")


class DataMetricDistribution(BaseModel):
    count: int

    value: str


class DataMetricNumeric(BaseModel):
    """
    For NUMERIC, SCALE, COUNT and OFFSET metrics. Null when nothing was captured, or
    without the `metric:read` permission.
    """

    average: float

    max: float

    median: float

    min: float

    p95: float


class DataMetric(BaseModel):
    check: Optional[DataMetricCheck]
    """The check’s tally. Null for a metric that is not a check."""

    distribution: Optional[List[DataMetricDistribution]]
    """
    How many values took each reading, for BOOLEAN, SCALE and CLASSIFICATION
    metrics. Null without the `metric:read` permission.
    """

    evaluated_calls: int = FieldInfo(alias="evaluatedCalls")
    """Counted simulations with at least one value."""

    is_check: bool = FieldInfo(alias="isCheck")
    """A threshold: one of the checks the run is judged on."""

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    metric_id: str = FieldInfo(alias="metricId")
    """The metric’s slug."""

    name: str

    numeric: Optional[DataMetricNumeric]
    """
    For NUMERIC, SCALE, COUNT and OFFSET metrics. Null when nothing was captured, or
    without the `metric:read` permission.
    """

    output_type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"] = FieldInfo(
        alias="outputType"
    )

    sample_size: int = FieldInfo(alias="sampleSize")
    """Values across those simulations. A per-turn metric has several per call."""

    unit_symbol: Optional[str] = FieldInfo(alias="unitSymbol")
    """Unit of `numeric`, e.g. `ms`."""


class DataRun(BaseModel):
    created_at: str = FieldInfo(alias="createdAt")

    duration_ms: Optional[int] = FieldInfo(alias="durationMs")
    """Wall-clock run time. Null until the run ends."""

    ended_at: Optional[str] = FieldInfo(alias="endedAt")

    run_number: Optional[int] = FieldInfo(alias="runNumber")
    """Per-project run number, shown as SR-42 in the app."""

    simulation_run_plan_id: str = FieldInfo(alias="simulationRunPlanId")

    simulation_run_plan_job_id: str = FieldInfo(alias="simulationRunPlanJobId")

    simulation_run_plan_name: Optional[str] = FieldInfo(alias="simulationRunPlanName")
    """The run plan’s name. Null when the plan has since been deleted."""

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

    triggered_by: Literal["SCHEDULED", "USER_TRIGGERED_FROM_UI", "RE_RUN", "TRIGGERED_FROM_API", "SYSTEM"] = FieldInfo(
        alias="triggeredBy"
    )


class DataSummary(BaseModel):
    call_pass_rate: Optional[float] = FieldInfo(alias="callPassRate")
    """passedCalls / evaluatedCalls, 0-100. Null when nothing was evaluated."""

    check_pass_rate: Optional[float] = FieldInfo(alias="checkPassRate")
    """
    Every (check, simulation) verdict pooled. 0-100. Null when nothing was
    evaluated.
    """

    completed_calls: int = FieldInfo(alias="completedCalls")
    """Counted simulations that connected and produced a conversation."""

    counted_calls: int = FieldInfo(alias="countedCalls")
    """Simulations whose results count: all but the invalidated ones."""

    evaluated_calls: int = FieldInfo(alias="evaluatedCalls")
    """Counted simulations at least one check graded."""

    failed_calls: int = FieldInfo(alias="failedCalls")
    """Evaluated simulations that failed at least one check."""

    passed_calls: int = FieldInfo(alias="passedCalls")
    """Evaluated simulations that passed every check."""

    score: Optional[float]
    """
    The run’s score: the mean of each check’s pass rate, the same number as
    `verdict.score`. 0-100. Null when nothing was evaluated.
    """

    total_calls: int = FieldInfo(alias="totalCalls")
    """Every simulation of the run, retries included."""


class DataSweepAttributionCheckWorseValue(BaseModel):
    """A value that failed a check significantly more often than the rest of the run."""

    adjusted_p_value: float = FieldInfo(alias="adjustedPValue")
    """
    How likely a difference at least this large would be by chance alone, after
    correcting for every comparison in the run (Benjamini-Hochberg). The value is
    called worse only when this is at most `falseDiscoveryRate`.
    """

    evaluated: int

    failed: int

    failure_rate: Optional[float] = FieldInfo(alias="failureRate")
    """Share of the counted simulations at this value that failed the check, 0-100."""

    key: str
    """
    The arm's identity: the override signature its calls ran with, e.g.
    `BACKGROUND_NOISE=DRIVING;BACKGROUND_NOISE_VOLUME=0.7`. Join on this rather than
    on `value`: a sweep can run one value as several arms (Driving at 70% and at
    100%), and those share a value.
    """

    label: str

    rest_failure_rate: Optional[float] = FieldInfo(alias="restFailureRate")
    """
    The same share across every other value combined, 0-100. This is what the value
    is compared with.
    """

    value: str


class DataSweepAttributionCheck(BaseModel):
    """How one check's failures relate to the swept property."""

    attribution: Literal["PROPERTY_ATTRIBUTABLE", "FOUND_UNATTRIBUTED", "WITHIN_NOISE"]
    """
    How this check relates to the swept property:
    - `PROPERTY_ATTRIBUTABLE`: at least one value failed it significantly more often
    than every other value combined. `worseValues` names them. This is the only case
    in which a value is called worse. - `FOUND_UNATTRIBUTED`: no value stands out,
    but the check failed on at least `foundUnattributedFailureRate`% of counted
    simulations overall. A real issue with the agent on which no value stood out, so
    the run cannot tie it to the property. It does not show the property had no
    effect: a small run may be unable to see one. - `WITHIN_NOISE`: neither. Any
    differences between values are within what chance produces.
    """

    evaluated: int

    failed: int

    failure_rate: Optional[float] = FieldInfo(alias="failureRate")
    """Share of counted simulations across every value that failed the check, 0-100."""

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    metric_name: str = FieldInfo(alias="metricName")

    worse_values: List[DataSweepAttributionCheckWorseValue] = FieldInfo(alias="worseValues")
    """
    The values significantly worse than the rest, most significant first. Empty
    unless `attribution` is `PROPERTY_ATTRIBUTABLE`.
    """


class DataSweepAttributionNeverSpokeValue(BaseModel):
    """
    A value your agent never spoke on significantly more often than the rest of the
    run.
    """

    adjusted_p_value: float = FieldInfo(alias="adjustedPValue")
    """
    How likely a difference at least this large would be by chance alone, after
    correcting across the values (Benjamini-Hochberg).
    """

    attempted: int
    """Simulations run at this value."""

    key: str
    """
    The arm's identity: the override signature its calls ran with, e.g.
    `BACKGROUND_NOISE=DRIVING;BACKGROUND_NOISE_VOLUME=0.7`. Join on this rather than
    on `value`: a sweep can run one value as several arms (Driving at 70% and at
    100%), and those share a value.
    """

    label: str

    rest_attempted: int = FieldInfo(alias="restAttempted")
    """Simulations run across every other value combined."""

    rest_silent_attempts: int = FieldInfo(alias="restSilentAttempts")
    """Simulations your agent never spoke on across every other value combined."""

    retries: int
    """Retries placed at this value because your agent never spoke."""

    silent_attempts: int = FieldInfo(alias="silentAttempts")
    """Simulations at this value your agent never spoke on, retried or not."""

    value: str


class DataSweepAttributionValue(BaseModel):
    """One value of the swept property."""

    attempted: int
    """
    Simulations run at this value. Simulations that failed on the Roark platform are
    left out, since they say nothing about your agent.
    """

    counted: int
    """
    Simulations that actually tested the property: not invalidated, and graded by at
    least one check. Only these are used in the comparison.
    """

    is_baseline: bool = FieldInfo(alias="isBaseline")
    """Whether this is the baseline the plan named."""

    key: str
    """
    The arm's identity: the override signature its calls ran with, e.g.
    `BACKGROUND_NOISE=DRIVING;BACKGROUND_NOISE_VOLUME=0.7`. Join on this rather than
    on `value`: a sweep can run one value as several arms (Driving at 70% and at
    100%), and those share a value.
    """

    label: str
    """
    The value in words, with what else the arm pinned, e.g. `American` or `Driving
    (70% noise)`.
    """

    retries: int
    """
    Of `attempted`, the retries of simulations your agent never spoke on. Zero
    unless the plan retries silent simulations.
    """

    score: Optional[float]
    """
    The mean of each check's pass rate at this value, 0-100, the same rule as the
    run's `score`. Descriptive only: a lower score alone never makes a value worse.
    Null when nothing counted.
    """

    silent_attempts: int = FieldInfo(alias="silentAttempts")
    """
    Of `attempted`, the simulations your agent never spoke on, whether or not a
    retry followed. They are invalidated, so they are never in `counted`.
    """

    testable: bool
    """
    Whether this value had at least `minArmCalls` counted simulations. A value below
    that is "insufficient data": it is reported with its numbers but never compared
    or ranked, because a rate from one or two calls cannot be told apart from luck.
    """

    value: str
    """The stored value of the swept property, e.g. `US`."""


class DataSweepAttribution(BaseModel):
    """
    For a run that swept a property (accent, background noise, speech pace and so
    on): which check failures the property caused.
    Each value is compared with every other value combined using a one-sided Fisher
    exact test, and every comparison in the run is corrected together with
    Benjamini-Hochberg. A value is only called worse when the difference is
    statistically significant, so a value that happened to fail a few more
    simulations by chance is not reported as a problem. Invalidated simulations and
    simulations that failed on the Roark platform are left out.
    """

    caveats: List[str]
    """Plain sentences on what this run could not see, ready to show to a reader."""

    checks: List[DataSweepAttributionCheck]
    """
    Every check the run was graded on: `PROPERTY_ATTRIBUTABLE` first, then
    `FOUND_UNATTRIBUTED`, then `WITHIN_NOISE`.
    """

    false_discovery_rate: float = FieldInfo(alias="falseDiscoveryRate")
    """The Benjamini-Hochberg false discovery rate the comparisons are held to."""

    found_unattributed_failure_rate: float = FieldInfo(alias="foundUnattributedFailureRate")
    """
    The overall failure rate, 0-100, at which a check with no standout value is
    reported as `FOUND_UNATTRIBUTED`.
    """

    min_arm_calls: int = FieldInfo(alias="minArmCalls")
    """Counted simulations a value needs before it is compared."""

    minimum_detectable_gap: Optional[float] = FieldInfo(alias="minimumDetectableGap")
    """
    Roughly how many percentage points more often a value would need to fail than
    the rest of the run to be flagged at this sample size. Optimistic: it uses
    simulation counts rather than the verdicts on each check and ignores the
    correction, so checks graded on fewer simulations need larger gaps. Large when
    few simulations ran per value: finding no significant difference then means the
    run could not see one, not that none exists.
    """

    never_spoke_values: List[DataSweepAttributionNeverSpokeValue] = FieldInfo(alias="neverSpokeValues")
    """
    The values your agent never spoke on significantly more often than the rest of
    the run, most significant first, tested the same way as `worseValues`. Empty on
    a run with no silent simulations.
    """

    testable_value_count: int = FieldInfo(alias="testableValueCount")
    """How many values had enough counted simulations to be compared."""

    tested_comparison_count: int = FieldInfo(alias="testedComparisonCount")
    """
    How many value and check pairs were actually tested. A value can have enough
    simulations and still go untested (no other value graded that check, or too few
    verdicts on it). When this is 0 no comparison ran, so an empty `worseValues`
    everywhere means nothing was tested, not that no value did worse.
    """

    values: List[DataSweepAttributionValue]
    """Every value of the swept property, baseline first."""


class DataVerdictCheck(BaseModel):
    """
    How one check did. Present for every check the run was judged on, passing or
    not.
    A check is a metric that yields a pass/fail: a threshold (`Silence Duration <=
    2s`) or a yes/no metric you authored. Provider readings such as `Comprehension
    Failure` are observations, not checks: their `true` is whatever the underlying
    field happens to mean, so they carry no passing side and never appear here. Put
    a threshold on one to judge it.
    """

    evaluated_sims: int = FieldInfo(alias="evaluatedSims")

    inherited: bool
    """
    Whether `minPassRate` is the 80% default (`true`) or a minimum this metric set
    for itself.
    """

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    min_pass_rate: float = FieldInfo(alias="minPassRate")
    """
    THE BAR it was judged against: the share of the run's simulations it had to
    pass.
    """

    pass_rate: Optional[float] = FieldInfo(alias="passRate")
    """
    This check's own pass rate, 0-100: the share of sims it evaluated that passed
    it. Null when it evaluated nothing.
    """

    passed: bool
    """`passRate >= minPassRate`."""

    passed_sims: int = FieldInfo(alias="passedSims")

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)


class DataVerdictFailureUnionMember0(BaseModel):
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
    """The status the run actually ended in."""

    type: Literal["RUN_NOT_COMPLETED"]


class DataVerdictFailureUnionMember1(BaseModel):
    evaluated_calls: int = FieldInfo(alias="evaluatedCalls")

    expected_calls: int = FieldInfo(alias="expectedCalls")

    type: Literal["INCOMPLETE_COVERAGE"]


class DataVerdictFailureUnionMember2(BaseModel):
    """
    Your agent never spoke on more than `maxShare` percent of the run. Those
    simulations are left out of every check, so the run fails on them whatever the
    checks say.
    """

    max_share: float = FieldInfo(alias="maxShare")
    """
    The largest share of simulations, 0-100, your agent may never speak on while the
    run can pass.
    """

    never_spoke_calls: int = FieldInfo(alias="neverSpokeCalls")
    """
    Test cases your agent never spoke on, judged on each test case’s last attempt: a
    silent simulation a retry later reached your agent on does not count here.
    """

    total_calls: int = FieldInfo(alias="totalCalls")
    """Every test case of the run whose last attempt reached your agent."""

    type: Literal["AGENT_NEVER_SPOKE"]

    agent_name: Optional[str] = FieldInfo(alias="agentName", default=None)
    """
    The agent as the run tested it. Null when the simulations tested more than one
    agent.
    """

    silent_attempts: Optional[int] = FieldInfo(alias="silentAttempts", default=None)
    """
    Every simulation your agent never spoke on, including the ones a retry replaced.
    Above `neverSpokeCalls` only when the plan retries silent simulations
    (`maxNoResponseRetries`).
    """


class DataVerdictFailureUnionMember3(BaseModel):
    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    type: Literal["METRIC_NOT_EVALUATED"]

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)
    """The check’s name, for rendering the failure."""


class DataVerdictFailureUnionMember4(BaseModel):
    inherited: bool
    """Whether the missed minimum was the 80% default (`true`) or this metric's own."""

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")

    min_pass_rate: float = FieldInfo(alias="minPassRate")

    pass_rate: float = FieldInfo(alias="passRate")

    type: Literal["METRIC_BELOW_MIN_PASS_RATE"]

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)
    """The check’s name, for rendering the failure."""


class DataVerdict(BaseModel):
    """
    Pass/fail verdict for the run, judged against the success criteria pinned on the
    run plan when the run started.
    """

    checks: List[DataVerdictCheck]
    """
    Every check the run was judged on, with its rate and the minimum it had to
    reach.
    Thresholds and authored yes/no metrics only. See `SimulationRunPlanJobCheck` for
    why a provider reading is not one.
    """

    failures: List[
        Union[
            DataVerdictFailureUnionMember0,
            DataVerdictFailureUnionMember1,
            DataVerdictFailureUnionMember2,
            DataVerdictFailureUnionMember3,
            DataVerdictFailureUnionMember4,
        ]
    ]
    """Every criterion the run missed. Empty when it passed."""

    passed: bool
    """
    Whether every check cleared its own `minPassRate` (and the run completed with
    full coverage). Use this as the CI exit status.
    Never derived from `score`: a run can score 95 and still fail, or score 40 and
    still pass.
    """

    score: Optional[float]
    """
    The run's headline quality number, 0-100: the mean of each check's own pass
    rate.
    Every check weighs the same, however many simulations it evaluated, which is the
    same way `passed` treats them. It is the number the Roark dashboard shows for
    this run.
    REPORTING ONLY, for dashboards and trend lines. Nothing is judged against it.
    Null when nothing was evaluated.
    """


class Data(BaseModel):
    """Everything the run report shows, in one response."""

    attempt_summary: DataAttemptSummary = FieldInfo(alias="attemptSummary")
    """
    The run’s simulations against its test cases. Differs from a plain job count
    only when the plan retries simulations your agent never spoke on.
    """

    breakdowns: DataBreakdown

    calls: List[DataCall]

    comparison: Optional[DataComparison]
    """Null when there is no earlier run of the plan to compare against."""

    debrief: Optional[DataDebrief]
    """
    The latest debrief. Null when none was generated, e.g. a run with no graded
    calls.
    """

    metrics: List[DataMetric]
    """Checks first, then other metrics."""

    run: DataRun

    summary: DataSummary

    sweep_attribution: Optional[DataSweepAttribution] = FieldInfo(alias="sweepAttribution")
    """
    For a run that swept a property: which values the failures concentrate on. Null
    otherwise.
    """

    verdict: Optional[DataVerdict]
    """Null until the run ends, and for a run with no check to judge."""


class SimulationRunPlanJobGetResultsResponse(BaseModel):
    data: Data
    """Everything the run report shows, in one response."""
