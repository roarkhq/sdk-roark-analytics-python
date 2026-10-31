# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import agent_draft_create_params, agent_draft_update_params, agent_draft_publish_params
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
from ..types.agent_draft_get_response import AgentDraftGetResponse
from ..types.agent_draft_create_response import AgentDraftCreateResponse
from ..types.agent_draft_delete_response import AgentDraftDeleteResponse
from ..types.agent_draft_update_response import AgentDraftUpdateResponse
from ..types.agent_draft_publish_response import AgentDraftPublishResponse

__all__ = ["AgentDraftResource", "AsyncAgentDraftResource"]


class AgentDraftResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentDraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AgentDraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentDraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AgentDraftResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        from_version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftCreateResponse:
        """
        Opens the agent's one shared draft, a copy of the live version or of an older
        published version. Fails with 409 when a draft is already open.

        Args:
          from_version_id: Start from this published version instead of the live one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agent/{agent_id}/draft",
            body=maybe_transform(
                {"from_version_id": from_version_id}, agent_draft_create_params.AgentDraftCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftCreateResponse,
        )

    def update(
        self,
        agent_id: str,
        *,
        settings: agent_draft_update_params.Setting,
        expected_revision: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftUpdateResponse:
        """Changes settings on the draft.

        Omitted settings stay as they are. Pass the
        revision you read as expectedRevision to fail with 409 if anyone edited the
        draft since, instead of applying on top of their edit.

        Args:
          settings: The settings to change. Omitted settings stay as they are; null clears one to
              the runtime default. subAgents replaces every speaker, model configs included,
              and must include `main`; in a model config, omitted fields use the runtime
              default.

          expected_revision: The draft's revision when you read it. When sent, the edit is refused if the
              draft changed since; when omitted, it applies on top of the latest edit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._put(
            f"/v1/agent/{agent_id}/draft",
            body=maybe_transform(
                {
                    "settings": settings,
                    "expected_revision": expected_revision,
                },
                agent_draft_update_params.AgentDraftUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftUpdateResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftDeleteResponse:
        """Throws the open draft away and returns it.

        The live version is unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._delete(
            f"/v1/agent/{agent_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftDeleteResponse,
        )

    def get(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftGetResponse:
        """
        The agent's open draft, with the issues that would stop it from being published.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agent/{agent_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftGetResponse,
        )

    def publish(
        self,
        agent_id: str,
        *,
        expected_revision: int,
        summary: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftPublishResponse:
        """
        Makes the draft the live version, numbered v1, v2, ... Fails with 409 if the
        draft was edited after expectedRevision, if another version was published since
        the draft started, or if it changes nothing; with 400 and the issues if the
        version cannot run.

        Args:
          expected_revision: The draft revision you reviewed.

          summary: What changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agent/{agent_id}/draft/publish",
            body=maybe_transform(
                {
                    "expected_revision": expected_revision,
                    "summary": summary,
                },
                agent_draft_publish_params.AgentDraftPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftPublishResponse,
        )


class AsyncAgentDraftResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentDraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentDraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentDraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAgentDraftResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        from_version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftCreateResponse:
        """
        Opens the agent's one shared draft, a copy of the live version or of an older
        published version. Fails with 409 when a draft is already open.

        Args:
          from_version_id: Start from this published version instead of the live one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agent/{agent_id}/draft",
            body=await async_maybe_transform(
                {"from_version_id": from_version_id}, agent_draft_create_params.AgentDraftCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftCreateResponse,
        )

    async def update(
        self,
        agent_id: str,
        *,
        settings: agent_draft_update_params.Setting,
        expected_revision: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftUpdateResponse:
        """Changes settings on the draft.

        Omitted settings stay as they are. Pass the
        revision you read as expectedRevision to fail with 409 if anyone edited the
        draft since, instead of applying on top of their edit.

        Args:
          settings: The settings to change. Omitted settings stay as they are; null clears one to
              the runtime default. subAgents replaces every speaker, model configs included,
              and must include `main`; in a model config, omitted fields use the runtime
              default.

          expected_revision: The draft's revision when you read it. When sent, the edit is refused if the
              draft changed since; when omitted, it applies on top of the latest edit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._put(
            f"/v1/agent/{agent_id}/draft",
            body=await async_maybe_transform(
                {
                    "settings": settings,
                    "expected_revision": expected_revision,
                },
                agent_draft_update_params.AgentDraftUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftUpdateResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftDeleteResponse:
        """Throws the open draft away and returns it.

        The live version is unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._delete(
            f"/v1/agent/{agent_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftDeleteResponse,
        )

    async def get(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftGetResponse:
        """
        The agent's open draft, with the issues that would stop it from being published.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agent/{agent_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftGetResponse,
        )

    async def publish(
        self,
        agent_id: str,
        *,
        expected_revision: int,
        summary: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDraftPublishResponse:
        """
        Makes the draft the live version, numbered v1, v2, ... Fails with 409 if the
        draft was edited after expectedRevision, if another version was published since
        the draft started, or if it changes nothing; with 400 and the issues if the
        version cannot run.

        Args:
          expected_revision: The draft revision you reviewed.

          summary: What changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agent/{agent_id}/draft/publish",
            body=await async_maybe_transform(
                {
                    "expected_revision": expected_revision,
                    "summary": summary,
                },
                agent_draft_publish_params.AgentDraftPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDraftPublishResponse,
        )


class AgentDraftResourceWithRawResponse:
    def __init__(self, agent_draft: AgentDraftResource) -> None:
        self._agent_draft = agent_draft

        self.create = to_raw_response_wrapper(
            agent_draft.create,
        )
        self.update = to_raw_response_wrapper(
            agent_draft.update,
        )
        self.delete = to_raw_response_wrapper(
            agent_draft.delete,
        )
        self.get = to_raw_response_wrapper(
            agent_draft.get,
        )
        self.publish = to_raw_response_wrapper(
            agent_draft.publish,
        )


class AsyncAgentDraftResourceWithRawResponse:
    def __init__(self, agent_draft: AsyncAgentDraftResource) -> None:
        self._agent_draft = agent_draft

        self.create = async_to_raw_response_wrapper(
            agent_draft.create,
        )
        self.update = async_to_raw_response_wrapper(
            agent_draft.update,
        )
        self.delete = async_to_raw_response_wrapper(
            agent_draft.delete,
        )
        self.get = async_to_raw_response_wrapper(
            agent_draft.get,
        )
        self.publish = async_to_raw_response_wrapper(
            agent_draft.publish,
        )


class AgentDraftResourceWithStreamingResponse:
    def __init__(self, agent_draft: AgentDraftResource) -> None:
        self._agent_draft = agent_draft

        self.create = to_streamed_response_wrapper(
            agent_draft.create,
        )
        self.update = to_streamed_response_wrapper(
            agent_draft.update,
        )
        self.delete = to_streamed_response_wrapper(
            agent_draft.delete,
        )
        self.get = to_streamed_response_wrapper(
            agent_draft.get,
        )
        self.publish = to_streamed_response_wrapper(
            agent_draft.publish,
        )


class AsyncAgentDraftResourceWithStreamingResponse:
    def __init__(self, agent_draft: AsyncAgentDraftResource) -> None:
        self._agent_draft = agent_draft

        self.create = async_to_streamed_response_wrapper(
            agent_draft.create,
        )
        self.update = async_to_streamed_response_wrapper(
            agent_draft.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            agent_draft.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            agent_draft.get,
        )
        self.publish = async_to_streamed_response_wrapper(
            agent_draft.publish,
        )
