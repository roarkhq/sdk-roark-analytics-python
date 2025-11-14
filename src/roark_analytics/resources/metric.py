# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.metric_get_definitions_response import MetricGetDefinitionsResponse

__all__ = ["MetricResource", "AsyncMetricResource"]


class MetricResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return MetricResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return MetricResourceWithStreamingResponse(self)

    def get_definitions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGetDefinitionsResponse:
        """
        Fetch all metric definitions available in the project, including both
        system-generated and custom metrics. Only returns metrics from enabled analysis
        packages.
        """
        return self._get(
            "/v1/metric/definitions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGetDefinitionsResponse,
        )


class AsyncMetricResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncMetricResourceWithStreamingResponse(self)

    async def get_definitions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGetDefinitionsResponse:
        """
        Fetch all metric definitions available in the project, including both
        system-generated and custom metrics. Only returns metrics from enabled analysis
        packages.
        """
        return await self._get(
            "/v1/metric/definitions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGetDefinitionsResponse,
        )


class MetricResourceWithRawResponse:
    def __init__(self, metric: MetricResource) -> None:
        self._metric = metric

        self.get_definitions = to_raw_response_wrapper(
            metric.get_definitions,
        )


class AsyncMetricResourceWithRawResponse:
    def __init__(self, metric: AsyncMetricResource) -> None:
        self._metric = metric

        self.get_definitions = async_to_raw_response_wrapper(
            metric.get_definitions,
        )


class MetricResourceWithStreamingResponse:
    def __init__(self, metric: MetricResource) -> None:
        self._metric = metric

        self.get_definitions = to_streamed_response_wrapper(
            metric.get_definitions,
        )


class AsyncMetricResourceWithStreamingResponse:
    def __init__(self, metric: AsyncMetricResource) -> None:
        self._metric = metric

        self.get_definitions = async_to_streamed_response_wrapper(
            metric.get_definitions,
        )
