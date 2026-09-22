# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    autoimprove_job_create_params,
    autoimprove_job_send_guidance_params,
    autoimprove_job_answer_question_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.autoimprove_job_list_response import AutoimproveJobListResponse
from ..types.autoimprove_job_cancel_response import AutoimproveJobCancelResponse
from ..types.autoimprove_job_create_response import AutoimproveJobCreateResponse
from ..types.autoimprove_job_dismiss_response import AutoimproveJobDismissResponse
from ..types.autoimprove_job_promote_response import AutoimproveJobPromoteResponse
from ..types.autoimprove_job_get_by_id_response import AutoimproveJobGetByIDResponse
from ..types.autoimprove_job_send_guidance_response import AutoimproveJobSendGuidanceResponse
from ..types.autoimprove_job_answer_question_response import AutoimproveJobAnswerQuestionResponse

__all__ = ["AutoimproveJobResource", "AsyncAutoimproveJobResource"]


class AutoimproveJobResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoimproveJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AutoimproveJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoimproveJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AutoimproveJobResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_id: str,
        objective_label: str,
        objective_metric_definition_id: str,
        customer_integration_id: str | Omit = omit,
        max_iterations: int | Omit = omit,
        max_sim_calls: int | Omit = omit,
        staging_agent_id: str | Omit = omit,
        target_value: float | Omit = omit,
        validation_run_plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobCreateResponse:
        """Commission Roark on an objective.

        It clones the agent into a staging shadow (or
        uses your designated staging agent), authors a validation suite of simulated
        callers, measures a baseline, changes the staging configuration, and re-tests
        until the objective metric passes its target. Production is never touched by the
        loop; verified changes wait for promotion. Requires an active provider
        integration (Vapi, Retell, or ElevenLabs) with agent config writes enabled. One
        live job per agent: starting a second returns a conflict. The job runs
        asynchronously; poll GET /v1/autoimprove/job/{jobId} or watch it in the
        dashboard. When its status is NEEDS_INPUT, answer via the answer endpoint; when
        AWAITING_PROMOTE, promote or dismiss.

        Args:
          agent_id: The production agent to improve. It is never modified until you promote.

          objective_label: Human-readable label for the objective, shown everywhere the job appears.

          objective_metric_definition_id: The metric that defines success: a pass/fail metric, or a threshold variant of a
              scale metric (for example "PII Handling >= 4"). Roark measures the pass rate of
              this metric across simulated calls.

          customer_integration_id: The provider integration whose credentials Roark uses. Omit to use the project's
              active integration for the agent's provider. The integration must have agent
              config writes enabled.

          max_iterations: Cap on decision turns. Defaults to 50.

          max_sim_calls: Cap on simulated calls dialed. Defaults to 200.

          staging_agent_id: An existing agent to stage changes on instead of the default shadow clone. Must
              be a different agent from agentId, on the same provider.

          target_value: The pass-rate percentage that counts as fixed. Defaults to 90.

          validation_run_plan_id: An existing simulation run plan to validate with. Omit to let Roark author its
              own suite.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/autoimprove/job",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "objective_label": objective_label,
                    "objective_metric_definition_id": objective_metric_definition_id,
                    "customer_integration_id": customer_integration_id,
                    "max_iterations": max_iterations,
                    "max_sim_calls": max_sim_calls,
                    "staging_agent_id": staging_agent_id,
                    "target_value": target_value,
                    "validation_run_plan_id": validation_run_plan_id,
                },
                autoimprove_job_create_params.AutoimproveJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobListResponse:
        """List the Autoimprove jobs in this project, most recent first, capped at 100.

        A
        job is one autonomous engagement: Roark improving one agent toward one objective
        metric on a staging copy, with a human-gated promote to production at the end.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/autoimprove/job",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobListResponse,
        )

    def answer_question(
        self,
        job_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobAnswerQuestionResponse:
        """Answer the question a job is blocked on.

        Only meaningful while the job status is
        NEEDS_INPUT (the open QUESTION entry carries the offered options; free text is
        also accepted). Otherwise returns a conflict.

        Args:
          text: The message for Roark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/v1/autoimprove/job/{job_id}/answer",
            body=maybe_transform(
                {"text": text}, autoimprove_job_answer_question_params.AutoimproveJobAnswerQuestionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobAnswerQuestionResponse,
        )

    def cancel(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobCancelResponse:
        """Stop a live job.

        Production is never changed by a cancel; everything the job set
        up (the shadow agent, its phone number, authored test flows and run plan) is
        cleaned up automatically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/v1/autoimprove/job/{job_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobCancelResponse,
        )

    def dismiss(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobDismissResponse:
        """
        Discard a verified job without promoting: production stays untouched and the
        staging resources are cleaned up. Only a job in AWAITING_PROMOTE can be
        dismissed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/v1/autoimprove/job/{job_id}/dismiss",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobDismissResponse,
        )

    def get_by_id(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobGetByIDResponse:
        """
        Fetch one job with its full worklog: every step Roark took, the validation
        batches with their pass-rate movement, any question it is waiting on, and its
        final report once concluded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/autoimprove/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobGetByIDResponse,
        )

    def promote(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobPromoteResponse:
        """Apply the verified staging changes to the PRODUCTION agent.

        Only a job in
        AWAITING_PROMOTE can be promoted. A snapshot of the production configuration is
        taken immediately before the write, so the promote is fully rollbackable. After
        the promote the staging shadow and its phone number are cleaned up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/v1/autoimprove/job/{job_id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobPromoteResponse,
        )

    def send_guidance(
        self,
        job_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobSendGuidanceResponse:
        """Steer Roark mid-job.

        The message is folded into its next decision and is
        binding. Accepted while the job is live (RUNNING, NEEDS_INPUT, or PAUSED); a
        concluded job returns a conflict.

        Args:
          text: The message for Roark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/v1/autoimprove/job/{job_id}/guidance",
            body=maybe_transform({"text": text}, autoimprove_job_send_guidance_params.AutoimproveJobSendGuidanceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobSendGuidanceResponse,
        )


class AsyncAutoimproveJobResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoimproveJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoimproveJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoimproveJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAutoimproveJobResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_id: str,
        objective_label: str,
        objective_metric_definition_id: str,
        customer_integration_id: str | Omit = omit,
        max_iterations: int | Omit = omit,
        max_sim_calls: int | Omit = omit,
        staging_agent_id: str | Omit = omit,
        target_value: float | Omit = omit,
        validation_run_plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobCreateResponse:
        """Commission Roark on an objective.

        It clones the agent into a staging shadow (or
        uses your designated staging agent), authors a validation suite of simulated
        callers, measures a baseline, changes the staging configuration, and re-tests
        until the objective metric passes its target. Production is never touched by the
        loop; verified changes wait for promotion. Requires an active provider
        integration (Vapi, Retell, or ElevenLabs) with agent config writes enabled. One
        live job per agent: starting a second returns a conflict. The job runs
        asynchronously; poll GET /v1/autoimprove/job/{jobId} or watch it in the
        dashboard. When its status is NEEDS_INPUT, answer via the answer endpoint; when
        AWAITING_PROMOTE, promote or dismiss.

        Args:
          agent_id: The production agent to improve. It is never modified until you promote.

          objective_label: Human-readable label for the objective, shown everywhere the job appears.

          objective_metric_definition_id: The metric that defines success: a pass/fail metric, or a threshold variant of a
              scale metric (for example "PII Handling >= 4"). Roark measures the pass rate of
              this metric across simulated calls.

          customer_integration_id: The provider integration whose credentials Roark uses. Omit to use the project's
              active integration for the agent's provider. The integration must have agent
              config writes enabled.

          max_iterations: Cap on decision turns. Defaults to 50.

          max_sim_calls: Cap on simulated calls dialed. Defaults to 200.

          staging_agent_id: An existing agent to stage changes on instead of the default shadow clone. Must
              be a different agent from agentId, on the same provider.

          target_value: The pass-rate percentage that counts as fixed. Defaults to 90.

          validation_run_plan_id: An existing simulation run plan to validate with. Omit to let Roark author its
              own suite.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/autoimprove/job",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "objective_label": objective_label,
                    "objective_metric_definition_id": objective_metric_definition_id,
                    "customer_integration_id": customer_integration_id,
                    "max_iterations": max_iterations,
                    "max_sim_calls": max_sim_calls,
                    "staging_agent_id": staging_agent_id,
                    "target_value": target_value,
                    "validation_run_plan_id": validation_run_plan_id,
                },
                autoimprove_job_create_params.AutoimproveJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobListResponse:
        """List the Autoimprove jobs in this project, most recent first, capped at 100.

        A
        job is one autonomous engagement: Roark improving one agent toward one objective
        metric on a staging copy, with a human-gated promote to production at the end.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/autoimprove/job",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobListResponse,
        )

    async def answer_question(
        self,
        job_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobAnswerQuestionResponse:
        """Answer the question a job is blocked on.

        Only meaningful while the job status is
        NEEDS_INPUT (the open QUESTION entry carries the offered options; free text is
        also accepted). Otherwise returns a conflict.

        Args:
          text: The message for Roark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/v1/autoimprove/job/{job_id}/answer",
            body=await async_maybe_transform(
                {"text": text}, autoimprove_job_answer_question_params.AutoimproveJobAnswerQuestionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobAnswerQuestionResponse,
        )

    async def cancel(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobCancelResponse:
        """Stop a live job.

        Production is never changed by a cancel; everything the job set
        up (the shadow agent, its phone number, authored test flows and run plan) is
        cleaned up automatically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/v1/autoimprove/job/{job_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobCancelResponse,
        )

    async def dismiss(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobDismissResponse:
        """
        Discard a verified job without promoting: production stays untouched and the
        staging resources are cleaned up. Only a job in AWAITING_PROMOTE can be
        dismissed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/v1/autoimprove/job/{job_id}/dismiss",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobDismissResponse,
        )

    async def get_by_id(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobGetByIDResponse:
        """
        Fetch one job with its full worklog: every step Roark took, the validation
        batches with their pass-rate movement, any question it is waiting on, and its
        final report once concluded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/autoimprove/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobGetByIDResponse,
        )

    async def promote(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobPromoteResponse:
        """Apply the verified staging changes to the PRODUCTION agent.

        Only a job in
        AWAITING_PROMOTE can be promoted. A snapshot of the production configuration is
        taken immediately before the write, so the promote is fully rollbackable. After
        the promote the staging shadow and its phone number are cleaned up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/v1/autoimprove/job/{job_id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobPromoteResponse,
        )

    async def send_guidance(
        self,
        job_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveJobSendGuidanceResponse:
        """Steer Roark mid-job.

        The message is folded into its next decision and is
        binding. Accepted while the job is live (RUNNING, NEEDS_INPUT, or PAUSED); a
        concluded job returns a conflict.

        Args:
          text: The message for Roark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/v1/autoimprove/job/{job_id}/guidance",
            body=await async_maybe_transform(
                {"text": text}, autoimprove_job_send_guidance_params.AutoimproveJobSendGuidanceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveJobSendGuidanceResponse,
        )


class AutoimproveJobResourceWithRawResponse:
    def __init__(self, autoimprove_job: AutoimproveJobResource) -> None:
        self._autoimprove_job = autoimprove_job

        self.create = to_raw_response_wrapper(
            autoimprove_job.create,
        )
        self.list = to_raw_response_wrapper(
            autoimprove_job.list,
        )
        self.answer_question = to_raw_response_wrapper(
            autoimprove_job.answer_question,
        )
        self.cancel = to_raw_response_wrapper(
            autoimprove_job.cancel,
        )
        self.dismiss = to_raw_response_wrapper(
            autoimprove_job.dismiss,
        )
        self.get_by_id = to_raw_response_wrapper(
            autoimprove_job.get_by_id,
        )
        self.promote = to_raw_response_wrapper(
            autoimprove_job.promote,
        )
        self.send_guidance = to_raw_response_wrapper(
            autoimprove_job.send_guidance,
        )


class AsyncAutoimproveJobResourceWithRawResponse:
    def __init__(self, autoimprove_job: AsyncAutoimproveJobResource) -> None:
        self._autoimprove_job = autoimprove_job

        self.create = async_to_raw_response_wrapper(
            autoimprove_job.create,
        )
        self.list = async_to_raw_response_wrapper(
            autoimprove_job.list,
        )
        self.answer_question = async_to_raw_response_wrapper(
            autoimprove_job.answer_question,
        )
        self.cancel = async_to_raw_response_wrapper(
            autoimprove_job.cancel,
        )
        self.dismiss = async_to_raw_response_wrapper(
            autoimprove_job.dismiss,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            autoimprove_job.get_by_id,
        )
        self.promote = async_to_raw_response_wrapper(
            autoimprove_job.promote,
        )
        self.send_guidance = async_to_raw_response_wrapper(
            autoimprove_job.send_guidance,
        )


class AutoimproveJobResourceWithStreamingResponse:
    def __init__(self, autoimprove_job: AutoimproveJobResource) -> None:
        self._autoimprove_job = autoimprove_job

        self.create = to_streamed_response_wrapper(
            autoimprove_job.create,
        )
        self.list = to_streamed_response_wrapper(
            autoimprove_job.list,
        )
        self.answer_question = to_streamed_response_wrapper(
            autoimprove_job.answer_question,
        )
        self.cancel = to_streamed_response_wrapper(
            autoimprove_job.cancel,
        )
        self.dismiss = to_streamed_response_wrapper(
            autoimprove_job.dismiss,
        )
        self.get_by_id = to_streamed_response_wrapper(
            autoimprove_job.get_by_id,
        )
        self.promote = to_streamed_response_wrapper(
            autoimprove_job.promote,
        )
        self.send_guidance = to_streamed_response_wrapper(
            autoimprove_job.send_guidance,
        )


class AsyncAutoimproveJobResourceWithStreamingResponse:
    def __init__(self, autoimprove_job: AsyncAutoimproveJobResource) -> None:
        self._autoimprove_job = autoimprove_job

        self.create = async_to_streamed_response_wrapper(
            autoimprove_job.create,
        )
        self.list = async_to_streamed_response_wrapper(
            autoimprove_job.list,
        )
        self.answer_question = async_to_streamed_response_wrapper(
            autoimprove_job.answer_question,
        )
        self.cancel = async_to_streamed_response_wrapper(
            autoimprove_job.cancel,
        )
        self.dismiss = async_to_streamed_response_wrapper(
            autoimprove_job.dismiss,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            autoimprove_job.get_by_id,
        )
        self.promote = async_to_streamed_response_wrapper(
            autoimprove_job.promote,
        )
        self.send_guidance = async_to_streamed_response_wrapper(
            autoimprove_job.send_guidance,
        )
