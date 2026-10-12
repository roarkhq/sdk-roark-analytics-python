# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import simulation_run_group_list_params, simulation_run_group_create_params
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
from ..types.simulation_run_group_list_response import SimulationRunGroupListResponse
from ..types.simulation_run_group_create_response import SimulationRunGroupCreateResponse
from ..types.simulation_run_group_delete_response import SimulationRunGroupDeleteResponse
from ..types.simulation_run_group_get_by_id_response import SimulationRunGroupGetByIDResponse
from ..types.simulation_run_group_regenerate_report_response import SimulationRunGroupRegenerateReportResponse

__all__ = ["SimulationRunGroupResource", "AsyncSimulationRunGroupResource"]


class SimulationRunGroupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationRunGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationRunGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationRunGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationRunGroupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str | Omit = omit,
        simulation_run_plan_ids: SequenceNotStr[str] | Omit = omit,
        simulation_run_plan_job_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupCreateResponse:
        """
        Groups several simulation runs so they read as one, and starts generating the
        group report: one document across every run, with a scorecard summed across them
        and the issues found, each merged from the per-run debriefs. Send
        `simulationRunPlanJobIds` to group runs that already exist (runs still in
        progress are fine: the report waits for them). Send `simulationRunPlanIds` to
        start one run of each plan and group those; this places real calls, exactly as
        starting each plan would. Poll GET /v1/simulation/run-group/{groupId} until
        `latestReport.status` is READY.

        Args:
          name: What to call the group. Defaults to the plans' names when starting plans, and to
              the runs' plan names when grouping existing runs.

          simulation_run_plan_ids: Plans to run once each, in display order (2 to 20). Each plan starts a run,
              exactly as POST /v1/simulation/plan/{planId}/job would. Send this or
              `simulationRunPlanJobIds`, not both.

          simulation_run_plan_job_ids: Runs that already exist, in display order (2 to 20). Runs still in progress are
              fine: the group report waits for them. Send this or `simulationRunPlanIds`, not
              both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulation/run-group",
            body=maybe_transform(
                {
                    "name": name,
                    "simulation_run_plan_ids": simulation_run_plan_ids,
                    "simulation_run_plan_job_ids": simulation_run_plan_job_ids,
                },
                simulation_run_group_create_params.SimulationRunGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunGroupCreateResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupListResponse:
        """
        Returns the run groups in the project, newest first, with their runs and where
        each group report stands. Read a report document from GET
        /v1/simulation/run-group/{groupId}.

        Args:
          limit: Maximum number of run groups to return (default: 20, max: 100)

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/run-group",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    simulation_run_group_list_params.SimulationRunGroupListParams,
                ),
            ),
            cast_to=SimulationRunGroupListResponse,
        )

    def delete(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupDeleteResponse:
        """Deletes a run group.

        Its runs, and their results, are untouched.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._delete(
            f"/v1/simulation/run-group/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunGroupDeleteResponse,
        )

    def get_by_id(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupGetByIDResponse:
        """
        Returns a run group with its runs in group order and its latest group report,
        including the report document once READY.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            f"/v1/simulation/run-group/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunGroupGetByIDResponse,
        )

    def regenerate_report(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupRegenerateReportResponse:
        """Generates the group report again over the latest state of its runs.

        Returns the
        report generation; if one is already in flight it is returned instead of
        starting another. Poll GET /v1/simulation/run-group/{groupId} until
        `latestReport.status` is READY.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            f"/v1/simulation/run-group/{group_id}/report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunGroupRegenerateReportResponse,
        )


class AsyncSimulationRunGroupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationRunGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationRunGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationRunGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationRunGroupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str | Omit = omit,
        simulation_run_plan_ids: SequenceNotStr[str] | Omit = omit,
        simulation_run_plan_job_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupCreateResponse:
        """
        Groups several simulation runs so they read as one, and starts generating the
        group report: one document across every run, with a scorecard summed across them
        and the issues found, each merged from the per-run debriefs. Send
        `simulationRunPlanJobIds` to group runs that already exist (runs still in
        progress are fine: the report waits for them). Send `simulationRunPlanIds` to
        start one run of each plan and group those; this places real calls, exactly as
        starting each plan would. Poll GET /v1/simulation/run-group/{groupId} until
        `latestReport.status` is READY.

        Args:
          name: What to call the group. Defaults to the plans' names when starting plans, and to
              the runs' plan names when grouping existing runs.

          simulation_run_plan_ids: Plans to run once each, in display order (2 to 20). Each plan starts a run,
              exactly as POST /v1/simulation/plan/{planId}/job would. Send this or
              `simulationRunPlanJobIds`, not both.

          simulation_run_plan_job_ids: Runs that already exist, in display order (2 to 20). Runs still in progress are
              fine: the group report waits for them. Send this or `simulationRunPlanIds`, not
              both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulation/run-group",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "simulation_run_plan_ids": simulation_run_plan_ids,
                    "simulation_run_plan_job_ids": simulation_run_plan_job_ids,
                },
                simulation_run_group_create_params.SimulationRunGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunGroupCreateResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupListResponse:
        """
        Returns the run groups in the project, newest first, with their runs and where
        each group report stands. Read a report document from GET
        /v1/simulation/run-group/{groupId}.

        Args:
          limit: Maximum number of run groups to return (default: 20, max: 100)

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/run-group",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    simulation_run_group_list_params.SimulationRunGroupListParams,
                ),
            ),
            cast_to=SimulationRunGroupListResponse,
        )

    async def delete(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupDeleteResponse:
        """Deletes a run group.

        Its runs, and their results, are untouched.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._delete(
            f"/v1/simulation/run-group/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunGroupDeleteResponse,
        )

    async def get_by_id(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupGetByIDResponse:
        """
        Returns a run group with its runs in group order and its latest group report,
        including the report document once READY.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            f"/v1/simulation/run-group/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunGroupGetByIDResponse,
        )

    async def regenerate_report(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationRunGroupRegenerateReportResponse:
        """Generates the group report again over the latest state of its runs.

        Returns the
        report generation; if one is already in flight it is returned instead of
        starting another. Poll GET /v1/simulation/run-group/{groupId} until
        `latestReport.status` is READY.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            f"/v1/simulation/run-group/{group_id}/report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationRunGroupRegenerateReportResponse,
        )


