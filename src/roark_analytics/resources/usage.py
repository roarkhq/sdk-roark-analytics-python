# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import usage_get_params
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
from ..types.usage_get_response import UsageGetResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        from_: str,
        to: str,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetResponse:
        """
        Report billable usage and cost for the organization over a time window, broken
        down by project (highest spend first). Pass `from`/`to` as ISO 8601 timestamps;
        optionally pass `projectId` to scope the report to one project. Amounts are
        billable spend only (what we absorb is never included). Authenticated by either
        an organization API key with the `usage:read` permission (any project in the
        organization), or a project API key with the `billing:read` permission (that
        key's own project only; any other `projectId` is a 403).

        Args:
          from_: Start of the window (inclusive), ISO 8601.

          to: End of the window (exclusive), ISO 8601. Must be after `from`, and the window
              may not exceed 366 days.

          project_id: Limit the report to a single project. Omit for the whole organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "project_id": project_id,
                    },
                    usage_get_params.UsageGetParams,
                ),
            ),
            cast_to=UsageGetResponse,
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        from_: str,
        to: str,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetResponse:
        """
        Report billable usage and cost for the organization over a time window, broken
        down by project (highest spend first). Pass `from`/`to` as ISO 8601 timestamps;
        optionally pass `projectId` to scope the report to one project. Amounts are
        billable spend only (what we absorb is never included). Authenticated by either
        an organization API key with the `usage:read` permission (any project in the
        organization), or a project API key with the `billing:read` permission (that
        key's own project only; any other `projectId` is a 403).

        Args:
          from_: Start of the window (inclusive), ISO 8601.

          to: End of the window (exclusive), ISO 8601. Must be after `from`, and the window
              may not exceed 366 days.

          project_id: Limit the report to a single project. Omit for the whole organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "project_id": project_id,
                    },
                    usage_get_params.UsageGetParams,
                ),
            ),
            cast_to=UsageGetResponse,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.get = to_raw_response_wrapper(
            usage.get,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get = async_to_raw_response_wrapper(
            usage.get,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.get = to_streamed_response_wrapper(
            usage.get,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get = async_to_streamed_response_wrapper(
            usage.get,
        )
