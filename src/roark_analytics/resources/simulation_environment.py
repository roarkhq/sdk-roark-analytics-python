# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import simulation_environment_list_params
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
from ..types.simulation_environment_list_response import SimulationEnvironmentListResponse
from ..types.simulation_environment_get_by_id_response import SimulationEnvironmentGetByIDResponse

__all__ = ["SimulationEnvironmentResource", "AsyncSimulationEnvironmentResource"]


class SimulationEnvironmentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationEnvironmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationEnvironmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationEnvironmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationEnvironmentResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentListResponse:
        """
        Returns a paginated list of environments: the project's own plus the
        environments Roark curates and shares across every project. Reference one by id
        when setting a customer flow variant's environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/environment",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    simulation_environment_list_params.SimulationEnvironmentListParams,
                ),
            ),
            cast_to=SimulationEnvironmentListResponse,
        )

    def get_by_id(
        self,
        environment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentGetByIDResponse:
        """
        Returns a single environment by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return self._get(
            f"/v1/simulation/environment/{environment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentGetByIDResponse,
        )


class AsyncSimulationEnvironmentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationEnvironmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationEnvironmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationEnvironmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationEnvironmentResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentListResponse:
        """
        Returns a paginated list of environments: the project's own plus the
        environments Roark curates and shares across every project. Reference one by id
        when setting a customer flow variant's environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/environment",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    simulation_environment_list_params.SimulationEnvironmentListParams,
                ),
            ),
            cast_to=SimulationEnvironmentListResponse,
        )

    async def get_by_id(
        self,
        environment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentGetByIDResponse:
        """
        Returns a single environment by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return await self._get(
            f"/v1/simulation/environment/{environment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentGetByIDResponse,
        )


class SimulationEnvironmentResourceWithRawResponse:
    def __init__(self, simulation_environment: SimulationEnvironmentResource) -> None:
        self._simulation_environment = simulation_environment

        self.list = to_raw_response_wrapper(
            simulation_environment.list,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_environment.get_by_id,
        )


class AsyncSimulationEnvironmentResourceWithRawResponse:
    def __init__(self, simulation_environment: AsyncSimulationEnvironmentResource) -> None:
        self._simulation_environment = simulation_environment

        self.list = async_to_raw_response_wrapper(
            simulation_environment.list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_environment.get_by_id,
        )


class SimulationEnvironmentResourceWithStreamingResponse:
    def __init__(self, simulation_environment: SimulationEnvironmentResource) -> None:
        self._simulation_environment = simulation_environment

        self.list = to_streamed_response_wrapper(
            simulation_environment.list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_environment.get_by_id,
        )


class AsyncSimulationEnvironmentResourceWithStreamingResponse:
    def __init__(self, simulation_environment: AsyncSimulationEnvironmentResource) -> None:
        self._simulation_environment = simulation_environment

        self.list = async_to_streamed_response_wrapper(
            simulation_environment.list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_environment.get_by_id,
        )
