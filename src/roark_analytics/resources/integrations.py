# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import integration_create_vapi_call_params, integration_create_retell_call_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.integration_create_vapi_call_response import IntegrationCreateVapiCallResponse
from ..types.integration_create_retell_call_response import IntegrationCreateRetellCallResponse

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return IntegrationsResourceWithStreamingResponse(self)

    def create_retell_call(
        self,
        *,
        retell_call_ended_payload: Dict[str, object],
        properties: Dict[str, object] | NotGiven = NOT_GIVEN,
        skip_already_imported: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationCreateRetellCallResponse:
        """
        Process and upload a Retell call to Roark evaluation

        Args:
          retell_call_ended_payload: Raw Retell data forwarded directly from the Retell call_ended webhook

          properties: Optional metadata (key-value pairs) to include with the call. Useful for
              filtering and display in call details.

          skip_already_imported: Skip already imported Retell calls with the same Retell call id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/retell/call",
            body=maybe_transform(
                {
                    "retell_call_ended_payload": retell_call_ended_payload,
                    "properties": properties,
                    "skip_already_imported": skip_already_imported,
                },
                integration_create_retell_call_params.IntegrationCreateRetellCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreateRetellCallResponse,
        )

    def create_vapi_call(
        self,
        *,
        vapi_end_of_call_report_payload: Dict[str, object],
        properties: Dict[str, object] | NotGiven = NOT_GIVEN,
        skip_already_imported: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationCreateVapiCallResponse:
        """
        Process and upload a VAPI call to Roark evaluation

        Args:
          vapi_end_of_call_report_payload: Raw Vapi data forwarded directly from the Vapi end-of-call-report webhook

          properties: Optional metadata (key-value pairs) to include with the call. Useful for
              filtering and display in call details.

          skip_already_imported: Skip already imported Vapi calls with the same Vapi call id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vapi/call",
            body=maybe_transform(
                {
                    "vapi_end_of_call_report_payload": vapi_end_of_call_report_payload,
                    "properties": properties,
                    "skip_already_imported": skip_already_imported,
                },
                integration_create_vapi_call_params.IntegrationCreateVapiCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreateVapiCallResponse,
        )


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def create_retell_call(
        self,
        *,
        retell_call_ended_payload: Dict[str, object],
        properties: Dict[str, object] | NotGiven = NOT_GIVEN,
        skip_already_imported: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationCreateRetellCallResponse:
        """
        Process and upload a Retell call to Roark evaluation

        Args:
          retell_call_ended_payload: Raw Retell data forwarded directly from the Retell call_ended webhook

          properties: Optional metadata (key-value pairs) to include with the call. Useful for
              filtering and display in call details.

          skip_already_imported: Skip already imported Retell calls with the same Retell call id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/retell/call",
            body=await async_maybe_transform(
                {
                    "retell_call_ended_payload": retell_call_ended_payload,
                    "properties": properties,
                    "skip_already_imported": skip_already_imported,
                },
                integration_create_retell_call_params.IntegrationCreateRetellCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreateRetellCallResponse,
        )

    async def create_vapi_call(
        self,
        *,
        vapi_end_of_call_report_payload: Dict[str, object],
        properties: Dict[str, object] | NotGiven = NOT_GIVEN,
        skip_already_imported: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationCreateVapiCallResponse:
        """
        Process and upload a VAPI call to Roark evaluation

        Args:
          vapi_end_of_call_report_payload: Raw Vapi data forwarded directly from the Vapi end-of-call-report webhook

          properties: Optional metadata (key-value pairs) to include with the call. Useful for
              filtering and display in call details.

          skip_already_imported: Skip already imported Vapi calls with the same Vapi call id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vapi/call",
            body=await async_maybe_transform(
                {
                    "vapi_end_of_call_report_payload": vapi_end_of_call_report_payload,
                    "properties": properties,
                    "skip_already_imported": skip_already_imported,
                },
                integration_create_vapi_call_params.IntegrationCreateVapiCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreateVapiCallResponse,
        )


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.create_retell_call = to_raw_response_wrapper(
            integrations.create_retell_call,
        )
        self.create_vapi_call = to_raw_response_wrapper(
            integrations.create_vapi_call,
        )


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.create_retell_call = async_to_raw_response_wrapper(
            integrations.create_retell_call,
        )
        self.create_vapi_call = async_to_raw_response_wrapper(
            integrations.create_vapi_call,
        )


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.create_retell_call = to_streamed_response_wrapper(
            integrations.create_retell_call,
        )
        self.create_vapi_call = to_streamed_response_wrapper(
            integrations.create_vapi_call,
        )


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.create_retell_call = async_to_streamed_response_wrapper(
            integrations.create_retell_call,
        )
        self.create_vapi_call = async_to_streamed_response_wrapper(
            integrations.create_vapi_call,
        )
