# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import simulation_run_plan_job_list_params, simulation_run_plan_job_start_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.simulation_run_plan_job_list_response import SimulationRunPlanJobListResponse
from ..types.simulation_run_plan_job_start_response import SimulationRunPlanJobStartResponse
from ..types.simulation_run_plan_job_get_by_id_response import SimulationRunPlanJobGetByIDResponse

__all__ = ["SimulationRunPlanJobResource", "AsyncSimulationRunPlanJobResource"]


class SimulationRunPlanJobResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationRunPlanJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationRunPlanJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationRunPlanJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationRunPlanJobResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        label_id: str | Omit = omit,
        label_name: str | Omit = omit,
        limit: int | Omit = omit,
        simulation_run_plan_id: str | Omit = omit,
        status: Literal[
            "PENDING",
            "QUEUED",
            "CREATING_SNAPSHOTS",
            "CREATING_SIMULATIONS",
            "RUNNING_SIMULATIONS",
            "COMPLETED",
            "FAILED",
            "TIMED_OUT",
            "CANCELLED",
            "CANCELLING",
            "ENDING_SIMULATIONS",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanJobListResponse:
        """Returns a paginated list of simulation run plan jobs.

        Filter by status, plan ID,
        or label to find specific simulation batches.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          label_id: Filter by label ID attached to the plan job. Use this if you know the label ID.

          label_name: Filter by label name attached to the plan job. More user-friendly alternative to
              labelId. Case-insensitive.

          limit: Maximum number of plan jobs to return (default: 20, max: 50)

          simulation_run_plan_id: Filter by simulation run plan ID

          status: Filter by plan job status (PENDING, CREATING_SNAPSHOTS, CREATING_SIMULATIONS,
              RUNNING_SIMULATIONS, ENDING_SIMULATIONS, COMPLETED, FAILED, TIMED_OUT,
              CANCELLED, CANCELLING)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/plan/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "label_id": label_id,
                        "label_name": label_name,
                        "limit": limit,
                        "simulation_run_plan_id": simulation_run_plan_id,
                        "status": status,
                    },
                    simulation_run_plan_job_list_params.SimulationRunPlanJobListParams,
                ),
            ),
            cast_to=SimulationRunPlanJobListResponse,
        )

    def get_by_id(
        self,
        job_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanJobGetByIDResponse:
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
            path_template("/v1/simulation/plan/job/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanJobGetByIDResponse,
        )

    def start(
        self,
        plan_id: object,
        *,
        flow_variables: Iterable[simulation_run_plan_job_start_params.FlowVariable] | Omit = omit,
        variables: Union[Dict[str, str], Iterable[simulation_run_plan_job_start_params.VariablesUnionMember1]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanJobStartResponse:
        """Create and execute a job for an existing simulation run plan.

        Optionally provide
        runtime variables to override plan-defined variables.

        Args:
          flow_variables: Runtime variable overrides targeted at the plan’s customer flows, taking
              precedence over the values pinned on the flow attachment.

              An entry without `variantId` applies to every variant the attachment resolves. A
              flow that is not attached to this plan, or a variant that does not belong to the
              flow, is rejected rather than ignored.

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
            path_template("/v1/simulation/plan/{plan_id}/job", plan_id=plan_id),
            body=maybe_transform(
                {
                    "flow_variables": flow_variables,
                    "variables": variables,
                },
                simulation_run_plan_job_start_params.SimulationRunPlanJobStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanJobStartResponse,
        )


class AsyncSimulationRunPlanJobResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationRunPlanJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationRunPlanJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationRunPlanJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationRunPlanJobResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | Omit = omit,
        label_id: str | Omit = omit,
        label_name: str | Omit = omit,
        limit: int | Omit = omit,
        simulation_run_plan_id: str | Omit = omit,
        status: Literal[
            "PENDING",
            "QUEUED",
            "CREATING_SNAPSHOTS",
            "CREATING_SIMULATIONS",
            "RUNNING_SIMULATIONS",
            "COMPLETED",
            "FAILED",
            "TIMED_OUT",
            "CANCELLED",
            "CANCELLING",
            "ENDING_SIMULATIONS",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanJobListResponse:
        """Returns a paginated list of simulation run plan jobs.

        Filter by status, plan ID,
        or label to find specific simulation batches.

        Args:
          after: Cursor for pagination - use the nextCursor value from a previous response

          label_id: Filter by label ID attached to the plan job. Use this if you know the label ID.

          label_name: Filter by label name attached to the plan job. More user-friendly alternative to
              labelId. Case-insensitive.

          limit: Maximum number of plan jobs to return (default: 20, max: 50)

          simulation_run_plan_id: Filter by simulation run plan ID

          status: Filter by plan job status (PENDING, CREATING_SNAPSHOTS, CREATING_SIMULATIONS,
              RUNNING_SIMULATIONS, ENDING_SIMULATIONS, COMPLETED, FAILED, TIMED_OUT,
              CANCELLED, CANCELLING)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/plan/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "label_id": label_id,
                        "label_name": label_name,
                        "limit": limit,
                        "simulation_run_plan_id": simulation_run_plan_id,
                        "status": status,
                    },
                    simulation_run_plan_job_list_params.SimulationRunPlanJobListParams,
                ),
            ),
            cast_to=SimulationRunPlanJobListResponse,
        )

    async def get_by_id(
        self,
        job_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanJobGetByIDResponse:
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
            path_template("/v1/simulation/plan/job/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanJobGetByIDResponse,
        )

    async def start(
        self,
        plan_id: object,
        *,
        flow_variables: Iterable[simulation_run_plan_job_start_params.FlowVariable] | Omit = omit,
        variables: Union[Dict[str, str], Iterable[simulation_run_plan_job_start_params.VariablesUnionMember1]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanJobStartResponse:
        """Create and execute a job for an existing simulation run plan.

        Optionally provide
        runtime variables to override plan-defined variables.

        Args:
          flow_variables: Runtime variable overrides targeted at the plan’s customer flows, taking
              precedence over the values pinned on the flow attachment.

              An entry without `variantId` applies to every variant the attachment resolves. A
              flow that is not attached to this plan, or a variant that does not belong to the
              flow, is rejected rather than ignored.

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
            path_template("/v1/simulation/plan/{plan_id}/job", plan_id=plan_id),
            body=await async_maybe_transform(
                {
                    "flow_variables": flow_variables,
                    "variables": variables,
                },
                simulation_run_plan_job_start_params.SimulationRunPlanJobStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunPlanJobStartResponse,
        )


class SimulationRunPlanJobResourceWithRawResponse:
    def __init__(self, simulation_run_plan_job: SimulationRunPlanJobResource) -> None:
        self._simulation_run_plan_job = simulation_run_plan_job

        self.list = to_raw_response_wrapper(
            simulation_run_plan_job.list,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_run_plan_job.get_by_id,
        )
        self.start = to_raw_response_wrapper(
            simulation_run_plan_job.start,
        )


class AsyncSimulationRunPlanJobResourceWithRawResponse:
    def __init__(self, simulation_run_plan_job: AsyncSimulationRunPlanJobResource) -> None:
        self._simulation_run_plan_job = simulation_run_plan_job

        self.list = async_to_raw_response_wrapper(
            simulation_run_plan_job.list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_run_plan_job.get_by_id,
        )
        self.start = async_to_raw_response_wrapper(
            simulation_run_plan_job.start,
        )


class SimulationRunPlanJobResourceWithStreamingResponse:
    def __init__(self, simulation_run_plan_job: SimulationRunPlanJobResource) -> None:
        self._simulation_run_plan_job = simulation_run_plan_job

        self.list = to_streamed_response_wrapper(
            simulation_run_plan_job.list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_run_plan_job.get_by_id,
        )
        self.start = to_streamed_response_wrapper(
            simulation_run_plan_job.start,
        )


class AsyncSimulationRunPlanJobResourceWithStreamingResponse:
    def __init__(self, simulation_run_plan_job: AsyncSimulationRunPlanJobResource) -> None:
        self._simulation_run_plan_job = simulation_run_plan_job

        self.list = async_to_streamed_response_wrapper(
            simulation_run_plan_job.list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_run_plan_job.get_by_id,
        )
        self.start = async_to_streamed_response_wrapper(
            simulation_run_plan_job.start,
        )
