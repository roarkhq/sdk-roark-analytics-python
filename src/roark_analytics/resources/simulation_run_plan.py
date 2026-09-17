# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    simulation_run_plan_list_params,
    simulation_run_plan_create_params,
    simulation_run_plan_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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

    def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.AgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        max_simulation_duration_seconds: int,
        metrics: Iterable[simulation_run_plan_create_params.Metric],
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
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_create_params.Flow] | Omit = omit,
        include_automatic_metrics: bool | Omit = omit,
        include_flow_metrics: bool | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        personas: Iterable[simulation_run_plan_create_params.AgentEndpoint] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_create_params.Scenario] | Omit = omit,
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
        reusable, named one to run later.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan. Reference each by `id` (UUID) or
              `slug`.

          name: Name of the run plan

          auto_run: Deprecated: use POST /v1/simulation/run, which starts a run and accepts runtime
              `variables` as well. This flag runs the plan with only the values pinned on it.

          comparison_baseline: The value of `comparisonProperty` every other value is measured against, for
              example `NONE` for `BACKGROUND_NOISE` or `NORMAL` for `SPEECH_PACE`. Must be a
              value that property can take. Stored rather than assumed, so the report can say
              "compared against US accent" instead of implying Roark decided which value is
              normal. Most properties have an obvious baseline and the dashboard prefills it;
              `GENDER` has none, so choose the one you are testing against.

          comparison_property: The property this run plan investigates: the one thing its arms differ by. Set
              it and the run report compares the arms on that property, so a run answers "what
              did background noise cost" rather than just "what did each arm score". Every
              value is a field already recorded on each call, so the report can label an arm
              `CRYING_BABY` rather than repeating a flow variant's title. Omit it and the
              report still compares when it can: it detects which property varies across the
              arms. Setting it is what tells the written summary what you were trying to find
              out, which detection cannot infer.

          comparison_values: Which values of `comparisonProperty` to run. This is what the plan costs: the
              flow is attached once per value, so ten values is ten times the calls of one.
              Omit it to run every value the property has, which for `ACCENT` is more than
              twenty. Send a subset to narrow the sweep, for example three accents you
              actually serve. A `comparisonBaseline` outside this set is rejected, because it
              would anchor every difference to an arm the run never made. Not stored as a
              field: the arms are the values. Reading the plan back returns them as its flow
              attachments.

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
        return self._post(
            "/v1/simulation/plan",
            body=maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
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
                    "personas": personas,
                    "scenarios": scenarios,
                    "silence_timeout_seconds": silence_timeout_seconds,
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
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: SequenceNotStr[str] | Omit = omit,
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
        max_simulation_duration_seconds: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_update_params.Metric] | Omit = omit,
        name: str | Omit = omit,
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

          comparison_baseline: The value every other value is measured against. See `POST /v1/simulation/plan`.
              A real value cannot be sent on its own: the property it belongs to decides which
              values are legal, and an omitted property means "leave unchanged", which this
              endpoint cannot check a baseline against. Send `comparisonProperty` with it, or
              get a `400`. `null` on its own IS allowed, and clears just the baseline while
              leaving the property set. Nothing needs validating when clearing, and a property
              with no baseline is a real state: the report falls back to that property's own
              norm, and `GENDER` has no norm to fall back to.

          comparison_property: The property this plan investigates. Send `null` to clear the comparison; omit
              the field to leave it unchanged. See `POST /v1/simulation/plan`. The pair moves
              together. Sending `comparisonProperty` also sets `comparisonBaseline` to
              whatever this request carries, or to `null` if it carries none, because a
              baseline is a value of one specific property and keeping the old one would store
              a pair that is not valid.

          comparison_values: Which values of `comparisonProperty` to run. See `POST /v1/simulation/plan`.
              Omitting it keeps the arms the plan already has, so an edit that only renames
              the plan never widens a sweep you deliberately narrowed, and never multiplies
              what it costs.

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

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan. Reference each by `id` (UUID) or
              `slug`.

          name: Name of the run plan

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
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
                    "name": name,
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

    async def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.AgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        max_simulation_duration_seconds: int,
        metrics: Iterable[simulation_run_plan_create_params.Metric],
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
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_plan_create_params.Flow] | Omit = omit,
        include_automatic_metrics: bool | Omit = omit,
        include_flow_metrics: bool | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        personas: Iterable[simulation_run_plan_create_params.AgentEndpoint] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_create_params.Scenario] | Omit = omit,
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
        reusable, named one to run later.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan. Reference each by `id` (UUID) or
              `slug`.

          name: Name of the run plan

          auto_run: Deprecated: use POST /v1/simulation/run, which starts a run and accepts runtime
              `variables` as well. This flag runs the plan with only the values pinned on it.

          comparison_baseline: The value of `comparisonProperty` every other value is measured against, for
              example `NONE` for `BACKGROUND_NOISE` or `NORMAL` for `SPEECH_PACE`. Must be a
              value that property can take. Stored rather than assumed, so the report can say
              "compared against US accent" instead of implying Roark decided which value is
              normal. Most properties have an obvious baseline and the dashboard prefills it;
              `GENDER` has none, so choose the one you are testing against.

          comparison_property: The property this run plan investigates: the one thing its arms differ by. Set
              it and the run report compares the arms on that property, so a run answers "what
              did background noise cost" rather than just "what did each arm score". Every
              value is a field already recorded on each call, so the report can label an arm
              `CRYING_BABY` rather than repeating a flow variant's title. Omit it and the
              report still compares when it can: it detects which property varies across the
              arms. Setting it is what tells the written summary what you were trying to find
              out, which detection cannot infer.

          comparison_values: Which values of `comparisonProperty` to run. This is what the plan costs: the
              flow is attached once per value, so ten values is ten times the calls of one.
              Omit it to run every value the property has, which for `ACCENT` is more than
              twenty. Send a subset to narrow the sweep, for example three accents you
              actually serve. A `comparisonBaseline` outside this set is rejected, because it
              would anchor every difference to an arm the run never made. Not stored as a
              field: the arms are the values. Reading the plan back returns them as its flow
              attachments.

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
        return await self._post(
            "/v1/simulation/plan",
            body=await async_maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
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
                    "personas": personas,
                    "scenarios": scenarios,
                    "silence_timeout_seconds": silence_timeout_seconds,
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
                "MEMORY_RELIABILITY",
                "RESPONSE_TIMING",
                "SPEECH_CLARITY",
                "SPEECH_PACE",
            ]
        ]
        | Omit = omit,
        comparison_values: SequenceNotStr[str] | Omit = omit,
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
        max_simulation_duration_seconds: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_update_params.Metric] | Omit = omit,
        name: str | Omit = omit,
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

          comparison_baseline: The value every other value is measured against. See `POST /v1/simulation/plan`.
              A real value cannot be sent on its own: the property it belongs to decides which
              values are legal, and an omitted property means "leave unchanged", which this
              endpoint cannot check a baseline against. Send `comparisonProperty` with it, or
              get a `400`. `null` on its own IS allowed, and clears just the baseline while
              leaving the property set. Nothing needs validating when clearing, and a property
              with no baseline is a real state: the report falls back to that property's own
              norm, and `GENDER` has no norm to fall back to.

          comparison_property: The property this plan investigates. Send `null` to clear the comparison; omit
              the field to leave it unchanged. See `POST /v1/simulation/plan`. The pair moves
              together. Sending `comparisonProperty` also sets `comparisonBaseline` to
              whatever this request carries, or to `null` if it carries none, because a
              baseline is a value of one specific property and keeping the old one would store
              a pair that is not valid.

          comparison_values: Which values of `comparisonProperty` to run. See `POST /v1/simulation/plan`.
              Omitting it keeps the arms the plan already has, so an edit that only renames
              the plan never widens a sweep you deliberately narrowed, and never multiplies
              what it costs.

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

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan. Reference each by `id` (UUID) or
              `slug`.

          name: Name of the run plan

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
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
                    "name": name,
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
