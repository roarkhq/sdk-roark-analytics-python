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
from ..types.simulation_job_tool_mock_list_response import SimulationJobToolMockListResponse

__all__ = ["SimulationJobToolMockResource", "AsyncSimulationJobToolMockResource"]


class SimulationJobToolMockResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationJobToolMockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationJobToolMockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationJobToolMockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationJobToolMockResourceWithStreamingResponse(self)

    def list(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationJobToolMockListResponse:
        """
        Every guarded tool invocation Roark answered during this simulation: what the
        agent tried to call, with what arguments, and the simulated response it
        received. Use this to assert tool behavior in CI after a test call, with zero
        real side effects. Empty when the agent's tools are not guarded (see the tool
        guard docs).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/simulation/job/{job_id}/tool-mock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationJobToolMockListResponse,
        )


class AsyncSimulationJobToolMockResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationJobToolMockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationJobToolMockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationJobToolMockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationJobToolMockResourceWithStreamingResponse(self)

    async def list(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationJobToolMockListResponse:
        """
        Every guarded tool invocation Roark answered during this simulation: what the
        agent tried to call, with what arguments, and the simulated response it
        received. Use this to assert tool behavior in CI after a test call, with zero
        real side effects. Empty when the agent's tools are not guarded (see the tool
        guard docs).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/simulation/job/{job_id}/tool-mock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationJobToolMockListResponse,
        )


class SimulationJobToolMockResourceWithRawResponse:
    def __init__(self, simulation_job_tool_mock: SimulationJobToolMockResource) -> None:
        self._simulation_job_tool_mock = simulation_job_tool_mock

        self.list = to_raw_response_wrapper(
            simulation_job_tool_mock.list,
        )


class AsyncSimulationJobToolMockResourceWithRawResponse:
    def __init__(self, simulation_job_tool_mock: AsyncSimulationJobToolMockResource) -> None:
        self._simulation_job_tool_mock = simulation_job_tool_mock

        self.list = async_to_raw_response_wrapper(
            simulation_job_tool_mock.list,
        )


class SimulationJobToolMockResourceWithStreamingResponse:
    def __init__(self, simulation_job_tool_mock: SimulationJobToolMockResource) -> None:
        self._simulation_job_tool_mock = simulation_job_tool_mock

        self.list = to_streamed_response_wrapper(
            simulation_job_tool_mock.list,
        )


class AsyncSimulationJobToolMockResourceWithStreamingResponse:
    def __init__(self, simulation_job_tool_mock: AsyncSimulationJobToolMockResource) -> None:
        self._simulation_job_tool_mock = simulation_job_tool_mock

        self.list = async_to_streamed_response_wrapper(
            simulation_job_tool_mock.list,
        )
