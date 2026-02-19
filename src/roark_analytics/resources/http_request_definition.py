# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    http_request_definition_list_params,
    http_request_definition_create_params,
    http_request_definition_update_params,
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
from ..types.http_request_definition_list_response import HTTPRequestDefinitionListResponse
from ..types.http_request_definition_create_response import HTTPRequestDefinitionCreateResponse
from ..types.http_request_definition_update_response import HTTPRequestDefinitionUpdateResponse
from ..types.http_request_definition_get_by_id_response import HTTPRequestDefinitionGetByIDResponse

__all__ = ["HTTPRequestDefinitionResource", "AsyncHTTPRequestDefinitionResource"]


class HTTPRequestDefinitionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTTPRequestDefinitionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return HTTPRequestDefinitionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTPRequestDefinitionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return HTTPRequestDefinitionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        scope: Literal["AGENT_OUTBOUND_DIAL"],
        url: str,
        body: Union[str, Dict[str, object], None] | Omit = omit,
        description: Optional[str] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        method: Literal["POST", "PUT", "PATCH", "GET"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPRequestDefinitionCreateResponse:
        """Creates a new HTTP request definition.

        The signing secret is only returned in
        this response and cannot be retrieved later.

        Args:
          scope: Scope: AGENT_OUTBOUND_DIAL

          url: URL for the HTTP request

          body: Request body template. Accepts a JSON object or a string with placeholders like
              {{phoneNumberToDial}}. Objects are serialized to JSON for storage.

          description: Description of the HTTP request definition

          headers: Request headers as key-value pairs

          method: HTTP method (default: POST)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/http-request-definition",
            body=maybe_transform(
                {
                    "scope": scope,
                    "url": url,
                    "body": body,
                    "description": description,
                    "headers": headers,
                    "method": method,
                },
                http_request_definition_create_params.HTTPRequestDefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPRequestDefinitionCreateResponse,
        )

    def update(
        self,
        definition_id: str,
        *,
        body: Union[str, Dict[str, object], None] | Omit = omit,
        description: Optional[str] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        method: Literal["POST", "PUT", "PATCH", "GET"] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPRequestDefinitionUpdateResponse:
        """
        Updates an existing HTTP request definition.

        Args:
          body: Request body template. Accepts a JSON object or a string with placeholders like
              {{phoneNumberToDial}}. Objects are serialized to JSON for storage.

          description: Description of the HTTP request definition

          headers: Request headers as key-value pairs

          method: HTTP method: POST, PUT, PATCH, or GET

          url: URL for the HTTP request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._put(
            f"/v1/http-request-definition/{definition_id}",
            body=maybe_transform(
                {
                    "body": body,
                    "description": description,
                    "headers": headers,
                    "method": method,
                    "url": url,
                },
                http_request_definition_update_params.HTTPRequestDefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPRequestDefinitionUpdateResponse,
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
    ) -> HTTPRequestDefinitionListResponse:
        """
        Returns a paginated list of HTTP request definitions for the authenticated
        project.

        Args:
          after: Cursor for pagination - definition ID to start after

          limit: Maximum number of definitions to return (default: 20, max: 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/http-request-definition",
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
                    http_request_definition_list_params.HTTPRequestDefinitionListParams,
                ),
            ),
            cast_to=HTTPRequestDefinitionListResponse,
        )

    def get_by_id(
        self,
        definition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPRequestDefinitionGetByIDResponse:
        """
        Returns a specific HTTP request definition by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._get(
            f"/v1/http-request-definition/{definition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPRequestDefinitionGetByIDResponse,
        )


class AsyncHTTPRequestDefinitionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTTPRequestDefinitionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHTTPRequestDefinitionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTPRequestDefinitionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncHTTPRequestDefinitionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        scope: Literal["AGENT_OUTBOUND_DIAL"],
        url: str,
        body: Union[str, Dict[str, object], None] | Omit = omit,
        description: Optional[str] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        method: Literal["POST", "PUT", "PATCH", "GET"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPRequestDefinitionCreateResponse:
        """Creates a new HTTP request definition.

        The signing secret is only returned in
        this response and cannot be retrieved later.

        Args:
          scope: Scope: AGENT_OUTBOUND_DIAL

          url: URL for the HTTP request

          body: Request body template. Accepts a JSON object or a string with placeholders like
              {{phoneNumberToDial}}. Objects are serialized to JSON for storage.

          description: Description of the HTTP request definition

          headers: Request headers as key-value pairs

          method: HTTP method (default: POST)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/http-request-definition",
            body=await async_maybe_transform(
                {
                    "scope": scope,
                    "url": url,
                    "body": body,
                    "description": description,
                    "headers": headers,
                    "method": method,
                },
                http_request_definition_create_params.HTTPRequestDefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPRequestDefinitionCreateResponse,
        )

    async def update(
        self,
        definition_id: str,
        *,
        body: Union[str, Dict[str, object], None] | Omit = omit,
        description: Optional[str] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        method: Literal["POST", "PUT", "PATCH", "GET"] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPRequestDefinitionUpdateResponse:
        """
        Updates an existing HTTP request definition.

        Args:
          body: Request body template. Accepts a JSON object or a string with placeholders like
              {{phoneNumberToDial}}. Objects are serialized to JSON for storage.

          description: Description of the HTTP request definition

          headers: Request headers as key-value pairs

          method: HTTP method: POST, PUT, PATCH, or GET

          url: URL for the HTTP request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return await self._put(
            f"/v1/http-request-definition/{definition_id}",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "description": description,
                    "headers": headers,
                    "method": method,
                    "url": url,
                },
                http_request_definition_update_params.HTTPRequestDefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPRequestDefinitionUpdateResponse,
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
    ) -> HTTPRequestDefinitionListResponse:
        """
        Returns a paginated list of HTTP request definitions for the authenticated
        project.

        Args:
          after: Cursor for pagination - definition ID to start after

          limit: Maximum number of definitions to return (default: 20, max: 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/http-request-definition",
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
                    http_request_definition_list_params.HTTPRequestDefinitionListParams,
                ),
            ),
            cast_to=HTTPRequestDefinitionListResponse,
        )

    async def get_by_id(
        self,
        definition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPRequestDefinitionGetByIDResponse:
        """
        Returns a specific HTTP request definition by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return await self._get(
            f"/v1/http-request-definition/{definition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPRequestDefinitionGetByIDResponse,
        )


class HTTPRequestDefinitionResourceWithRawResponse:
    def __init__(self, http_request_definition: HTTPRequestDefinitionResource) -> None:
        self._http_request_definition = http_request_definition

        self.create = to_raw_response_wrapper(
            http_request_definition.create,
        )
        self.update = to_raw_response_wrapper(
            http_request_definition.update,
        )
        self.list = to_raw_response_wrapper(
            http_request_definition.list,
        )
        self.get_by_id = to_raw_response_wrapper(
            http_request_definition.get_by_id,
        )


class AsyncHTTPRequestDefinitionResourceWithRawResponse:
    def __init__(self, http_request_definition: AsyncHTTPRequestDefinitionResource) -> None:
        self._http_request_definition = http_request_definition

        self.create = async_to_raw_response_wrapper(
            http_request_definition.create,
        )
        self.update = async_to_raw_response_wrapper(
            http_request_definition.update,
        )
        self.list = async_to_raw_response_wrapper(
            http_request_definition.list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            http_request_definition.get_by_id,
        )


class HTTPRequestDefinitionResourceWithStreamingResponse:
    def __init__(self, http_request_definition: HTTPRequestDefinitionResource) -> None:
        self._http_request_definition = http_request_definition

        self.create = to_streamed_response_wrapper(
            http_request_definition.create,
        )
        self.update = to_streamed_response_wrapper(
            http_request_definition.update,
        )
        self.list = to_streamed_response_wrapper(
            http_request_definition.list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            http_request_definition.get_by_id,
        )


class AsyncHTTPRequestDefinitionResourceWithStreamingResponse:
    def __init__(self, http_request_definition: AsyncHTTPRequestDefinitionResource) -> None:
        self._http_request_definition = http_request_definition

        self.create = async_to_streamed_response_wrapper(
            http_request_definition.create,
        )
        self.update = async_to_streamed_response_wrapper(
            http_request_definition.update,
        )
        self.list = async_to_streamed_response_wrapper(
            http_request_definition.list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            http_request_definition.get_by_id,
        )
