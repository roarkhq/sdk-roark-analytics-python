# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    simulation_run_plan_list_params,
    simulation_run_plan_create_params,
    simulation_run_plan_update_params,
)
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
from ..types.simulation_run_plan_list_response import SimulationRunPlanListResponse
from ..types.simulation_run_plan_create_response import SimulationRunPlanCreateResponse
from ..types.simulation_run_plan_delete_response import SimulationRunPlanDeleteResponse
from ..types.simulation_run_plan_update_response import SimulationRunPlanUpdateResponse
from ..types.simulation_run_plan_get_by_id_response import SimulationRunPlanGetByIDResponse

__all__ = ["SimulationRunPlanResource", "AsyncSimulationRunPlanResource"]


class SimulationRunPlanResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationRunPlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationRunPlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationRunPlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationRunPlanResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.AgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        max_simulation_duration_seconds: int,
        metrics: Iterable[simulation_run_plan_create_params.Metric],
        name: str,
        personas: Iterable[simulation_run_plan_create_params.Persona],
        scenarios: Iterable[simulation_run_plan_create_params.Scenario],
        auto_run: bool | Omit = omit,
        description: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanCreateResponse:
        """Creates a new simulation run plan.

        Optionally triggers a job immediately if
        autoRun is true.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan

          name: Name of the run plan

          personas: Personas to include in this run plan

          scenarios: Scenarios to include in this run plan. The same scenario ID can appear multiple
              times with different variables.

          auto_run: Whether to automatically trigger a job after creating the run plan

          description: Description of the run plan

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          iteration_count: Number of iterations to run for each test case. Must be 1 for OUTBOUND
              direction.

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulation/plan",
            body=maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
                    "name": name,
                    "personas": personas,
                    "scenarios": scenarios,
                    "auto_run": auto_run,
                    "description": description,
                    "end_call_phrases": end_call_phrases,
                    "execution_mode": execution_mode,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "silence_timeout_seconds": silence_timeout_seconds,
                },
                simulation_run_plan_create_params.SimulationRunPlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanCreateResponse,
        )

    def update(
        self,
        plan_id: str,
        *,
        agent_endpoints: Iterable[simulation_run_plan_update_params.AgentEndpoint] | Omit = omit,
        description: str | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_update_params.Metric] | Omit = omit,
        name: str | Omit = omit,
        personas: Iterable[simulation_run_plan_update_params.Persona] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_update_params.Scenario] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanUpdateResponse:
        """
        Updates an existing simulation run plan by its ID.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          description: Description of the run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          iteration_count: Number of iterations to run for each test case. Must be 1 for OUTBOUND
              direction.

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan

          name: Name of the run plan

          personas: Personas to include in this run plan

          scenarios: Scenarios to include in this run plan. The same scenario ID can appear multiple
              times with different variables.

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._put(
            f"/v1/simulation/plan/{plan_id}",
            body=maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "description": description,
                    "direction": direction,
                    "end_call_phrases": end_call_phrases,
                    "execution_mode": execution_mode,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
                    "name": name,
                    "personas": personas,
                    "scenarios": scenarios,
                    "silence_timeout_seconds": silence_timeout_seconds,
                },
                simulation_run_plan_update_params.SimulationRunPlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanListResponse:
        """Returns a paginated list of simulation run plans.

        Optionally filter by search
        text or agent ID.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          agent_id: Filter run plans by agent ID

          limit: Maximum number of run plans to return (default: 20, max: 50)

          search_text: Search text to filter run plans by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/plan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "limit": limit,
                        "search_text": search_text,
                    },
                    simulation_run_plan_list_params.SimulationRunPlanListParams,
                ),
            ),
            cast_to=SimulationRunPlanListResponse,
        )

    def delete(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanDeleteResponse:
        """
        Soft-deletes a simulation run plan by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._delete(
            f"/v1/simulation/plan/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanDeleteResponse,
        )

    def get_by_id(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanGetByIDResponse:
        """
        Returns a specific simulation run plan by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get(
            f"/v1/simulation/plan/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanGetByIDResponse,
        )


class AsyncSimulationRunPlanResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationRunPlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationRunPlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationRunPlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationRunPlanResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_endpoints: Iterable[simulation_run_plan_create_params.AgentEndpoint],
        direction: Literal["INBOUND", "OUTBOUND"],
        max_simulation_duration_seconds: int,
        metrics: Iterable[simulation_run_plan_create_params.Metric],
        name: str,
        personas: Iterable[simulation_run_plan_create_params.Persona],
        scenarios: Iterable[simulation_run_plan_create_params.Scenario],
        auto_run: bool | Omit = omit,
        description: str | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanCreateResponse:
        """Creates a new simulation run plan.

        Optionally triggers a job immediately if
        autoRun is true.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan

          name: Name of the run plan

          personas: Personas to include in this run plan

          scenarios: Scenarios to include in this run plan. The same scenario ID can appear multiple
              times with different variables.

          auto_run: Whether to automatically trigger a job after creating the run plan

          description: Description of the run plan

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          iteration_count: Number of iterations to run for each test case. Must be 1 for OUTBOUND
              direction.

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulation/plan",
            body=await async_maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "direction": direction,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
                    "name": name,
                    "personas": personas,
                    "scenarios": scenarios,
                    "auto_run": auto_run,
                    "description": description,
                    "end_call_phrases": end_call_phrases,
                    "execution_mode": execution_mode,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "silence_timeout_seconds": silence_timeout_seconds,
                },
                simulation_run_plan_create_params.SimulationRunPlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanCreateResponse,
        )

    async def update(
        self,
        plan_id: str,
        *,
        agent_endpoints: Iterable[simulation_run_plan_update_params.AgentEndpoint] | Omit = omit,
        description: str | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        end_call_phrases: SequenceNotStr[str] | Omit = omit,
        execution_mode: Literal["PARALLEL", "SEQUENTIAL_SAME_RUN_PLAN", "SEQUENTIAL_PROJECT"] | Omit = omit,
        iteration_count: int | Omit = omit,
        max_concurrent_jobs: int | Omit = omit,
        max_simulation_duration_seconds: int | Omit = omit,
        metrics: Iterable[simulation_run_plan_update_params.Metric] | Omit = omit,
        name: str | Omit = omit,
        personas: Iterable[simulation_run_plan_update_params.Persona] | Omit = omit,
        scenarios: Iterable[simulation_run_plan_update_params.Scenario] | Omit = omit,
        silence_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanUpdateResponse:
        """
        Updates an existing simulation run plan by its ID.

        Args:
          agent_endpoints: Agent endpoints to include in this run plan

          description: Description of the run plan

          direction: Direction of the simulation (INBOUND or OUTBOUND)

          end_call_phrases: Phrases that trigger end of call. Empty array disables the feature.

          execution_mode: Execution mode (PARALLEL or SEQUENTIAL)

          iteration_count: Number of iterations to run for each test case. Must be 1 for OUTBOUND
              direction.

          max_concurrent_jobs: Maximum number of concurrent simulation jobs

          max_simulation_duration_seconds: Maximum duration in seconds for each simulation

          metrics: Metric definitions to include in this run plan

          name: Name of the run plan

          personas: Personas to include in this run plan

          scenarios: Scenarios to include in this run plan. The same scenario ID can appear multiple
              times with different variables.

          silence_timeout_seconds: Timeout in seconds for silence detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._put(
            f"/v1/simulation/plan/{plan_id}",
            body=await async_maybe_transform(
                {
                    "agent_endpoints": agent_endpoints,
                    "description": description,
                    "direction": direction,
                    "end_call_phrases": end_call_phrases,
                    "execution_mode": execution_mode,
                    "iteration_count": iteration_count,
                    "max_concurrent_jobs": max_concurrent_jobs,
                    "max_simulation_duration_seconds": max_simulation_duration_seconds,
                    "metrics": metrics,
                    "name": name,
                    "personas": personas,
                    "scenarios": scenarios,
                    "silence_timeout_seconds": silence_timeout_seconds,
                },
                simulation_run_plan_update_params.SimulationRunPlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanListResponse:
        """Returns a paginated list of simulation run plans.

        Optionally filter by search
        text or agent ID.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          agent_id: Filter run plans by agent ID

          limit: Maximum number of run plans to return (default: 20, max: 50)

          search_text: Search text to filter run plans by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/plan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "limit": limit,
                        "search_text": search_text,
                    },
                    simulation_run_plan_list_params.SimulationRunPlanListParams,
                ),
            ),
            cast_to=SimulationRunPlanListResponse,
        )

    async def delete(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanDeleteResponse:
        """
        Soft-deletes a simulation run plan by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._delete(
            f"/v1/simulation/plan/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanDeleteResponse,
        )

    async def get_by_id(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanGetByIDResponse:
        """
        Returns a specific simulation run plan by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._get(
            f"/v1/simulation/plan/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanGetByIDResponse,
        )


class SimulationRunPlanResourceWithRawResponse:
    def __init__(self, simulation_run_plan: SimulationRunPlanResource) -> None:
        self._simulation_run_plan = simulation_run_plan

        self.create = to_raw_response_wrapper(
            simulation_run_plan.create,
        )
        self.update = to_raw_response_wrapper(
            simulation_run_plan.update,
        )
        self.list = to_raw_response_wrapper(
            simulation_run_plan.list,
        )
        self.delete = to_raw_response_wrapper(
            simulation_run_plan.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_run_plan.get_by_id,
        )


class AsyncSimulationRunPlanResourceWithRawResponse:
    def __init__(self, simulation_run_plan: AsyncSimulationRunPlanResource) -> None:
        self._simulation_run_plan = simulation_run_plan

        self.create = async_to_raw_response_wrapper(
            simulation_run_plan.create,
        )
        self.update = async_to_raw_response_wrapper(
            simulation_run_plan.update,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_run_plan.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simulation_run_plan.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_run_plan.get_by_id,
        )


class SimulationRunPlanResourceWithStreamingResponse:
    def __init__(self, simulation_run_plan: SimulationRunPlanResource) -> None:
        self._simulation_run_plan = simulation_run_plan

        self.create = to_streamed_response_wrapper(
            simulation_run_plan.create,
        )
        self.update = to_streamed_response_wrapper(
            simulation_run_plan.update,
        )
        self.list = to_streamed_response_wrapper(
            simulation_run_plan.list,
        )
        self.delete = to_streamed_response_wrapper(
            simulation_run_plan.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_run_plan.get_by_id,
        )


class AsyncSimulationRunPlanResourceWithStreamingResponse:
    def __init__(self, simulation_run_plan: AsyncSimulationRunPlanResource) -> None:
        self._simulation_run_plan = simulation_run_plan

        self.create = async_to_streamed_response_wrapper(
            simulation_run_plan.create,
        )
        self.update = async_to_streamed_response_wrapper(
            simulation_run_plan.update,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_run_plan.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simulation_run_plan.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_run_plan.get_by_id,
        )
