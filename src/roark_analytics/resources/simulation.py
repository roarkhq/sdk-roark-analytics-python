# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional, overload
from typing_extensions import Literal

import httpx

from ..types import (
    simulation_run_params,
    simulation_mock_tool_params,
    simulation_generate_resources_params,
    simulation_guide_resource_generation_params,
    simulation_list_resource_generations_params,
    simulation_answer_resource_generation_params,
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
from ..types.simulation_run_response import SimulationRunResponse
from ..types.simulation_mock_tool_response import SimulationMockToolResponse
from ..types.simulation_generate_resources_response import SimulationGenerateResourcesResponse
from ..types.simulation_get_resource_generation_response import SimulationGetResourceGenerationResponse
from ..types.simulation_guide_resource_generation_response import SimulationGuideResourceGenerationResponse
from ..types.simulation_list_resource_generations_response import SimulationListResourceGenerationsResponse
from ..types.simulation_answer_resource_generation_response import SimulationAnswerResourceGenerationResponse
from ..types.simulation_cancel_resource_generation_response import SimulationCancelResourceGenerationResponse

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

    def answer_resource_generation(
        self,
        generation_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationAnswerResourceGenerationResponse:
        """
        Answers the question a simulation resource generation is waiting on (status
        NEEDS_INPUT). If nobody answers within 15 minutes, it goes ahead with its
        default.

        Args:
          text: What you want the generation to know

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return self._post(
            f"/v1/simulation/generations/resources/{generation_id}/answer",
            body=maybe_transform(
                {"text": text}, simulation_answer_resource_generation_params.SimulationAnswerResourceGenerationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationAnswerResourceGenerationResponse,
        )

    def cancel_resource_generation(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCancelResourceGenerationResponse:
        """Stops a running simulation resource generation.

        Flows and metrics it already
        created are kept; no run plan is made. Refused once the generation has finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return self._post(
            f"/v1/simulation/generations/resources/{generation_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCancelResourceGenerationResponse,
        )

    def generate_resources(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        agent_endpoint_id: str | Omit = omit,
        capabilities: List[
            Literal[
                "APPOINTMENT_BOOKING",
                "FAQ",
                "IDENTITY_VERIFICATION",
                "ACCOUNT_MANAGEMENT",
                "BILLING_AND_PAYMENTS",
                "ORDER_MANAGEMENT",
                "TROUBLESHOOTING",
                "CALL_ROUTING",
                "LEAD_QUALIFICATION",
                "COLLECTIONS",
                "OUTBOUND_CALLING",
            ]
        ]
        | Omit = omit,
        explore: simulation_generate_resources_params.Explore | Omit = omit,
        industry: Literal[
            "HEALTHCARE",
            "FINANCIAL_SERVICES",
            "INSURANCE",
            "DEBT_COLLECTION",
            "RETAIL",
            "TRAVEL_AND_HOSPITALITY",
            "TELECOMMUNICATIONS",
            "TECHNOLOGY",
            "PUBLIC_SECTOR",
            "UTILITIES",
            "LOGISTICS",
            "AUTOMOTIVE",
            "HOME_SERVICES",
            "RESTAURANTS",
            "EDUCATION",
            "RECRUITING_AND_STAFFING",
            "OTHER",
        ]
        | Omit = omit,
        industry_description: str | Omit = omit,
        testing_instructions: str | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGenerateResourcesResponse:
        """
        Works out what to test for an existing agent, then creates the customer flows,
        metrics and checks to simulate it, and a run plan that runs them. It does not
        create or change the agent. It also reads the agent's recent production calls
        and open issues. Run it again and it builds on what earlier generations made,
        adding only what changed; when nothing has, it finishes straight away and says
        so. Runs in the background: watch the `simulation.resource_generation.completed`
        webhook, or poll `GET /v1/simulation/generations/resources/{generationId}`.
        Takes one agent for now. Refused while another generation for the agent is
        running. Needs the 'simulation:create' and 'metric:create' permissions.
        Exploration also needs 'simulation:run', and is turned off for keys without it
        unless explore.enabled is set.

        Args:
          agent_ids: The agents to generate simulation resources for. One agent per generation for
              now.

          agent_endpoint_id: The endpoint the run plan calls. Defaults to the agent's newest endpoint.

          capabilities: The capabilities to test. Omit to let Roark work them out from the agent.

          explore: Exploration settings

          industry: The industry the agent serves.

          industry_description: The industry in your own words, when none of the listed ones fits. Use it with
              industry OTHER.

          testing_instructions: What you want tested, in your own words. Each scenario you describe becomes a
              flow.

          website_url: A page Roark reads to learn about the business.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulation/generations/resources",
            body=maybe_transform(
                {
                    "agent_ids": agent_ids,
                    "agent_endpoint_id": agent_endpoint_id,
                    "capabilities": capabilities,
                    "explore": explore,
                    "industry": industry,
                    "industry_description": industry_description,
                    "testing_instructions": testing_instructions,
                    "website_url": website_url,
                },
                simulation_generate_resources_params.SimulationGenerateResourcesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGenerateResourcesResponse,
        )

    def get_resource_generation(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGetResourceGenerationResponse:
        """
        Returns one simulation resource generation, for example the one a webhook named.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return self._get(
            f"/v1/simulation/generations/resources/{generation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGetResourceGenerationResponse,
        )

    def guide_resource_generation(
        self,
        generation_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGuideResourceGenerationResponse:
        """
        Tells a running simulation resource generation what to focus on or avoid, in
        your own words. It reads it on its next turn and it outranks its own plan.
        Refused once the generation has finished.

        Args:
          text: What you want the generation to know

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return self._post(
            f"/v1/simulation/generations/resources/{generation_id}/guidance",
            body=maybe_transform(
                {"text": text}, simulation_guide_resource_generation_params.SimulationGuideResourceGenerationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGuideResourceGenerationResponse,
        )

    def list_resource_generations(
        self,
        *,
        agent_ids: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationListResourceGenerationsResponse:
        """
        Returns the project's simulation resource generations, newest first, optionally
        only for some agents: each one's progress, the run plan it created, and every
        flow, metric and check it added or left out, with the reason and the source it
        came from.

        Args:
          agent_ids: Only generations for these agents, comma-separated, at most 100. Omit for every
              agent.

          limit: How many to return, newest first. Default 20, max 50.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/generations/resources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_ids": agent_ids,
                        "limit": limit,
                    },
                    simulation_list_resource_generations_params.SimulationListResourceGenerationsParams,
                ),
            ),
            cast_to=SimulationListResourceGenerationsResponse,
        )

    def mock_tool(
        self,
        *,
        simulation_job_id: str,
        tool_name: str,
        arguments: Dict[str, object] | Omit = omit,
        session_id: str | Omit = omit,
        tool_description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationMockToolResponse:
        """The server half of the tool guard for code-first agents.

        When a guarded tool
        fires during a Roark test call, send the invocation here instead of executing
        it: Roark answers with a simulated backend response that is valid JSON, shaped
        by the tool contract you pass, consistent with the test scenario, and consistent
        with earlier mocked responses in the same call. Real callers are never affected:
        the guard only diverts when the agent-config resolve response identified the
        session as a Roark simulation, and this endpoint independently re-validates the
        simulation before answering. Failure contract for your wrapper: `404` means the
        simulation id is unknown to this project (treat the session as real). `409`
        means the simulation has already ended (stale session state: do NOT execute the
        real tool; return your static fallback). `5xx` means generation failed (return
        your static fallback). Identical retries (same tool, same arguments) within a
        few minutes return the stored response, so double-fired handlers stay
        consistent.

        Args:
          simulation_job_id: The simulation this session belongs to, from the agent-config resolve response
              (`simulationJobId`). Roark re-validates it against the live simulation before
              answering.

          tool_name: The tool the agent invoked.

          arguments: The arguments the agent called the tool with, verbatim.

          session_id: Your session or room identifier, echoed back in logs for correlation.

          tool_description: The tool's contract: its description and, ideally, its parameter and return
              shape. The more contract you pass, the more faithful the simulated response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulation/tool-mock",
            body=maybe_transform(
                {
                    "simulation_job_id": simulation_job_id,
                    "tool_name": tool_name,
                    "arguments": arguments,
                    "session_id": session_id,
                    "tool_description": tool_description,
                },
                simulation_mock_tool_params.SimulationMockToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationMockToolResponse,
        )

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
          plan_id: The run plan to run, saved or hidden. Rename or unhide it with `PUT
              /v1/simulation/plan/{planId}`.

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
        plan_config_key: str,
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
          plan_config_key: The config key of a plan to run, as applied from config as code
              (`simulationPlan/<name>`). Runs a config-managed plan by name, with no id
              lookup. Unique per project.

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
        additional_metrics: Iterable[simulation_run_params.RunSimulationFromConfigPlanMetric] | Omit = omit,
        calls_per_second: Optional[float] | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_values: List[Union[str, simulation_run_params.ComparisonArm]] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        environment_id: str | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_params.RunSimulationFromConfigPlanFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        persona_id: str | Omit = omit,
        questions: Iterable[simulation_run_params.RunSimulationFromTemplateQuestion] | Omit = omit,
        ramp_up_seconds: Optional[int] | Omit = omit,
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

          additional_metrics: Metrics to collect on top of the template's own, referenced by `id` or `slug`
              like a plan's `metrics`. The template's metrics and checks always run; naming
              one of them here again keeps it once, with the success criteria you set on it.

          calls_per_second: The most simulations a run starts per second (0.01-10), fractional allowed: 0.2
              starts one every 5 seconds. Omitted or `null` starts them as fast as
              `maxConcurrentJobs` allows. The concurrency limit still applies on top, so a run
              holds the rate only while calls last under `maxConcurrentJobs` /
              `callsPerSecond` seconds. A run reports the rate it achieved as
              `dialRate.achievedCallsPerSecond`. A rate above the project's concurrency limit
              / 30 is refused with 400: that limit could only hold it with calls under 30
              seconds.

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

          name: What to call this. Defaults to the template's name and the date, and required
              with `saveAsPlan`.

          no_response_retry_backoff_seconds: Seconds a retry waits before it dials (30-600). Only used when
              `maxNoResponseRetries` is above 0.

          persona_id: For `question-answer-check`: the persona that asks the questions.

          questions: For the `question-answer-check` template: the questions to ask and the answer
              expected for each. Every question runs as its own graded call.

          ramp_up_seconds: Seconds over which the rate climbs linearly from 0 to `callsPerSecond` (0-3600).
              Omitted, `null` or 0 starts at the full rate. Only used with `callsPerSecond`.

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

    @required_args(["plan"], ["plan_id"], ["plan_config_key"], ["agent_endpoints", "direction", "template"])
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
        plan_config_key: str | Omit = omit,
        agent_endpoints: Iterable[simulation_run_params.RunSimulationFromConfigPlanAgentEndpoint] | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        template: str | Omit = omit,
        additional_metrics: Iterable[simulation_run_params.RunSimulationFromConfigPlanMetric] | Omit = omit,
        calls_per_second: Optional[float] | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_values: List[Union[str, simulation_run_params.ComparisonArm]] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        environment_id: str | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_params.RunSimulationFromConfigPlanFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        persona_id: str | Omit = omit,
        questions: Iterable[simulation_run_params.RunSimulationFromTemplateQuestion] | Omit = omit,
        ramp_up_seconds: Optional[int] | Omit = omit,
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
                    "plan_config_key": plan_config_key,
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "template": template,
                    "additional_metrics": additional_metrics,
                    "calls_per_second": calls_per_second,
                    "comparison_baseline": comparison_baseline,
                    "comparison_values": comparison_values,
                    "end_call_phrases": end_call_phrases,
                    "end_call_reasons": end_call_reasons,
                    "enrich_with_live_conversation": enrich_with_live_conversation,
                    "environment_id": environment_id,
                    "execution_mode": execution_mode,
                    "flows": flows,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_no_response_retries": max_no_response_retries,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "name": name,
                    "no_response_retry_backoff_seconds": no_response_retry_backoff_seconds,
                    "persona_id": persona_id,
                    "questions": questions,
                    "ramp_up_seconds": ramp_up_seconds,
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

    async def answer_resource_generation(
        self,
        generation_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationAnswerResourceGenerationResponse:
        """
        Answers the question a simulation resource generation is waiting on (status
        NEEDS_INPUT). If nobody answers within 15 minutes, it goes ahead with its
        default.

        Args:
          text: What you want the generation to know

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return await self._post(
            f"/v1/simulation/generations/resources/{generation_id}/answer",
            body=await async_maybe_transform(
                {"text": text}, simulation_answer_resource_generation_params.SimulationAnswerResourceGenerationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationAnswerResourceGenerationResponse,
        )

    async def cancel_resource_generation(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCancelResourceGenerationResponse:
        """Stops a running simulation resource generation.

        Flows and metrics it already
        created are kept; no run plan is made. Refused once the generation has finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return await self._post(
            f"/v1/simulation/generations/resources/{generation_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCancelResourceGenerationResponse,
        )

    async def generate_resources(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        agent_endpoint_id: str | Omit = omit,
        capabilities: List[
            Literal[
                "APPOINTMENT_BOOKING",
                "FAQ",
                "IDENTITY_VERIFICATION",
                "ACCOUNT_MANAGEMENT",
                "BILLING_AND_PAYMENTS",
                "ORDER_MANAGEMENT",
                "TROUBLESHOOTING",
                "CALL_ROUTING",
                "LEAD_QUALIFICATION",
                "COLLECTIONS",
                "OUTBOUND_CALLING",
            ]
        ]
        | Omit = omit,
        explore: simulation_generate_resources_params.Explore | Omit = omit,
        industry: Literal[
            "HEALTHCARE",
            "FINANCIAL_SERVICES",
            "INSURANCE",
            "DEBT_COLLECTION",
            "RETAIL",
            "TRAVEL_AND_HOSPITALITY",
            "TELECOMMUNICATIONS",
            "TECHNOLOGY",
            "PUBLIC_SECTOR",
            "UTILITIES",
            "LOGISTICS",
            "AUTOMOTIVE",
            "HOME_SERVICES",
            "RESTAURANTS",
            "EDUCATION",
            "RECRUITING_AND_STAFFING",
            "OTHER",
        ]
        | Omit = omit,
        industry_description: str | Omit = omit,
        testing_instructions: str | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGenerateResourcesResponse:
        """
        Works out what to test for an existing agent, then creates the customer flows,
        metrics and checks to simulate it, and a run plan that runs them. It does not
        create or change the agent. It also reads the agent's recent production calls
        and open issues. Run it again and it builds on what earlier generations made,
        adding only what changed; when nothing has, it finishes straight away and says
        so. Runs in the background: watch the `simulation.resource_generation.completed`
        webhook, or poll `GET /v1/simulation/generations/resources/{generationId}`.
        Takes one agent for now. Refused while another generation for the agent is
        running. Needs the 'simulation:create' and 'metric:create' permissions.
        Exploration also needs 'simulation:run', and is turned off for keys without it
        unless explore.enabled is set.

        Args:
          agent_ids: The agents to generate simulation resources for. One agent per generation for
              now.

          agent_endpoint_id: The endpoint the run plan calls. Defaults to the agent's newest endpoint.

          capabilities: The capabilities to test. Omit to let Roark work them out from the agent.

          explore: Exploration settings

          industry: The industry the agent serves.

          industry_description: The industry in your own words, when none of the listed ones fits. Use it with
              industry OTHER.

          testing_instructions: What you want tested, in your own words. Each scenario you describe becomes a
              flow.

          website_url: A page Roark reads to learn about the business.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulation/generations/resources",
            body=await async_maybe_transform(
                {
                    "agent_ids": agent_ids,
                    "agent_endpoint_id": agent_endpoint_id,
                    "capabilities": capabilities,
                    "explore": explore,
                    "industry": industry,
                    "industry_description": industry_description,
                    "testing_instructions": testing_instructions,
                    "website_url": website_url,
                },
                simulation_generate_resources_params.SimulationGenerateResourcesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGenerateResourcesResponse,
        )

    async def get_resource_generation(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGetResourceGenerationResponse:
        """
        Returns one simulation resource generation, for example the one a webhook named.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return await self._get(
            f"/v1/simulation/generations/resources/{generation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGetResourceGenerationResponse,
        )

    async def guide_resource_generation(
        self,
        generation_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGuideResourceGenerationResponse:
        """
        Tells a running simulation resource generation what to focus on or avoid, in
        your own words. It reads it on its next turn and it outranks its own plan.
        Refused once the generation has finished.

        Args:
          text: What you want the generation to know

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return await self._post(
            f"/v1/simulation/generations/resources/{generation_id}/guidance",
            body=await async_maybe_transform(
                {"text": text}, simulation_guide_resource_generation_params.SimulationGuideResourceGenerationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGuideResourceGenerationResponse,
        )

    async def list_resource_generations(
        self,
        *,
        agent_ids: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationListResourceGenerationsResponse:
        """
        Returns the project's simulation resource generations, newest first, optionally
        only for some agents: each one's progress, the run plan it created, and every
        flow, metric and check it added or left out, with the reason and the source it
        came from.

        Args:
          agent_ids: Only generations for these agents, comma-separated, at most 100. Omit for every
              agent.

          limit: How many to return, newest first. Default 20, max 50.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/generations/resources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_ids": agent_ids,
                        "limit": limit,
                    },
                    simulation_list_resource_generations_params.SimulationListResourceGenerationsParams,
                ),
            ),
            cast_to=SimulationListResourceGenerationsResponse,
        )

    async def mock_tool(
        self,
        *,
        simulation_job_id: str,
        tool_name: str,
        arguments: Dict[str, object] | Omit = omit,
        session_id: str | Omit = omit,
        tool_description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationMockToolResponse:
        """The server half of the tool guard for code-first agents.

        When a guarded tool
        fires during a Roark test call, send the invocation here instead of executing
        it: Roark answers with a simulated backend response that is valid JSON, shaped
        by the tool contract you pass, consistent with the test scenario, and consistent
        with earlier mocked responses in the same call. Real callers are never affected:
        the guard only diverts when the agent-config resolve response identified the
        session as a Roark simulation, and this endpoint independently re-validates the
        simulation before answering. Failure contract for your wrapper: `404` means the
        simulation id is unknown to this project (treat the session as real). `409`
        means the simulation has already ended (stale session state: do NOT execute the
        real tool; return your static fallback). `5xx` means generation failed (return
        your static fallback). Identical retries (same tool, same arguments) within a
        few minutes return the stored response, so double-fired handlers stay
        consistent.

        Args:
          simulation_job_id: The simulation this session belongs to, from the agent-config resolve response
              (`simulationJobId`). Roark re-validates it against the live simulation before
              answering.

          tool_name: The tool the agent invoked.

          arguments: The arguments the agent called the tool with, verbatim.

          session_id: Your session or room identifier, echoed back in logs for correlation.

          tool_description: The tool's contract: its description and, ideally, its parameter and return
              shape. The more contract you pass, the more faithful the simulated response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulation/tool-mock",
            body=await async_maybe_transform(
                {
                    "simulation_job_id": simulation_job_id,
                    "tool_name": tool_name,
                    "arguments": arguments,
                    "session_id": session_id,
                    "tool_description": tool_description,
                },
                simulation_mock_tool_params.SimulationMockToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationMockToolResponse,
        )

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
          plan_id: The run plan to run, saved or hidden. Rename or unhide it with `PUT
              /v1/simulation/plan/{planId}`.

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
        plan_config_key: str,
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
          plan_config_key: The config key of a plan to run, as applied from config as code
              (`simulationPlan/<name>`). Runs a config-managed plan by name, with no id
              lookup. Unique per project.

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
        additional_metrics: Iterable[simulation_run_params.RunSimulationFromConfigPlanMetric] | Omit = omit,
        calls_per_second: Optional[float] | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_values: List[Union[str, simulation_run_params.ComparisonArm]] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        environment_id: str | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_params.RunSimulationFromConfigPlanFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        persona_id: str | Omit = omit,
        questions: Iterable[simulation_run_params.RunSimulationFromTemplateQuestion] | Omit = omit,
        ramp_up_seconds: Optional[int] | Omit = omit,
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

          additional_metrics: Metrics to collect on top of the template's own, referenced by `id` or `slug`
              like a plan's `metrics`. The template's metrics and checks always run; naming
              one of them here again keeps it once, with the success criteria you set on it.

          calls_per_second: The most simulations a run starts per second (0.01-10), fractional allowed: 0.2
              starts one every 5 seconds. Omitted or `null` starts them as fast as
              `maxConcurrentJobs` allows. The concurrency limit still applies on top, so a run
              holds the rate only while calls last under `maxConcurrentJobs` /
              `callsPerSecond` seconds. A run reports the rate it achieved as
              `dialRate.achievedCallsPerSecond`. A rate above the project's concurrency limit
              / 30 is refused with 400: that limit could only hold it with calls under 30
              seconds.

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

          name: What to call this. Defaults to the template's name and the date, and required
              with `saveAsPlan`.

          no_response_retry_backoff_seconds: Seconds a retry waits before it dials (30-600). Only used when
              `maxNoResponseRetries` is above 0.

          persona_id: For `question-answer-check`: the persona that asks the questions.

          questions: For the `question-answer-check` template: the questions to ask and the answer
              expected for each. Every question runs as its own graded call.

          ramp_up_seconds: Seconds over which the rate climbs linearly from 0 to `callsPerSecond` (0-3600).
              Omitted, `null` or 0 starts at the full rate. Only used with `callsPerSecond`.

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

    @required_args(["plan"], ["plan_id"], ["plan_config_key"], ["agent_endpoints", "direction", "template"])
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
        plan_config_key: str | Omit = omit,
        agent_endpoints: Iterable[simulation_run_params.RunSimulationFromConfigPlanAgentEndpoint] | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        template: str | Omit = omit,
        additional_metrics: Iterable[simulation_run_params.RunSimulationFromConfigPlanMetric] | Omit = omit,
        calls_per_second: Optional[float] | Omit = omit,
        comparison_baseline: Optional[str] | Omit = omit,
        comparison_values: List[Union[str, simulation_run_params.ComparisonArm]] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        end_call_reasons: SequenceNotStr[str] | Omit = omit,
        enrich_with_live_conversation: bool | Omit = omit,
        environment_id: str | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        flows: Iterable[simulation_run_params.RunSimulationFromConfigPlanFlow] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_no_response_retries: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        name: str | Omit = omit,
        no_response_retry_backoff_seconds: int | Omit = omit,
        persona_id: str | Omit = omit,
        questions: Iterable[simulation_run_params.RunSimulationFromTemplateQuestion] | Omit = omit,
        ramp_up_seconds: Optional[int] | Omit = omit,
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
                    "plan_config_key": plan_config_key,
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "template": template,
                    "additional_metrics": additional_metrics,
                    "calls_per_second": calls_per_second,
                    "comparison_baseline": comparison_baseline,
                    "comparison_values": comparison_values,
                    "end_call_phrases": end_call_phrases,
                    "end_call_reasons": end_call_reasons,
                    "enrich_with_live_conversation": enrich_with_live_conversation,
                    "environment_id": environment_id,
                    "execution_mode": execution_mode,
                    "flows": flows,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_no_response_retries": max_no_response_retries,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "name": name,
                    "no_response_retry_backoff_seconds": no_response_retry_backoff_seconds,
                    "persona_id": persona_id,
                    "questions": questions,
                    "ramp_up_seconds": ramp_up_seconds,
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

        self.answer_resource_generation = to_raw_response_wrapper(
            simulation.answer_resource_generation,
        )
        self.cancel_resource_generation = to_raw_response_wrapper(
            simulation.cancel_resource_generation,
        )
        self.generate_resources = to_raw_response_wrapper(
            simulation.generate_resources,
        )
        self.get_resource_generation = to_raw_response_wrapper(
            simulation.get_resource_generation,
        )
        self.guide_resource_generation = to_raw_response_wrapper(
            simulation.guide_resource_generation,
        )
        self.list_resource_generations = to_raw_response_wrapper(
            simulation.list_resource_generations,
        )
        self.mock_tool = to_raw_response_wrapper(
            simulation.mock_tool,
        )
        self.run = to_raw_response_wrapper(
            simulation.run,
        )


class AsyncSimulationResourceWithRawResponse:
    def __init__(self, simulation: AsyncSimulationResource) -> None:
        self._simulation = simulation

        self.answer_resource_generation = async_to_raw_response_wrapper(
            simulation.answer_resource_generation,
        )
        self.cancel_resource_generation = async_to_raw_response_wrapper(
            simulation.cancel_resource_generation,
        )
        self.generate_resources = async_to_raw_response_wrapper(
            simulation.generate_resources,
        )
        self.get_resource_generation = async_to_raw_response_wrapper(
            simulation.get_resource_generation,
        )
        self.guide_resource_generation = async_to_raw_response_wrapper(
            simulation.guide_resource_generation,
        )
        self.list_resource_generations = async_to_raw_response_wrapper(
            simulation.list_resource_generations,
        )
        self.mock_tool = async_to_raw_response_wrapper(
            simulation.mock_tool,
        )
        self.run = async_to_raw_response_wrapper(
            simulation.run,
        )


class SimulationResourceWithStreamingResponse:
    def __init__(self, simulation: SimulationResource) -> None:
        self._simulation = simulation

        self.answer_resource_generation = to_streamed_response_wrapper(
            simulation.answer_resource_generation,
        )
        self.cancel_resource_generation = to_streamed_response_wrapper(
            simulation.cancel_resource_generation,
        )
        self.generate_resources = to_streamed_response_wrapper(
            simulation.generate_resources,
        )
        self.get_resource_generation = to_streamed_response_wrapper(
            simulation.get_resource_generation,
        )
        self.guide_resource_generation = to_streamed_response_wrapper(
            simulation.guide_resource_generation,
        )
        self.list_resource_generations = to_streamed_response_wrapper(
            simulation.list_resource_generations,
        )
        self.mock_tool = to_streamed_response_wrapper(
            simulation.mock_tool,
        )
        self.run = to_streamed_response_wrapper(
            simulation.run,
        )


class AsyncSimulationResourceWithStreamingResponse:
    def __init__(self, simulation: AsyncSimulationResource) -> None:
        self._simulation = simulation

        self.answer_resource_generation = async_to_streamed_response_wrapper(
            simulation.answer_resource_generation,
        )
        self.cancel_resource_generation = async_to_streamed_response_wrapper(
            simulation.cancel_resource_generation,
        )
        self.generate_resources = async_to_streamed_response_wrapper(
            simulation.generate_resources,
        )
        self.get_resource_generation = async_to_streamed_response_wrapper(
            simulation.get_resource_generation,
        )
        self.guide_resource_generation = async_to_streamed_response_wrapper(
            simulation.guide_resource_generation,
        )
        self.list_resource_generations = async_to_streamed_response_wrapper(
            simulation.list_resource_generations,
        )
        self.mock_tool = async_to_streamed_response_wrapper(
            simulation.mock_tool,
        )
        self.run = async_to_streamed_response_wrapper(
            simulation.run,
        )
