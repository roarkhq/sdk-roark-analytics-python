# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import analytics_query_params
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
from ..types.analytics_query_response import AnalyticsQueryResponse
from ..types.analytics_get_schema_response import AnalyticsGetSchemaResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)

    def get_schema(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetSchemaResponse:
        """
        Lists what can go into an analytics query for this project: every metric by slug
        with its output type, default aggregation and the aggregations it supports; the
        measure types; the filter and breakdown types with the properties each accepts;
        and the custom call properties seen in the project. Read this first when
        building a query.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/analytics/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalyticsGetSchemaResponse,
        )

    def query(
        self,
        *,
        measures: Iterable[analytics_query_params.Measure],
        comparison_groups: Iterable[analytics_query_params.ComparisonGroup] | Omit = omit,
        comparison_mode: Literal["NONE", "PREVIOUS_PERIOD"] | Omit = omit,
        filters: Iterable[analytics_query_params.MeasureFilter] | Omit = omit,
        include_buckets: bool | Omit = omit,
        interval: Literal["HOUR", "DAY", "WEEK", "MONTH"] | Omit = omit,
        time_range: Union[
            analytics_query_params.TimeRangeUnionMember0,
            analytics_query_params.TimeRangeUnionMember1,
            analytics_query_params.TimeRangeUnionMember2,
            analytics_query_params.TimeRangeUnionMember3,
        ]
        | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsQueryResponse:
        """
        Aggregates metric values and conversation counts over a time window and returns
        one series per measure, with a total for the window and per-interval buckets.
        The same query a dashboard widget runs, without saving anything. - `measures`:
        what to aggregate. A METRIC measure names its metric by slug; CONVERSATION
        counts conversations; UPTIME reads health checks. The aggregation defaults by
        the metric's output type. - `timeRange`: LAST n DAYS/WEEKS/MONTHS, a
        CALENDAR_ALIGNED period (TODAY, THIS_MONTH, ...), FIXED from/to, or SINCE.
        Defaults to the last 30 days; at most 731 days. Calendar periods and buckets
        align to `timezone` (IANA, default UTC). - `filters` apply to every measure; a
        measure's own `filters` add to them. - `breakdown` on a measure returns one
        series per value (largest 50 kept). - `comparisonGroups` (2 to 5) run every
        measure once per named filter set; `comparisonMode: PREVIOUS_PERIOD` adds the
        preceding window's values. Values are in the metric's display units. A PASS_RATE
        is a 0 to 1 share; `sampleSize` 0 means no data. A query the analytics store
        cannot answer returns 400 naming the unsupported part.

        Args:
          measures: What to aggregate: 1 to 10 measures.

          comparison_groups: Run every measure once per named filter set, e.g. one group per agent.

          comparison_mode: PREVIOUS_PERIOD adds the preceding window of the same length to every series.

          filters: Applied to every measure, on top of each measure's own filters.

          include_buckets: Set false to return only the window totals.

          interval: Bucket size. Defaults from the window's length and steps coarser when the window
              would exceed 500 buckets.

          time_range: Defaults to the last 30 days.

          timezone: IANA zone that buckets and calendar periods align to, e.g. America/New_York.
              Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/analytics/query",
            body=maybe_transform(
                {
                    "measures": measures,
                    "comparison_groups": comparison_groups,
                    "comparison_mode": comparison_mode,
                    "filters": filters,
                    "include_buckets": include_buckets,
                    "interval": interval,
                    "time_range": time_range,
                    "timezone": timezone,
                },
                analytics_query_params.AnalyticsQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalyticsQueryResponse,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def get_schema(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetSchemaResponse:
        """
        Lists what can go into an analytics query for this project: every metric by slug
        with its output type, default aggregation and the aggregations it supports; the
        measure types; the filter and breakdown types with the properties each accepts;
        and the custom call properties seen in the project. Read this first when
        building a query.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/analytics/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalyticsGetSchemaResponse,
        )

    async def query(
        self,
        *,
        measures: Iterable[analytics_query_params.Measure],
        comparison_groups: Iterable[analytics_query_params.ComparisonGroup] | Omit = omit,
        comparison_mode: Literal["NONE", "PREVIOUS_PERIOD"] | Omit = omit,
        filters: Iterable[analytics_query_params.MeasureFilter] | Omit = omit,
        include_buckets: bool | Omit = omit,
        interval: Literal["HOUR", "DAY", "WEEK", "MONTH"] | Omit = omit,
        time_range: Union[
            analytics_query_params.TimeRangeUnionMember0,
            analytics_query_params.TimeRangeUnionMember1,
            analytics_query_params.TimeRangeUnionMember2,
            analytics_query_params.TimeRangeUnionMember3,
        ]
        | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsQueryResponse:
        """
        Aggregates metric values and conversation counts over a time window and returns
        one series per measure, with a total for the window and per-interval buckets.
        The same query a dashboard widget runs, without saving anything. - `measures`:
        what to aggregate. A METRIC measure names its metric by slug; CONVERSATION
        counts conversations; UPTIME reads health checks. The aggregation defaults by
        the metric's output type. - `timeRange`: LAST n DAYS/WEEKS/MONTHS, a
        CALENDAR_ALIGNED period (TODAY, THIS_MONTH, ...), FIXED from/to, or SINCE.
        Defaults to the last 30 days; at most 731 days. Calendar periods and buckets
        align to `timezone` (IANA, default UTC). - `filters` apply to every measure; a
        measure's own `filters` add to them. - `breakdown` on a measure returns one
        series per value (largest 50 kept). - `comparisonGroups` (2 to 5) run every
        measure once per named filter set; `comparisonMode: PREVIOUS_PERIOD` adds the
        preceding window's values. Values are in the metric's display units. A PASS_RATE
        is a 0 to 1 share; `sampleSize` 0 means no data. A query the analytics store
        cannot answer returns 400 naming the unsupported part.

        Args:
          measures: What to aggregate: 1 to 10 measures.

          comparison_groups: Run every measure once per named filter set, e.g. one group per agent.

          comparison_mode: PREVIOUS_PERIOD adds the preceding window of the same length to every series.

          filters: Applied to every measure, on top of each measure's own filters.

          include_buckets: Set false to return only the window totals.

          interval: Bucket size. Defaults from the window's length and steps coarser when the window
              would exceed 500 buckets.

          time_range: Defaults to the last 30 days.

          timezone: IANA zone that buckets and calendar periods align to, e.g. America/New_York.
              Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/analytics/query",
            body=await async_maybe_transform(
                {
                    "measures": measures,
                    "comparison_groups": comparison_groups,
                    "comparison_mode": comparison_mode,
                    "filters": filters,
                    "include_buckets": include_buckets,
                    "interval": interval,
                    "time_range": time_range,
                    "timezone": timezone,
                },
                analytics_query_params.AnalyticsQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalyticsQueryResponse,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_schema = to_raw_response_wrapper(
            analytics.get_schema,
        )
        self.query = to_raw_response_wrapper(
            analytics.query,
        )


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_schema = async_to_raw_response_wrapper(
            analytics.get_schema,
        )
        self.query = async_to_raw_response_wrapper(
            analytics.query,
        )


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_schema = to_streamed_response_wrapper(
            analytics.get_schema,
        )
        self.query = to_streamed_response_wrapper(
            analytics.query,
        )


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_schema = async_to_streamed_response_wrapper(
            analytics.get_schema,
        )
        self.query = async_to_streamed_response_wrapper(
            analytics.query,
        )
