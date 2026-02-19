# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import agent_endpoint_list_params, agent_endpoint_create_params, agent_endpoint_update_params
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
from ..types.agent_endpoint_list_response import AgentEndpointListResponse
from ..types.agent_endpoint_create_response import AgentEndpointCreateResponse
from ..types.agent_endpoint_update_response import AgentEndpointUpdateResponse
from ..types.agent_endpoint_get_by_id_response import AgentEndpointGetByIDResponse

__all__ = ["AgentEndpointResource", "AsyncAgentEndpointResource"]


class AgentEndpointResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentEndpointResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AgentEndpointResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentEndpointResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AgentEndpointResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_id: str,
        direction: Literal["INCOMING", "OUTGOING", "INCOMING_AND_OUTGOING"],
        value: str,
        environment: str | Omit = omit,
        outbound_dial_http_request_definition_id: Optional[str] | Omit = omit,
        outbound_dial_type: Literal["NONE", "HTTP_REQUEST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentEndpointCreateResponse:
        """
        Creates a new agent endpoint for the authenticated project.

        Args:
          agent_id: Agent ID to associate this endpoint with

          direction: Call direction: INCOMING, OUTGOING, or INCOMING_AND_OUTGOING

          value: Phone number in E.164 format (e.g., +12345678900)

          environment: Environment name (default: production)

          outbound_dial_http_request_definition_id: ID of the HTTP request definition for outbound dialing (required when
              outboundDialType is HTTP_REQUEST)

          outbound_dial_type: Outbound dial type: NONE or HTTP_REQUEST (default: NONE)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agent/endpoint",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "direction": direction,
                    "value": value,
                    "environment": environment,
                    "outbound_dial_http_request_definition_id": outbound_dial_http_request_definition_id,
                    "outbound_dial_type": outbound_dial_type,
                },
                agent_endpoint_create_params.AgentEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentEndpointCreateResponse,
        )

    def update(
        self,
        endpoint_id: str,
        *,
        environment: str | Omit = omit,
        outbound_dial_http_request_definition_id: Optional[str] | Omit = omit,
        outbound_dial_type: Literal["NONE", "HTTP_REQUEST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentEndpointUpdateResponse:
        """Updates an existing agent endpoint by its ID.

        Only environment and
        outboundDialType can be modified.

        Args:
          environment: Environment name

          outbound_dial_http_request_definition_id: ID of the HTTP request definition for outbound dialing

          outbound_dial_type: Outbound dial type: NONE or HTTP_REQUEST

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint_id:
            raise ValueError(f"Expected a non-empty value for `endpoint_id` but received {endpoint_id!r}")
        return self._put(
            f"/v1/agent/endpoint/{endpoint_id}",
            body=maybe_transform(
                {
                    "environment": environment,
                    "outbound_dial_http_request_definition_id": outbound_dial_http_request_definition_id,
                    "outbound_dial_type": outbound_dial_type,
                },
                agent_endpoint_update_params.AgentEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentEndpointUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentEndpointListResponse:
        """
        Returns a paginated list of agent endpoints for the authenticated project.

        Args:
          after: Cursor for pagination - endpoint ID to start after

          agent_id: Filter by agent ID

          limit: Maximum number of endpoints to return (default: 20, max: 50)

          search_text: Search text to filter endpoints

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/agent/endpoint",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "limit": limit,
                        "search_text": search_text,
                    },
                    agent_endpoint_list_params.AgentEndpointListParams,
                ),
            ),
            cast_to=AgentEndpointListResponse,
        )

    def get_by_id(
        self,
        endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentEndpointGetByIDResponse:
        """
        Returns a specific agent endpoint by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint_id:
            raise ValueError(f"Expected a non-empty value for `endpoint_id` but received {endpoint_id!r}")
        return self._get(
            f"/v1/agent/endpoint/{endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentEndpointGetByIDResponse,
        )


class AsyncAgentEndpointResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentEndpointResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentEndpointResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentEndpointResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAgentEndpointResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_id: str,
        direction: Literal["INCOMING", "OUTGOING", "INCOMING_AND_OUTGOING"],
        value: str,
        environment: str | Omit = omit,
        outbound_dial_http_request_definition_id: Optional[str] | Omit = omit,
        outbound_dial_type: Literal["NONE", "HTTP_REQUEST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentEndpointCreateResponse:
        """
        Creates a new agent endpoint for the authenticated project.

        Args:
          agent_id: Agent ID to associate this endpoint with

          direction: Call direction: INCOMING, OUTGOING, or INCOMING_AND_OUTGOING

          value: Phone number in E.164 format (e.g., +12345678900)

          environment: Environment name (default: production)

          outbound_dial_http_request_definition_id: ID of the HTTP request definition for outbound dialing (required when
              outboundDialType is HTTP_REQUEST)

          outbound_dial_type: Outbound dial type: NONE or HTTP_REQUEST (default: NONE)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agent/endpoint",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "direction": direction,
                    "value": value,
                    "environment": environment,
                    "outbound_dial_http_request_definition_id": outbound_dial_http_request_definition_id,
                    "outbound_dial_type": outbound_dial_type,
                },
                agent_endpoint_create_params.AgentEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentEndpointCreateResponse,
        )

    async def update(
        self,
        endpoint_id: str,
        *,
        environment: str | Omit = omit,
        outbound_dial_http_request_definition_id: Optional[str] | Omit = omit,
        outbound_dial_type: Literal["NONE", "HTTP_REQUEST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentEndpointUpdateResponse:
        """Updates an existing agent endpoint by its ID.

        Only environment and
        outboundDialType can be modified.

        Args:
          environment: Environment name

          outbound_dial_http_request_definition_id: ID of the HTTP request definition for outbound dialing

          outbound_dial_type: Outbound dial type: NONE or HTTP_REQUEST

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint_id:
            raise ValueError(f"Expected a non-empty value for `endpoint_id` but received {endpoint_id!r}")
        return await self._put(
            f"/v1/agent/endpoint/{endpoint_id}",
            body=await async_maybe_transform(
                {
                    "environment": environment,
                    "outbound_dial_http_request_definition_id": outbound_dial_http_request_definition_id,
                    "outbound_dial_type": outbound_dial_type,
                },
                agent_endpoint_update_params.AgentEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentEndpointUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentEndpointListResponse:
        """
        Returns a paginated list of agent endpoints for the authenticated project.

        Args:
          after: Cursor for pagination - endpoint ID to start after

          agent_id: Filter by agent ID

          limit: Maximum number of endpoints to return (default: 20, max: 50)

          search_text: Search text to filter endpoints

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/agent/endpoint",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "limit": limit,
                        "search_text": search_text,
                    },
                    agent_endpoint_list_params.AgentEndpointListParams,
                ),
            ),
            cast_to=AgentEndpointListResponse,
        )

    async def get_by_id(
        self,
        endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentEndpointGetByIDResponse:
        """
        Returns a specific agent endpoint by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint_id:
            raise ValueError(f"Expected a non-empty value for `endpoint_id` but received {endpoint_id!r}")
        return await self._get(
            f"/v1/agent/endpoint/{endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentEndpointGetByIDResponse,
        )


class AgentEndpointResourceWithRawResponse:
    def __init__(self, agent_endpoint: AgentEndpointResource) -> None:
        self._agent_endpoint = agent_endpoint

        self.create = to_raw_response_wrapper(
            agent_endpoint.create,
        )
        self.update = to_raw_response_wrapper(
            agent_endpoint.update,
        )
        self.list = to_raw_response_wrapper(
            agent_endpoint.list,
        )
        self.get_by_id = to_raw_response_wrapper(
            agent_endpoint.get_by_id,
        )


class AsyncAgentEndpointResourceWithRawResponse:
    def __init__(self, agent_endpoint: AsyncAgentEndpointResource) -> None:
        self._agent_endpoint = agent_endpoint

        self.create = async_to_raw_response_wrapper(
            agent_endpoint.create,
        )
        self.update = async_to_raw_response_wrapper(
            agent_endpoint.update,
        )
        self.list = async_to_raw_response_wrapper(
            agent_endpoint.list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            agent_endpoint.get_by_id,
        )


class AgentEndpointResourceWithStreamingResponse:
    def __init__(self, agent_endpoint: AgentEndpointResource) -> None:
        self._agent_endpoint = agent_endpoint

        self.create = to_streamed_response_wrapper(
            agent_endpoint.create,
        )
        self.update = to_streamed_response_wrapper(
            agent_endpoint.update,
        )
        self.list = to_streamed_response_wrapper(
            agent_endpoint.list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            agent_endpoint.get_by_id,
        )


class AsyncAgentEndpointResourceWithStreamingResponse:
    def __init__(self, agent_endpoint: AsyncAgentEndpointResource) -> None:
        self._agent_endpoint = agent_endpoint

        self.create = async_to_streamed_response_wrapper(
            agent_endpoint.create,
        )
        self.update = async_to_streamed_response_wrapper(
            agent_endpoint.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agent_endpoint.list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            agent_endpoint.get_by_id,
        )
