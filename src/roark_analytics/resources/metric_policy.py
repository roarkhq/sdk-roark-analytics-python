# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import metric_policy_list_params, metric_policy_create_params, metric_policy_update_params
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
from ..types.metric_policy_list_response import MetricPolicyListResponse
from ..types.metric_policy_create_response import MetricPolicyCreateResponse
from ..types.metric_policy_delete_response import MetricPolicyDeleteResponse
from ..types.metric_policy_update_response import MetricPolicyUpdateResponse
from ..types.metric_policy_get_by_id_response import MetricPolicyGetByIDResponse

__all__ = ["MetricPolicyResource", "AsyncMetricPolicyResource"]


class MetricPolicyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricPolicyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return MetricPolicyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricPolicyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return MetricPolicyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        metrics: Iterable[metric_policy_create_params.Metric],
        name: str,
        conditions: Iterable[metric_policy_create_params.Condition] | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyCreateResponse:
        """Creates a new metric policy.

        Policies define which metrics to collect and under
        what conditions.

        Args:
          metrics: Metric definitions to collect when this policy matches

          name: Name of the metric policy

          conditions: Condition groups. Omit to match all calls.

          status: Status of the policy (default: ACTIVE)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/metric/policies",
            body=maybe_transform(
                {
                    "metrics": metrics,
                    "name": name,
                    "conditions": conditions,
                    "status": status,
                },
                metric_policy_create_params.MetricPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricPolicyCreateResponse,
        )

    def update(
        self,
        policy_id: str,
        *,
        conditions: Iterable[metric_policy_update_params.Condition] | Omit = omit,
        metrics: Iterable[metric_policy_update_params.Metric] | Omit = omit,
        name: str | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyUpdateResponse:
        """Updates an existing metric policy.

        System policies cannot be modified.

        Args:
          conditions: Condition groups. Omit to keep existing, provide empty array to remove all
              conditions.

          metrics: Metric definitions to collect when this policy matches

          name: Name of the metric policy

          status: Status of the policy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._put(
            f"/v1/metric/policies/{policy_id}",
            body=maybe_transform(
                {
                    "conditions": conditions,
                    "metrics": metrics,
                    "name": name,
                    "status": status,
                },
                metric_policy_update_params.MetricPolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricPolicyUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyListResponse:
        """
        Returns a paginated list of metric policies for the project, including system
        policies.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          limit: Maximum number of policies to return (default: 20, max: 50)

          status: Filter by policy status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/metric/policies",
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
                    metric_policy_list_params.MetricPolicyListParams,
                ),
            ),
            cast_to=MetricPolicyListResponse,
        )

    def delete(
        self,
        policy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyDeleteResponse:
        """Soft-deletes a metric policy.

        System policies cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._delete(
            f"/v1/metric/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricPolicyDeleteResponse,
        )

    def get_by_id(
        self,
        policy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyGetByIDResponse:
        """
        Returns a specific metric policy with its conditions and metrics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            f"/v1/metric/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricPolicyGetByIDResponse,
        )


class AsyncMetricPolicyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricPolicyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricPolicyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricPolicyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncMetricPolicyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        metrics: Iterable[metric_policy_create_params.Metric],
        name: str,
        conditions: Iterable[metric_policy_create_params.Condition] | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyCreateResponse:
        """Creates a new metric policy.

        Policies define which metrics to collect and under
        what conditions.

        Args:
          metrics: Metric definitions to collect when this policy matches

          name: Name of the metric policy

          conditions: Condition groups. Omit to match all calls.

          status: Status of the policy (default: ACTIVE)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/metric/policies",
            body=await async_maybe_transform(
                {
                    "metrics": metrics,
                    "name": name,
                    "conditions": conditions,
                    "status": status,
                },
                metric_policy_create_params.MetricPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricPolicyCreateResponse,
        )

    async def update(
        self,
        policy_id: str,
        *,
        conditions: Iterable[metric_policy_update_params.Condition] | Omit = omit,
        metrics: Iterable[metric_policy_update_params.Metric] | Omit = omit,
        name: str | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyUpdateResponse:
        """Updates an existing metric policy.

        System policies cannot be modified.

        Args:
          conditions: Condition groups. Omit to keep existing, provide empty array to remove all
              conditions.

          metrics: Metric definitions to collect when this policy matches

          name: Name of the metric policy

          status: Status of the policy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._put(
            f"/v1/metric/policies/{policy_id}",
            body=await async_maybe_transform(
                {
                    "conditions": conditions,
                    "metrics": metrics,
                    "name": name,
                    "status": status,
                },
                metric_policy_update_params.MetricPolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricPolicyUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyListResponse:
        """
        Returns a paginated list of metric policies for the project, including system
        policies.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          limit: Maximum number of policies to return (default: 20, max: 50)

          status: Filter by policy status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/metric/policies",
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
                    metric_policy_list_params.MetricPolicyListParams,
                ),
            ),
            cast_to=MetricPolicyListResponse,
        )

    async def delete(
        self,
        policy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyDeleteResponse:
        """Soft-deletes a metric policy.

        System policies cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._delete(
            f"/v1/metric/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricPolicyDeleteResponse,
        )

    async def get_by_id(
        self,
        policy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricPolicyGetByIDResponse:
        """
        Returns a specific metric policy with its conditions and metrics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            f"/v1/metric/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricPolicyGetByIDResponse,
        )


class MetricPolicyResourceWithRawResponse:
    def __init__(self, metric_policy: MetricPolicyResource) -> None:
        self._metric_policy = metric_policy

        self.create = to_raw_response_wrapper(
            metric_policy.create,
        )
        self.update = to_raw_response_wrapper(
            metric_policy.update,
        )
        self.list = to_raw_response_wrapper(
            metric_policy.list,
        )
        self.delete = to_raw_response_wrapper(
            metric_policy.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            metric_policy.get_by_id,
        )


class AsyncMetricPolicyResourceWithRawResponse:
    def __init__(self, metric_policy: AsyncMetricPolicyResource) -> None:
        self._metric_policy = metric_policy

        self.create = async_to_raw_response_wrapper(
            metric_policy.create,
        )
        self.update = async_to_raw_response_wrapper(
            metric_policy.update,
        )
        self.list = async_to_raw_response_wrapper(
            metric_policy.list,
        )
        self.delete = async_to_raw_response_wrapper(
            metric_policy.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            metric_policy.get_by_id,
        )


class MetricPolicyResourceWithStreamingResponse:
    def __init__(self, metric_policy: MetricPolicyResource) -> None:
        self._metric_policy = metric_policy

        self.create = to_streamed_response_wrapper(
            metric_policy.create,
        )
        self.update = to_streamed_response_wrapper(
            metric_policy.update,
        )
        self.list = to_streamed_response_wrapper(
            metric_policy.list,
        )
        self.delete = to_streamed_response_wrapper(
            metric_policy.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            metric_policy.get_by_id,
        )


class AsyncMetricPolicyResourceWithStreamingResponse:
    def __init__(self, metric_policy: AsyncMetricPolicyResource) -> None:
        self._metric_policy = metric_policy

        self.create = async_to_streamed_response_wrapper(
            metric_policy.create,
        )
        self.update = async_to_streamed_response_wrapper(
            metric_policy.update,
        )
        self.list = async_to_streamed_response_wrapper(
            metric_policy.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            metric_policy.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            metric_policy.get_by_id,
        )
