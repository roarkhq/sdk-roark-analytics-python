# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    simulation_tool_fixture_list_params,
    simulation_tool_fixture_create_params,
    simulation_tool_fixture_update_params,
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
from ..types.simulation_tool_fixture_list_response import SimulationToolFixtureListResponse
from ..types.simulation_tool_fixture_create_response import SimulationToolFixtureCreateResponse
from ..types.simulation_tool_fixture_delete_response import SimulationToolFixtureDeleteResponse
from ..types.simulation_tool_fixture_update_response import SimulationToolFixtureUpdateResponse

__all__ = ["SimulationToolFixtureResource", "AsyncSimulationToolFixtureResource"]


class SimulationToolFixtureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationToolFixtureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationToolFixtureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationToolFixtureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationToolFixtureResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        tool_name: str,
        customer_flow_variant_id: str | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        response: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationToolFixtureCreateResponse:
        """
        Create-or-replace by scope: one fixture per tool project-wide, plus one per
        (tool, flow variant). Setting the same scope twice replaces the response, so CI
        can apply fixtures idempotently. During Roark test calls the tool guard answers
        with the fixture verbatim instead of generating a response; real callers are
        never affected.

        Args:
          tool_name: The tool this fixture answers for.

          customer_flow_variant_id: Pin the fixture to one flow variant (scenario). Omit for a project-wide fixture.
              A variant-pinned fixture beats the project-wide one.

          description: Why this fixture exists.

          enabled: Defaults to true.

          response: The exact JSON to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulation/tool-fixture",
            body=maybe_transform(
                {
                    "tool_name": tool_name,
                    "customer_flow_variant_id": customer_flow_variant_id,
                    "description": description,
                    "enabled": enabled,
                    "response": response,
                },
                simulation_tool_fixture_create_params.SimulationToolFixtureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationToolFixtureCreateResponse,
        )

    def update(
        self,
        fixture_id: str,
        *,
        description: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        response: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationToolFixtureUpdateResponse:
        """
        Change the response, description, or enabled state of an existing fixture.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fixture_id:
            raise ValueError(f"Expected a non-empty value for `fixture_id` but received {fixture_id!r}")
        return self._put(
            f"/v1/simulation/tool-fixture/{fixture_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "response": response,
                },
                simulation_tool_fixture_update_params.SimulationToolFixtureUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationToolFixtureUpdateResponse,
        )

    def list(
        self,
        *,
        tool_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationToolFixtureListResponse:
        """
        All deterministic tool responses configured for this project, optionally
        filtered by tool.

        Args:
          tool_name: Only fixtures for this tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/tool-fixture",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tool_name": tool_name}, simulation_tool_fixture_list_params.SimulationToolFixtureListParams
                ),
            ),
            cast_to=SimulationToolFixtureListResponse,
        )

    def delete(
        self,
        fixture_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationToolFixtureDeleteResponse:
        """
        The tool goes back to scenario-aware generated responses in test calls.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fixture_id:
            raise ValueError(f"Expected a non-empty value for `fixture_id` but received {fixture_id!r}")
        return self._delete(
            f"/v1/simulation/tool-fixture/{fixture_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationToolFixtureDeleteResponse,
        )


class AsyncSimulationToolFixtureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationToolFixtureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationToolFixtureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationToolFixtureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationToolFixtureResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        tool_name: str,
        customer_flow_variant_id: str | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        response: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationToolFixtureCreateResponse:
        """
        Create-or-replace by scope: one fixture per tool project-wide, plus one per
        (tool, flow variant). Setting the same scope twice replaces the response, so CI
        can apply fixtures idempotently. During Roark test calls the tool guard answers
        with the fixture verbatim instead of generating a response; real callers are
        never affected.

        Args:
          tool_name: The tool this fixture answers for.

          customer_flow_variant_id: Pin the fixture to one flow variant (scenario). Omit for a project-wide fixture.
              A variant-pinned fixture beats the project-wide one.

          description: Why this fixture exists.

          enabled: Defaults to true.

          response: The exact JSON to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulation/tool-fixture",
            body=await async_maybe_transform(
                {
                    "tool_name": tool_name,
                    "customer_flow_variant_id": customer_flow_variant_id,
                    "description": description,
                    "enabled": enabled,
                    "response": response,
                },
                simulation_tool_fixture_create_params.SimulationToolFixtureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationToolFixtureCreateResponse,
        )

    async def update(
        self,
        fixture_id: str,
        *,
        description: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        response: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationToolFixtureUpdateResponse:
        """
        Change the response, description, or enabled state of an existing fixture.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fixture_id:
            raise ValueError(f"Expected a non-empty value for `fixture_id` but received {fixture_id!r}")
        return await self._put(
            f"/v1/simulation/tool-fixture/{fixture_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "response": response,
                },
                simulation_tool_fixture_update_params.SimulationToolFixtureUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationToolFixtureUpdateResponse,
        )

    async def list(
        self,
        *,
        tool_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationToolFixtureListResponse:
        """
        All deterministic tool responses configured for this project, optionally
        filtered by tool.

        Args:
          tool_name: Only fixtures for this tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/tool-fixture",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tool_name": tool_name}, simulation_tool_fixture_list_params.SimulationToolFixtureListParams
                ),
            ),
            cast_to=SimulationToolFixtureListResponse,
        )

    async def delete(
        self,
        fixture_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationToolFixtureDeleteResponse:
        """
        The tool goes back to scenario-aware generated responses in test calls.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fixture_id:
            raise ValueError(f"Expected a non-empty value for `fixture_id` but received {fixture_id!r}")
        return await self._delete(
            f"/v1/simulation/tool-fixture/{fixture_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationToolFixtureDeleteResponse,
        )


class SimulationToolFixtureResourceWithRawResponse:
    def __init__(self, simulation_tool_fixture: SimulationToolFixtureResource) -> None:
        self._simulation_tool_fixture = simulation_tool_fixture

        self.create = to_raw_response_wrapper(
            simulation_tool_fixture.create,
        )
        self.update = to_raw_response_wrapper(
            simulation_tool_fixture.update,
        )
        self.list = to_raw_response_wrapper(
            simulation_tool_fixture.list,
        )
        self.delete = to_raw_response_wrapper(
            simulation_tool_fixture.delete,
        )


class AsyncSimulationToolFixtureResourceWithRawResponse:
    def __init__(self, simulation_tool_fixture: AsyncSimulationToolFixtureResource) -> None:
        self._simulation_tool_fixture = simulation_tool_fixture

        self.create = async_to_raw_response_wrapper(
            simulation_tool_fixture.create,
        )
        self.update = async_to_raw_response_wrapper(
            simulation_tool_fixture.update,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_tool_fixture.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simulation_tool_fixture.delete,
        )


class SimulationToolFixtureResourceWithStreamingResponse:
    def __init__(self, simulation_tool_fixture: SimulationToolFixtureResource) -> None:
        self._simulation_tool_fixture = simulation_tool_fixture

        self.create = to_streamed_response_wrapper(
            simulation_tool_fixture.create,
        )
        self.update = to_streamed_response_wrapper(
            simulation_tool_fixture.update,
        )
        self.list = to_streamed_response_wrapper(
            simulation_tool_fixture.list,
        )
        self.delete = to_streamed_response_wrapper(
            simulation_tool_fixture.delete,
        )


class AsyncSimulationToolFixtureResourceWithStreamingResponse:
    def __init__(self, simulation_tool_fixture: AsyncSimulationToolFixtureResource) -> None:
        self._simulation_tool_fixture = simulation_tool_fixture

        self.create = async_to_streamed_response_wrapper(
            simulation_tool_fixture.create,
        )
        self.update = async_to_streamed_response_wrapper(
            simulation_tool_fixture.update,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_tool_fixture.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simulation_tool_fixture.delete,
        )
