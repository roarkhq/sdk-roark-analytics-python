# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal

import httpx

from ..types import mcp_server_create_params, mcp_server_update_params, mcp_server_discover_params
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
from ..types.mcp_server_list_response import McpServerListResponse
from ..types.mcp_server_create_response import McpServerCreateResponse
from ..types.mcp_server_delete_response import McpServerDeleteResponse
from ..types.mcp_server_update_response import McpServerUpdateResponse
from ..types.mcp_server_refresh_response import McpServerRefreshResponse
from ..types.mcp_server_discover_response import McpServerDiscoverResponse
from ..types.mcp_server_get_by_id_response import McpServerGetByIDResponse

__all__ = ["McpServerResource", "AsyncMcpServerResource"]


class McpServerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> McpServerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return McpServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpServerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return McpServerResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        label: str,
        url: str,
        auth: Dict[str, object] | Omit = omit,
        directory_key: Optional[str] | Omit = omit,
        transport: Literal["STREAMABLE_HTTP", "SSE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """Connects to the server, reads its tools, then stores it for the project.

        A
        server that does not answer, or refuses the credential, returns 400 and nothing
        is stored. The credential is encrypted and never returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connections/mcp-server",
            body=maybe_transform(
                {
                    "label": label,
                    "url": url,
                    "auth": auth,
                    "directory_key": directory_key,
                    "transport": transport,
                },
                mcp_server_create_params.McpServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerCreateResponse,
        )

    def update(
        self,
        server_id: str,
        *,
        auth: Union[
            mcp_server_update_params.AuthUnionMember0,
            mcp_server_update_params.AuthUnionMember1,
            mcp_server_update_params.AuthUnionMember2,
        ]
        | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """Renames the server or replaces its credential.

        A new credential is checked by
        connecting with it first; one the server refuses returns 400 and changes
        nothing.

        Args:
          auth: How the server authenticates. Stored encrypted; never returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._patch(
            f"/v1/connections/mcp-server/{server_id}",
            body=maybe_transform(
                {
                    "auth": auth,
                    "label": label,
                },
                mcp_server_update_params.McpServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerListResponse:
        """
        The project's MCP servers, by label, each with the tools it offered when last
        checked. Credentials are never returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/connections/mcp-server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerListResponse,
        )

    def delete(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerDeleteResponse:
        """Deletes the server and its stored credential.

        A server a tool still uses returns
        409, naming the tools.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._delete(
            f"/v1/connections/mcp-server/{server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerDeleteResponse,
        )

    def discover(
        self,
        *,
        url: str,
        auth: Dict[str, object] | Omit = omit,
        transport: Literal["STREAMABLE_HTTP", "SSE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerDiscoverResponse:
        """
        Connects to a server and returns the tools it offers, without storing anything.
        Use it to check a url and credential before connecting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connections/mcp-server/discover",
            body=maybe_transform(
                {
                    "url": url,
                    "auth": auth,
                    "transport": transport,
                },
                mcp_server_discover_params.McpServerDiscoverParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerDiscoverResponse,
        )

    def get_by_id(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerGetByIDResponse:
        """One MCP server.

        The credential is never returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._get(
            f"/v1/connections/mcp-server/{server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerGetByIDResponse,
        )

    def refresh(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerRefreshResponse:
        """Connects to the server again and records the tools it offers now.

        Agents keep
        calling the tools they were given; a new tool reaches an agent only once you add
        it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._post(
            f"/v1/connections/mcp-server/{server_id}/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerRefreshResponse,
        )


class AsyncMcpServerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMcpServerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpServerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncMcpServerResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        label: str,
        url: str,
        auth: Dict[str, object] | Omit = omit,
        directory_key: Optional[str] | Omit = omit,
        transport: Literal["STREAMABLE_HTTP", "SSE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """Connects to the server, reads its tools, then stores it for the project.

        A
        server that does not answer, or refuses the credential, returns 400 and nothing
        is stored. The credential is encrypted and never returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connections/mcp-server",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "url": url,
                    "auth": auth,
                    "directory_key": directory_key,
                    "transport": transport,
                },
                mcp_server_create_params.McpServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerCreateResponse,
        )

    async def update(
        self,
        server_id: str,
        *,
        auth: Union[
            mcp_server_update_params.AuthUnionMember0,
            mcp_server_update_params.AuthUnionMember1,
            mcp_server_update_params.AuthUnionMember2,
        ]
        | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """Renames the server or replaces its credential.

        A new credential is checked by
        connecting with it first; one the server refuses returns 400 and changes
        nothing.

        Args:
          auth: How the server authenticates. Stored encrypted; never returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._patch(
            f"/v1/connections/mcp-server/{server_id}",
            body=await async_maybe_transform(
                {
                    "auth": auth,
                    "label": label,
                },
                mcp_server_update_params.McpServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerListResponse:
        """
        The project's MCP servers, by label, each with the tools it offered when last
        checked. Credentials are never returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/connections/mcp-server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerListResponse,
        )

    async def delete(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerDeleteResponse:
        """Deletes the server and its stored credential.

        A server a tool still uses returns
        409, naming the tools.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._delete(
            f"/v1/connections/mcp-server/{server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerDeleteResponse,
        )

    async def discover(
        self,
        *,
        url: str,
        auth: Dict[str, object] | Omit = omit,
        transport: Literal["STREAMABLE_HTTP", "SSE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerDiscoverResponse:
        """
        Connects to a server and returns the tools it offers, without storing anything.
        Use it to check a url and credential before connecting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connections/mcp-server/discover",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "auth": auth,
                    "transport": transport,
                },
                mcp_server_discover_params.McpServerDiscoverParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerDiscoverResponse,
        )

    async def get_by_id(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerGetByIDResponse:
        """One MCP server.

        The credential is never returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._get(
            f"/v1/connections/mcp-server/{server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerGetByIDResponse,
        )

    async def refresh(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerRefreshResponse:
        """Connects to the server again and records the tools it offers now.

        Agents keep
        calling the tools they were given; a new tool reaches an agent only once you add
        it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._post(
            f"/v1/connections/mcp-server/{server_id}/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerRefreshResponse,
        )


class McpServerResourceWithRawResponse:
    def __init__(self, mcp_server: McpServerResource) -> None:
        self._mcp_server = mcp_server

        self.create = to_raw_response_wrapper(
            mcp_server.create,
        )
        self.update = to_raw_response_wrapper(
            mcp_server.update,
        )
        self.list = to_raw_response_wrapper(
            mcp_server.list,
        )
        self.delete = to_raw_response_wrapper(
            mcp_server.delete,
        )
        self.discover = to_raw_response_wrapper(
            mcp_server.discover,
        )
        self.get_by_id = to_raw_response_wrapper(
            mcp_server.get_by_id,
        )
        self.refresh = to_raw_response_wrapper(
            mcp_server.refresh,
        )


class AsyncMcpServerResourceWithRawResponse:
    def __init__(self, mcp_server: AsyncMcpServerResource) -> None:
        self._mcp_server = mcp_server

        self.create = async_to_raw_response_wrapper(
            mcp_server.create,
        )
        self.update = async_to_raw_response_wrapper(
            mcp_server.update,
        )
        self.list = async_to_raw_response_wrapper(
            mcp_server.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mcp_server.delete,
        )
        self.discover = async_to_raw_response_wrapper(
            mcp_server.discover,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            mcp_server.get_by_id,
        )
        self.refresh = async_to_raw_response_wrapper(
            mcp_server.refresh,
        )


class McpServerResourceWithStreamingResponse:
    def __init__(self, mcp_server: McpServerResource) -> None:
        self._mcp_server = mcp_server

        self.create = to_streamed_response_wrapper(
            mcp_server.create,
        )
        self.update = to_streamed_response_wrapper(
            mcp_server.update,
        )
        self.list = to_streamed_response_wrapper(
            mcp_server.list,
        )
        self.delete = to_streamed_response_wrapper(
            mcp_server.delete,
        )
        self.discover = to_streamed_response_wrapper(
            mcp_server.discover,
        )
        self.get_by_id = to_streamed_response_wrapper(
            mcp_server.get_by_id,
        )
        self.refresh = to_streamed_response_wrapper(
            mcp_server.refresh,
        )


class AsyncMcpServerResourceWithStreamingResponse:
    def __init__(self, mcp_server: AsyncMcpServerResource) -> None:
        self._mcp_server = mcp_server

        self.create = async_to_streamed_response_wrapper(
            mcp_server.create,
        )
        self.update = async_to_streamed_response_wrapper(
            mcp_server.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mcp_server.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mcp_server.delete,
        )
        self.discover = async_to_streamed_response_wrapper(
            mcp_server.discover,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            mcp_server.get_by_id,
        )
        self.refresh = async_to_streamed_response_wrapper(
            mcp_server.refresh,
        )
