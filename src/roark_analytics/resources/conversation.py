# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import conversation_list_params
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
from ..types.conversation_list_response import ConversationListResponse
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

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        modality: Literal["voice", "chat", "call"] | Omit = omit,
        started_from: str | Omit = omit,
        started_to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """Calls and chats in the project as one list, most recent start first.

        A
        conversation is listed once it is recorded: a call when it connects, a chat when
        it ends. Listing calls needs `call:read`, chats `chat:read`, and both kinds
        both.

        Args:
          after: The `nextCursor` of the previous page.

          limit: How many to return (default 20, max 100).

          modality: Only `voice`, or only `chat`. Both by default.

          started_from: Only conversations that started at or after this time.

          started_to: Only conversations that started at or before this time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/conversation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "modality": modality,
                        "started_from": started_from,
                        "started_to": started_to,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

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
        """A call or chat by its id, whichever it is.

        One started through `POST
        /v1/agent/{agentId}/conversations` reads back from the moment it is created,
        before it is recorded. For its transcript and metrics, read it as a call or
        chat, as `modality` says.

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

    async def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        modality: Literal["voice", "chat", "call"] | Omit = omit,
        started_from: str | Omit = omit,
        started_to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """Calls and chats in the project as one list, most recent start first.

        A
        conversation is listed once it is recorded: a call when it connects, a chat when
        it ends. Listing calls needs `call:read`, chats `chat:read`, and both kinds
        both.

        Args:
          after: The `nextCursor` of the previous page.

          limit: How many to return (default 20, max 100).

          modality: Only `voice`, or only `chat`. Both by default.

          started_from: Only conversations that started at or after this time.

          started_to: Only conversations that started at or before this time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/conversation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "modality": modality,
                        "started_from": started_from,
                        "started_to": started_to,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

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
        """A call or chat by its id, whichever it is.

        One started through `POST
        /v1/agent/{agentId}/conversations` reads back from the moment it is created,
        before it is recorded. For its transcript and metrics, read it as a call or
        chat, as `modality` says.

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

        self.list = to_raw_response_wrapper(
            conversation.list,
        )
        self.get_by_id = to_raw_response_wrapper(
            conversation.get_by_id,
        )


class AsyncConversationResourceWithRawResponse:
    def __init__(self, conversation: AsyncConversationResource) -> None:
        self._conversation = conversation

        self.list = async_to_raw_response_wrapper(
            conversation.list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            conversation.get_by_id,
        )


class ConversationResourceWithStreamingResponse:
    def __init__(self, conversation: ConversationResource) -> None:
        self._conversation = conversation

        self.list = to_streamed_response_wrapper(
            conversation.list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            conversation.get_by_id,
        )


class AsyncConversationResourceWithStreamingResponse:
    def __init__(self, conversation: AsyncConversationResource) -> None:
        self._conversation = conversation

        self.list = async_to_streamed_response_wrapper(
            conversation.list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            conversation.get_by_id,
        )
