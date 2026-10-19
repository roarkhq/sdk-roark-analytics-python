# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import simulation_group_list_params, simulation_group_create_params, simulation_group_update_params
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
from ..types.simulation_group_run_response import SimulationGroupRunResponse
from ..types.simulation_group_list_response import SimulationGroupListResponse
from ..types.simulation_group_create_response import SimulationGroupCreateResponse
from ..types.simulation_group_delete_response import SimulationGroupDeleteResponse
from ..types.simulation_group_update_response import SimulationGroupUpdateResponse
from ..types.simulation_group_get_by_id_response import SimulationGroupGetByIDResponse

__all__ = ["SimulationGroupResource", "AsyncSimulationGroupResource"]


class SimulationGroupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationGroupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        simulation_run_plan_ids: SequenceNotStr[str],
        description: Optional[str] | Omit = omit,
        notifications: simulation_group_create_params.Notification | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGroupCreateResponse:
        """Saves a named set of plans to run together, again and again.

        Nothing runs yet:
        POST /v1/simulation/group/{groupId}/run starts one run of every plan and groups
        them into a run group with one combined report. Slack channels need Slack
        connected to the project. Email is on by default.

        Args:
          name: What to call the group.

          simulation_run_plan_ids: The plans to run together, in run order (2 to 20). Duplicates are dropped.

          description: What the group is for.

          notifications: Defaults to email on (to the default audience) and no Slack.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulation/group",
            body=maybe_transform(
                {
                    "name": name,
                    "simulation_run_plan_ids": simulation_run_plan_ids,
                    "description": description,
                    "notifications": notifications,
                },
                simulation_group_create_params.SimulationGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupCreateResponse,
        )

    def update(
        self,
        group_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        notifications: simulation_group_update_params.Notification | Omit = omit,
        simulation_run_plan_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGroupUpdateResponse:
        """Edits a saved simulation group.

        Omitted fields keep their current value;
        `notifications`, when sent, replaces the settings as a whole. Run groups it
        already started keep theirs. A group managed by config as code (`configManaged:
        true`) returns 409: change it in the config file.

        Args:
          description: Send null to clear it.

          notifications: Replaces the notification settings as a whole.

          simulation_run_plan_ids: Replaces the plans, in run order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._put(
            f"/v1/simulation/group/{group_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "notifications": notifications,
                    "simulation_run_plan_ids": simulation_run_plan_ids,
                },
                simulation_group_update_params.SimulationGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupUpdateResponse,
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
    ) -> SimulationGroupListResponse:
        """
        Returns the saved simulation groups in the project, most recently edited first,
        each with its plans in run order and notification settings.

        Args:
          limit: Maximum number of groups to return (default: 20, max: 100)

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/group",
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
                    simulation_group_list_params.SimulationGroupListParams,
                ),
            ),
            cast_to=SimulationGroupListResponse,
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
    ) -> SimulationGroupDeleteResponse:
        """Deletes a saved simulation group and any schedules that run it.

        Run groups it
        already started, and their reports, stay. A group managed by config as code
        returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._delete(
            f"/v1/simulation/group/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupDeleteResponse,
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
    ) -> SimulationGroupGetByIDResponse:
        """
        Returns a saved simulation group with its plans in run order and notification
        settings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            f"/v1/simulation/group/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupGetByIDResponse,
        )

    def run(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGroupRunResponse:
        """
        Starts one run of every plan in the group, exactly as POST
        /v1/simulation/plan/{planId}/job would for each, and groups the runs into a run
        group whose combined report is announced through the group's notification
        settings once it is ready. This places real calls. Config-managed groups can be
        run here too. Returns the run group. Poll GET /v1/simulation/run-group/{groupId}
        until `latestReport.status` is READY. If a plan cannot start after others did,
        the runs that started are still grouped and the 400 names the run group id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            f"/v1/simulation/group/{group_id}/run",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupRunResponse,
        )


class AsyncSimulationGroupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationGroupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        simulation_run_plan_ids: SequenceNotStr[str],
        description: Optional[str] | Omit = omit,
        notifications: simulation_group_create_params.Notification | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGroupCreateResponse:
        """Saves a named set of plans to run together, again and again.

        Nothing runs yet:
        POST /v1/simulation/group/{groupId}/run starts one run of every plan and groups
        them into a run group with one combined report. Slack channels need Slack
        connected to the project. Email is on by default.

        Args:
          name: What to call the group.

          simulation_run_plan_ids: The plans to run together, in run order (2 to 20). Duplicates are dropped.

          description: What the group is for.

          notifications: Defaults to email on (to the default audience) and no Slack.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulation/group",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "simulation_run_plan_ids": simulation_run_plan_ids,
                    "description": description,
                    "notifications": notifications,
                },
                simulation_group_create_params.SimulationGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupCreateResponse,
        )

    async def update(
        self,
        group_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        notifications: simulation_group_update_params.Notification | Omit = omit,
        simulation_run_plan_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGroupUpdateResponse:
        """Edits a saved simulation group.

        Omitted fields keep their current value;
        `notifications`, when sent, replaces the settings as a whole. Run groups it
        already started keep theirs. A group managed by config as code (`configManaged:
        true`) returns 409: change it in the config file.

        Args:
          description: Send null to clear it.

          notifications: Replaces the notification settings as a whole.

          simulation_run_plan_ids: Replaces the plans, in run order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._put(
            f"/v1/simulation/group/{group_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "notifications": notifications,
                    "simulation_run_plan_ids": simulation_run_plan_ids,
                },
                simulation_group_update_params.SimulationGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupUpdateResponse,
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
    ) -> SimulationGroupListResponse:
        """
        Returns the saved simulation groups in the project, most recently edited first,
        each with its plans in run order and notification settings.

        Args:
          limit: Maximum number of groups to return (default: 20, max: 100)

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/group",
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
                    simulation_group_list_params.SimulationGroupListParams,
                ),
            ),
            cast_to=SimulationGroupListResponse,
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
    ) -> SimulationGroupDeleteResponse:
        """Deletes a saved simulation group and any schedules that run it.

        Run groups it
        already started, and their reports, stay. A group managed by config as code
        returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._delete(
            f"/v1/simulation/group/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupDeleteResponse,
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
    ) -> SimulationGroupGetByIDResponse:
        """
        Returns a saved simulation group with its plans in run order and notification
        settings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            f"/v1/simulation/group/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupGetByIDResponse,
        )

    async def run(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationGroupRunResponse:
        """
        Starts one run of every plan in the group, exactly as POST
        /v1/simulation/plan/{planId}/job would for each, and groups the runs into a run
        group whose combined report is announced through the group's notification
        settings once it is ready. This places real calls. Config-managed groups can be
        run here too. Returns the run group. Poll GET /v1/simulation/run-group/{groupId}
        until `latestReport.status` is READY. If a plan cannot start after others did,
        the runs that started are still grouped and the 400 names the run group id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            f"/v1/simulation/group/{group_id}/run",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationGroupRunResponse,
        )


class SimulationGroupResourceWithRawResponse:
    def __init__(self, simulation_group: SimulationGroupResource) -> None:
        self._simulation_group = simulation_group

        self.create = to_raw_response_wrapper(
            simulation_group.create,
        )
        self.update = to_raw_response_wrapper(
            simulation_group.update,
        )
        self.list = to_raw_response_wrapper(
            simulation_group.list,
        )
        self.delete = to_raw_response_wrapper(
            simulation_group.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_group.get_by_id,
        )
        self.run = to_raw_response_wrapper(
            simulation_group.run,
        )


class AsyncSimulationGroupResourceWithRawResponse:
    def __init__(self, simulation_group: AsyncSimulationGroupResource) -> None:
        self._simulation_group = simulation_group

        self.create = async_to_raw_response_wrapper(
            simulation_group.create,
        )
        self.update = async_to_raw_response_wrapper(
            simulation_group.update,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_group.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simulation_group.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_group.get_by_id,
        )
        self.run = async_to_raw_response_wrapper(
            simulation_group.run,
        )


class SimulationGroupResourceWithStreamingResponse:
    def __init__(self, simulation_group: SimulationGroupResource) -> None:
        self._simulation_group = simulation_group

        self.create = to_streamed_response_wrapper(
            simulation_group.create,
        )
        self.update = to_streamed_response_wrapper(
            simulation_group.update,
        )
        self.list = to_streamed_response_wrapper(
            simulation_group.list,
        )
        self.delete = to_streamed_response_wrapper(
            simulation_group.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_group.get_by_id,
        )
        self.run = to_streamed_response_wrapper(
            simulation_group.run,
        )


class AsyncSimulationGroupResourceWithStreamingResponse:
    def __init__(self, simulation_group: AsyncSimulationGroupResource) -> None:
        self._simulation_group = simulation_group

        self.create = async_to_streamed_response_wrapper(
            simulation_group.create,
        )
        self.update = async_to_streamed_response_wrapper(
            simulation_group.update,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_group.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simulation_group.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_group.get_by_id,
        )
        self.run = async_to_streamed_response_wrapper(
            simulation_group.run,
        )
