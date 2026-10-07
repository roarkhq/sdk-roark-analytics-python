# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional, overload
from typing_extensions import Literal

import httpx

from ..types import (
    simulation_run_plan_list_params,
    simulation_run_plan_create_params,
    simulation_run_plan_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.simulation_run_plan_list_response import SimulationRunPlanListResponse
from ..types.simulation_run_plan_create_response import SimulationRunPlanCreateResponse
from ..types.simulation_run_plan_delete_response import SimulationRunPlanDeleteResponse
from ..types.simulation_run_plan_update_response import SimulationRunPlanUpdateResponse
from ..types.simulation_run_plan_get_by_id_response import SimulationRunPlanGetByIDResponse

__all__ = ["SimulationRunPlanResource", "AsyncSimulationRunPlanResource"]


class SimulationRunPlanResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationRunPlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationRunPlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationRunPlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationRunPlanResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        max_simulation_duration_seconds: int,
        name: str,
        auto_run: bool | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_property: Optional[
            Literal[
                "ACCENT",
                "AGE",
                "BACKGROUND_NOISE",
                "BACKGROUND_NOISE_VOLUME",
                "BASE_EMOTION",
                "CONFIRMATION_STYLE",
                "GENDER",
                "INTENT_CLARITY",
                "LANGUAGE",
                "INTERRUPTION",
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: List[Union[str, simulation_run_plan_create_params.ComparisonArm]] | Omit = omit,
        description: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigFlow] | Omit = omit,
        include_automatic_metrics: bool | Omit = omit,
        include_flow_metrics: bool | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigMetric] | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        personas: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigScenario] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanCreateResponse:
        """Creates a new simulation run plan.

        To run a simulation, use POST
        /v1/simulation/run instead: it starts a run from a plan or from an inline
        configuration, and takes runtime variables. Create a plan here when you want a
        reusable, named one to run later. Send `template` instead of a full
        configuration to save one of the built-in templates as a plan. It takes the same
        fields as the template variant of POST /v1/simulation/run, builds the same plan,
        and never starts it. To compare one property, attach the flow once and send
        `comparisonProperty` with the `comparisonValues` to run: the plan attaches the
        flow once per value.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          name: Name of the run plan

          auto_run: Deprecated: use POST /v1/simulation/run, which starts a run and accepts runtime
              `variables` as well. This flag runs the plan with only the values pinned on it.

          comparison_baseline: The reference value of `comparisonProperty`, for example `NONE` for
              `BACKGROUND_NOISE` or `NORMAL` for `SPEECH_PACE`: shown first in the results.
              Must be a value that property can take. Whether a value did significantly worse
              does not depend on it: that is decided against every other value combined (see
              `sweepAttribution`). Stored rather than assumed, so the report can say "compared
              against US accent" instead of implying Roark decided which value is normal. Omit
              it and the property's own norm is used, as the dashboard prefills it, or none
              when your `comparisonValues` leave the norm out. `GENDER` has no norm, so choose
              the one you are testing against.

          comparison_property: The property this run plan investigates: the one thing its arms differ by. Set
              it and the run report compares the arms on that property, so a run answers "what
              did background noise cost" rather than just "what did each arm score". Every
              value is a field already recorded on each call, so the report can label an arm
              `CRYING_BABY` rather than repeating a flow variant's title. Omit it and the
              report still compares when it can: it detects which property varies across the
              arms. Setting it is what tells the written summary what you were trying to find
              out, which detection cannot infer.

          comparison_values: The arms to run, for a plan that sweeps `comparisonProperty`. This is what the
              plan costs: the flow is attached once per arm, so ten arms is ten times the
              calls of one. Attach each flow once, as you would without a comparison: the plan
              builds the arms, running the happy path or edge cases you selected under every
              arm. Built arms need at least 5 calls per arm (`iterationCount` times the test
              cases per arm), or the plan is refused with `400`. Flows that all carry
              `overrides` on `comparisonProperty` already are the arms and are kept as you
              wrote them; a mix of flows with and without one is refused. Each entry is one
              arm. A bare value runs it plain: `"CITY"`. An object runs the value with
              something pinned on that arm only, such as a noise level per bed: `{ "value":
              "OFFICE", "backgroundNoiseVolume": 0.6 }` plays OFFICE at 60% while the other
              beds keep the default. List a value more than once with different pins to run it
              as several arms: DRIVING at 0.7 and DRIVING at 1 are two arms, reported as
              `Driving (70% noise)` and `Driving (100% noise)`, and `"DRIVING"` beside them
              keeps the plain arm too. The sweep still varies one property; what an arm pins
              is part of "everything else" for that arm only, so the report still compares the
              arms on `comparisonProperty`. Omit it to run every value the property has,
              plain, which for `ACCENT` is more than twenty. A `comparisonBaseline` outside
              the values listed is rejected, because it would anchor every difference to an
              arm the run never made. A value the property cannot take, a pin the sweep cannot
              account for, or the same arm listed twice is rejected with `400`. Not stored as
              a field: the arms are the values. Reading the plan back returns them as its flow
              attachments, each with its pins as `overrides`.

          description: Description of the run plan

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          end_call_reasons: Semantic conditions that trigger end of call. The LLM evaluates the conversation
              against these conditions. Empty array disables the feature.

          enrich_with_live_conversation: Merge the customer's own recording of the real call into each simulation, so
              metrics can be scored against the live leg as well as the simulated one. This is
              the API equivalent of the dashboard's live-enrichment toggle. With this on, the
              run provisions a phone number and holds each call open for up to 15 minutes
              waiting for a matching call to be posted to POST /v1/call. A call matches on the
              provisioned number (`roarkPhoneNumber` on the job) with a start time inside the
              simulation window. If nothing arrives, the simulation still completes and any
              `LIVE`-sourced metric produces no value. Required by any metric whose
              `requiresLiveConversation` is true: without it that metric is silently skipped.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          flows: Customer flows to include in this run plan. The same flow can appear more than
              once with a different persona override, different variables, or different
              `overrides`: attaching it once per value of one property is how you compare that
              property without a template.

          include_automatic_metrics: Let the run add metrics by itself off the attached flows, on top of the
              `metrics` named here. Two attach this way today: Agent Expectations wherever an
              attached flow has agent expectations written on it, and Keypad Entry wherever
              one has steps where the agent is expected to press keys. Both grade something
              authored on the flow that nothing else measures, which is why it is on by
              default. Set false when the `metrics` list is meant to be exhaustive: a plan
              testing only whether the caller can complete the flow may not want the agent
              graded on its expectations as well. False also pins the plan against any
              automatic metric Roark adds later.

          include_flow_metrics: Also collect each attached flow's own metrics, on top of the `metrics` named
              here. Default true, which is what you want when you brought your own flows and
              their graders. Set false for a run whose metric list is meant to be exhaustive:
              a template like Load Testing or Voicemail deliberately grades a narrow set, and
              inheriting every flow metric on top multiplies analysis cost across the volume
              without adding signal. GET /v1/simulation/template returns the value each
              template expects.

          iteration_count: Number of iterations to run for each test case (1-10000)

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_no_response_retries: How many more times to run a test case when the agent under test never responds:
              it never speaks on a call or never replies in a chat (0-10). 0 turns retries
              off. Failed checks and failures on Roark’s side are never retried. Each retry is
              a separate attempt, billed like any other, so a plan retrying N times can place
              up to N + 1 calls per test case. Every silent attempt stays on the run with its
              own call; the run settles once each test case has a final attempt, and the agent
              never spoke verdict is judged on each test case’s last attempt.

          metrics: Metric definitions to include in this run plan. Reference each by `id` (UUID) or
              `slug`. Optional when the attached `flows` carry the grading: metrics a flow
              declares itself (with `includeFlowMetrics`), or the Agent Expectations and
              Keypad Entry metrics a run adds for flows with expectations or expected keypad
              entries (with `includeAutomaticMetrics`). A plan with nothing to grade is
              rejected with a 400.

          no_response_retry_backoff_seconds: Seconds a retry waits before it dials (30-600). Only used when
              `maxNoResponseRetries` is above 0.

          personas: Personas to include in this run plan. Required with `scenarios`; ignored with
              `flows`, where each variant carries its own persona.

          scenarios: Deprecated: use `flows` instead. Scenarios to include in this run plan. The same
              scenario ID can appear multiple times with different variables.

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        template: str,
        additional_metrics: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigMetric] | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_values: List[Union[str, simulation_run_plan_create_params.ComparisonArm]] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        environment_id: str | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        persona_id: str | Omit = omit,
        questions: Iterable[simulation_run_plan_create_params.CreateRunPlanFromTemplateQuestion] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanCreateResponse:
        """Creates a new simulation run plan.

        To run a simulation, use POST
        /v1/simulation/run instead: it starts a run from a plan or from an inline
        configuration, and takes runtime variables. Create a plan here when you want a
        reusable, named one to run later. Send `template` instead of a full
        configuration to save one of the built-in templates as a plan. It takes the same
        fields as the template variant of POST /v1/simulation/run, builds the same plan,
        and never starts it. To compare one property, attach the flow once and send
        `comparisonProperty` with the `comparisonValues` to run: the plan attaches the
        flow once per value.

        Args:
          agent_endpoints: The agent endpoints to call. No template can know these.

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          template: The template to run, as listed by GET /v1/simulation/template.

          additional_metrics: Metrics to collect on top of the template's own, referenced by `id` or `slug`
              like a plan's `metrics`. The template's metrics and checks always run; naming
              one of them here again keeps it once, with the success criteria you set on it.

          comparison_baseline: The sweep's reference value, shown first in the results. Defaults to the
              template's own baseline, as returned by GET /v1/simulation/template. Whether a
              value did significantly worse does not depend on it: that is decided against
              every other value combined. Send it with `comparisonValues` and it must be one
              of them, or the request is rejected: anchoring every difference to an arm the
              run never made would measure it against nothing. Leave it out and the template's
              own baseline is used, and quietly dropped if your narrowing excluded it, since
              that one you did not choose.

          comparison_values: The arms of the sweep to run, for a template that sweeps one (GET
              /v1/simulation/template returns `sweep.property` for those that do). This is
              what the run costs: the flow is called once per arm, so ten arms is ten times
              the calls of one. Omit it to run every value the property has, plain, which for
              `accent-handling` is more than twenty. Send a subset to narrow it, for example
              the three accents you actually serve. An object entry pins something on that arm
              only, such as a noise level per bed on `background-noise-robustness`: `{
              "value": "OFFICE", "backgroundNoiseVolume": 0.6 }` plays OFFICE at 60% while the
              other beds keep the default. See `POST /v1/simulation/plan`.

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          end_call_reasons: Semantic conditions that trigger end of call. The LLM evaluates the conversation
              against these conditions. Defaults to the template's `defaultEndCallReasons`, as
              returned by GET /v1/simulation/template. Pass an empty array to run with none.

          enrich_with_live_conversation: Merge the customer's own recording of the real call into each simulation, so
              metrics can be scored against the live leg as well as the simulated one. This is
              the API equivalent of the dashboard's live-enrichment toggle. With this on, the
              run provisions a phone number and holds each call open for up to 15 minutes
              waiting for a matching call to be posted to POST /v1/call. A call matches on the
              provisioned number (`roarkPhoneNumber` on the job) with a start time inside the
              simulation window. If nothing arrives, the simulation still completes and any
              `LIVE`-sourced metric produces no value. Required by any metric whose
              `requiresLiveConversation` is true: without it that metric is silently skipped.

          environment_id: For `question-answer-check`: the environment the calls run in.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          flows: The flows to run, in the same shape a run plan takes them. Required when the
              template lists no flows of its own: it presets what to measure, and this says
              what to measure it on. Optional when it does, where these REPLACE the ones it
              would have run, so you can narrow a suite to the cases you care about. Either
              way, GET /v1/simulation/template lists the flows and variant ids each template
              covers. On a template that sweeps a property, every value runs exactly what you
              select here: the happy path, the edge cases you name, or `edgeCases: "ALL"`.
              Each selected case is a call per value per iteration, so naming three edge cases
              triples the run.

          iteration_count: Runs per test case (1-10000). Defaults to 1, or to 6 for a template that sweeps
              a property. A sweep needs at least 5 calls per value (test cases per value times
              iterations) to compare its values, and a lower count is refused with 400.

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_no_response_retries: How many more times to run a test case when the agent under test never responds:
              it never speaks on a call or never replies in a chat (0-10). 0 turns retries
              off. Failed checks and failures on Roark’s side are never retried. Each retry is
              a separate attempt, billed like any other, so a plan retrying N times can place
              up to N + 1 calls per test case. Every silent attempt stays on the run with its
              own call; the run settles once each test case has a final attempt, and the agent
              never spoke verdict is judged on each test case’s last attempt.

          max_simulation_duration_seconds: Defaults to the template's `defaultMaxSimulationDurationSeconds`, as returned by
              GET /v1/simulation/template.

          name: Name of the run plan. Defaults to the template's name and the date.

          no_response_retry_backoff_seconds: Seconds a retry waits before it dials (30-600). Only used when
              `maxNoResponseRetries` is above 0.

          persona_id: For `question-answer-check`: the persona that asks the questions.

          questions: For the `question-answer-check` template: the questions to ask and the answer
              expected for each. Every question runs as its own graded call.

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["agent_endpoints", "direction", "max_simulation_duration_seconds", "name"],
        ["agent_endpoints", "direction", "template"],
    )
    def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        auto_run: bool | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_property: Optional[
            Literal[
                "ACCENT",
                "AGE",
                "BACKGROUND_NOISE",
                "BACKGROUND_NOISE_VOLUME",
                "BASE_EMOTION",
                "CONFIRMATION_STYLE",
                "GENDER",
                "INTENT_CLARITY",
                "LANGUAGE",
                "INTERRUPTION",
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: List[Union[str, simulation_run_plan_create_params.ComparisonArm]] | Omit = omit,
        description: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigFlow] | Omit = omit,
        include_automatic_metrics: bool | Omit = omit,
        include_flow_metrics: bool | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigMetric] | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        personas: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigScenario] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        template: str | Omit = omit,
        additional_metrics: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigMetric] | Omit = omit,
        environment_id: str | Omit = omit,
        persona_id: str | Omit = omit,
        questions: Iterable[simulation_run_plan_create_params.CreateRunPlanFromTemplateQuestion] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanCreateResponse:
        return self._post(
            "/v1/simulation/plan",
            body=maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "name": name,
                    "auto_run": auto_run,
                    "comparison_baseline": comparison_baseline,
                    "comparison_property": comparison_property,
                    "comparison_values": comparison_values,
                    "description": description,
                    "end_call_phrases": end_call_phrases,
                    "end_call_reasons": end_call_reasons,
                    "enrich_with_live_conversation": enrich_with_live_conversation,
                    "execution_mode": execution_mode,
                    "flows": flows,
                    "include_automatic_metrics": include_automatic_metrics,
                    "include_flow_metrics": include_flow_metrics,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_no_response_retries": max_no_response_retries,
                    "metrics": metrics,
                    "no_response_retry_backoff_seconds": no_response_retry_backoff_seconds,
                    "personas": personas,
                    "scenarios": scenarios,
                    "silence_timeout_seconds": silence_timeout_seconds,
                    "template": template,
                    "additional_metrics": additional_metrics,
                    "environment_id": environment_id,
                    "persona_id": persona_id,
                    "questions": questions,
                },
                simulation_run_plan_create_params.SimulationRunPlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanCreateResponse,
        )

    def update(
        self,
        plan_id: str,
        *,
        agent_endpoints: Iterable[simulation_run_plan_update_params.AgentEndpoint] | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_property: Optional[
            Literal[
                "ACCENT",
                "AGE",
                "BACKGROUND_NOISE",
                "BACKGROUND_NOISE_VOLUME",
                "BASE_EMOTION",
                "CONFIRMATION_STYLE",
                "GENDER",
                "INTENT_CLARITY",
                "LANGUAGE",
                "INTERRUPTION",
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: List[Union[str, simulation_run_plan_update_params.ComparisonArm]] | Omit = omit,
        description: str | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_update_params.Flow] | Omit = omit,
        include_automatic_metrics: bool | Omit = omit,
        include_flow_metrics: bool | Omit = omit,
        is_hidden: bool | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_update_params.Metric] | Omit = omit,
        name: str | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        personas: Iterable[simulation_run_plan_update_params.AgentEndpoint] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_update_params.Scenario] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanUpdateResponse:
        """
        Updates an existing simulation run plan by its ID.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          comparison_baseline: The reference value, shown first in the results. See `POST /v1/simulation/plan`.
              A real value cannot be sent on its own: the property it belongs to decides which
              values are legal, and an omitted property means "leave unchanged", which this
              endpoint cannot check a baseline against. Send `comparisonProperty` with it, or
              get a `400`. `null` on its own IS allowed, and clears just the baseline while
              leaving the property set. Nothing needs validating when clearing, and a property
              with no baseline is a real state: the report falls back to that property's own
              norm, and `GENDER` has no norm to fall back to.

          comparison_property: The property this plan investigates. Send `null` to clear the comparison; omit
              the field to leave it unchanged. See `POST /v1/simulation/plan`. The pair moves
              together. Sending `comparisonProperty` without `comparisonBaseline` keeps the
              stored baseline when the property is unchanged and the baseline is still one of
              the values being run. Otherwise it becomes the new property's norm, or `null`
              when that norm is not being run either, because a baseline is a value of one
              specific property.

          comparison_values: The arms to run. See `POST /v1/simulation/plan`. Omitting it keeps the arms the
              plan already has, pins included, so an edit that only renames the plan never
              widens a sweep you deliberately narrowed, and never multiplies what it costs.
              Send it with `comparisonProperty` and `flows`, which the arms are rebuilt from.

          description: Description of the run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          end_call_reasons: Semantic conditions that trigger end of call. The LLM evaluates the conversation
              against these conditions. Empty array disables the feature.

          enrich_with_live_conversation: Whether to merge the customer's own live recording into each simulation of this
              plan.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          flows: Replaces the customer flows attached to this run plan. Omit to leave them
              unchanged; send an empty array to detach them all.

          include_automatic_metrics: Whether to let the run add metrics by itself off the attached flows. See `POST
              /v1/simulation/plan`.

          include_flow_metrics: Whether to also collect each attached flow's own metrics, on top of this plan's
              list.

          is_hidden: Whether this plan is hidden from GET /v1/simulation/plan. A run started without
              `saveAsPlan` creates a hidden plan to carry it. Send `{ "name": "...",
              "isHidden": false }` to keep that configuration as a reusable plan, which is
              what the app does when you save a one-off run.

          iteration_count: Number of iterations to run for each test case (1-10000)

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_no_response_retries: How many more times to run a test case when the agent under test never responds:
              it never speaks on a call or never replies in a chat (0-10). 0 turns retries
              off. Failed checks and failures on Roark’s side are never retried. Each retry is
              a separate attempt, billed like any other, so a plan retrying N times can place
              up to N + 1 calls per test case. Every silent attempt stays on the run with its
              own call; the run settles once each test case has a final attempt, and the agent
              never spoke verdict is judged on each test case’s last attempt.

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan. Reference each by `id` (UUID) or
              `slug`.

          name: Name of the run plan

          no_response_retry_backoff_seconds: Seconds a retry waits before it dials (30-600). Only used when
              `maxNoResponseRetries` is above 0.

          personas: Personas to include in this run plan

          scenarios: Deprecated: use `flows` instead. Replaces the scenarios on this run plan. Omit
              to leave them unchanged; send an empty array to detach them all, which is how a
              scenario-based plan is moved over to flows.

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._put(
            f"/v1/simulation/plan/{plan_id}",
            body=maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "comparison_baseline": comparison_baseline,
                    "comparison_property": comparison_property,
                    "comparison_values": comparison_values,
                    "description": description,
                    "direction": direction,
                    "end_call_phrases": end_call_phrases,
                    "end_call_reasons": end_call_reasons,
                    "enrich_with_live_conversation": enrich_with_live_conversation,
                    "execution_mode": execution_mode,
                    "flows": flows,
                    "include_automatic_metrics": include_automatic_metrics,
                    "include_flow_metrics": include_flow_metrics,
                    "is_hidden": is_hidden,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_no_response_retries": max_no_response_retries,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
                    "name": name,
                    "no_response_retry_backoff_seconds": no_response_retry_backoff_seconds,
                    "personas": personas,
                    "scenarios": scenarios,
                    "silence_timeout_seconds": silence_timeout_seconds,
                },
                simulation_run_plan_update_params.SimulationRunPlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanListResponse:
        """Returns a paginated list of simulation run plans.

        Optionally filter by search
        text or agent ID.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          agent_id: Filter run plans by agent ID

          limit: Maximum number of run plans to return (default: 20, max: 50)

          search_text: Search text to filter run plans by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/plan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "limit": limit,
                        "search_text": search_text,
                    },
                    simulation_run_plan_list_params.SimulationRunPlanListParams,
                ),
            ),
            cast_to=SimulationRunPlanListResponse,
        )

    def delete(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanDeleteResponse:
        """
        Soft-deletes a simulation run plan by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._delete(
            f"/v1/simulation/plan/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanDeleteResponse,
        )

    def get_by_id(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanGetByIDResponse:
        """
        Returns a specific simulation run plan by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get(
            f"/v1/simulation/plan/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanGetByIDResponse,
        )


class AsyncSimulationRunPlanResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationRunPlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationRunPlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationRunPlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationRunPlanResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        max_simulation_duration_seconds: int,
        name: str,
        auto_run: bool | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_property: Optional[
            Literal[
                "ACCENT",
                "AGE",
                "BACKGROUND_NOISE",
                "BACKGROUND_NOISE_VOLUME",
                "BASE_EMOTION",
                "CONFIRMATION_STYLE",
                "GENDER",
                "INTENT_CLARITY",
                "LANGUAGE",
                "INTERRUPTION",
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: List[Union[str, simulation_run_plan_create_params.ComparisonArm]] | Omit = omit,
        description: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigFlow] | Omit = omit,
        include_automatic_metrics: bool | Omit = omit,
        include_flow_metrics: bool | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigMetric] | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        personas: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigScenario] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanCreateResponse:
        """Creates a new simulation run plan.

        To run a simulation, use POST
        /v1/simulation/run instead: it starts a run from a plan or from an inline
        configuration, and takes runtime variables. Create a plan here when you want a
        reusable, named one to run later. Send `template` instead of a full
        configuration to save one of the built-in templates as a plan. It takes the same
        fields as the template variant of POST /v1/simulation/run, builds the same plan,
        and never starts it. To compare one property, attach the flow once and send
        `comparisonProperty` with the `comparisonValues` to run: the plan attaches the
        flow once per value.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          name: Name of the run plan

          auto_run: Deprecated: use POST /v1/simulation/run, which starts a run and accepts runtime
              `variables` as well. This flag runs the plan with only the values pinned on it.

          comparison_baseline: The reference value of `comparisonProperty`, for example `NONE` for
              `BACKGROUND_NOISE` or `NORMAL` for `SPEECH_PACE`: shown first in the results.
              Must be a value that property can take. Whether a value did significantly worse
              does not depend on it: that is decided against every other value combined (see
              `sweepAttribution`). Stored rather than assumed, so the report can say "compared
              against US accent" instead of implying Roark decided which value is normal. Omit
              it and the property's own norm is used, as the dashboard prefills it, or none
              when your `comparisonValues` leave the norm out. `GENDER` has no norm, so choose
              the one you are testing against.

          comparison_property: The property this run plan investigates: the one thing its arms differ by. Set
              it and the run report compares the arms on that property, so a run answers "what
              did background noise cost" rather than just "what did each arm score". Every
              value is a field already recorded on each call, so the report can label an arm
              `CRYING_BABY` rather than repeating a flow variant's title. Omit it and the
              report still compares when it can: it detects which property varies across the
              arms. Setting it is what tells the written summary what you were trying to find
              out, which detection cannot infer.

          comparison_values: The arms to run, for a plan that sweeps `comparisonProperty`. This is what the
              plan costs: the flow is attached once per arm, so ten arms is ten times the
              calls of one. Attach each flow once, as you would without a comparison: the plan
              builds the arms, running the happy path or edge cases you selected under every
              arm. Built arms need at least 5 calls per arm (`iterationCount` times the test
              cases per arm), or the plan is refused with `400`. Flows that all carry
              `overrides` on `comparisonProperty` already are the arms and are kept as you
              wrote them; a mix of flows with and without one is refused. Each entry is one
              arm. A bare value runs it plain: `"CITY"`. An object runs the value with
              something pinned on that arm only, such as a noise level per bed: `{ "value":
              "OFFICE", "backgroundNoiseVolume": 0.6 }` plays OFFICE at 60% while the other
              beds keep the default. List a value more than once with different pins to run it
              as several arms: DRIVING at 0.7 and DRIVING at 1 are two arms, reported as
              `Driving (70% noise)` and `Driving (100% noise)`, and `"DRIVING"` beside them
              keeps the plain arm too. The sweep still varies one property; what an arm pins
              is part of "everything else" for that arm only, so the report still compares the
              arms on `comparisonProperty`. Omit it to run every value the property has,
              plain, which for `ACCENT` is more than twenty. A `comparisonBaseline` outside
              the values listed is rejected, because it would anchor every difference to an
              arm the run never made. A value the property cannot take, a pin the sweep cannot
              account for, or the same arm listed twice is rejected with `400`. Not stored as
              a field: the arms are the values. Reading the plan back returns them as its flow
              attachments, each with its pins as `overrides`.

          description: Description of the run plan

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          end_call_reasons: Semantic conditions that trigger end of call. The LLM evaluates the conversation
              against these conditions. Empty array disables the feature.

          enrich_with_live_conversation: Merge the customer's own recording of the real call into each simulation, so
              metrics can be scored against the live leg as well as the simulated one. This is
              the API equivalent of the dashboard's live-enrichment toggle. With this on, the
              run provisions a phone number and holds each call open for up to 15 minutes
              waiting for a matching call to be posted to POST /v1/call. A call matches on the
              provisioned number (`roarkPhoneNumber` on the job) with a start time inside the
              simulation window. If nothing arrives, the simulation still completes and any
              `LIVE`-sourced metric produces no value. Required by any metric whose
              `requiresLiveConversation` is true: without it that metric is silently skipped.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          flows: Customer flows to include in this run plan. The same flow can appear more than
              once with a different persona override, different variables, or different
              `overrides`: attaching it once per value of one property is how you compare that
              property without a template.

          include_automatic_metrics: Let the run add metrics by itself off the attached flows, on top of the
              `metrics` named here. Two attach this way today: Agent Expectations wherever an
              attached flow has agent expectations written on it, and Keypad Entry wherever
              one has steps where the agent is expected to press keys. Both grade something
              authored on the flow that nothing else measures, which is why it is on by
              default. Set false when the `metrics` list is meant to be exhaustive: a plan
              testing only whether the caller can complete the flow may not want the agent
              graded on its expectations as well. False also pins the plan against any
              automatic metric Roark adds later.

          include_flow_metrics: Also collect each attached flow's own metrics, on top of the `metrics` named
              here. Default true, which is what you want when you brought your own flows and
              their graders. Set false for a run whose metric list is meant to be exhaustive:
              a template like Load Testing or Voicemail deliberately grades a narrow set, and
              inheriting every flow metric on top multiplies analysis cost across the volume
              without adding signal. GET /v1/simulation/template returns the value each
              template expects.

          iteration_count: Number of iterations to run for each test case (1-10000)

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_no_response_retries: How many more times to run a test case when the agent under test never responds:
              it never speaks on a call or never replies in a chat (0-10). 0 turns retries
              off. Failed checks and failures on Roark’s side are never retried. Each retry is
              a separate attempt, billed like any other, so a plan retrying N times can place
              up to N + 1 calls per test case. Every silent attempt stays on the run with its
              own call; the run settles once each test case has a final attempt, and the agent
              never spoke verdict is judged on each test case’s last attempt.

          metrics: Metric definitions to include in this run plan. Reference each by `id` (UUID) or
              `slug`. Optional when the attached `flows` carry the grading: metrics a flow
              declares itself (with `includeFlowMetrics`), or the Agent Expectations and
              Keypad Entry metrics a run adds for flows with expectations or expected keypad
              entries (with `includeAutomaticMetrics`). A plan with nothing to grade is
              rejected with a 400.

          no_response_retry_backoff_seconds: Seconds a retry waits before it dials (30-600). Only used when
              `maxNoResponseRetries` is above 0.

          personas: Personas to include in this run plan. Required with `scenarios`; ignored with
              `flows`, where each variant carries its own persona.

          scenarios: Deprecated: use `flows` instead. Scenarios to include in this run plan. The same
              scenario ID can appear multiple times with different variables.

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        template: str,
        additional_metrics: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigMetric] | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_values: List[Union[str, simulation_run_plan_create_params.ComparisonArm]] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        environment_id: str | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        persona_id: str | Omit = omit,
        questions: Iterable[simulation_run_plan_create_params.CreateRunPlanFromTemplateQuestion] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanCreateResponse:
        """Creates a new simulation run plan.

        To run a simulation, use POST
        /v1/simulation/run instead: it starts a run from a plan or from an inline
        configuration, and takes runtime variables. Create a plan here when you want a
        reusable, named one to run later. Send `template` instead of a full
        configuration to save one of the built-in templates as a plan. It takes the same
        fields as the template variant of POST /v1/simulation/run, builds the same plan,
        and never starts it. To compare one property, attach the flow once and send
        `comparisonProperty` with the `comparisonValues` to run: the plan attaches the
        flow once per value.

        Args:
          agent_endpoints: The agent endpoints to call. No template can know these.

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          template: The template to run, as listed by GET /v1/simulation/template.

          additional_metrics: Metrics to collect on top of the template's own, referenced by `id` or `slug`
              like a plan's `metrics`. The template's metrics and checks always run; naming
              one of them here again keeps it once, with the success criteria you set on it.

          comparison_baseline: The sweep's reference value, shown first in the results. Defaults to the
              template's own baseline, as returned by GET /v1/simulation/template. Whether a
              value did significantly worse does not depend on it: that is decided against
              every other value combined. Send it with `comparisonValues` and it must be one
              of them, or the request is rejected: anchoring every difference to an arm the
              run never made would measure it against nothing. Leave it out and the template's
              own baseline is used, and quietly dropped if your narrowing excluded it, since
              that one you did not choose.

          comparison_values: The arms of the sweep to run, for a template that sweeps one (GET
              /v1/simulation/template returns `sweep.property` for those that do). This is
              what the run costs: the flow is called once per arm, so ten arms is ten times
              the calls of one. Omit it to run every value the property has, plain, which for
              `accent-handling` is more than twenty. Send a subset to narrow it, for example
              the three accents you actually serve. An object entry pins something on that arm
              only, such as a noise level per bed on `background-noise-robustness`: `{
              "value": "OFFICE", "backgroundNoiseVolume": 0.6 }` plays OFFICE at 60% while the
              other beds keep the default. See `POST /v1/simulation/plan`.

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          end_call_reasons: Semantic conditions that trigger end of call. The LLM evaluates the conversation
              against these conditions. Defaults to the template's `defaultEndCallReasons`, as
              returned by GET /v1/simulation/template. Pass an empty array to run with none.

          enrich_with_live_conversation: Merge the customer's own recording of the real call into each simulation, so
              metrics can be scored against the live leg as well as the simulated one. This is
              the API equivalent of the dashboard's live-enrichment toggle. With this on, the
              run provisions a phone number and holds each call open for up to 15 minutes
              waiting for a matching call to be posted to POST /v1/call. A call matches on the
              provisioned number (`roarkPhoneNumber` on the job) with a start time inside the
              simulation window. If nothing arrives, the simulation still completes and any
              `LIVE`-sourced metric produces no value. Required by any metric whose
              `requiresLiveConversation` is true: without it that metric is silently skipped.

          environment_id: For `question-answer-check`: the environment the calls run in.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          flows: The flows to run, in the same shape a run plan takes them. Required when the
              template lists no flows of its own: it presets what to measure, and this says
              what to measure it on. Optional when it does, where these REPLACE the ones it
              would have run, so you can narrow a suite to the cases you care about. Either
              way, GET /v1/simulation/template lists the flows and variant ids each template
              covers. On a template that sweeps a property, every value runs exactly what you
              select here: the happy path, the edge cases you name, or `edgeCases: "ALL"`.
              Each selected case is a call per value per iteration, so naming three edge cases
              triples the run.

          iteration_count: Runs per test case (1-10000). Defaults to 1, or to 6 for a template that sweeps
              a property. A sweep needs at least 5 calls per value (test cases per value times
              iterations) to compare its values, and a lower count is refused with 400.

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_no_response_retries: How many more times to run a test case when the agent under test never responds:
              it never speaks on a call or never replies in a chat (0-10). 0 turns retries
              off. Failed checks and failures on Roark’s side are never retried. Each retry is
              a separate attempt, billed like any other, so a plan retrying N times can place
              up to N + 1 calls per test case. Every silent attempt stays on the run with its
              own call; the run settles once each test case has a final attempt, and the agent
              never spoke verdict is judged on each test case’s last attempt.

          max_simulation_duration_seconds: Defaults to the template's `defaultMaxSimulationDurationSeconds`, as returned by
              GET /v1/simulation/template.

          name: Name of the run plan. Defaults to the template's name and the date.

          no_response_retry_backoff_seconds: Seconds a retry waits before it dials (30-600). Only used when
              `maxNoResponseRetries` is above 0.

          persona_id: For `question-answer-check`: the persona that asks the questions.

          questions: For the `question-answer-check` template: the questions to ask and the answer
              expected for each. Every question runs as its own graded call.

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["agent_endpoints", "direction", "max_simulation_duration_seconds", "name"],
        ["agent_endpoints", "direction", "template"],
    )
    async def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        auto_run: bool | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_property: Optional[
            Literal[
                "ACCENT",
                "AGE",
                "BACKGROUND_NOISE",
                "BACKGROUND_NOISE_VOLUME",
                "BASE_EMOTION",
                "CONFIRMATION_STYLE",
                "GENDER",
                "INTENT_CLARITY",
                "LANGUAGE",
                "INTERRUPTION",
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: List[Union[str, simulation_run_plan_create_params.ComparisonArm]] | Omit = omit,
        description: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigFlow] | Omit = omit,
        include_automatic_metrics: bool | Omit = omit,
        include_flow_metrics: bool | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigMetric] | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        personas: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigAgentEndpoint] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigScenario] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        template: str | Omit = omit,
        additional_metrics: Iterable[simulation_run_plan_create_params.CreateRunPlanFromConfigMetric] | Omit = omit,
        environment_id: str | Omit = omit,
        persona_id: str | Omit = omit,
        questions: Iterable[simulation_run_plan_create_params.CreateRunPlanFromTemplateQuestion] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanCreateResponse:
        return await self._post(
            "/v1/simulation/plan",
            body=await async_maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "name": name,
                    "auto_run": auto_run,
                    "comparison_baseline": comparison_baseline,
                    "comparison_property": comparison_property,
                    "comparison_values": comparison_values,
                    "description": description,
                    "end_call_phrases": end_call_phrases,
                    "end_call_reasons": end_call_reasons,
                    "enrich_with_live_conversation": enrich_with_live_conversation,
                    "execution_mode": execution_mode,
                    "flows": flows,
                    "include_automatic_metrics": include_automatic_metrics,
                    "include_flow_metrics": include_flow_metrics,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_no_response_retries": max_no_response_retries,
                    "metrics": metrics,
                    "no_response_retry_backoff_seconds": no_response_retry_backoff_seconds,
                    "personas": personas,
                    "scenarios": scenarios,
                    "silence_timeout_seconds": silence_timeout_seconds,
                    "template": template,
                    "additional_metrics": additional_metrics,
                    "environment_id": environment_id,
                    "persona_id": persona_id,
                    "questions": questions,
                },
                simulation_run_plan_create_params.SimulationRunPlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanCreateResponse,
        )

    async def update(
        self,
        plan_id: str,
        *,
        agent_endpoints: Iterable[simulation_run_plan_update_params.AgentEndpoint] | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_property: Optional[
            Literal[
                "ACCENT",
                "AGE",
                "BACKGROUND_NOISE",
                "BACKGROUND_NOISE_VOLUME",
                "BASE_EMOTION",
                "CONFIRMATION_STYLE",
                "GENDER",
                "INTENT_CLARITY",
                "LANGUAGE",
                "INTERRUPTION",
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: List[Union[str, simulation_run_plan_update_params.ComparisonArm]] | Omit = omit,
        description: str | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_update_params.Flow] | Omit = omit,
        include_automatic_metrics: bool | Omit = omit,
        include_flow_metrics: bool | Omit = omit,
        is_hidden: bool | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_update_params.Metric] | Omit = omit,
        name: str | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        personas: Iterable[simulation_run_plan_update_params.AgentEndpoint] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_update_params.Scenario] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanUpdateResponse:
        """
        Updates an existing simulation run plan by its ID.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          comparison_baseline: The reference value, shown first in the results. See `POST /v1/simulation/plan`.
              A real value cannot be sent on its own: the property it belongs to decides which
              values are legal, and an omitted property means "leave unchanged", which this
              endpoint cannot check a baseline against. Send `comparisonProperty` with it, or
              get a `400`. `null` on its own IS allowed, and clears just the baseline while
              leaving the property set. Nothing needs validating when clearing, and a property
              with no baseline is a real state: the report falls back to that property's own
              norm, and `GENDER` has no norm to fall back to.

          comparison_property: The property this plan investigates. Send `null` to clear the comparison; omit
              the field to leave it unchanged. See `POST /v1/simulation/plan`. The pair moves
              together. Sending `comparisonProperty` without `comparisonBaseline` keeps the
              stored baseline when the property is unchanged and the baseline is still one of
              the values being run. Otherwise it becomes the new property's norm, or `null`
              when that norm is not being run either, because a baseline is a value of one
              specific property.

          comparison_values: The arms to run. See `POST /v1/simulation/plan`. Omitting it keeps the arms the
              plan already has, pins included, so an edit that only renames the plan never
              widens a sweep you deliberately narrowed, and never multiplies what it costs.
              Send it with `comparisonProperty` and `flows`, which the arms are rebuilt from.

          description: Description of the run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          end_call_reasons: Semantic conditions that trigger end of call. The LLM evaluates the conversation
              against these conditions. Empty array disables the feature.

          enrich_with_live_conversation: Whether to merge the customer's own live recording into each simulation of this
              plan.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          flows: Replaces the customer flows attached to this run plan. Omit to leave them
              unchanged; send an empty array to detach them all.

          include_automatic_metrics: Whether to let the run add metrics by itself off the attached flows. See `POST
              /v1/simulation/plan`.

          include_flow_metrics: Whether to also collect each attached flow's own metrics, on top of this plan's
              list.

          is_hidden: Whether this plan is hidden from GET /v1/simulation/plan. A run started without
              `saveAsPlan` creates a hidden plan to carry it. Send `{ "name": "...",
              "isHidden": false }` to keep that configuration as a reusable plan, which is
              what the app does when you save a one-off run.

          iteration_count: Number of iterations to run for each test case (1-10000)

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_no_response_retries: How many more times to run a test case when the agent under test never responds:
              it never speaks on a call or never replies in a chat (0-10). 0 turns retries
              off. Failed checks and failures on Roark’s side are never retried. Each retry is
              a separate attempt, billed like any other, so a plan retrying N times can place
              up to N + 1 calls per test case. Every silent attempt stays on the run with its
              own call; the run settles once each test case has a final attempt, and the agent
              never spoke verdict is judged on each test case’s last attempt.

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan. Reference each by `id` (UUID) or
              `slug`.

          name: Name of the run plan

          no_response_retry_backoff_seconds: Seconds a retry waits before it dials (30-600). Only used when
              `maxNoResponseRetries` is above 0.

          personas: Personas to include in this run plan

          scenarios: Deprecated: use `flows` instead. Replaces the scenarios on this run plan. Omit
              to leave them unchanged; send an empty array to detach them all, which is how a
              scenario-based plan is moved over to flows.

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._put(
            f"/v1/simulation/plan/{plan_id}",
            body=await async_maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "comparison_baseline": comparison_baseline,
                    "comparison_property": comparison_property,
                    "comparison_values": comparison_values,
                    "description": description,
                    "direction": direction,
                    "end_call_phrases": end_call_phrases,
                    "end_call_reasons": end_call_reasons,
                    "enrich_with_live_conversation": enrich_with_live_conversation,
                    "execution_mode": execution_mode,
                    "flows": flows,
                    "include_automatic_metrics": include_automatic_metrics,
                    "include_flow_metrics": include_flow_metrics,
                    "is_hidden": is_hidden,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_no_response_retries": max_no_response_retries,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
                    "name": name,
                    "no_response_retry_backoff_seconds": no_response_retry_backoff_seconds,
                    "personas": personas,
                    "scenarios": scenarios,
                    "silence_timeout_seconds": silence_timeout_seconds,
                },
                simulation_run_plan_update_params.SimulationRunPlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanListResponse:
        """Returns a paginated list of simulation run plans.

        Optionally filter by search
        text or agent ID.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          agent_id: Filter run plans by agent ID

          limit: Maximum number of run plans to return (default: 20, max: 50)

          search_text: Search text to filter run plans by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/plan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "limit": limit,
                        "search_text": search_text,
                    },
                    simulation_run_plan_list_params.SimulationRunPlanListParams,
                ),
            ),
            cast_to=SimulationRunPlanListResponse,
        )

    async def delete(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanDeleteResponse:
        """
        Soft-deletes a simulation run plan by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._delete(
            f"/v1/simulation/plan/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanDeleteResponse,
        )

    async def get_by_id(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanGetByIDResponse:
        """
        Returns a specific simulation run plan by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._get(
            f"/v1/simulation/plan/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanGetByIDResponse,
        )


class SimulationRunPlanResourceWithRawResponse:
    def __init__(self, simulation_run_plan: SimulationRunPlanResource) -> None:
        self._simulation_run_plan = simulation_run_plan

        self.create = to_raw_response_wrapper(
            simulation_run_plan.create,
        )
        self.update = to_raw_response_wrapper(
            simulation_run_plan.update,
        )
        self.list = to_raw_response_wrapper(
            simulation_run_plan.list,
        )
        self.delete = to_raw_response_wrapper(
            simulation_run_plan.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_run_plan.get_by_id,
        )


class AsyncSimulationRunPlanResourceWithRawResponse:
    def __init__(self, simulation_run_plan: AsyncSimulationRunPlanResource) -> None:
        self._simulation_run_plan = simulation_run_plan

        self.create = async_to_raw_response_wrapper(
            simulation_run_plan.create,
        )
        self.update = async_to_raw_response_wrapper(
            simulation_run_plan.update,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_run_plan.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simulation_run_plan.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_run_plan.get_by_id,
        )


class SimulationRunPlanResourceWithStreamingResponse:
    def __init__(self, simulation_run_plan: SimulationRunPlanResource) -> None:
        self._simulation_run_plan = simulation_run_plan

        self.create = to_streamed_response_wrapper(
            simulation_run_plan.create,
        )
        self.update = to_streamed_response_wrapper(
            simulation_run_plan.update,
        )
        self.list = to_streamed_response_wrapper(
            simulation_run_plan.list,
        )
        self.delete = to_streamed_response_wrapper(
            simulation_run_plan.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_run_plan.get_by_id,
        )


class AsyncSimulationRunPlanResourceWithStreamingResponse:
    def __init__(self, simulation_run_plan: AsyncSimulationRunPlanResource) -> None:
        self._simulation_run_plan = simulation_run_plan

        self.create = async_to_streamed_response_wrapper(
            simulation_run_plan.create,
        )
        self.update = async_to_streamed_response_wrapper(
            simulation_run_plan.update,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_run_plan.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simulation_run_plan.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_run_plan.get_by_id,
        )
