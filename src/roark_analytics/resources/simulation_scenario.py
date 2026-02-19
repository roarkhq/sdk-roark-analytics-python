# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    simulation_scenario_list_params,
    simulation_scenario_create_params,
    simulation_scenario_update_params,
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
from ..types.simulation_scenario_list_response import SimulationScenarioListResponse
from ..types.simulation_scenario_create_response import SimulationScenarioCreateResponse
from ..types.simulation_scenario_delete_response import SimulationScenarioDeleteResponse
from ..types.simulation_scenario_update_response import SimulationScenarioUpdateResponse
from ..types.simulation_scenario_get_by_id_response import SimulationScenarioGetByIDResponse

__all__ = ["SimulationScenarioResource", "AsyncSimulationScenarioResource"]


class SimulationScenarioResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationScenarioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationScenarioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationScenarioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationScenarioResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        steps: Iterable[simulation_scenario_create_params.Step],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationScenarioCreateResponse:
        """
        Creates a new simulation scenario for the authenticated project.

        Args:
          name: Name of the scenario (used as the START node content)

          steps: Ordered list of steps for the scenario (at least one step is required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulation/scenario",
            body=maybe_transform(
                {
                    "name": name,
                    "steps": steps,
                },
                simulation_scenario_create_params.SimulationScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationScenarioCreateResponse,
        )

    def update(
        self,
        scenario_id: str,
        *,
        step_changes: Iterable[simulation_scenario_update_params.StepChange],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationScenarioUpdateResponse:
        """
        Updates an existing simulation scenario by its ID.

        Args:
          step_changes: List of step changes to apply to the scenario

          name: New name for the scenario (updates the START node content)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return self._put(
            f"/v1/simulation/scenario/{scenario_id}",
            body=maybe_transform(
                {
                    "step_changes": step_changes,
                    "name": name,
                },
                simulation_scenario_update_params.SimulationScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationScenarioUpdateResponse,
        )

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
    ) -> SimulationScenarioListResponse:
        """
        Returns a paginated list of simulation scenarios for the authenticated project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/scenario",
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
                    simulation_scenario_list_params.SimulationScenarioListParams,
                ),
            ),
            cast_to=SimulationScenarioListResponse,
        )

    def delete(
        self,
        scenario_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationScenarioDeleteResponse:
        """
        Deletes a simulation scenario by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return self._delete(
            f"/v1/simulation/scenario/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationScenarioDeleteResponse,
        )

    def get_by_id(
        self,
        scenario_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationScenarioGetByIDResponse:
        """
        Returns a specific simulation scenario by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return self._get(
            f"/v1/simulation/scenario/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationScenarioGetByIDResponse,
        )


class AsyncSimulationScenarioResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationScenarioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationScenarioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationScenarioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationScenarioResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        steps: Iterable[simulation_scenario_create_params.Step],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationScenarioCreateResponse:
        """
        Creates a new simulation scenario for the authenticated project.

        Args:
          name: Name of the scenario (used as the START node content)

          steps: Ordered list of steps for the scenario (at least one step is required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulation/scenario",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "steps": steps,
                },
                simulation_scenario_create_params.SimulationScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationScenarioCreateResponse,
        )

    async def update(
        self,
        scenario_id: str,
        *,
        step_changes: Iterable[simulation_scenario_update_params.StepChange],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationScenarioUpdateResponse:
        """
        Updates an existing simulation scenario by its ID.

        Args:
          step_changes: List of step changes to apply to the scenario

          name: New name for the scenario (updates the START node content)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return await self._put(
            f"/v1/simulation/scenario/{scenario_id}",
            body=await async_maybe_transform(
                {
                    "step_changes": step_changes,
                    "name": name,
                },
                simulation_scenario_update_params.SimulationScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationScenarioUpdateResponse,
        )

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
    ) -> SimulationScenarioListResponse:
        """
        Returns a paginated list of simulation scenarios for the authenticated project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/scenario",
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
                    simulation_scenario_list_params.SimulationScenarioListParams,
                ),
            ),
            cast_to=SimulationScenarioListResponse,
        )

    async def delete(
        self,
        scenario_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationScenarioDeleteResponse:
        """
        Deletes a simulation scenario by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return await self._delete(
            f"/v1/simulation/scenario/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationScenarioDeleteResponse,
        )

    async def get_by_id(
        self,
        scenario_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationScenarioGetByIDResponse:
        """
        Returns a specific simulation scenario by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return await self._get(
            f"/v1/simulation/scenario/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationScenarioGetByIDResponse,
        )


class SimulationScenarioResourceWithRawResponse:
    def __init__(self, simulation_scenario: SimulationScenarioResource) -> None:
        self._simulation_scenario = simulation_scenario

        self.create = to_raw_response_wrapper(
            simulation_scenario.create,
        )
        self.update = to_raw_response_wrapper(
            simulation_scenario.update,
        )
        self.list = to_raw_response_wrapper(
            simulation_scenario.list,
        )
        self.delete = to_raw_response_wrapper(
            simulation_scenario.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_scenario.get_by_id,
        )


class AsyncSimulationScenarioResourceWithRawResponse:
    def __init__(self, simulation_scenario: AsyncSimulationScenarioResource) -> None:
        self._simulation_scenario = simulation_scenario

        self.create = async_to_raw_response_wrapper(
            simulation_scenario.create,
        )
        self.update = async_to_raw_response_wrapper(
            simulation_scenario.update,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_scenario.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simulation_scenario.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_scenario.get_by_id,
        )


class SimulationScenarioResourceWithStreamingResponse:
    def __init__(self, simulation_scenario: SimulationScenarioResource) -> None:
        self._simulation_scenario = simulation_scenario

        self.create = to_streamed_response_wrapper(
            simulation_scenario.create,
        )
        self.update = to_streamed_response_wrapper(
            simulation_scenario.update,
        )
        self.list = to_streamed_response_wrapper(
            simulation_scenario.list,
        )
        self.delete = to_streamed_response_wrapper(
            simulation_scenario.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_scenario.get_by_id,
        )


class AsyncSimulationScenarioResourceWithStreamingResponse:
    def __init__(self, simulation_scenario: AsyncSimulationScenarioResource) -> None:
        self._simulation_scenario = simulation_scenario

        self.create = async_to_streamed_response_wrapper(
            simulation_scenario.create,
        )
        self.update = async_to_streamed_response_wrapper(
            simulation_scenario.update,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_scenario.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simulation_scenario.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_scenario.get_by_id,
        )
