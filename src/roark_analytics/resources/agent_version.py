# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import agent_version_list_params, agent_version_rollback_params
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
from ..types.agent_version_list_response import AgentVersionListResponse
from ..types.agent_version_rollback_response import AgentVersionRollbackResponse
from ..types.agent_version_get_by_id_response import AgentVersionGetByIDResponse

__all__ = ["AgentVersionResource", "AsyncAgentVersionResource"]


class AgentVersionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentVersionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AgentVersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentVersionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AgentVersionResourceWithStreamingResponse(self)

    def list(
        self,
        agent_id: str,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVersionListResponse:
        """
        The open draft first, if there is one, then published versions newest first.
        Paginated: pass `pagination.nextCursor` as `after` for the next page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agent/{agent_id}/versions",
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
                    agent_version_list_params.AgentVersionListParams,
                ),
            ),
            cast_to=AgentVersionListResponse,
        )

    def get_by_id(
        self,
        version_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVersionGetByIDResponse:
        """
        One version with every setting, plus the issues that stop it from running, if
        any.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agent/{agent_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVersionGetByIDResponse,
        )

    def rollback(
        self,
        version_id: str,
        *,
        agent_id: str,
        expected_live_version_id: str | Omit = omit,
        summary: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVersionRollbackResponse:
        """
        Publishes a new version, numbered after the latest, with this version's settings
        and makes it live. History stays append-only. An open draft started before this
        is kept but can no longer be published (409 `agent_draft_base_changed`); discard
        it or start a new one. Pass `expectedLiveVersionId` to be refused (409
        `agent_live_version_changed`) if another version went live since you read it.

        Args:
          expected_live_version_id: The live version when you decided to roll back. When sent, the rollback is
              refused with 409 if another version went live since.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agent/{agent_id}/versions/{version_id}/rollback",
            body=maybe_transform(
                {
                    "expected_live_version_id": expected_live_version_id,
                    "summary": summary,
                },
                agent_version_rollback_params.AgentVersionRollbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVersionRollbackResponse,
        )


class AsyncAgentVersionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentVersionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentVersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentVersionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAgentVersionResourceWithStreamingResponse(self)

    async def list(
        self,
        agent_id: str,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVersionListResponse:
        """
        The open draft first, if there is one, then published versions newest first.
        Paginated: pass `pagination.nextCursor` as `after` for the next page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agent/{agent_id}/versions",
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
                    agent_version_list_params.AgentVersionListParams,
                ),
            ),
            cast_to=AgentVersionListResponse,
        )

    async def get_by_id(
        self,
        version_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVersionGetByIDResponse:
        """
        One version with every setting, plus the issues that stop it from running, if
        any.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agent/{agent_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVersionGetByIDResponse,
        )

    async def rollback(
        self,
        version_id: str,
        *,
        agent_id: str,
        expected_live_version_id: str | Omit = omit,
        summary: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVersionRollbackResponse:
        """
        Publishes a new version, numbered after the latest, with this version's settings
        and makes it live. History stays append-only. An open draft started before this
        is kept but can no longer be published (409 `agent_draft_base_changed`); discard
        it or start a new one. Pass `expectedLiveVersionId` to be refused (409
        `agent_live_version_changed`) if another version went live since you read it.

        Args:
          expected_live_version_id: The live version when you decided to roll back. When sent, the rollback is
              refused with 409 if another version went live since.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agent/{agent_id}/versions/{version_id}/rollback",
            body=await async_maybe_transform(
                {
                    "expected_live_version_id": expected_live_version_id,
                    "summary": summary,
                },
                agent_version_rollback_params.AgentVersionRollbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVersionRollbackResponse,
        )


class AgentVersionResourceWithRawResponse:
    def __init__(self, agent_version: AgentVersionResource) -> None:
        self._agent_version = agent_version

        self.list = to_raw_response_wrapper(
            agent_version.list,
        )
        self.get_by_id = to_raw_response_wrapper(
            agent_version.get_by_id,
        )
        self.rollback = to_raw_response_wrapper(
            agent_version.rollback,
        )


class AsyncAgentVersionResourceWithRawResponse:
    def __init__(self, agent_version: AsyncAgentVersionResource) -> None:
        self._agent_version = agent_version

        self.list = async_to_raw_response_wrapper(
            agent_version.list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            agent_version.get_by_id,
        )
        self.rollback = async_to_raw_response_wrapper(
            agent_version.rollback,
        )


class AgentVersionResourceWithStreamingResponse:
    def __init__(self, agent_version: AgentVersionResource) -> None:
        self._agent_version = agent_version

        self.list = to_streamed_response_wrapper(
            agent_version.list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            agent_version.get_by_id,
        )
        self.rollback = to_streamed_response_wrapper(
            agent_version.rollback,
        )


class AsyncAgentVersionResourceWithStreamingResponse:
    def __init__(self, agent_version: AsyncAgentVersionResource) -> None:
        self._agent_version = agent_version

        self.list = async_to_streamed_response_wrapper(
            agent_version.list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            agent_version.get_by_id,
        )
        self.rollback = async_to_streamed_response_wrapper(
            agent_version.rollback,
        )
