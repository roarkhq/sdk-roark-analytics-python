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
from ..types.simulation_template_list_response import SimulationTemplateListResponse

__all__ = ["SimulationTemplateResource", "AsyncSimulationTemplateResource"]


class SimulationTemplateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationTemplateResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationTemplateListResponse:
        """
        Returns the built-in simulation templates, each resolved against this project:
        the metric and check definitions it collects, and the flows it runs with the
        variants it covers. A template is a preset rather than a stored object, so
        building a run from one produces an ordinary run plan you own and can edit
        afterwards. Pass a `slug` as `template` to POST /v1/simulation/run. Every entry
        is complete, so there is no per-template endpoint to follow up with, and the
        list is a fixed catalogue rather than a paginated one. Only templates a request
        can actually run are listed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/template",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationTemplateListResponse,
        )


class AsyncSimulationTemplateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationTemplateResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationTemplateListResponse:
        """
        Returns the built-in simulation templates, each resolved against this project:
        the metric and check definitions it collects, and the flows it runs with the
        variants it covers. A template is a preset rather than a stored object, so
        building a run from one produces an ordinary run plan you own and can edit
        afterwards. Pass a `slug` as `template` to POST /v1/simulation/run. Every entry
        is complete, so there is no per-template endpoint to follow up with, and the
        list is a fixed catalogue rather than a paginated one. Only templates a request
        can actually run are listed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/template",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationTemplateListResponse,
        )


class SimulationTemplateResourceWithRawResponse:
    def __init__(self, simulation_template: SimulationTemplateResource) -> None:
        self._simulation_template = simulation_template

        self.list = to_raw_response_wrapper(
            simulation_template.list,
        )


class AsyncSimulationTemplateResourceWithRawResponse:
    def __init__(self, simulation_template: AsyncSimulationTemplateResource) -> None:
        self._simulation_template = simulation_template

        self.list = async_to_raw_response_wrapper(
            simulation_template.list,
        )


class SimulationTemplateResourceWithStreamingResponse:
    def __init__(self, simulation_template: SimulationTemplateResource) -> None:
        self._simulation_template = simulation_template

        self.list = to_streamed_response_wrapper(
            simulation_template.list,
        )


class AsyncSimulationTemplateResourceWithStreamingResponse:
    def __init__(self, simulation_template: AsyncSimulationTemplateResource) -> None:
        self._simulation_template = simulation_template

        self.list = async_to_streamed_response_wrapper(
            simulation_template.list,
        )
