# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import simulation_list_scenarios_params, simulation_lookup_simulation_job_params
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
from ..types.simulation_list_scenarios_response import SimulationListScenariosResponse
from ..types.simulation_get_run_plan_job_response import SimulationGetRunPlanJobResponse
from ..types.simulation_start_run_plan_job_response import SimulationStartRunPlanJobResponse
from ..types.simulation_lookup_simulation_job_response import SimulationLookupSimulationJobResponse
from ..types.simulation_get_simulation_job_by_id_response import SimulationGetSimulationJobByIDResponse

__all__ = ["SimulationResource", "AsyncSimulationResource"]


class SimulationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationResourceWithStreamingResponse(self)

    def get_run_plan_job(
        self,
        job_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGetRunPlanJobResponse:
        """
        Retrieve details of a simulation plan job including all associated simulation
        jobs (calls)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/simulation/plan/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGetRunPlanJobResponse,
        )

    def get_simulation_job_by_id(
        self,
        job_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGetSimulationJobByIDResponse:
        """Get a individual simulation run directly by its ID.

        This is generally part of a
        larger simulation run plan job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/simulation/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGetSimulationJobByIDResponse,
        )

    def list_scenarios(
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
    ) -> SimulationListScenariosResponse:
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
                    simulation_list_scenarios_params.SimulationListScenariosParams,
                ),
            ),
            cast_to=SimulationListScenariosResponse,
        )

    def lookup_simulation_job(
        self,
        *,
        roark_phone_number: object,
        call_received_at: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationLookupSimulationJobResponse:
        """
        Find the matching simulation using the number used by the Roark simulation
        agent.

        Args:
          roark_phone_number: Phone number provisioned by Roark for the simulation job in E.164 format. In the
              case of an inbound simulation, this is the number that calls your agent; in the
              case of an outbound simulation, this is the number you call from your agent.

          call_received_at: ISO 8601 timestamp of when the call was received. Alternatively, any time
              between the start and end of the call is valid. Defaults to the current time,
              which fetches any jobs that are currently ongoing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/job/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "roark_phone_number": roark_phone_number,
                        "call_received_at": call_received_at,
                    },
                    simulation_lookup_simulation_job_params.SimulationLookupSimulationJobParams,
                ),
            ),
            cast_to=SimulationLookupSimulationJobResponse,
        )

    def start_run_plan_job(
        self,
        plan_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationStartRunPlanJobResponse:
        """
        Create and execute a job for an existing simulation run plan

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/v1/simulation/plan/{plan_id}/job",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationStartRunPlanJobResponse,
        )


class AsyncSimulationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationResourceWithStreamingResponse(self)

    async def get_run_plan_job(
        self,
        job_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGetRunPlanJobResponse:
        """
        Retrieve details of a simulation plan job including all associated simulation
        jobs (calls)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/simulation/plan/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGetRunPlanJobResponse,
        )

    async def get_simulation_job_by_id(
        self,
        job_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGetSimulationJobByIDResponse:
        """Get a individual simulation run directly by its ID.

        This is generally part of a
        larger simulation run plan job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/simulation/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGetSimulationJobByIDResponse,
        )

    async def list_scenarios(
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
    ) -> SimulationListScenariosResponse:
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
                    simulation_list_scenarios_params.SimulationListScenariosParams,
                ),
            ),
            cast_to=SimulationListScenariosResponse,
        )

    async def lookup_simulation_job(
        self,
        *,
        roark_phone_number: object,
        call_received_at: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationLookupSimulationJobResponse:
        """
        Find the matching simulation using the number used by the Roark simulation
        agent.

        Args:
          roark_phone_number: Phone number provisioned by Roark for the simulation job in E.164 format. In the
              case of an inbound simulation, this is the number that calls your agent; in the
              case of an outbound simulation, this is the number you call from your agent.

          call_received_at: ISO 8601 timestamp of when the call was received. Alternatively, any time
              between the start and end of the call is valid. Defaults to the current time,
              which fetches any jobs that are currently ongoing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/job/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "roark_phone_number": roark_phone_number,
                        "call_received_at": call_received_at,
                    },
                    simulation_lookup_simulation_job_params.SimulationLookupSimulationJobParams,
                ),
            ),
            cast_to=SimulationLookupSimulationJobResponse,
        )

    async def start_run_plan_job(
        self,
        plan_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationStartRunPlanJobResponse:
        """
        Create and execute a job for an existing simulation run plan

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/v1/simulation/plan/{plan_id}/job",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationStartRunPlanJobResponse,
        )


class SimulationResourceWithRawResponse:
    def __init__(self, simulation: SimulationResource) -> None:
        self._simulation = simulation

        self.get_run_plan_job = to_raw_response_wrapper(
            simulation.get_run_plan_job,
        )
        self.get_simulation_job_by_id = to_raw_response_wrapper(
            simulation.get_simulation_job_by_id,
        )
        self.list_scenarios = to_raw_response_wrapper(
            simulation.list_scenarios,
        )
        self.lookup_simulation_job = to_raw_response_wrapper(
            simulation.lookup_simulation_job,
        )
        self.start_run_plan_job = to_raw_response_wrapper(
            simulation.start_run_plan_job,
        )


class AsyncSimulationResourceWithRawResponse:
    def __init__(self, simulation: AsyncSimulationResource) -> None:
        self._simulation = simulation

        self.get_run_plan_job = async_to_raw_response_wrapper(
            simulation.get_run_plan_job,
        )
        self.get_simulation_job_by_id = async_to_raw_response_wrapper(
            simulation.get_simulation_job_by_id,
        )
        self.list_scenarios = async_to_raw_response_wrapper(
            simulation.list_scenarios,
        )
        self.lookup_simulation_job = async_to_raw_response_wrapper(
            simulation.lookup_simulation_job,
        )
        self.start_run_plan_job = async_to_raw_response_wrapper(
            simulation.start_run_plan_job,
        )


class SimulationResourceWithStreamingResponse:
    def __init__(self, simulation: SimulationResource) -> None:
        self._simulation = simulation

        self.get_run_plan_job = to_streamed_response_wrapper(
            simulation.get_run_plan_job,
        )
        self.get_simulation_job_by_id = to_streamed_response_wrapper(
            simulation.get_simulation_job_by_id,
        )
        self.list_scenarios = to_streamed_response_wrapper(
            simulation.list_scenarios,
        )
        self.lookup_simulation_job = to_streamed_response_wrapper(
            simulation.lookup_simulation_job,
        )
        self.start_run_plan_job = to_streamed_response_wrapper(
            simulation.start_run_plan_job,
        )


class AsyncSimulationResourceWithStreamingResponse:
    def __init__(self, simulation: AsyncSimulationResource) -> None:
        self._simulation = simulation

        self.get_run_plan_job = async_to_streamed_response_wrapper(
            simulation.get_run_plan_job,
        )
        self.get_simulation_job_by_id = async_to_streamed_response_wrapper(
            simulation.get_simulation_job_by_id,
        )
        self.list_scenarios = async_to_streamed_response_wrapper(
            simulation.list_scenarios,
        )
        self.lookup_simulation_job = async_to_streamed_response_wrapper(
            simulation.lookup_simulation_job,
        )
        self.start_run_plan_job = async_to_streamed_response_wrapper(
            simulation.start_run_plan_job,
        )
