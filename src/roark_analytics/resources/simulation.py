# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, overload
from typing_extensions import Literal

import httpx

from ..types import simulation_run_params
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
from ..types.simulation_run_response import SimulationRunResponse

__all__ = ["SimulationResource", "AsyncSimulationResource"]


class SimulationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationResourceWithStreamingResponse(self)

    @overload
    def run(
        self,
        *,
        plan: simulation_run_params.RunSimulationFromConfigPlan,
        save_as_plan: bool | Omit = omit,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """Starts a simulation and returns the run.

        Send `template` to run one of the
        built-in templates: it supplies the metrics and checks, and for some templates
        the flows too, so the request only names the agent and the direction. Send
        `plan` to describe a simulation yourself and run it once. Send `planId` to run a
        plan you already have. `template` and `plan` both resolve to a run plan,
        returned as `simulationRunPlanId`. Add `saveAsPlan` to keep it, or read it back
        to see exactly what ran. A plan built from a template is a snapshot: retuning
        the template later never changes what that plan runs, which is what makes a
        saved one safe to pin in CI.

        Args:
          plan: The simulation to run: what to call, who calls it, and what to measure.

          save_as_plan: Keeps this configuration as a run plan, listed by GET /v1/simulation/plan and
              re-runnable with `planId`. Requires `plan.name`, since a plan you meant to keep
              should not be filed under a generated one. Omitted or false gives a one-off. The
              run still needs a plan to execute, so one is created either way, but it is
              hidden: it carries this run and nothing else.

          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned. An object applies them to the whole run: { "orderNumber": "12345",
              "tier": "gold" } An array applies them per flow, or to just its happy path or
              one of its edge cases, when a single set will not do. Each entry carries what it
              applies to: [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345"
              } }, { "flowId": "550e8400-...", "happyPath": true, "variables": {
              "orderNumber": "55555" } }, { "flowId": "550e8400-...", "edgeCaseId":
              "7a3d2e1f-...", "variables": { "orderNumber": "67890" } } ] An entry that
              narrows to neither covers everything that flow resolves. A flow this plan does
              not attach, or an edge case that does not belong to the flow, is rejected rather
              than ignored. A plan built on scenarios rather than customer flows targets them
              the same way, with `scenarioId` in place of `flowId`. That form is deprecated
              alongside scenarios themselves, and still accepted so runs against those plans
              keep working.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        plan_id: str,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """Starts a simulation and returns the run.

        Send `template` to run one of the
        built-in templates: it supplies the metrics and checks, and for some templates
        the flows too, so the request only names the agent and the direction. Send
        `plan` to describe a simulation yourself and run it once. Send `planId` to run a
        plan you already have. `template` and `plan` both resolve to a run plan,
        returned as `simulationRunPlanId`. Add `saveAsPlan` to keep it, or read it back
        to see exactly what ran. A plan built from a template is a snapshot: retuning
        the template later never changes what that plan runs, which is what makes a
        saved one safe to pin in CI.

        Args:
          plan_id: The run plan to run, saved or hidden. Rename or unhide it with PUT
              /v1/simulation/plan/{planId}.

          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned. An object applies them to the whole run: { "orderNumber": "12345",
              "tier": "gold" } An array applies them per flow, or to just its happy path or
              one of its edge cases, when a single set will not do. Each entry carries what it
              applies to: [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345"
              } }, { "flowId": "550e8400-...", "happyPath": true, "variables": {
              "orderNumber": "55555" } }, { "flowId": "550e8400-...", "edgeCaseId":
              "7a3d2e1f-...", "variables": { "orderNumber": "67890" } } ] An entry that
              narrows to neither covers everything that flow resolves. A flow this plan does
              not attach, or an edge case that does not belong to the flow, is rejected rather
              than ignored. A plan built on scenarios rather than customer flows targets them
              the same way, with `scenarioId` in place of `flowId`. That form is deprecated
              alongside scenarios themselves, and still accepted so runs against those plans
              keep working.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_params.RunSimulationFromConfigPlanAgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        template: str,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_params.RunSimulationFromConfigPlanFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        save_as_plan: bool | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        variables: Union[Dict[str, str], Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """Starts a simulation and returns the run.

        Send `template` to run one of the
        built-in templates: it supplies the metrics and checks, and for some templates
        the flows too, so the request only names the agent and the direction. Send
        `plan` to describe a simulation yourself and run it once. Send `planId` to run a
        plan you already have. `template` and `plan` both resolve to a run plan,
        returned as `simulationRunPlanId`. Add `saveAsPlan` to keep it, or read it back
        to see exactly what ran. A plan built from a template is a snapshot: retuning
        the template later never changes what that plan runs, which is what makes a
        saved one safe to pin in CI.

        Args:
          agent_endpoints: The agent endpoints to call. No template can know these.

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          template: The template to run, as listed by GET /v1/simulation/template.

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

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          flows: The flows to run, in the same shape a run plan takes them. Required when the
              template lists no flows of its own: it presets what to measure, and this says
              what to measure it on. Optional when it does, where these REPLACE the ones it
              would have run, so you can narrow a suite to the cases you care about. Either
              way, GET /v1/simulation/template lists the flows and variant ids each template
              covers.

          iteration_count: Number of iterations to run for each test case (1-10000)

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_simulation_duration_seconds: Defaults to the template's `defaultMaxSimulationDurationSeconds`, as returned by
              GET /v1/simulation/template.

          name: What to call this. Defaults to the template's name and the date, and required
              with `saveAsPlan`.

          save_as_plan: Keeps the resolved configuration as a run plan, listed by GET
              /v1/simulation/plan and re-runnable with `planId`. Requires `name`.

          silence_timeout_seconds: Timeout in seconds for silence detection

          variables: Values for the {{variables}} the run resolves. An object applies them
              everywhere; an array targets a flow, its happy path, or one of its edge cases
              with `flowId`. The scenario-scoped form the other variants accept is not valid
              here: a template run is always flow-based, so there would be no scenario for it
              to reach.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["plan"], ["plan_id"], ["agent_endpoints", "direction", "template"])
    def run(
        self,
        *,
        plan: simulation_run_params.RunSimulationFromConfigPlan | Omit = omit,
        save_as_plan: bool | Omit = omit,
        variables: Union[
            Union[
                Dict[str, str],
                Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1],
                Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember2],
            ],
            Union[Dict[str, str], Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1]],
        ]
        | Omit = omit,
        plan_id: str | Omit = omit,
        agent_endpoints: Iterable[simulation_run_params.RunSimulationFromConfigPlanAgentEndpoint] | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        template: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_params.RunSimulationFromConfigPlanFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        return self._post(
            "/v1/simulation/run",
            body=maybe_transform(
                {
                    "plan": plan,
                    "save_as_plan": save_as_plan,
                    "variables": variables,
                    "plan_id": plan_id,
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "template": template,
                    "end_call_phrases": end_call_phrases,
                    "end_call_reasons": end_call_reasons,
                    "enrich_with_live_conversation": enrich_with_live_conversation,
                    "execution_mode": execution_mode,
                    "flows": flows,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "name": name,
                    "silence_timeout_seconds": silence_timeout_seconds,
                },
                simulation_run_params.SimulationRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunResponse,
        )


class AsyncSimulationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationResourceWithStreamingResponse(self)

    @overload
    async def run(
        self,
        *,
        plan: simulation_run_params.RunSimulationFromConfigPlan,
        save_as_plan: bool | Omit = omit,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """Starts a simulation and returns the run.

        Send `template` to run one of the
        built-in templates: it supplies the metrics and checks, and for some templates
        the flows too, so the request only names the agent and the direction. Send
        `plan` to describe a simulation yourself and run it once. Send `planId` to run a
        plan you already have. `template` and `plan` both resolve to a run plan,
        returned as `simulationRunPlanId`. Add `saveAsPlan` to keep it, or read it back
        to see exactly what ran. A plan built from a template is a snapshot: retuning
        the template later never changes what that plan runs, which is what makes a
        saved one safe to pin in CI.

        Args:
          plan: The simulation to run: what to call, who calls it, and what to measure.

          save_as_plan: Keeps this configuration as a run plan, listed by GET /v1/simulation/plan and
              re-runnable with `planId`. Requires `plan.name`, since a plan you meant to keep
              should not be filed under a generated one. Omitted or false gives a one-off. The
              run still needs a plan to execute, so one is created either way, but it is
              hidden: it carries this run and nothing else.

          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned. An object applies them to the whole run: { "orderNumber": "12345",
              "tier": "gold" } An array applies them per flow, or to just its happy path or
              one of its edge cases, when a single set will not do. Each entry carries what it
              applies to: [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345"
              } }, { "flowId": "550e8400-...", "happyPath": true, "variables": {
              "orderNumber": "55555" } }, { "flowId": "550e8400-...", "edgeCaseId":
              "7a3d2e1f-...", "variables": { "orderNumber": "67890" } } ] An entry that
              narrows to neither covers everything that flow resolves. A flow this plan does
              not attach, or an edge case that does not belong to the flow, is rejected rather
              than ignored. A plan built on scenarios rather than customer flows targets them
              the same way, with `scenarioId` in place of `flowId`. That form is deprecated
              alongside scenarios themselves, and still accepted so runs against those plans
              keep working.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        plan_id: str,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """Starts a simulation and returns the run.

        Send `template` to run one of the
        built-in templates: it supplies the metrics and checks, and for some templates
        the flows too, so the request only names the agent and the direction. Send
        `plan` to describe a simulation yourself and run it once. Send `planId` to run a
        plan you already have. `template` and `plan` both resolve to a run plan,
        returned as `simulationRunPlanId`. Add `saveAsPlan` to keep it, or read it back
        to see exactly what ran. A plan built from a template is a snapshot: retuning
        the template later never changes what that plan runs, which is what makes a
        saved one safe to pin in CI.

        Args:
          plan_id: The run plan to run, saved or hidden. Rename or unhide it with PUT
              /v1/simulation/plan/{planId}.

          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned. An object applies them to the whole run: { "orderNumber": "12345",
              "tier": "gold" } An array applies them per flow, or to just its happy path or
              one of its edge cases, when a single set will not do. Each entry carries what it
              applies to: [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345"
              } }, { "flowId": "550e8400-...", "happyPath": true, "variables": {
              "orderNumber": "55555" } }, { "flowId": "550e8400-...", "edgeCaseId":
              "7a3d2e1f-...", "variables": { "orderNumber": "67890" } } ] An entry that
              narrows to neither covers everything that flow resolves. A flow this plan does
              not attach, or an edge case that does not belong to the flow, is rejected rather
              than ignored. A plan built on scenarios rather than customer flows targets them
              the same way, with `scenarioId` in place of `flowId`. That form is deprecated
              alongside scenarios themselves, and still accepted so runs against those plans
              keep working.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_params.RunSimulationFromConfigPlanAgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        template: str,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_params.RunSimulationFromConfigPlanFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        save_as_plan: bool | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        variables: Union[Dict[str, str], Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """Starts a simulation and returns the run.

        Send `template` to run one of the
        built-in templates: it supplies the metrics and checks, and for some templates
        the flows too, so the request only names the agent and the direction. Send
        `plan` to describe a simulation yourself and run it once. Send `planId` to run a
        plan you already have. `template` and `plan` both resolve to a run plan,
        returned as `simulationRunPlanId`. Add `saveAsPlan` to keep it, or read it back
        to see exactly what ran. A plan built from a template is a snapshot: retuning
        the template later never changes what that plan runs, which is what makes a
        saved one safe to pin in CI.

        Args:
          agent_endpoints: The agent endpoints to call. No template can know these.

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          template: The template to run, as listed by GET /v1/simulation/template.

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

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          flows: The flows to run, in the same shape a run plan takes them. Required when the
              template lists no flows of its own: it presets what to measure, and this says
              what to measure it on. Optional when it does, where these REPLACE the ones it
              would have run, so you can narrow a suite to the cases you care about. Either
              way, GET /v1/simulation/template lists the flows and variant ids each template
              covers.

          iteration_count: Number of iterations to run for each test case (1-10000)

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_simulation_duration_seconds: Defaults to the template's `defaultMaxSimulationDurationSeconds`, as returned by
              GET /v1/simulation/template.

          name: What to call this. Defaults to the template's name and the date, and required
              with `saveAsPlan`.

          save_as_plan: Keeps the resolved configuration as a run plan, listed by GET
              /v1/simulation/plan and re-runnable with `planId`. Requires `name`.

          silence_timeout_seconds: Timeout in seconds for silence detection

          variables: Values for the {{variables}} the run resolves. An object applies them
              everywhere; an array targets a flow, its happy path, or one of its edge cases
              with `flowId`. The scenario-scoped form the other variants accept is not valid
              here: a template run is always flow-based, so there would be no scenario for it
              to reach.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["plan"], ["plan_id"], ["agent_endpoints", "direction", "template"])
    async def run(
        self,
        *,
        plan: simulation_run_params.RunSimulationFromConfigPlan | Omit = omit,
        save_as_plan: bool | Omit = omit,
        variables: Union[
            Union[
                Dict[str, str],
                Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1],
                Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember2],
            ],
            Union[Dict[str, str], Iterable[simulation_run_params.RunSimulationFromConfigVariableUnionMember1]],
        ]
        | Omit = omit,
        plan_id: str | Omit = omit,
        agent_endpoints: Iterable[simulation_run_params.RunSimulationFromConfigPlanAgentEndpoint] | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        template: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_params.RunSimulationFromConfigPlanFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        return await self._post(
            "/v1/simulation/run",
            body=await async_maybe_transform(
                {
                    "plan": plan,
                    "save_as_plan": save_as_plan,
                    "variables": variables,
                    "plan_id": plan_id,
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "template": template,
                    "end_call_phrases": end_call_phrases,
                    "end_call_reasons": end_call_reasons,
                    "enrich_with_live_conversation": enrich_with_live_conversation,
                    "execution_mode": execution_mode,
                    "flows": flows,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "name": name,
                    "silence_timeout_seconds": silence_timeout_seconds,
                },
                simulation_run_params.SimulationRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunResponse,
        )


class SimulationResourceWithRawResponse:
    def __init__(self, simulation: SimulationResource) -> None:
        self._simulation = simulation

        self.run = to_raw_response_wrapper(
            simulation.run,
        )


class AsyncSimulationResourceWithRawResponse:
    def __init__(self, simulation: AsyncSimulationResource) -> None:
        self._simulation = simulation

        self.run = async_to_raw_response_wrapper(
            simulation.run,
        )


class SimulationResourceWithStreamingResponse:
    def __init__(self, simulation: SimulationResource) -> None:
        self._simulation = simulation

        self.run = to_streamed_response_wrapper(
            simulation.run,
        )


class AsyncSimulationResourceWithStreamingResponse:
    def __init__(self, simulation: AsyncSimulationResource) -> None:
        self._simulation = simulation

        self.run = async_to_streamed_response_wrapper(
            simulation.run,
        )
