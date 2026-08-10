# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ..types import simulation_run_params
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
from ..types.simulation_run_response import SimulationRunResponse

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

    def run(
        self,
        *,
        flow_variables: Iterable[simulation_run_params.FlowVariable] | Omit = omit,
        plan: simulation_run_params.Plan | Omit = omit,
        plan_id: str | Omit = omit,
        save_as_plan_name: str | Omit = omit,
        variables: Union[Dict[str, str], Iterable[simulation_run_params.VariablesUnionMember1]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """
        Runs a simulation and returns the run that was started.

        Describe the simulation in `plan`, or name an existing one with `planId`. Every
        run is backed by a run plan, but you only get one you can see and re-use if you
        ask for it with `saveAsPlanName`; otherwise the plan is created hidden and
        simply carries the run.

        This replaces creating a plan and then starting a job against it. The response
        carries `simulationJobCount`, the number of calls the run places, each of which
        is billed.

        Args:
          flow_variables: Runtime variable overrides targeted at the plan’s customer flows, taking
              precedence over the values pinned on the flow attachment.

              An entry without `variantId` applies to every variant the attachment resolves. A
              flow that is not attached to this plan, or a variant that does not belong to the
              flow, is rejected rather than ignored.

          plan: The simulation to run. A run plan is created for it behind the scenes.

          plan_id: Run a plan that already exists instead of describing one. Mutually exclusive
              with `plan`.

          save_as_plan_name: Keep this run as a reusable plan under this name.

              Left unset, the run still needs a plan to execute, but it is created hidden: it
              does not appear in GET /v1/simulation/plan and exists only to carry the run.
              Applies only alongside `plan`, since `planId` names a plan that already exists.

          variables: Runtime variables that override the values defined on the plan. Accepts one of
              two formats:

              Option 1, global (a flat key-value object): { "orderNumber": "12345",
              "environment": "staging" }

              Option 2, per-scenario (an array of objects with scenarioId + variables): [ {
              "scenarioId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
              "scenarioId": "7a3d2e1f-...", "variables": { "orderNumber": "67890" } } ]

              On a flow-based plan the global format applies to every variant the run
              resolves. The per-scenario format targets scenarios, so use `flowVariables` to
              override a specific flow or variant instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulation/run",
            body=maybe_transform(
                {
                    "flow_variables": flow_variables,
                    "plan": plan,
                    "plan_id": plan_id,
                    "save_as_plan_name": save_as_plan_name,
                    "variables": variables,
                },
                simulation_run_params.SimulationRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunResponse,
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

    async def run(
        self,
        *,
        flow_variables: Iterable[simulation_run_params.FlowVariable] | Omit = omit,
        plan: simulation_run_params.Plan | Omit = omit,
        plan_id: str | Omit = omit,
        save_as_plan_name: str | Omit = omit,
        variables: Union[Dict[str, str], Iterable[simulation_run_params.VariablesUnionMember1]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """
        Runs a simulation and returns the run that was started.

        Describe the simulation in `plan`, or name an existing one with `planId`. Every
        run is backed by a run plan, but you only get one you can see and re-use if you
        ask for it with `saveAsPlanName`; otherwise the plan is created hidden and
        simply carries the run.

        This replaces creating a plan and then starting a job against it. The response
        carries `simulationJobCount`, the number of calls the run places, each of which
        is billed.

        Args:
          flow_variables: Runtime variable overrides targeted at the plan’s customer flows, taking
              precedence over the values pinned on the flow attachment.

              An entry without `variantId` applies to every variant the attachment resolves. A
              flow that is not attached to this plan, or a variant that does not belong to the
              flow, is rejected rather than ignored.

          plan: The simulation to run. A run plan is created for it behind the scenes.

          plan_id: Run a plan that already exists instead of describing one. Mutually exclusive
              with `plan`.

          save_as_plan_name: Keep this run as a reusable plan under this name.

              Left unset, the run still needs a plan to execute, but it is created hidden: it
              does not appear in GET /v1/simulation/plan and exists only to carry the run.
              Applies only alongside `plan`, since `planId` names a plan that already exists.

          variables: Runtime variables that override the values defined on the plan. Accepts one of
              two formats:

              Option 1, global (a flat key-value object): { "orderNumber": "12345",
              "environment": "staging" }

              Option 2, per-scenario (an array of objects with scenarioId + variables): [ {
              "scenarioId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
              "scenarioId": "7a3d2e1f-...", "variables": { "orderNumber": "67890" } } ]

              On a flow-based plan the global format applies to every variant the run
              resolves. The per-scenario format targets scenarios, so use `flowVariables` to
              override a specific flow or variant instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulation/run",
            body=await async_maybe_transform(
                {
                    "flow_variables": flow_variables,
                    "plan": plan,
                    "plan_id": plan_id,
                    "save_as_plan_name": save_as_plan_name,
                    "variables": variables,
                },
                simulation_run_params.SimulationRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunResponse,
        )


class SimulationResourceWithRawResponse:
    def __init__(self, simulation: SimulationResource) -> None:
        self._simulation = simulation

        self.run = to_raw_response_wrapper(
            simulation.run,
        )


class AsyncSimulationResourceWithRawResponse:
    def __init__(self, simulation: AsyncSimulationResource) -> None:
        self._simulation = simulation

        self.run = async_to_raw_response_wrapper(
            simulation.run,
        )


class SimulationResourceWithStreamingResponse:
    def __init__(self, simulation: SimulationResource) -> None:
        self._simulation = simulation

        self.run = to_streamed_response_wrapper(
            simulation.run,
        )


class AsyncSimulationResourceWithStreamingResponse:
    def __init__(self, simulation: AsyncSimulationResource) -> None:
        self._simulation = simulation

        self.run = async_to_streamed_response_wrapper(
            simulation.run,
        )