class SimulationRunGroupResourceWithRawResponse:
    def __init__(self, simulation_run_group: SimulationRunGroupResource) -> None:
        self._simulation_run_group = simulation_run_group

        self.create = to_raw_response_wrapper(
            simulation_run_group.create,
        )
        self.list = to_raw_response_wrapper(
            simulation_run_group.list,
        )
        self.delete = to_raw_response_wrapper(
            simulation_run_group.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_run_group.get_by_id,
        )
        self.regenerate_report = to_raw_response_wrapper(
            simulation_run_group.regenerate_report,
        )


class AsyncSimulationRunGroupResourceWithRawResponse:
    def __init__(self, simulation_run_group: AsyncSimulationRunGroupResource) -> None:
        self._simulation_run_group = simulation_run_group

        self.create = async_to_raw_response_wrapper(
            simulation_run_group.create,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_run_group.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simulation_run_group.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_run_group.get_by_id,
        )
        self.regenerate_report = async_to_raw_response_wrapper(
            simulation_run_group.regenerate_report,
        )


class SimulationRunGroupResourceWithStreamingResponse:
    def __init__(self, simulation_run_group: SimulationRunGroupResource) -> None:
        self._simulation_run_group = simulation_run_group

        self.create = to_streamed_response_wrapper(
            simulation_run_group.create,
        )
        self.list = to_streamed_response_wrapper(
            simulation_run_group.list,
        )
        self.delete = to_streamed_response_wrapper(
            simulation_run_group.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_run_group.get_by_id,
        )
        self.regenerate_report = to_streamed_response_wrapper(
            simulation_run_group.regenerate_report,
        )


class AsyncSimulationRunGroupResourceWithStreamingResponse:
    def __init__(self, simulation_run_group: AsyncSimulationRunGroupResource) -> None:
        self._simulation_run_group = simulation_run_group

        self.create = async_to_streamed_response_wrapper(
            simulation_run_group.create,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_run_group.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simulation_run_group.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_run_group.get_by_id,
        )
        self.regenerate_report = async_to_streamed_response_wrapper(
            simulation_run_group.regenerate_report,
        )
