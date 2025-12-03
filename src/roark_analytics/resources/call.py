# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import call_get_metrics_params
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
from ..types.call_get_by_id_response import CallGetByIDResponse
from ..types.call_get_metrics_response import CallGetMetricsResponse
from ..types.call_get_sentiment_runs_response import CallGetSentimentRunsResponse
from ..types.call_get_evaluation_runs_response import CallGetEvaluationRunsResponse

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

    def get_evaluation_runs(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetEvaluationRunsResponse:
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
            cast_to=CallGetEvaluationRunsResponse,
        )

    def get_metrics(
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
    ) -> CallGetMetricsResponse:
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
                query=maybe_transform({"flatten": flatten}, call_get_metrics_params.CallGetMetricsParams),
            ),
            cast_to=CallGetMetricsResponse,
        )

    def get_sentiment_runs(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetSentimentRunsResponse:
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
            cast_to=CallGetSentimentRunsResponse,
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

    async def get_evaluation_runs(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetEvaluationRunsResponse:
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
            cast_to=CallGetEvaluationRunsResponse,
        )

    async def get_metrics(
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
    ) -> CallGetMetricsResponse:
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
                query=await async_maybe_transform({"flatten": flatten}, call_get_metrics_params.CallGetMetricsParams),
            ),
            cast_to=CallGetMetricsResponse,
        )

    async def get_sentiment_runs(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetSentimentRunsResponse:
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
            cast_to=CallGetSentimentRunsResponse,
        )


class CallResourceWithRawResponse:
    def __init__(self, call: CallResource) -> None:
        self._call = call

        self.get_by_id = to_raw_response_wrapper(
            call.get_by_id,
        )
        self.get_evaluation_runs = to_raw_response_wrapper(
            call.get_evaluation_runs,
        )
        self.get_metrics = to_raw_response_wrapper(
            call.get_metrics,
        )
        self.get_sentiment_runs = to_raw_response_wrapper(
            call.get_sentiment_runs,
        )


class AsyncCallResourceWithRawResponse:
    def __init__(self, call: AsyncCallResource) -> None:
        self._call = call

        self.get_by_id = async_to_raw_response_wrapper(
            call.get_by_id,
        )
        self.get_evaluation_runs = async_to_raw_response_wrapper(
            call.get_evaluation_runs,
        )
        self.get_metrics = async_to_raw_response_wrapper(
            call.get_metrics,
        )
        self.get_sentiment_runs = async_to_raw_response_wrapper(
            call.get_sentiment_runs,
        )


class CallResourceWithStreamingResponse:
    def __init__(self, call: CallResource) -> None:
        self._call = call

        self.get_by_id = to_streamed_response_wrapper(
            call.get_by_id,
        )
        self.get_evaluation_runs = to_streamed_response_wrapper(
            call.get_evaluation_runs,
        )
        self.get_metrics = to_streamed_response_wrapper(
            call.get_metrics,
        )
        self.get_sentiment_runs = to_streamed_response_wrapper(
            call.get_sentiment_runs,
        )


class AsyncCallResourceWithStreamingResponse:
    def __init__(self, call: AsyncCallResource) -> None:
        self._call = call

        self.get_by_id = async_to_streamed_response_wrapper(
            call.get_by_id,
        )
        self.get_evaluation_runs = async_to_streamed_response_wrapper(
            call.get_evaluation_runs,
        )
        self.get_metrics = async_to_streamed_response_wrapper(
            call.get_metrics,
        )
        self.get_sentiment_runs = async_to_streamed_response_wrapper(
            call.get_sentiment_runs,
        )
