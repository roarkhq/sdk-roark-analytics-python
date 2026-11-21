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
from ..types.simulation_phone_number_list_response import SimulationPhoneNumberListResponse

__all__ = ["SimulationPhoneNumberResource", "AsyncSimulationPhoneNumberResource"]


class SimulationPhoneNumberResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationPhoneNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationPhoneNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationPhoneNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationPhoneNumberResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPhoneNumberListResponse:
        """
        Returns every number Roark may place simulation calls to your agent from,
        ordered by number. Use it to allowlist simulation traffic or to tell it apart
        from real callers. The shared pool changes as Roark adds and retires numbers, so
        fetch the list again before you update an allowlist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/phone-number",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationPhoneNumberListResponse,
        )


class AsyncSimulationPhoneNumberResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationPhoneNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationPhoneNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationPhoneNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationPhoneNumberResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPhoneNumberListResponse:
        """
        Returns every number Roark may place simulation calls to your agent from,
        ordered by number. Use it to allowlist simulation traffic or to tell it apart
        from real callers. The shared pool changes as Roark adds and retires numbers, so
        fetch the list again before you update an allowlist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/phone-number",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationPhoneNumberListResponse,
        )


class SimulationPhoneNumberResourceWithRawResponse:
    def __init__(self, simulation_phone_number: SimulationPhoneNumberResource) -> None:
        self._simulation_phone_number = simulation_phone_number

        self.list = to_raw_response_wrapper(
            simulation_phone_number.list,
        )


class AsyncSimulationPhoneNumberResourceWithRawResponse:
    def __init__(self, simulation_phone_number: AsyncSimulationPhoneNumberResource) -> None:
        self._simulation_phone_number = simulation_phone_number

        self.list = async_to_raw_response_wrapper(
            simulation_phone_number.list,
        )


class SimulationPhoneNumberResourceWithStreamingResponse:
    def __init__(self, simulation_phone_number: SimulationPhoneNumberResource) -> None:
        self._simulation_phone_number = simulation_phone_number

        self.list = to_streamed_response_wrapper(
            simulation_phone_number.list,
        )


class AsyncSimulationPhoneNumberResourceWithStreamingResponse:
    def __init__(self, simulation_phone_number: AsyncSimulationPhoneNumberResource) -> None:
        self._simulation_phone_number = simulation_phone_number

        self.list = async_to_streamed_response_wrapper(
            simulation_phone_number.list,
        )
