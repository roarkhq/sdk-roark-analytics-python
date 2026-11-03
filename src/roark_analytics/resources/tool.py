# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import tool_list_params, tool_create_params, tool_update_params
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
from ..types.tool_list_response import ToolListResponse
from ..types.tool_create_response import ToolCreateResponse
from ..types.tool_delete_response import ToolDeleteResponse
from ..types.tool_update_response import ToolUpdateResponse
from ..types.tool_get_by_id_response import ToolGetByIDResponse

__all__ = ["ToolResource", "AsyncToolResource"]


class ToolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return ToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return ToolResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        agent_id: Optional[str] | Omit = omit,
        expected_result: Optional[str] | Omit = omit,
        inputs: Iterable[tool_create_params.Input] | Omit = omit,
        invocation_criteria: Optional[str] | Omit = omit,
        runtime: Optional[tool_create_params.Runtime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateResponse:
        """Creates a tool and declares its first version.

        A tool only recorded from calls
        under the same name is adopted; one already declared returns 409. Give it a
        `runtime` for a hosted agent to call your endpoint. Header values are returned
        on read, so keep secrets out of them.

        Args:
          description: When the agent should use the tool

          runtime: Omit or null for a tool that is only graded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tool",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "agent_id": agent_id,
                    "expected_result": expected_result,
                    "inputs": inputs,
                    "invocation_criteria": invocation_criteria,
                    "runtime": runtime,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCreateResponse,
        )

    def update(
        self,
        tool_id: str,
        *,
        description: str,
        name: str,
        agent_id: Optional[str] | Omit = omit,
        expected_result: Optional[str] | Omit = omit,
        inputs: Iterable[tool_update_params.Input] | Omit = omit,
        invocation_criteria: Optional[str] | Omit = omit,
        runtime: Optional[tool_update_params.Runtime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolUpdateResponse:
        """
        Replaces the tool: its name, scope, inputs, description, grading hints and
        runtime. A field left out is cleared, so omitting agentId makes the tool
        project-wide. A change declares a new version; agent versions pinned to an older
        one keep it.

        Args:
          description: When the agent should use the tool

          runtime: Omit or null for a tool that is only graded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._put(
            f"/v1/tool/{tool_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "agent_id": agent_id,
                    "expected_result": expected_result,
                    "inputs": inputs,
                    "invocation_criteria": invocation_criteria,
                    "runtime": runtime,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolUpdateResponse,
        )

    def list(
        self,
        *,
        agent_id: str | Omit = omit,
        include_built_in: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        The project's tools and the built-in ones, each with its latest version: inputs,
        description and, for a tool a hosted agent runs, its request. Attach one to an
        agent draft by id.

        Args:
          agent_id: Only tools scoped to this agent

          include_built_in: Include the built-in tools (default true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "include_built_in": include_built_in,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    def delete(
        self,
        tool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolDeleteResponse:
        """Deletes a tool no agent version uses.

        A tool an agent version uses returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._delete(
            f"/v1/tool/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolDeleteResponse,
        )

    def get_by_id(
        self,
        tool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolGetByIDResponse:
        """
        Get a tool

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._get(
            f"/v1/tool/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGetByIDResponse,
        )


class AsyncToolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncToolResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        agent_id: Optional[str] | Omit = omit,
        expected_result: Optional[str] | Omit = omit,
        inputs: Iterable[tool_create_params.Input] | Omit = omit,
        invocation_criteria: Optional[str] | Omit = omit,
        runtime: Optional[tool_create_params.Runtime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateResponse:
        """Creates a tool and declares its first version.

        A tool only recorded from calls
        under the same name is adopted; one already declared returns 409. Give it a
        `runtime` for a hosted agent to call your endpoint. Header values are returned
        on read, so keep secrets out of them.

        Args:
          description: When the agent should use the tool

          runtime: Omit or null for a tool that is only graded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tool",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "agent_id": agent_id,
                    "expected_result": expected_result,
                    "inputs": inputs,
                    "invocation_criteria": invocation_criteria,
                    "runtime": runtime,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCreateResponse,
        )

    async def update(
        self,
        tool_id: str,
        *,
        description: str,
        name: str,
        agent_id: Optional[str] | Omit = omit,
        expected_result: Optional[str] | Omit = omit,
        inputs: Iterable[tool_update_params.Input] | Omit = omit,
        invocation_criteria: Optional[str] | Omit = omit,
        runtime: Optional[tool_update_params.Runtime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolUpdateResponse:
        """
        Replaces the tool: its name, scope, inputs, description, grading hints and
        runtime. A field left out is cleared, so omitting agentId makes the tool
        project-wide. A change declares a new version; agent versions pinned to an older
        one keep it.

        Args:
          description: When the agent should use the tool

          runtime: Omit or null for a tool that is only graded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._put(
            f"/v1/tool/{tool_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "agent_id": agent_id,
                    "expected_result": expected_result,
                    "inputs": inputs,
                    "invocation_criteria": invocation_criteria,
                    "runtime": runtime,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolUpdateResponse,
        )

    async def list(
        self,
        *,
        agent_id: str | Omit = omit,
        include_built_in: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        The project's tools and the built-in ones, each with its latest version: inputs,
        description and, for a tool a hosted agent runs, its request. Attach one to an
        agent draft by id.

        Args:
          agent_id: Only tools scoped to this agent

          include_built_in: Include the built-in tools (default true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "include_built_in": include_built_in,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    async def delete(
        self,
        tool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolDeleteResponse:
        """Deletes a tool no agent version uses.

        A tool an agent version uses returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._delete(
            f"/v1/tool/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolDeleteResponse,
        )

    async def get_by_id(
        self,
        tool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolGetByIDResponse:
        """
        Get a tool

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._get(
            f"/v1/tool/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGetByIDResponse,
        )


class ToolResourceWithRawResponse:
    def __init__(self, tool: ToolResource) -> None:
        self._tool = tool

        self.create = to_raw_response_wrapper(
            tool.create,
        )
        self.update = to_raw_response_wrapper(
            tool.update,
        )
        self.list = to_raw_response_wrapper(
            tool.list,
        )
        self.delete = to_raw_response_wrapper(
            tool.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            tool.get_by_id,
        )


class AsyncToolResourceWithRawResponse:
    def __init__(self, tool: AsyncToolResource) -> None:
        self._tool = tool

        self.create = async_to_raw_response_wrapper(
            tool.create,
        )
        self.update = async_to_raw_response_wrapper(
            tool.update,
        )
        self.list = async_to_raw_response_wrapper(
            tool.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tool.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            tool.get_by_id,
        )


class ToolResourceWithStreamingResponse:
    def __init__(self, tool: ToolResource) -> None:
        self._tool = tool

        self.create = to_streamed_response_wrapper(
            tool.create,
        )
        self.update = to_streamed_response_wrapper(
            tool.update,
        )
        self.list = to_streamed_response_wrapper(
            tool.list,
        )
        self.delete = to_streamed_response_wrapper(
            tool.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            tool.get_by_id,
        )


class AsyncToolResourceWithStreamingResponse:
    def __init__(self, tool: AsyncToolResource) -> None:
        self._tool = tool

        self.create = async_to_streamed_response_wrapper(
            tool.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tool.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tool.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tool.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            tool.get_by_id,
        )
