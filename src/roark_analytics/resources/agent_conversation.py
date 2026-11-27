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
from ..types.agent_conversation_create_response import AgentConversationCreateResponse

__all__ = ["AgentConversationResource", "AsyncAgentConversationResource"]


class AgentConversationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentConversationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AgentConversationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentConversationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AgentConversationResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConversationCreateResponse:
        """
        Starts a voice conversation (`modality: voice`) or chat (`modality: chat`) with
        this Roark-hosted agent and returns its id right away. `channel: web` is a
        conversation in a browser on your site. Call this endpoint from your server,
        never the browser: it needs your API key. Give the page only `web.clientToken`;
        the web SDK spends it to join from one of `allowedOrigins` before
        `web.clientTokenExpiresAt`. Read it back with `GET
        /v1/conversation/{conversationId}` straight away: `PENDING` until the browser
        joins, `IN_PROGRESS`, then `ENDED`. One nobody joins ends without ever starting
        and is never billed. Starting a voice conversation needs `call:create`, a chat
        `chat:create`, and the agent a published version that takes that kind.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agent/{agent_id}/conversations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConversationCreateResponse,
        )


class AsyncAgentConversationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentConversationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentConversationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentConversationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAgentConversationResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConversationCreateResponse:
        """
        Starts a voice conversation (`modality: voice`) or chat (`modality: chat`) with
        this Roark-hosted agent and returns its id right away. `channel: web` is a
        conversation in a browser on your site. Call this endpoint from your server,
        never the browser: it needs your API key. Give the page only `web.clientToken`;
        the web SDK spends it to join from one of `allowedOrigins` before
        `web.clientTokenExpiresAt`. Read it back with `GET
        /v1/conversation/{conversationId}` straight away: `PENDING` until the browser
        joins, `IN_PROGRESS`, then `ENDED`. One nobody joins ends without ever starting
        and is never billed. Starting a voice conversation needs `call:create`, a chat
        `chat:create`, and the agent a published version that takes that kind.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agent/{agent_id}/conversations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConversationCreateResponse,
        )


class AgentConversationResourceWithRawResponse:
    def __init__(self, agent_conversation: AgentConversationResource) -> None:
        self._agent_conversation = agent_conversation

        self.create = to_raw_response_wrapper(
            agent_conversation.create,
        )


class AsyncAgentConversationResourceWithRawResponse:
    def __init__(self, agent_conversation: AsyncAgentConversationResource) -> None:
        self._agent_conversation = agent_conversation

        self.create = async_to_raw_response_wrapper(
            agent_conversation.create,
        )


class AgentConversationResourceWithStreamingResponse:
    def __init__(self, agent_conversation: AgentConversationResource) -> None:
        self._agent_conversation = agent_conversation

        self.create = to_streamed_response_wrapper(
            agent_conversation.create,
        )


class AsyncAgentConversationResourceWithStreamingResponse:
    def __init__(self, agent_conversation: AsyncAgentConversationResource) -> None:
        self._agent_conversation = agent_conversation

        self.create = async_to_streamed_response_wrapper(
            agent_conversation.create,
        )
