# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    benchmark_get_target_params,
    benchmark_list_metrics_params,
    benchmark_get_leaderboard_params,
    benchmark_list_target_history_params,
    benchmark_list_target_score_samples_params,
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
from ..types.benchmark_get_target_response import BenchmarkGetTargetResponse
from ..types.benchmark_list_suites_response import BenchmarkListSuitesResponse
from ..types.benchmark_list_metrics_response import BenchmarkListMetricsResponse
from ..types.benchmark_get_leaderboard_response import BenchmarkGetLeaderboardResponse
from ..types.benchmark_list_target_history_response import BenchmarkListTargetHistoryResponse
from ..types.benchmark_list_target_score_samples_response import BenchmarkListTargetScoreSamplesResponse

__all__ = ["BenchmarkResource", "AsyncBenchmarkResource"]


class BenchmarkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BenchmarkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return BenchmarkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenchmarkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return BenchmarkResourceWithStreamingResponse(self)

    def get_leaderboard(
        self,
        *,
        suite: str,
        condition_key: str | Omit = omit,
        limit: int | Omit = omit,
        metrics: str | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort_by: str | Omit = omit,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkGetLeaderboardResponse:
        """
        Returns one ranked page of a suite version’s published targets, each with the
        metric cells it is judged on. Ranking happens in the database, so paging through
        the board is consistent. Every default the server applies (suite version,
        condition, sort metric, sort direction) is echoed on the response, so a page can
        be cited without guessing how it was ordered.

        Args:
          limit: Maximum number of records to return (default: 20, max: 100)

          metrics: Comma-separated metric keys to project per row. Defaults to the headline set.

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/benchmark/leaderboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "suite": suite,
                        "condition_key": condition_key,
                        "limit": limit,
                        "metrics": metrics,
                        "offset": offset,
                        "order": order,
                        "sort_by": sort_by,
                        "suite_version": suite_version,
                    },
                    benchmark_get_leaderboard_params.BenchmarkGetLeaderboardParams,
                ),
            ),
            cast_to=BenchmarkGetLeaderboardResponse,
        )

    def get_target(
        self,
        target_key: str,
        *,
        suite: str,
        publication_id: str | Omit = omit,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkGetTargetResponse:
        """
        Returns a target’s published sweep and every one of its aggregate cells: the
        overall rollup plus a set per condition. Defaults to the current sweep; pass
        `publicationId` from the history endpoint to read a superseded one, which is how
        a regression is compared generation to generation. Numbers only — no transcript
        and no audio.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_key:
            raise ValueError(f"Expected a non-empty value for `target_key` but received {target_key!r}")
        return self._get(
            f"/v1/benchmark/target/{target_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "suite": suite,
                        "publication_id": publication_id,
                        "suite_version": suite_version,
                    },
                    benchmark_get_target_params.BenchmarkGetTargetParams,
                ),
            ),
            cast_to=BenchmarkGetTargetResponse,
        )

    def list_metrics(
        self,
        *,
        suite: str,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListMetricsResponse:
        """
        Returns the metrics a suite version published, each with the direction that
        counts as better. Use it to pick a valid `sortBy` for the leaderboard: a metric
        key outside this list is rejected rather than silently ranking every target
        null.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/benchmark/metric",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "suite": suite,
                        "suite_version": suite_version,
                    },
                    benchmark_list_metrics_params.BenchmarkListMetricsParams,
                ),
            ),
            cast_to=BenchmarkListMetricsResponse,
        )

    def list_suites(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListSuitesResponse:
        """
        Returns every benchmark suite with published results, along with the suite
        version the other endpoints default to. Start here: the suite name is a required
        parameter everywhere else and there is no other way to discover it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/benchmark/suite",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenchmarkListSuitesResponse,
        )

    def list_target_history(
        self,
        target_key: str,
        *,
        suite: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListTargetHistoryResponse:
        """
        Returns every sweep published for a target, newest first, including superseded
        ones. This is the trend read: it answers "did this model regress?" from Roark’s
        own published record. Metadata only — pass a row’s `publicationId` to GET
        /v1/benchmark/target/{targetKey} for that generation’s numbers.

        Args:
          limit: Maximum number of records to return (default: 20, max: 100)

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_key:
            raise ValueError(f"Expected a non-empty value for `target_key` but received {target_key!r}")
        return self._get(
            f"/v1/benchmark/target/{target_key}/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "suite": suite,
                        "limit": limit,
                        "offset": offset,
                        "suite_version": suite_version,
                    },
                    benchmark_list_target_history_params.BenchmarkListTargetHistoryParams,
                ),
            ),
            cast_to=BenchmarkListTargetHistoryResponse,
        )

    def list_target_score_samples(
        self,
        target_key: str,
        *,
        suite: str,
        condition_key: str | Omit = omit,
        limit: int | Omit = omit,
        metric_key: str | Omit = omit,
        offset: int | Omit = omit,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListTargetScoreSamplesResponse:
        """
        Returns the individual scored calls behind a target’s aggregate cells, each with
        the scorer’s rationale — the "why is this number what it is" read. Filter to one
        cell with `conditionKey` and `metricKey`. Metrics computed without a rationale
        (latencies, counts) contribute no samples. Returns reasoning only: no transcript
        and no audio.

        Args:
          limit: Maximum number of records to return (default: 20, max: 100)

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_key:
            raise ValueError(f"Expected a non-empty value for `target_key` but received {target_key!r}")
        return self._get(
            f"/v1/benchmark/target/{target_key}/score-sample",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "suite": suite,
                        "condition_key": condition_key,
                        "limit": limit,
                        "metric_key": metric_key,
                        "offset": offset,
                        "suite_version": suite_version,
                    },
                    benchmark_list_target_score_samples_params.BenchmarkListTargetScoreSamplesParams,
                ),
            ),
            cast_to=BenchmarkListTargetScoreSamplesResponse,
        )


class AsyncBenchmarkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBenchmarkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBenchmarkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenchmarkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncBenchmarkResourceWithStreamingResponse(self)

    async def get_leaderboard(
        self,
        *,
        suite: str,
        condition_key: str | Omit = omit,
        limit: int | Omit = omit,
        metrics: str | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort_by: str | Omit = omit,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkGetLeaderboardResponse:
        """
        Returns one ranked page of a suite version’s published targets, each with the
        metric cells it is judged on. Ranking happens in the database, so paging through
        the board is consistent. Every default the server applies (suite version,
        condition, sort metric, sort direction) is echoed on the response, so a page can
        be cited without guessing how it was ordered.

        Args:
          limit: Maximum number of records to return (default: 20, max: 100)

          metrics: Comma-separated metric keys to project per row. Defaults to the headline set.

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/benchmark/leaderboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "suite": suite,
                        "condition_key": condition_key,
                        "limit": limit,
                        "metrics": metrics,
                        "offset": offset,
                        "order": order,
                        "sort_by": sort_by,
                        "suite_version": suite_version,
                    },
                    benchmark_get_leaderboard_params.BenchmarkGetLeaderboardParams,
                ),
            ),
            cast_to=BenchmarkGetLeaderboardResponse,
        )

    async def get_target(
        self,
        target_key: str,
        *,
        suite: str,
        publication_id: str | Omit = omit,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkGetTargetResponse:
        """
        Returns a target’s published sweep and every one of its aggregate cells: the
        overall rollup plus a set per condition. Defaults to the current sweep; pass
        `publicationId` from the history endpoint to read a superseded one, which is how
        a regression is compared generation to generation. Numbers only — no transcript
        and no audio.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_key:
            raise ValueError(f"Expected a non-empty value for `target_key` but received {target_key!r}")
        return await self._get(
            f"/v1/benchmark/target/{target_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "suite": suite,
                        "publication_id": publication_id,
                        "suite_version": suite_version,
                    },
                    benchmark_get_target_params.BenchmarkGetTargetParams,
                ),
            ),
            cast_to=BenchmarkGetTargetResponse,
        )

    async def list_metrics(
        self,
        *,
        suite: str,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListMetricsResponse:
        """
        Returns the metrics a suite version published, each with the direction that
        counts as better. Use it to pick a valid `sortBy` for the leaderboard: a metric
        key outside this list is rejected rather than silently ranking every target
        null.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/benchmark/metric",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "suite": suite,
                        "suite_version": suite_version,
                    },
                    benchmark_list_metrics_params.BenchmarkListMetricsParams,
                ),
            ),
            cast_to=BenchmarkListMetricsResponse,
        )

    async def list_suites(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListSuitesResponse:
        """
        Returns every benchmark suite with published results, along with the suite
        version the other endpoints default to. Start here: the suite name is a required
        parameter everywhere else and there is no other way to discover it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/benchmark/suite",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenchmarkListSuitesResponse,
        )

    async def list_target_history(
        self,
        target_key: str,
        *,
        suite: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListTargetHistoryResponse:
        """
        Returns every sweep published for a target, newest first, including superseded
        ones. This is the trend read: it answers "did this model regress?" from Roark’s
        own published record. Metadata only — pass a row’s `publicationId` to GET
        /v1/benchmark/target/{targetKey} for that generation’s numbers.

        Args:
          limit: Maximum number of records to return (default: 20, max: 100)

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_key:
            raise ValueError(f"Expected a non-empty value for `target_key` but received {target_key!r}")
        return await self._get(
            f"/v1/benchmark/target/{target_key}/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "suite": suite,
                        "limit": limit,
                        "offset": offset,
                        "suite_version": suite_version,
                    },
                    benchmark_list_target_history_params.BenchmarkListTargetHistoryParams,
                ),
            ),
            cast_to=BenchmarkListTargetHistoryResponse,
        )

    async def list_target_score_samples(
        self,
        target_key: str,
        *,
        suite: str,
        condition_key: str | Omit = omit,
        limit: int | Omit = omit,
        metric_key: str | Omit = omit,
        offset: int | Omit = omit,
        suite_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkListTargetScoreSamplesResponse:
        """
        Returns the individual scored calls behind a target’s aggregate cells, each with
        the scorer’s rationale — the "why is this number what it is" read. Filter to one
        cell with `conditionKey` and `metricKey`. Metrics computed without a rationale
        (latencies, counts) contribute no samples. Returns reasoning only: no transcript
        and no audio.

        Args:
          limit: Maximum number of records to return (default: 20, max: 100)

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_key:
            raise ValueError(f"Expected a non-empty value for `target_key` but received {target_key!r}")
        return await self._get(
            f"/v1/benchmark/target/{target_key}/score-sample",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "suite": suite,
                        "condition_key": condition_key,
                        "limit": limit,
                        "metric_key": metric_key,
                        "offset": offset,
                        "suite_version": suite_version,
                    },
                    benchmark_list_target_score_samples_params.BenchmarkListTargetScoreSamplesParams,
                ),
            ),
            cast_to=BenchmarkListTargetScoreSamplesResponse,
        )


