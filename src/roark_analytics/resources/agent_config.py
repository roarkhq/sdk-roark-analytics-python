# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import agent_config_update_params, agent_config_resolve_params
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
from ..types.agent_config_list_response import AgentConfigListResponse
from ..types.agent_config_update_response import AgentConfigUpdateResponse
from ..types.agent_config_promote_response import AgentConfigPromoteResponse
from ..types.agent_config_resolve_response import AgentConfigResolveResponse
from ..types.agent_config_get_by_id_response import AgentConfigGetByIDResponse
from ..types.agent_config_delete_staging_response import AgentConfigDeleteStagingResponse

__all__ = ["AgentConfigResource", "AsyncAgentConfigResource"]


class AgentConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AgentConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AgentConfigResourceWithStreamingResponse(self)

    def update(
        self,
        key: str,
        *,
        channel: Literal["production", "staging"],
        document: Dict[str, object],
        agent_id: str | Omit = omit,
        summary: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigUpdateResponse:
        """Write a new revision onto a channel.

        Writing production creates the key when it
        does not exist; writing staging stages a candidate that only Roark-recognized
        simulation sessions will read. Every write is a new revision; nothing is
        overwritten.

        Args:
          channel: Which channel to write.

          document: The full config JSON for the new revision.

          agent_id: Link this config to a Roark agent (the one your calls report). Required before
              Autoimprove can run on it: the link is how a fix finds the config channel.

          summary: One-line story of the change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._put(
            f"/v1/agent-config/{key}",
            body=maybe_transform(
                {
                    "channel": channel,
                    "document": document,
                    "agent_id": agent_id,
                    "summary": summary,
                },
                agent_config_update_params.AgentConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigUpdateResponse,
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
    ) -> AgentConfigListResponse:
        """List the managed agent configs in this project, most recent first."""
        return self._get(
            "/v1/agent-config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigListResponse,
        )

    def delete_staging(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigDeleteStagingResponse:
        """Clear the staging channel.

        Production is untouched; recognized simulation
        sessions go back to reading production.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._delete(
            f"/v1/agent-config/{key}/staging",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigDeleteStagingResponse,
        )

    def get_by_id(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigGetByIDResponse:
        """
        Fetch one managed config with its channel pointers and recent revisions, newest
        first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            f"/v1/agent-config/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigGetByIDResponse,
        )

    def promote(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigPromoteResponse:
        """Point the production channel at the staging revision.

        Real traffic reads it from
        the next session onward; roll back by writing the prior revision id to
        production (the chain preserves every state).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._post(
            f"/v1/agent-config/{key}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigPromoteResponse,
        )

    def resolve(
        self,
        key: str,
        *,
        defaults: Dict[str, object] | Omit = omit,
        session: agent_config_resolve_params.Session | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigResolveResponse:
        """The call your agent makes at session start.

        Returns the config JSON for this
        session, with per-session simulation recognition built in: when the session was
        originated by a Roark simulation (matched by caller number against the calls
        Roark has in flight), the STAGING revision is served for that session only, so
        Autoimprove candidates are tested on your real deployment. Real traffic always
        resolves to production; any recognition miss degrades to production too. On the
        first fetch of an unknown key, pass `defaults` (your baked-in config): the key
        is registered and the defaults become revision 1. That makes integration a
        single call. Cache the response per session; do not fetch per turn.

        Args:
          defaults: Your baked-in config. On the first fetch of an unknown key this registers the
              config and becomes revision 1, so integration is a single call. Ignored once the
              key exists.

          session: Session context. When the call was originated by a Roark simulation, Roark
              recognizes it here and serves the staging revision for this session only; real
              traffic always gets production.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._post(
            f"/v1/agent-config/{key}/resolve",
            body=maybe_transform(
                {
                    "defaults": defaults,
                    "session": session,
                },
                agent_config_resolve_params.AgentConfigResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigResolveResponse,
        )


class AsyncAgentConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAgentConfigResourceWithStreamingResponse(self)

    async def update(
        self,
        key: str,
        *,
        channel: Literal["production", "staging"],
        document: Dict[str, object],
        agent_id: str | Omit = omit,
        summary: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigUpdateResponse:
        """Write a new revision onto a channel.

        Writing production creates the key when it
        does not exist; writing staging stages a candidate that only Roark-recognized
        simulation sessions will read. Every write is a new revision; nothing is
        overwritten.

        Args:
          channel: Which channel to write.

          document: The full config JSON for the new revision.

          agent_id: Link this config to a Roark agent (the one your calls report). Required before
              Autoimprove can run on it: the link is how a fix finds the config channel.

          summary: One-line story of the change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._put(
            f"/v1/agent-config/{key}",
            body=await async_maybe_transform(
                {
                    "channel": channel,
                    "document": document,
                    "agent_id": agent_id,
                    "summary": summary,
                },
                agent_config_update_params.AgentConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigUpdateResponse,
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
    ) -> AgentConfigListResponse:
        """List the managed agent configs in this project, most recent first."""
        return await self._get(
            "/v1/agent-config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigListResponse,
        )

    async def delete_staging(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigDeleteStagingResponse:
        """Clear the staging channel.

        Production is untouched; recognized simulation
        sessions go back to reading production.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._delete(
            f"/v1/agent-config/{key}/staging",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigDeleteStagingResponse,
        )

    async def get_by_id(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigGetByIDResponse:
        """
        Fetch one managed config with its channel pointers and recent revisions, newest
        first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            f"/v1/agent-config/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigGetByIDResponse,
        )

    async def promote(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigPromoteResponse:
        """Point the production channel at the staging revision.

        Real traffic reads it from
        the next session onward; roll back by writing the prior revision id to
        production (the chain preserves every state).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._post(
            f"/v1/agent-config/{key}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigPromoteResponse,
        )

    async def resolve(
        self,
        key: str,
        *,
        defaults: Dict[str, object] | Omit = omit,
        session: agent_config_resolve_params.Session | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConfigResolveResponse:
        """The call your agent makes at session start.

        Returns the config JSON for this
        session, with per-session simulation recognition built in: when the session was
        originated by a Roark simulation (matched by caller number against the calls
        Roark has in flight), the STAGING revision is served for that session only, so
        Autoimprove candidates are tested on your real deployment. Real traffic always
        resolves to production; any recognition miss degrades to production too. On the
        first fetch of an unknown key, pass `defaults` (your baked-in config): the key
        is registered and the defaults become revision 1. That makes integration a
        single call. Cache the response per session; do not fetch per turn.

        Args:
          defaults: Your baked-in config. On the first fetch of an unknown key this registers the
              config and becomes revision 1, so integration is a single call. Ignored once the
              key exists.

          session: Session context. When the call was originated by a Roark simulation, Roark
              recognizes it here and serves the staging revision for this session only; real
              traffic always gets production.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._post(
            f"/v1/agent-config/{key}/resolve",
            body=await async_maybe_transform(
                {
                    "defaults": defaults,
                    "session": session,
                },
                agent_config_resolve_params.AgentConfigResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConfigResolveResponse,
        )


class AgentConfigResourceWithRawResponse:
    def __init__(self, agent_config: AgentConfigResource) -> None:
        self._agent_config = agent_config

        self.update = to_raw_response_wrapper(
            agent_config.update,
        )
        self.list = to_raw_response_wrapper(
            agent_config.list,
        )
        self.delete_staging = to_raw_response_wrapper(
            agent_config.delete_staging,
        )
        self.get_by_id = to_raw_response_wrapper(
            agent_config.get_by_id,
        )
        self.promote = to_raw_response_wrapper(
            agent_config.promote,
        )
        self.resolve = to_raw_response_wrapper(
            agent_config.resolve,
        )


class AsyncAgentConfigResourceWithRawResponse:
    def __init__(self, agent_config: AsyncAgentConfigResource) -> None:
        self._agent_config = agent_config

        self.update = async_to_raw_response_wrapper(
            agent_config.update,
        )
        self.list = async_to_raw_response_wrapper(
            agent_config.list,
        )
        self.delete_staging = async_to_raw_response_wrapper(
            agent_config.delete_staging,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            agent_config.get_by_id,
        )
        self.promote = async_to_raw_response_wrapper(
            agent_config.promote,
        )
        self.resolve = async_to_raw_response_wrapper(
            agent_config.resolve,
        )


class AgentConfigResourceWithStreamingResponse:
    def __init__(self, agent_config: AgentConfigResource) -> None:
        self._agent_config = agent_config

        self.update = to_streamed_response_wrapper(
            agent_config.update,
        )
        self.list = to_streamed_response_wrapper(
            agent_config.list,
        )
        self.delete_staging = to_streamed_response_wrapper(
            agent_config.delete_staging,
        )
        self.get_by_id = to_streamed_response_wrapper(
            agent_config.get_by_id,
        )
        self.promote = to_streamed_response_wrapper(
            agent_config.promote,
        )
        self.resolve = to_streamed_response_wrapper(
            agent_config.resolve,
        )


class AsyncAgentConfigResourceWithStreamingResponse:
    def __init__(self, agent_config: AsyncAgentConfigResource) -> None:
        self._agent_config = agent_config

        self.update = async_to_streamed_response_wrapper(
            agent_config.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agent_config.list,
        )
        self.delete_staging = async_to_streamed_response_wrapper(
            agent_config.delete_staging,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            agent_config.get_by_id,
        )
        self.promote = async_to_streamed_response_wrapper(
            agent_config.promote,
        )
        self.resolve = async_to_streamed_response_wrapper(
            agent_config.resolve,
        )
