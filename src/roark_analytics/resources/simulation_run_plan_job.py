# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
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
            "PREPARING_CAPACITY",
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

          status: Filter by plan job status (PENDING, QUEUED, CREATING_SNAPSHOTS,
              CREATING_SIMULATIONS, PREPARING_CAPACITY, RUNNING_SIMULATIONS, COMPLETED,
              FAILED, TIMED_OUT, CANCELLED, CANCELLING, ENDING_SIMULATIONS)

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

    @typing_extensions.deprecated("deprecated")
    def start(
        self,
        plan_id: object,
        *,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_plan_job_start_params.VariablesUnionMember1],
            Iterable[simulation_run_plan_job_start_params.VariablesUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanJobStartResponse:
        """
        Deprecated: use POST /v1/simulation/run, which does the same thing and can also
        take the plan configuration inline, so a one-off run does not have to create a
        plan first.

        Creates and executes a job for an existing simulation run plan. Optionally
        provide runtime variables to override plan-defined variables.

        Args:
          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned.

              An object applies them to the whole run:

              { "orderNumber": "12345", "tier": "gold" }

              An array applies them per flow, or to just its happy path or one of its edge
              cases, when a single set will not do. Each entry carries what it applies to:

              [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
              "flowId": "550e8400-...", "happyPath": true, "variables": { "orderNumber":
              "55555" } }, { "flowId": "550e8400-...", "edgeCaseId": "7a3d2e1f-...",
              "variables": { "orderNumber": "67890" } } ]

              An entry that narrows to neither covers everything that flow resolves. A flow
              this plan does not attach, or an edge case that does not belong to the flow, is
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
        return self._post(
            path_template("/v1/simulation/plan/{plan_id}/job", plan_id=plan_id),
            body=maybe_transform(
                {"variables": variables}, simulation_run_plan_job_start_params.SimulationRunPlanJobStartParams
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
            "PREPARING_CAPACITY",
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

          status: Filter by plan job status (PENDING, QUEUED, CREATING_SNAPSHOTS,
              CREATING_SIMULATIONS, PREPARING_CAPACITY, RUNNING_SIMULATIONS, COMPLETED,
              FAILED, TIMED_OUT, CANCELLED, CANCELLING, ENDING_SIMULATIONS)

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

    @typing_extensions.deprecated("deprecated")
    async def start(
        self,
        plan_id: object,
        *,
        variables: Union[
            Dict[str, str],
            Iterable[simulation_run_plan_job_start_params.VariablesUnionMember1],
            Iterable[simulation_run_plan_job_start_params.VariablesUnionMember2],
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunPlanJobStartResponse:
        """
        Deprecated: use POST /v1/simulation/run, which does the same thing and can also
        take the plan configuration inline, so a one-off run does not have to create a
        plan first.

        Creates and executes a job for an existing simulation run plan. Optionally
        provide runtime variables to override plan-defined variables.

        Args:
          variables: Values for the {{variables}} the run resolves, overriding whatever the plan has
              pinned.

              An object applies them to the whole run:

              { "orderNumber": "12345", "tier": "gold" }

              An array applies them per flow, or to just its happy path or one of its edge
              cases, when a single set will not do. Each entry carries what it applies to:

              [ { "flowId": "550e8400-...", "variables": { "orderNumber": "12345" } }, {
              "flowId": "550e8400-...", "happyPath": true, "variables": { "orderNumber":
              "55555" } }, { "flowId": "550e8400-...", "edgeCaseId": "7a3d2e1f-...",
              "variables": { "orderNumber": "67890" } } ]

              An entry that narrows to neither covers everything that flow resolves. A flow
              this plan does not attach, or an edge case that does not belong to the flow, is
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
        return await self._post(
            path_template("/v1/simulation/plan/{plan_id}/job", plan_id=plan_id),
            body=await async_maybe_transform(
                {"variables": variables}, simulation_run_plan_job_start_params.SimulationRunPlanJobStartParams
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
        self.start = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                simulation_run_plan_job.start,  # pyright: ignore[reportDeprecated],
            )
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
        self.start = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                simulation_run_plan_job.start,  # pyright: ignore[reportDeprecated],
            )
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
        self.start = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                simulation_run_plan_job.start,  # pyright: ignore[reportDeprecated],
            )
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
        self.start = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                simulation_run_plan_job.start,  # pyright: ignore[reportDeprecated],
            )
        )
