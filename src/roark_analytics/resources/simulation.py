# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import overload

import httpx

from ..types import simulation_run_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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

    @overload
    def run(
        self,
        *,
        plan: simulation_run_params.RunSimulationFromConfigPlan,
        save_plan_as: str | Omit = omit,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromConfigVariablesUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromConfigVariablesUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """
        Starts a simulation and returns the run.

        Send `plan` to describe a simulation and run it once. Add `savePlanAs` to keep
        that configuration as a reusable run plan. Send `planId` instead to run a plan
        you already have.

        Args:
          plan: The simulation to run: what to call, who calls it, and what to measure.

          save_plan_as: Keeps this configuration as a run plan under this name, listed by GET
              /v1/simulation/plan and re-runnable with `planId`.

              Omit it for a one-off. The run still needs a plan to execute, so one is created
              either way, but an unnamed one is hidden: it carries this run and nothing else.

          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned.

              An object applies them to the whole run:

              { "orderNumber": "12345", "tier": "gold" }

              An array applies them per flow, or per variant of one, when a single set will
              not do. Each entry carries what it applies to:

              [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
              "flowId": "550e8400-...", "variantId": "7a3d2e1f-...", "variables": {
              "orderNumber": "67890" } } ]

              An entry without `variantId` covers every variant that flow resolves. A flow
              this plan does not attach, or a variant that does not belong to the flow, is
              rejected rather than ignored.

              A plan built on scenarios rather than customer flows targets them the same way,
              with `scenarioId` in place of `flowId`. That form is deprecated alongside
              scenarios themselves, and still accepted so runs against those plans keep
              working.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        plan_id: str,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromPlanIDVariablesUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromPlanIDVariablesUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """
        Starts a simulation and returns the run.

        Send `plan` to describe a simulation and run it once. Add `savePlanAs` to keep
        that configuration as a reusable run plan. Send `planId` instead to run a plan
        you already have.

        Args:
          plan_id: The run plan to run, saved or hidden. Rename or unhide it with PUT
              /v1/simulation/plan/{planId}.

          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned.

              An object applies them to the whole run:

              { "orderNumber": "12345", "tier": "gold" }

              An array applies them per flow, or per variant of one, when a single set will
              not do. Each entry carries what it applies to:

              [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
              "flowId": "550e8400-...", "variantId": "7a3d2e1f-...", "variables": {
              "orderNumber": "67890" } } ]

              An entry without `variantId` covers every variant that flow resolves. A flow
              this plan does not attach, or a variant that does not belong to the flow, is
              rejected rather than ignored.

              A plan built on scenarios rather than customer flows targets them the same way,
              with `scenarioId` in place of `flowId`. That form is deprecated alongside
              scenarios themselves, and still accepted so runs against those plans keep
              working.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["plan"], ["plan_id"])
    def run(
        self,
        *,
        plan: simulation_run_params.RunSimulationFromConfigPlan | Omit = omit,
        save_plan_as: str | Omit = omit,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromConfigVariablesUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromConfigVariablesUnionMember2],
        ]
        | Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromPlanIDVariablesUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromPlanIDVariablesUnionMember2],
        ]
        | Omit = omit,
        plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        return self._post(
            "/v1/simulation/run",
            body=maybe_transform(
                {
                    "plan": plan,
                    "save_plan_as": save_plan_as,
                    "variables": variables,
                    "plan_id": plan_id,
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

    @overload
    async def run(
        self,
        *,
        plan: simulation_run_params.RunSimulationFromConfigPlan,
        save_plan_as: str | Omit = omit,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromConfigVariablesUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromConfigVariablesUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """
        Starts a simulation and returns the run.

        Send `plan` to describe a simulation and run it once. Add `savePlanAs` to keep
        that configuration as a reusable run plan. Send `planId` instead to run a plan
        you already have.

        Args:
          plan: The simulation to run: what to call, who calls it, and what to measure.

          save_plan_as: Keeps this configuration as a run plan under this name, listed by GET
              /v1/simulation/plan and re-runnable with `planId`.

              Omit it for a one-off. The run still needs a plan to execute, so one is created
              either way, but an unnamed one is hidden: it carries this run and nothing else.

          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned.

              An object applies them to the whole run:

              { "orderNumber": "12345", "tier": "gold" }

              An array applies them per flow, or per variant of one, when a single set will
              not do. Each entry carries what it applies to:

              [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
              "flowId": "550e8400-...", "variantId": "7a3d2e1f-...", "variables": {
              "orderNumber": "67890" } } ]

              An entry without `variantId` covers every variant that flow resolves. A flow
              this plan does not attach, or a variant that does not belong to the flow, is
              rejected rather than ignored.

              A plan built on scenarios rather than customer flows targets them the same way,
              with `scenarioId` in place of `flowId`. That form is deprecated alongside
              scenarios themselves, and still accepted so runs against those plans keep
              working.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        plan_id: str,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromPlanIDVariablesUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromPlanIDVariablesUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        """
        Starts a simulation and returns the run.

        Send `plan` to describe a simulation and run it once. Add `savePlanAs` to keep
        that configuration as a reusable run plan. Send `planId` instead to run a plan
        you already have.

        Args:
          plan_id: The run plan to run, saved or hidden. Rename or unhide it with PUT
              /v1/simulation/plan/{planId}.

          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned.

              An object applies them to the whole run:

              { "orderNumber": "12345", "tier": "gold" }

              An array applies them per flow, or per variant of one, when a single set will
              not do. Each entry carries what it applies to:

              [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
              "flowId": "550e8400-...", "variantId": "7a3d2e1f-...", "variables": {
              "orderNumber": "67890" } } ]

              An entry without `variantId` covers every variant that flow resolves. A flow
              this plan does not attach, or a variant that does not belong to the flow, is
              rejected rather than ignored.

              A plan built on scenarios rather than customer flows targets them the same way,
              with `scenarioId` in place of `flowId`. That form is deprecated alongside
              scenarios themselves, and still accepted so runs against those plans keep
              working.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["plan"], ["plan_id"])
    async def run(
        self,
        *,
        plan: simulation_run_params.RunSimulationFromConfigPlan | Omit = omit,
        save_plan_as: str | Omit = omit,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromConfigVariablesUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromConfigVariablesUnionMember2],
        ]
        | Union[
            Dict[str, str],
            Iterable[simulation_run_params.RunSimulationFromPlanIDVariablesUnionMember1],
            Iterable[simulation_run_params.RunSimulationFromPlanIDVariablesUnionMember2],
        ]
        | Omit = omit,
        plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunResponse:
        return await self._post(
            "/v1/simulation/run",
            body=await async_maybe_transform(
                {
                    "plan": plan,
                    "save_plan_as": save_plan_as,
                    "variables": variables,
                    "plan_id": plan_id,
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
