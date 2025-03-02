# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import call_analysis_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.call_analysis_create_response import CallAnalysisCreateResponse
from ..types.call_analysis_retrieve_response import CallAnalysisRetrieveResponse

__all__ = ["CallAnalysisResource", "AsyncCallAnalysisResource"]


class CallAnalysisResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallAnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return CallAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallAnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return CallAnalysisResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        call_direction: Literal["INBOUND", "OUTBOUND"],
        interface_type: Literal["PHONE", "WEB"],
        participants: Iterable[call_analysis_create_params.Participant],
        recording_url: str,
        started_at: str,
        ended_reason: str | NotGiven = NOT_GIVEN,
        is_test: bool | NotGiven = NOT_GIVEN,
        stereo_recording_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallAnalysisCreateResponse:
        """
        Upload a new call recording

        Args:
          call_direction: Direction of the call (INBOUND or OUTBOUND)

          interface_type: Interface type of the call (PHONE or WEB)

          participants: Exactly two participants in the call

          recording_url: URL of source recording (must be an accessible WAV file). Can be a signed URL.

          started_at: When the call started (ISO 8601 format)

          ended_reason: Reason why the call ended (optional)

          is_test: Whether this is a test call

          stereo_recording_url: URL of source stereo recording in WAV format. Must be accessible. Can be a
              signed URL. While optional it allows for a richer audio player

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/call-analysis",
            body=maybe_transform(
                {
                    "call_direction": call_direction,
                    "interface_type": interface_type,
                    "participants": participants,
                    "recording_url": recording_url,
                    "started_at": started_at,
                    "ended_reason": ended_reason,
                    "is_test": is_test,
                    "stereo_recording_url": stereo_recording_url,
                },
                call_analysis_create_params.CallAnalysisCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallAnalysisCreateResponse,
        )

    def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallAnalysisRetrieveResponse:
        """
        Fetch a call analysis job by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/call-analysis/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallAnalysisRetrieveResponse,
        )


class AsyncCallAnalysisResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallAnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallAnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncCallAnalysisResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        call_direction: Literal["INBOUND", "OUTBOUND"],
        interface_type: Literal["PHONE", "WEB"],
        participants: Iterable[call_analysis_create_params.Participant],
        recording_url: str,
        started_at: str,
        ended_reason: str | NotGiven = NOT_GIVEN,
        is_test: bool | NotGiven = NOT_GIVEN,
        stereo_recording_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallAnalysisCreateResponse:
        """
        Upload a new call recording

        Args:
          call_direction: Direction of the call (INBOUND or OUTBOUND)

          interface_type: Interface type of the call (PHONE or WEB)

          participants: Exactly two participants in the call

          recording_url: URL of source recording (must be an accessible WAV file). Can be a signed URL.

          started_at: When the call started (ISO 8601 format)

          ended_reason: Reason why the call ended (optional)

          is_test: Whether this is a test call

          stereo_recording_url: URL of source stereo recording in WAV format. Must be accessible. Can be a
              signed URL. While optional it allows for a richer audio player

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/call-analysis",
            body=await async_maybe_transform(
                {
                    "call_direction": call_direction,
                    "interface_type": interface_type,
                    "participants": participants,
                    "recording_url": recording_url,
                    "started_at": started_at,
                    "ended_reason": ended_reason,
                    "is_test": is_test,
                    "stereo_recording_url": stereo_recording_url,
                },
                call_analysis_create_params.CallAnalysisCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallAnalysisCreateResponse,
        )

    async def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallAnalysisRetrieveResponse:
        """
        Fetch a call analysis job by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/call-analysis/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallAnalysisRetrieveResponse,
        )


class CallAnalysisResourceWithRawResponse:
    def __init__(self, call_analysis: CallAnalysisResource) -> None:
        self._call_analysis = call_analysis

        self.create = to_raw_response_wrapper(
            call_analysis.create,
        )
        self.retrieve = to_raw_response_wrapper(
            call_analysis.retrieve,
        )


class AsyncCallAnalysisResourceWithRawResponse:
    def __init__(self, call_analysis: AsyncCallAnalysisResource) -> None:
        self._call_analysis = call_analysis

        self.create = async_to_raw_response_wrapper(
            call_analysis.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            call_analysis.retrieve,
        )


class CallAnalysisResourceWithStreamingResponse:
    def __init__(self, call_analysis: CallAnalysisResource) -> None:
        self._call_analysis = call_analysis

        self.create = to_streamed_response_wrapper(
            call_analysis.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            call_analysis.retrieve,
        )


class AsyncCallAnalysisResourceWithStreamingResponse:
    def __init__(self, call_analysis: AsyncCallAnalysisResource) -> None:
        self._call_analysis = call_analysis

        self.create = async_to_streamed_response_wrapper(
            call_analysis.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            call_analysis.retrieve,
        )
