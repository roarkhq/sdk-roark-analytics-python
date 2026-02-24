# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import metric_collection_job_list_params, metric_collection_job_create_params
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
from ..types.metric_collection_job_list_response import MetricCollectionJobListResponse
from ..types.metric_collection_job_create_response import MetricCollectionJobCreateResponse
from ..types.metric_collection_job_get_by_id_response import MetricCollectionJobGetByIDResponse

__all__ = ["MetricCollectionJobResource", "AsyncMetricCollectionJobResource"]


class MetricCollectionJobResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricCollectionJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return MetricCollectionJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricCollectionJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return MetricCollectionJobResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        call_ids: SequenceNotStr[str],
        metrics: Iterable[metric_collection_job_create_params.Metric],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCollectionJobCreateResponse:
        """
        Creates a metric collection job for the specified calls and metrics, then
        triggers processing.

        Args:
          call_ids: Call IDs to collect metrics for

          metrics: Metric definitions to collect

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/metric/collection-jobs",
            body=maybe_transform(
                {
                    "call_ids": call_ids,
                    "metrics": metrics,
                },
                metric_collection_job_create_params.MetricCollectionJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricCollectionJobCreateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["PENDING", "PROCESSING", "COMPLETED", "FAILED", "CANCELED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCollectionJobListResponse:
        """
        Returns a paginated list of metric collection jobs for the project.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          limit: Maximum number of jobs to return (default: 20, max: 50)

          status: Filter by job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/metric/collection-jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "status": status,
                    },
                    metric_collection_job_list_params.MetricCollectionJobListParams,
                ),
            ),
            cast_to=MetricCollectionJobListResponse,
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
    ) -> MetricCollectionJobGetByIDResponse:
        """
        Returns a specific metric collection job with progress information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/metric/collection-jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricCollectionJobGetByIDResponse,
        )


class AsyncMetricCollectionJobResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricCollectionJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricCollectionJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricCollectionJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncMetricCollectionJobResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        call_ids: SequenceNotStr[str],
        metrics: Iterable[metric_collection_job_create_params.Metric],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCollectionJobCreateResponse:
        """
        Creates a metric collection job for the specified calls and metrics, then
        triggers processing.

        Args:
          call_ids: Call IDs to collect metrics for

          metrics: Metric definitions to collect

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/metric/collection-jobs",
            body=await async_maybe_transform(
                {
                    "call_ids": call_ids,
                    "metrics": metrics,
                },
                metric_collection_job_create_params.MetricCollectionJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricCollectionJobCreateResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["PENDING", "PROCESSING", "COMPLETED", "FAILED", "CANCELED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCollectionJobListResponse:
        """
        Returns a paginated list of metric collection jobs for the project.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          limit: Maximum number of jobs to return (default: 20, max: 50)

          status: Filter by job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/metric/collection-jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "status": status,
                    },
                    metric_collection_job_list_params.MetricCollectionJobListParams,
                ),
            ),
            cast_to=MetricCollectionJobListResponse,
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
    ) -> MetricCollectionJobGetByIDResponse:
        """
        Returns a specific metric collection job with progress information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/metric/collection-jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricCollectionJobGetByIDResponse,
        )


class MetricCollectionJobResourceWithRawResponse:
    def __init__(self, metric_collection_job: MetricCollectionJobResource) -> None:
        self._metric_collection_job = metric_collection_job

        self.create = to_raw_response_wrapper(
            metric_collection_job.create,
        )
        self.list = to_raw_response_wrapper(
            metric_collection_job.list,
        )
        self.get_by_id = to_raw_response_wrapper(
            metric_collection_job.get_by_id,
        )


class AsyncMetricCollectionJobResourceWithRawResponse:
    def __init__(self, metric_collection_job: AsyncMetricCollectionJobResource) -> None:
        self._metric_collection_job = metric_collection_job

        self.create = async_to_raw_response_wrapper(
            metric_collection_job.create,
        )
        self.list = async_to_raw_response_wrapper(
            metric_collection_job.list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            metric_collection_job.get_by_id,
        )


class MetricCollectionJobResourceWithStreamingResponse:
    def __init__(self, metric_collection_job: MetricCollectionJobResource) -> None:
        self._metric_collection_job = metric_collection_job

        self.create = to_streamed_response_wrapper(
            metric_collection_job.create,
        )
        self.list = to_streamed_response_wrapper(
            metric_collection_job.list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            metric_collection_job.get_by_id,
        )


class AsyncMetricCollectionJobResourceWithStreamingResponse:
    def __init__(self, metric_collection_job: AsyncMetricCollectionJobResource) -> None:
        self._metric_collection_job = metric_collection_job

        self.create = async_to_streamed_response_wrapper(
            metric_collection_job.create,
        )
        self.list = async_to_streamed_response_wrapper(
            metric_collection_job.list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            metric_collection_job.get_by_id,
        )
