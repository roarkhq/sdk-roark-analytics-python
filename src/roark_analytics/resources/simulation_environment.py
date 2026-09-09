# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    simulation_environment_list_params,
    simulation_environment_create_params,
    simulation_environment_update_params,
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
from ..types.simulation_environment_list_response import SimulationEnvironmentListResponse
from ..types.simulation_environment_create_response import SimulationEnvironmentCreateResponse
from ..types.simulation_environment_delete_response import SimulationEnvironmentDeleteResponse
from ..types.simulation_environment_update_response import SimulationEnvironmentUpdateResponse
from ..types.simulation_environment_get_by_id_response import SimulationEnvironmentGetByIDResponse

__all__ = ["SimulationEnvironmentResource", "AsyncSimulationEnvironmentResource"]


class SimulationEnvironmentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationEnvironmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationEnvironmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationEnvironmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationEnvironmentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ],
        name: str,
        background_noise_volume: float | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentCreateResponse:
        """
        Creates an environment for the project: a noise bed and the level it plays at.
        Reference it by id when setting a customer flow variant's environment. Roark's
        curated presets always play at the default level, so this is how a project gets
        the same bed louder or quieter.

        Args:
          background_noise: The noise bed played underneath the simulated caller. NONE plays nothing.

          name: Display name, shown wherever a flow variant references the environment

          background_noise_volume: How loud the bed plays, as a gain from 0 (silent) to 1 (as loud as the caller).
              Defaults to 0.1, which sits well under the caller. Ignored on Vapi endpoints,
              which have no level control.

          description: Optional note on when to use this environment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulation/environment",
            body=maybe_transform(
                {
                    "background_noise": background_noise,
                    "name": name,
                    "background_noise_volume": background_noise_volume,
                    "description": description,
                },
                simulation_environment_create_params.SimulationEnvironmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentCreateResponse,
        )

    def update(
        self,
        environment_id: str,
        *,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        background_noise_volume: float | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentUpdateResponse:
        """Updates one of the project's environments.

        Only the fields sent are changed.
        Runs already built keep the snapshot they were built with. Roark-curated
        environments cannot be edited (403).

        Args:
          background_noise: The noise bed played underneath the simulated caller. NONE plays nothing.

          background_noise_volume: How loud the bed plays, as a gain from 0 (silent) to 1 (as loud as the caller).
              Defaults to 0.1, which sits well under the caller. Ignored on Vapi endpoints,
              which have no level control.

          description: Optional note on when to use this environment

          name: Display name, shown wherever a flow variant references the environment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return self._put(
            f"/v1/simulation/environment/{environment_id}",
            body=maybe_transform(
                {
                    "background_noise": background_noise,
                    "background_noise_volume": background_noise_volume,
                    "description": description,
                    "name": name,
                },
                simulation_environment_update_params.SimulationEnvironmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentUpdateResponse,
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
    ) -> SimulationEnvironmentListResponse:
        """
        Returns a paginated list of environments: the project's own plus the
        environments Roark curates and shares across every project. Reference one by id
        when setting a customer flow variant's environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/environment",
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
                    simulation_environment_list_params.SimulationEnvironmentListParams,
                ),
            ),
            cast_to=SimulationEnvironmentListResponse,
        )

    def delete(
        self,
        environment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentDeleteResponse:
        """Soft-deletes one of the project's environments.

        It disappears from reads and
        cannot be picked for new runs; runs already built keep their snapshot. Refused
        (409) while a live customer flow variant still uses it: move those variants
        first. Roark-curated environments cannot be deleted (403).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return self._delete(
            f"/v1/simulation/environment/{environment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentDeleteResponse,
        )

    def get_by_id(
        self,
        environment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentGetByIDResponse:
        """
        Returns a single environment by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return self._get(
            f"/v1/simulation/environment/{environment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentGetByIDResponse,
        )


class AsyncSimulationEnvironmentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationEnvironmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationEnvironmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationEnvironmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationEnvironmentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ],
        name: str,
        background_noise_volume: float | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentCreateResponse:
        """
        Creates an environment for the project: a noise bed and the level it plays at.
        Reference it by id when setting a customer flow variant's environment. Roark's
        curated presets always play at the default level, so this is how a project gets
        the same bed louder or quieter.

        Args:
          background_noise: The noise bed played underneath the simulated caller. NONE plays nothing.

          name: Display name, shown wherever a flow variant references the environment

          background_noise_volume: How loud the bed plays, as a gain from 0 (silent) to 1 (as loud as the caller).
              Defaults to 0.1, which sits well under the caller. Ignored on Vapi endpoints,
              which have no level control.

          description: Optional note on when to use this environment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulation/environment",
            body=await async_maybe_transform(
                {
                    "background_noise": background_noise,
                    "name": name,
                    "background_noise_volume": background_noise_volume,
                    "description": description,
                },
                simulation_environment_create_params.SimulationEnvironmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentCreateResponse,
        )

    async def update(
        self,
        environment_id: str,
        *,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        background_noise_volume: float | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentUpdateResponse:
        """Updates one of the project's environments.

        Only the fields sent are changed.
        Runs already built keep the snapshot they were built with. Roark-curated
        environments cannot be edited (403).

        Args:
          background_noise: The noise bed played underneath the simulated caller. NONE plays nothing.

          background_noise_volume: How loud the bed plays, as a gain from 0 (silent) to 1 (as loud as the caller).
              Defaults to 0.1, which sits well under the caller. Ignored on Vapi endpoints,
              which have no level control.

          description: Optional note on when to use this environment

          name: Display name, shown wherever a flow variant references the environment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return await self._put(
            f"/v1/simulation/environment/{environment_id}",
            body=await async_maybe_transform(
                {
                    "background_noise": background_noise,
                    "background_noise_volume": background_noise_volume,
                    "description": description,
                    "name": name,
                },
                simulation_environment_update_params.SimulationEnvironmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentUpdateResponse,
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
    ) -> SimulationEnvironmentListResponse:
        """
        Returns a paginated list of environments: the project's own plus the
        environments Roark curates and shares across every project. Reference one by id
        when setting a customer flow variant's environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/environment",
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
                    simulation_environment_list_params.SimulationEnvironmentListParams,
                ),
            ),
            cast_to=SimulationEnvironmentListResponse,
        )

    async def delete(
        self,
        environment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentDeleteResponse:
        """Soft-deletes one of the project's environments.

        It disappears from reads and
        cannot be picked for new runs; runs already built keep their snapshot. Refused
        (409) while a live customer flow variant still uses it: move those variants
        first. Roark-curated environments cannot be deleted (403).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return await self._delete(
            f"/v1/simulation/environment/{environment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentDeleteResponse,
        )

    async def get_by_id(
        self,
        environment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationEnvironmentGetByIDResponse:
        """
        Returns a single environment by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return await self._get(
            f"/v1/simulation/environment/{environment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationEnvironmentGetByIDResponse,
        )


class SimulationEnvironmentResourceWithRawResponse:
    def __init__(self, simulation_environment: SimulationEnvironmentResource) -> None:
        self._simulation_environment = simulation_environment

        self.create = to_raw_response_wrapper(
            simulation_environment.create,
        )
        self.update = to_raw_response_wrapper(
            simulation_environment.update,
        )
        self.list = to_raw_response_wrapper(
            simulation_environment.list,
        )
        self.delete = to_raw_response_wrapper(
            simulation_environment.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_environment.get_by_id,
        )


class AsyncSimulationEnvironmentResourceWithRawResponse:
    def __init__(self, simulation_environment: AsyncSimulationEnvironmentResource) -> None:
        self._simulation_environment = simulation_environment

        self.create = async_to_raw_response_wrapper(
            simulation_environment.create,
        )
        self.update = async_to_raw_response_wrapper(
            simulation_environment.update,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_environment.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simulation_environment.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_environment.get_by_id,
        )


class SimulationEnvironmentResourceWithStreamingResponse:
    def __init__(self, simulation_environment: SimulationEnvironmentResource) -> None:
        self._simulation_environment = simulation_environment

        self.create = to_streamed_response_wrapper(
            simulation_environment.create,
        )
        self.update = to_streamed_response_wrapper(
            simulation_environment.update,
        )
        self.list = to_streamed_response_wrapper(
            simulation_environment.list,
        )
        self.delete = to_streamed_response_wrapper(
            simulation_environment.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_environment.get_by_id,
        )


class AsyncSimulationEnvironmentResourceWithStreamingResponse:
    def __init__(self, simulation_environment: AsyncSimulationEnvironmentResource) -> None:
        self._simulation_environment = simulation_environment

        self.create = async_to_streamed_response_wrapper(
            simulation_environment.create,
        )
        self.update = async_to_streamed_response_wrapper(
            simulation_environment.update,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_environment.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simulation_environment.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_environment.get_by_id,
        )