class BenchmarkResourceWithRawResponse:
    def __init__(self, benchmark: BenchmarkResource) -> None:
        self._benchmark = benchmark

        self.get_leaderboard = to_raw_response_wrapper(
            benchmark.get_leaderboard,
        )
        self.get_target = to_raw_response_wrapper(
            benchmark.get_target,
        )
        self.list_metrics = to_raw_response_wrapper(
            benchmark.list_metrics,
        )
        self.list_suites = to_raw_response_wrapper(
            benchmark.list_suites,
        )
        self.list_target_history = to_raw_response_wrapper(
            benchmark.list_target_history,
        )
        self.list_target_score_samples = to_raw_response_wrapper(
            benchmark.list_target_score_samples,
        )


class AsyncBenchmarkResourceWithRawResponse:
    def __init__(self, benchmark: AsyncBenchmarkResource) -> None:
        self._benchmark = benchmark

        self.get_leaderboard = async_to_raw_response_wrapper(
            benchmark.get_leaderboard,
        )
        self.get_target = async_to_raw_response_wrapper(
            benchmark.get_target,
        )
        self.list_metrics = async_to_raw_response_wrapper(
            benchmark.list_metrics,
        )
        self.list_suites = async_to_raw_response_wrapper(
            benchmark.list_suites,
        )
        self.list_target_history = async_to_raw_response_wrapper(
            benchmark.list_target_history,
        )
        self.list_target_score_samples = async_to_raw_response_wrapper(
            benchmark.list_target_score_samples,
        )


class BenchmarkResourceWithStreamingResponse:
    def __init__(self, benchmark: BenchmarkResource) -> None:
        self._benchmark = benchmark

        self.get_leaderboard = to_streamed_response_wrapper(
            benchmark.get_leaderboard,
        )
        self.get_target = to_streamed_response_wrapper(
            benchmark.get_target,
        )
        self.list_metrics = to_streamed_response_wrapper(
            benchmark.list_metrics,
        )
        self.list_suites = to_streamed_response_wrapper(
            benchmark.list_suites,
        )
        self.list_target_history = to_streamed_response_wrapper(
            benchmark.list_target_history,
        )
        self.list_target_score_samples = to_streamed_response_wrapper(
            benchmark.list_target_score_samples,
        )


class AsyncBenchmarkResourceWithStreamingResponse:
    def __init__(self, benchmark: AsyncBenchmarkResource) -> None:
        self._benchmark = benchmark

        self.get_leaderboard = async_to_streamed_response_wrapper(
            benchmark.get_leaderboard,
        )
        self.get_target = async_to_streamed_response_wrapper(
            benchmark.get_target,
        )
        self.list_metrics = async_to_streamed_response_wrapper(
            benchmark.list_metrics,
        )
        self.list_suites = async_to_streamed_response_wrapper(
            benchmark.list_suites,
        )
        self.list_target_history = async_to_streamed_response_wrapper(
            benchmark.list_target_history,
        )
        self.list_target_score_samples = async_to_streamed_response_wrapper(
            benchmark.list_target_score_samples,
        )
