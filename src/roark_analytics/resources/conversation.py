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
from ..types.conversation_get_by_id_response import ConversationGetByIDResponse

__all__ = ["ConversationResource", "AsyncConversationResource"]


class ConversationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return ConversationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return ConversationResourceWithStreamingResponse(self)

    def get_by_id(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationGetByIDResponse:
        """Fetches one conversation by its id, whether it is a call or a chat.

        The same
        endpoint reads both modalities, and `modality` in the response says which one it
        is, so you do not need to know it up front. A conversation started with `POST
        /v1/agent/{agentId}/conversations` reads back from the moment it is created,
        before it is recorded as a call or chat. For its transcript and metrics, use the
        call or chat endpoints that match its `modality`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            f"/v1/conversation/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationGetByIDResponse,
        )


class AsyncConversationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncConversationResourceWithStreamingResponse(self)

    async def get_by_id(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationGetByIDResponse:
        """Fetches one conversation by its id, whether it is a call or a chat.

        The same
        endpoint reads both modalities, and `modality` in the response says which one it
        is, so you do not need to know it up front. A conversation started with `POST
        /v1/agent/{agentId}/conversations` reads back from the moment it is created,
        before it is recorded as a call or chat. For its transcript and metrics, use the
        call or chat endpoints that match its `modality`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            f"/v1/conversation/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationGetByIDResponse,
        )


class ConversationResourceWithRawResponse:
    def __init__(self, conversation: ConversationResource) -> None:
        self._conversation = conversation

        self.get_by_id = to_raw_response_wrapper(
            conversation.get_by_id,
        )


class AsyncConversationResourceWithRawResponse:
    def __init__(self, conversation: AsyncConversationResource) -> None:
        self._conversation = conversation

        self.get_by_id = async_to_raw_response_wrapper(
            conversation.get_by_id,
        )


class ConversationResourceWithStreamingResponse:
    def __init__(self, conversation: ConversationResource) -> None:
        self._conversation = conversation

        self.get_by_id = to_streamed_response_wrapper(
            conversation.get_by_id,
        )


class AsyncConversationResourceWithStreamingResponse:
    def __init__(self, conversation: AsyncConversationResource) -> None:
        self._conversation = conversation

        self.get_by_id = async_to_streamed_response_wrapper(
            conversation.get_by_id,
        )
