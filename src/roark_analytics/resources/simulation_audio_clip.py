# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.simulation_audio_clip_list_response import SimulationAudioClipListResponse

__all__ = ["SimulationAudioClipResource", "AsyncSimulationAudioClipResource"]


class SimulationAudioClipResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationAudioClipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationAudioClipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationAudioClipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationAudioClipResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationAudioClipListResponse:
        """
        Returns the audio a CUSTOMER_AUDIO step can play: hold music, hold tones and
        ringback. Name one as the step's `audioClip`. A fixed catalogue, so it is not
        paginated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/audio-clip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationAudioClipListResponse,
        )


class AsyncSimulationAudioClipResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationAudioClipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationAudioClipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationAudioClipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationAudioClipResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationAudioClipListResponse:
        """
        Returns the audio a CUSTOMER_AUDIO step can play: hold music, hold tones and
        ringback. Name one as the step's `audioClip`. A fixed catalogue, so it is not
        paginated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/audio-clip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationAudioClipListResponse,
        )


class SimulationAudioClipResourceWithRawResponse:
    def __init__(self, simulation_audio_clip: SimulationAudioClipResource) -> None:
        self._simulation_audio_clip = simulation_audio_clip

        self.list = to_raw_response_wrapper(
            simulation_audio_clip.list,
        )


class AsyncSimulationAudioClipResourceWithRawResponse:
    def __init__(self, simulation_audio_clip: AsyncSimulationAudioClipResource) -> None:
        self._simulation_audio_clip = simulation_audio_clip

        self.list = async_to_raw_response_wrapper(
            simulation_audio_clip.list,
        )


class SimulationAudioClipResourceWithStreamingResponse:
    def __init__(self, simulation_audio_clip: SimulationAudioClipResource) -> None:
        self._simulation_audio_clip = simulation_audio_clip

        self.list = to_streamed_response_wrapper(
            simulation_audio_clip.list,
        )


class AsyncSimulationAudioClipResourceWithStreamingResponse:
    def __init__(self, simulation_audio_clip: AsyncSimulationAudioClipResource) -> None:
        self._simulation_audio_clip = simulation_audio_clip

        self.list = async_to_streamed_response_wrapper(
            simulation_audio_clip.list,
        )
