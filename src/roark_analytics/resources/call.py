# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import call_list_params, call_create_params, call_list_metrics_params
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
from ..types.call_list_response import CallListResponse
from ..types.call_create_response import CallCreateResponse
from ..types.call_get_by_id_response import CallGetByIDResponse
from ..types.call_list_metrics_response import CallListMetricsResponse
from ..types.call_list_sentiment_runs_response import CallListSentimentRunsResponse
from ..types.call_list_evaluation_runs_response import CallListEvaluationRunsResponse

__all__ = ["CallResource", "AsyncCallResource"]


class CallResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return CallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return CallResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        call_direction: Literal["INBOUND", "OUTBOUND"],
        interface_type: Literal["PHONE", "WEB"],
        recording_url: str,
        started_at: str,
        agent: call_create_params.Agent | Omit = omit,
        agents: Iterable[call_create_params.Agent] | Omit = omit,
        customer: call_create_params.Customer | Omit = omit,
        customers: Iterable[call_create_params.Customer] | Omit = omit,
        ended_status: Literal[
            "PARTICIPANTS_DID_NOT_SPEAK",
            "AGENT_DID_NOT_ANSWER",
            "AGENT_DID_NOT_SPEAK",
            "AGENT_STOPPED_SPEAKING",
            "AGENT_ENDED_CALL",
            "AGENT_TRANSFERRED_CALL",
            "AGENT_BUSY",
            "AGENT_ERROR",
            "CUSTOMER_ENDED_CALL",
            "VOICE_MAIL_REACHED",
            "SILENCE_TIME_OUT",
            "PHONE_CALL_PROVIDER_CONNECTION_ERROR",
            "CUSTOMER_DID_NOT_ANSWER",
            "CUSTOMER_DID_NOT_SPEAK",
            "CUSTOMER_STOPPED_SPEAKING",
            "CUSTOMER_BUSY",
            "DIAL_ERROR",
            "MAX_DURATION_REACHED",
            "UNKNOWN",
        ]
        | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        stereo_recording_url: str | Omit = omit,
        tool_invocations: Iterable[call_create_params.ToolInvocation] | Omit = omit,
        transcript: Iterable[call_create_params.Transcript] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallCreateResponse:
        """
        Create a new call with recording, transcript, agents, and customers

        Args:
          call_direction: Direction of the call (INBOUND or OUTBOUND)

          interface_type: Interface type of the call (PHONE or WEB)

          recording_url: URL of source recording (must be an accessible WAV, MP3, or MP4 file). Can be a
              signed URL.

          started_at: When the call started (ISO 8601 format)

          agent: Single agent participating in the call. Use this for simpler API when you have
              only one agent.

          agents: Agents participating in the call. Each agent requires identification and prompt
              information.

          customer: Single customer participating in the call. Use this for simpler API when you
              have only one customer.

          customers: Customers participating in the call.

          ended_status: High-level call end status, indicating how the call terminated

          properties: Custom properties to include with the call. These can be used for filtering and
              will show in the call details page

          stereo_recording_url: URL of source stereo recording. Must be accessible. Can be a signed URL.
              Supported formats: WAV, MP3, MP4.

          tool_invocations: List of tool invocations made during the call

          transcript: List of transcript entries made during the call

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/call",
            body=maybe_transform(
                {
                    "call_direction": call_direction,
                    "interface_type": interface_type,
                    "recording_url": recording_url,
                    "started_at": started_at,
                    "agent": agent,
                    "agents": agents,
                    "customer": customer,
                    "customers": customers,
                    "ended_status": ended_status,
                    "properties": properties,
                    "stereo_recording_url": stereo_recording_url,
                    "tool_invocations": tool_invocations,
                    "transcript": transcript,
                },
                call_create_params.CallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallCreateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        sort_by: Literal["createdAt", "startedAt", "endedAt", "duration", "title", "status"] | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        status: Literal["RINGING", "IN_PROGRESS", "ENDED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListResponse:
        """
        Returns a paginated list of calls for the authenticated project.

        Args:
          after: Cursor for pagination - use the nextCursor value (call ID) from a previous
              response

          limit: Maximum number of calls to return (default: 20, max: 100)

          search_text: Search text to filter calls by title, summary, or transcript

          sort_by: Field to sort by (default: createdAt)

          sort_direction: Sort direction (default: desc)

          status: Filter by call status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/call",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "search_text": search_text,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                        "status": status,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            cast_to=CallListResponse,
        )

    def get_by_id(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetByIDResponse:
        """
        Retrieve an existing call by its unique identifier

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._get(
            f"/v1/call/{call_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallGetByIDResponse,
        )

    def list_evaluation_runs(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListEvaluationRunsResponse:
        """
        Fetch all evaluation run results for a specific call.

        Args:
          call_id: ID of the call to fetch evaluation run for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._get(
            f"/v1/call/{call_id}/evaluation-run",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallListEvaluationRunsResponse,
        )

    def list_metrics(
        self,
        call_id: str,
        *,
        flatten: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListMetricsResponse:
        """
        Fetch all call-level metrics for a specific call, including both
        system-generated and custom metrics. Only returns successfully computed metrics.

        Args:
          flatten:
              Whether to return a flat list instead of grouped by metric definition (default:
              false)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._get(
            f"/v1/call/{call_id}/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"flatten": flatten}, call_list_metrics_params.CallListMetricsParams),
            ),
            cast_to=CallListMetricsResponse,
        )

    def list_sentiment_runs(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListSentimentRunsResponse:
        """
        Fetch detailed sentiment analysis results for a specific call, including
        emotional tone, key phrases, and sentiment scores.

        Args:
          call_id: ID of the call to fetch sentiment run for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._get(
            f"/v1/call/{call_id}/sentiment-run",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallListSentimentRunsResponse,
        )


class AsyncCallResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncCallResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        call_direction: Literal["INBOUND", "OUTBOUND"],
        interface_type: Literal["PHONE", "WEB"],
        recording_url: str,
        started_at: str,
        agent: call_create_params.Agent | Omit = omit,
        agents: Iterable[call_create_params.Agent] | Omit = omit,
        customer: call_create_params.Customer | Omit = omit,
        customers: Iterable[call_create_params.Customer] | Omit = omit,
        ended_status: Literal[
            "PARTICIPANTS_DID_NOT_SPEAK",
            "AGENT_DID_NOT_ANSWER",
            "AGENT_DID_NOT_SPEAK",
            "AGENT_STOPPED_SPEAKING",
            "AGENT_ENDED_CALL",
            "AGENT_TRANSFERRED_CALL",
            "AGENT_BUSY",
            "AGENT_ERROR",
            "CUSTOMER_ENDED_CALL",
            "VOICE_MAIL_REACHED",
            "SILENCE_TIME_OUT",
            "PHONE_CALL_PROVIDER_CONNECTION_ERROR",
            "CUSTOMER_DID_NOT_ANSWER",
            "CUSTOMER_DID_NOT_SPEAK",
            "CUSTOMER_STOPPED_SPEAKING",
            "CUSTOMER_BUSY",
            "DIAL_ERROR",
            "MAX_DURATION_REACHED",
            "UNKNOWN",
        ]
        | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        stereo_recording_url: str | Omit = omit,
        tool_invocations: Iterable[call_create_params.ToolInvocation] | Omit = omit,
        transcript: Iterable[call_create_params.Transcript] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallCreateResponse:
        """
        Create a new call with recording, transcript, agents, and customers

        Args:
          call_direction: Direction of the call (INBOUND or OUTBOUND)

          interface_type: Interface type of the call (PHONE or WEB)

          recording_url: URL of source recording (must be an accessible WAV, MP3, or MP4 file). Can be a
              signed URL.

          started_at: When the call started (ISO 8601 format)

          agent: Single agent participating in the call. Use this for simpler API when you have
              only one agent.

          agents: Agents participating in the call. Each agent requires identification and prompt
              information.

          customer: Single customer participating in the call. Use this for simpler API when you
              have only one customer.

          customers: Customers participating in the call.

          ended_status: High-level call end status, indicating how the call terminated

          properties: Custom properties to include with the call. These can be used for filtering and
              will show in the call details page

          stereo_recording_url: URL of source stereo recording. Must be accessible. Can be a signed URL.
              Supported formats: WAV, MP3, MP4.

          tool_invocations: List of tool invocations made during the call

          transcript: List of transcript entries made during the call

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/call",
            body=await async_maybe_transform(
                {
                    "call_direction": call_direction,
                    "interface_type": interface_type,
                    "recording_url": recording_url,
                    "started_at": started_at,
                    "agent": agent,
                    "agents": agents,
                    "customer": customer,
                    "customers": customers,
                    "ended_status": ended_status,
                    "properties": properties,
                    "stereo_recording_url": stereo_recording_url,
                    "tool_invocations": tool_invocations,
                    "transcript": transcript,
                },
                call_create_params.CallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallCreateResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        sort_by: Literal["createdAt", "startedAt", "endedAt", "duration", "title", "status"] | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        status: Literal["RINGING", "IN_PROGRESS", "ENDED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListResponse:
        """
        Returns a paginated list of calls for the authenticated project.

        Args:
          after: Cursor for pagination - use the nextCursor value (call ID) from a previous
              response

          limit: Maximum number of calls to return (default: 20, max: 100)

          search_text: Search text to filter calls by title, summary, or transcript

          sort_by: Field to sort by (default: createdAt)

          sort_direction: Sort direction (default: desc)

          status: Filter by call status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/call",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "search_text": search_text,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                        "status": status,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            cast_to=CallListResponse,
        )

    async def get_by_id(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetByIDResponse:
        """
        Retrieve an existing call by its unique identifier

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._get(
            f"/v1/call/{call_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallGetByIDResponse,
        )

    async def list_evaluation_runs(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListEvaluationRunsResponse:
        """
        Fetch all evaluation run results for a specific call.

        Args:
          call_id: ID of the call to fetch evaluation run for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._get(
            f"/v1/call/{call_id}/evaluation-run",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallListEvaluationRunsResponse,
        )

    async def list_metrics(
        self,
        call_id: str,
        *,
        flatten: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListMetricsResponse:
        """
        Fetch all call-level metrics for a specific call, including both
        system-generated and custom metrics. Only returns successfully computed metrics.

        Args:
          flatten:
              Whether to return a flat list instead of grouped by metric definition (default:
              false)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._get(
            f"/v1/call/{call_id}/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"flatten": flatten}, call_list_metrics_params.CallListMetricsParams),
            ),
            cast_to=CallListMetricsResponse,
        )

    async def list_sentiment_runs(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListSentimentRunsResponse:
        """
        Fetch detailed sentiment analysis results for a specific call, including
        emotional tone, key phrases, and sentiment scores.

        Args:
          call_id: ID of the call to fetch sentiment run for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._get(
            f"/v1/call/{call_id}/sentiment-run",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallListSentimentRunsResponse,
        )


class CallResourceWithRawResponse:
    def __init__(self, call: CallResource) -> None:
        self._call = call

        self.create = to_raw_response_wrapper(
            call.create,
        )
        self.list = to_raw_response_wrapper(
            call.list,
        )
        self.get_by_id = to_raw_response_wrapper(
            call.get_by_id,
        )
        self.list_evaluation_runs = to_raw_response_wrapper(
            call.list_evaluation_runs,
        )
        self.list_metrics = to_raw_response_wrapper(
            call.list_metrics,
        )
        self.list_sentiment_runs = to_raw_response_wrapper(
            call.list_sentiment_runs,
        )


class AsyncCallResourceWithRawResponse:
    def __init__(self, call: AsyncCallResource) -> None:
        self._call = call

        self.create = async_to_raw_response_wrapper(
            call.create,
        )
        self.list = async_to_raw_response_wrapper(
            call.list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            call.get_by_id,
        )
        self.list_evaluation_runs = async_to_raw_response_wrapper(
            call.list_evaluation_runs,
        )
        self.list_metrics = async_to_raw_response_wrapper(
            call.list_metrics,
        )
        self.list_sentiment_runs = async_to_raw_response_wrapper(
            call.list_sentiment_runs,
        )


class CallResourceWithStreamingResponse:
    def __init__(self, call: CallResource) -> None:
        self._call = call

        self.create = to_streamed_response_wrapper(
            call.create,
        )
        self.list = to_streamed_response_wrapper(
            call.list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            call.get_by_id,
        )
        self.list_evaluation_runs = to_streamed_response_wrapper(
            call.list_evaluation_runs,
        )
        self.list_metrics = to_streamed_response_wrapper(
            call.list_metrics,
        )
        self.list_sentiment_runs = to_streamed_response_wrapper(
            call.list_sentiment_runs,
        )


class AsyncCallResourceWithStreamingResponse:
    def __init__(self, call: AsyncCallResource) -> None:
        self._call = call

        self.create = async_to_streamed_response_wrapper(
            call.create,
        )
        self.list = async_to_streamed_response_wrapper(
            call.list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            call.get_by_id,
        )
        self.list_evaluation_runs = async_to_streamed_response_wrapper(
            call.list_evaluation_runs,
        )
        self.list_metrics = async_to_streamed_response_wrapper(
            call.list_metrics,
        )
        self.list_sentiment_runs = async_to_streamed_response_wrapper(
            call.list_sentiment_runs,
        )
