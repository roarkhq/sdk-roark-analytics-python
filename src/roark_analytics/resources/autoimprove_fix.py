# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    autoimprove_fix_create_params,
    autoimprove_fix_send_guidance_params,
    autoimprove_fix_answer_question_params,
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
from ..types.autoimprove_fix_list_response import AutoimproveFixListResponse
from ..types.autoimprove_fix_cancel_response import AutoimproveFixCancelResponse
from ..types.autoimprove_fix_create_response import AutoimproveFixCreateResponse
from ..types.autoimprove_fix_dismiss_response import AutoimproveFixDismissResponse
from ..types.autoimprove_fix_promote_response import AutoimproveFixPromoteResponse
from ..types.autoimprove_fix_get_by_id_response import AutoimproveFixGetByIDResponse
from ..types.autoimprove_fix_send_guidance_response import AutoimproveFixSendGuidanceResponse
from ..types.autoimprove_fix_answer_question_response import AutoimproveFixAnswerQuestionResponse

__all__ = ["AutoimproveFixResource", "AsyncAutoimproveFixResource"]


class AutoimproveFixResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoimproveFixResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AutoimproveFixResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoimproveFixResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AutoimproveFixResourceWithStreamingResponse(self)

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
    ) -> AutoimproveFixCreateResponse:
        """Commission Roark on an objective.

        It clones the agent into a staging shadow (or
        uses your designated staging agent), authors a validation suite of simulated
        callers, measures a baseline, changes the staging configuration, and re-tests
        until the objective metric passes its target. Production is never touched by the
        loop; a verified fix waits for promotion. Requires an active provider
        integration (Vapi or Retell) with agent config writes enabled. One live fix per
        agent: starting a second returns a conflict. The fix runs asynchronously; poll
        GET /v1/autoimprove/fix/{fixId} or watch it in the dashboard. When its status is
        NEEDS_INPUT, answer via the answer endpoint; when AWAITING_PROMOTE, promote or
        dismiss.

        Args:
          agent_id: The production agent to improve. It is never modified until you promote.

          objective_label: Human-readable label for the objective, shown everywhere the fix appears.

          objective_metric_definition_id: The metric that defines success: a pass/fail metric, or a threshold variant of a
              scale metric (for example "PII Handling >= 4"). Roark measures the pass rate of
              this metric across simulated calls.

          customer_integration_id: The provider integration whose credentials Roark uses. Omit to use the project's
              active integration for the agent's provider. The integration must have agent
              config writes enabled.

          max_iterations: Cap on decision turns. Defaults to 10.

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
            "/v1/autoimprove/fix",
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
                autoimprove_fix_create_params.AutoimproveFixCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixCreateResponse,
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
    ) -> AutoimproveFixListResponse:
        """List the Autoimprove fixes in this project, most recent first, capped at 100.

        A
        fix is one autonomous engagement: Roark improving one agent toward one objective
        metric on a staging copy, with a human-gated promote to production at the end.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/autoimprove/fix",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixListResponse,
        )

    def answer_question(
        self,
        fix_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixAnswerQuestionResponse:
        """Answer the question a fix is blocked on.

        Only meaningful while the fix status is
        NEEDS_INPUT (the open QUESTION entry carries the offered options; free text is
        also accepted). Otherwise returns a conflict.

        Args:
          text: The message for Roark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return self._post(
            f"/v1/autoimprove/fix/{fix_id}/answer",
            body=maybe_transform(
                {"text": text}, autoimprove_fix_answer_question_params.AutoimproveFixAnswerQuestionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixAnswerQuestionResponse,
        )

    def cancel(
        self,
        fix_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixCancelResponse:
        """Stop a live fix.

        Production is never changed by a cancel; everything the fix set
        up (the shadow agent, its phone number, authored test flows and run plan) is
        cleaned up automatically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return self._post(
            f"/v1/autoimprove/fix/{fix_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixCancelResponse,
        )

    def dismiss(
        self,
        fix_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixDismissResponse:
        """
        Discard a verified fix without promoting: production stays untouched and the
        staging resources are cleaned up. Only a fix in AWAITING_PROMOTE can be
        dismissed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return self._post(
            f"/v1/autoimprove/fix/{fix_id}/dismiss",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixDismissResponse,
        )

    def get_by_id(
        self,
        fix_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixGetByIDResponse:
        """
        Fetch one fix with its full worklog: every step Roark took, the validation
        batches with their pass-rate movement, any question it is waiting on, and its
        final report once concluded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return self._get(
            f"/v1/autoimprove/fix/{fix_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixGetByIDResponse,
        )

    def promote(
        self,
        fix_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixPromoteResponse:
        """Apply the verified staging changes to the PRODUCTION agent.

        Only a fix in
        AWAITING_PROMOTE can be promoted. A snapshot of the production configuration is
        taken immediately before the write, so the promote is fully rollbackable. After
        the promote the staging shadow and its phone number are cleaned up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return self._post(
            f"/v1/autoimprove/fix/{fix_id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixPromoteResponse,
        )

    def send_guidance(
        self,
        fix_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixSendGuidanceResponse:
        """Steer Roark mid-fix.

        The message is folded into its next decision and is
        binding. Accepted while the fix is live (RUNNING, NEEDS_INPUT, or PAUSED); a
        concluded fix returns a conflict.

        Args:
          text: The message for Roark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return self._post(
            f"/v1/autoimprove/fix/{fix_id}/guidance",
            body=maybe_transform({"text": text}, autoimprove_fix_send_guidance_params.AutoimproveFixSendGuidanceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixSendGuidanceResponse,
        )


class AsyncAutoimproveFixResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoimproveFixResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoimproveFixResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoimproveFixResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAutoimproveFixResourceWithStreamingResponse(self)

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
    ) -> AutoimproveFixCreateResponse:
        """Commission Roark on an objective.

        It clones the agent into a staging shadow (or
        uses your designated staging agent), authors a validation suite of simulated
        callers, measures a baseline, changes the staging configuration, and re-tests
        until the objective metric passes its target. Production is never touched by the
        loop; a verified fix waits for promotion. Requires an active provider
        integration (Vapi or Retell) with agent config writes enabled. One live fix per
        agent: starting a second returns a conflict. The fix runs asynchronously; poll
        GET /v1/autoimprove/fix/{fixId} or watch it in the dashboard. When its status is
        NEEDS_INPUT, answer via the answer endpoint; when AWAITING_PROMOTE, promote or
        dismiss.

        Args:
          agent_id: The production agent to improve. It is never modified until you promote.

          objective_label: Human-readable label for the objective, shown everywhere the fix appears.

          objective_metric_definition_id: The metric that defines success: a pass/fail metric, or a threshold variant of a
              scale metric (for example "PII Handling >= 4"). Roark measures the pass rate of
              this metric across simulated calls.

          customer_integration_id: The provider integration whose credentials Roark uses. Omit to use the project's
              active integration for the agent's provider. The integration must have agent
              config writes enabled.

          max_iterations: Cap on decision turns. Defaults to 10.

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
            "/v1/autoimprove/fix",
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
                autoimprove_fix_create_params.AutoimproveFixCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixCreateResponse,
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
    ) -> AutoimproveFixListResponse:
        """List the Autoimprove fixes in this project, most recent first, capped at 100.

        A
        fix is one autonomous engagement: Roark improving one agent toward one objective
        metric on a staging copy, with a human-gated promote to production at the end.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/autoimprove/fix",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixListResponse,
        )

    async def answer_question(
        self,
        fix_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixAnswerQuestionResponse:
        """Answer the question a fix is blocked on.

        Only meaningful while the fix status is
        NEEDS_INPUT (the open QUESTION entry carries the offered options; free text is
        also accepted). Otherwise returns a conflict.

        Args:
          text: The message for Roark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return await self._post(
            f"/v1/autoimprove/fix/{fix_id}/answer",
            body=await async_maybe_transform(
                {"text": text}, autoimprove_fix_answer_question_params.AutoimproveFixAnswerQuestionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixAnswerQuestionResponse,
        )

    async def cancel(
        self,
        fix_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixCancelResponse:
        """Stop a live fix.

        Production is never changed by a cancel; everything the fix set
        up (the shadow agent, its phone number, authored test flows and run plan) is
        cleaned up automatically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return await self._post(
            f"/v1/autoimprove/fix/{fix_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixCancelResponse,
        )

    async def dismiss(
        self,
        fix_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixDismissResponse:
        """
        Discard a verified fix without promoting: production stays untouched and the
        staging resources are cleaned up. Only a fix in AWAITING_PROMOTE can be
        dismissed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return await self._post(
            f"/v1/autoimprove/fix/{fix_id}/dismiss",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixDismissResponse,
        )

    async def get_by_id(
        self,
        fix_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixGetByIDResponse:
        """
        Fetch one fix with its full worklog: every step Roark took, the validation
        batches with their pass-rate movement, any question it is waiting on, and its
        final report once concluded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return await self._get(
            f"/v1/autoimprove/fix/{fix_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixGetByIDResponse,
        )

    async def promote(
        self,
        fix_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixPromoteResponse:
        """Apply the verified staging changes to the PRODUCTION agent.

        Only a fix in
        AWAITING_PROMOTE can be promoted. A snapshot of the production configuration is
        taken immediately before the write, so the promote is fully rollbackable. After
        the promote the staging shadow and its phone number are cleaned up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return await self._post(
            f"/v1/autoimprove/fix/{fix_id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixPromoteResponse,
        )

    async def send_guidance(
        self,
        fix_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoimproveFixSendGuidanceResponse:
        """Steer Roark mid-fix.

        The message is folded into its next decision and is
        binding. Accepted while the fix is live (RUNNING, NEEDS_INPUT, or PAUSED); a
        concluded fix returns a conflict.

        Args:
          text: The message for Roark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fix_id:
            raise ValueError(f"Expected a non-empty value for `fix_id` but received {fix_id!r}")
        return await self._post(
            f"/v1/autoimprove/fix/{fix_id}/guidance",
            body=await async_maybe_transform(
                {"text": text}, autoimprove_fix_send_guidance_params.AutoimproveFixSendGuidanceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoimproveFixSendGuidanceResponse,
        )


class AutoimproveFixResourceWithRawResponse:
    def __init__(self, autoimprove_fix: AutoimproveFixResource) -> None:
        self._autoimprove_fix = autoimprove_fix

        self.create = to_raw_response_wrapper(
            autoimprove_fix.create,
        )
        self.list = to_raw_response_wrapper(
            autoimprove_fix.list,
        )
        self.answer_question = to_raw_response_wrapper(
            autoimprove_fix.answer_question,
        )
        self.cancel = to_raw_response_wrapper(
            autoimprove_fix.cancel,
        )
        self.dismiss = to_raw_response_wrapper(
            autoimprove_fix.dismiss,
        )
        self.get_by_id = to_raw_response_wrapper(
            autoimprove_fix.get_by_id,
        )
        self.promote = to_raw_response_wrapper(
            autoimprove_fix.promote,
        )
        self.send_guidance = to_raw_response_wrapper(
            autoimprove_fix.send_guidance,
        )


class AsyncAutoimproveFixResourceWithRawResponse:
    def __init__(self, autoimprove_fix: AsyncAutoimproveFixResource) -> None:
        self._autoimprove_fix = autoimprove_fix

        self.create = async_to_raw_response_wrapper(
            autoimprove_fix.create,
        )
        self.list = async_to_raw_response_wrapper(
            autoimprove_fix.list,
        )
        self.answer_question = async_to_raw_response_wrapper(
            autoimprove_fix.answer_question,
        )
        self.cancel = async_to_raw_response_wrapper(
            autoimprove_fix.cancel,
        )
        self.dismiss = async_to_raw_response_wrapper(
            autoimprove_fix.dismiss,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            autoimprove_fix.get_by_id,
        )
        self.promote = async_to_raw_response_wrapper(
            autoimprove_fix.promote,
        )
        self.send_guidance = async_to_raw_response_wrapper(
            autoimprove_fix.send_guidance,
        )


class AutoimproveFixResourceWithStreamingResponse:
    def __init__(self, autoimprove_fix: AutoimproveFixResource) -> None:
        self._autoimprove_fix = autoimprove_fix

        self.create = to_streamed_response_wrapper(
            autoimprove_fix.create,
        )
        self.list = to_streamed_response_wrapper(
            autoimprove_fix.list,
        )
        self.answer_question = to_streamed_response_wrapper(
            autoimprove_fix.answer_question,
        )
        self.cancel = to_streamed_response_wrapper(
            autoimprove_fix.cancel,
        )
        self.dismiss = to_streamed_response_wrapper(
            autoimprove_fix.dismiss,
        )
        self.get_by_id = to_streamed_response_wrapper(
            autoimprove_fix.get_by_id,
        )
        self.promote = to_streamed_response_wrapper(
            autoimprove_fix.promote,
        )
        self.send_guidance = to_streamed_response_wrapper(
            autoimprove_fix.send_guidance,
        )


class AsyncAutoimproveFixResourceWithStreamingResponse:
    def __init__(self, autoimprove_fix: AsyncAutoimproveFixResource) -> None:
        self._autoimprove_fix = autoimprove_fix

        self.create = async_to_streamed_response_wrapper(
            autoimprove_fix.create,
        )
        self.list = async_to_streamed_response_wrapper(
            autoimprove_fix.list,
        )
        self.answer_question = async_to_streamed_response_wrapper(
            autoimprove_fix.answer_question,
        )
        self.cancel = async_to_streamed_response_wrapper(
            autoimprove_fix.cancel,
        )
        self.dismiss = async_to_streamed_response_wrapper(
            autoimprove_fix.dismiss,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            autoimprove_fix.get_by_id,
        )
        self.promote = async_to_streamed_response_wrapper(
            autoimprove_fix.promote,
        )
        self.send_guidance = async_to_streamed_response_wrapper(
            autoimprove_fix.send_guidance,
        )
