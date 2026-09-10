# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import agent_prompt_update_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.agent_prompt_list_response import AgentPromptListResponse
from ..types.agent_prompt_update_response import AgentPromptUpdateResponse
from ..types.agent_prompt_list_versions_response import AgentPromptListVersionsResponse

__all__ = ["AgentPromptResource", "AsyncAgentPromptResource"]


class AgentPromptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentPromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AgentPromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentPromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AgentPromptResourceWithStreamingResponse(self)

    def update(
        self,
        agent_id: str,
        *,
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentPromptUpdateResponse:
        """Sets the agent's API-managed prompt.

        This is its own version history (`source:
        API_MANAGED`), separate from prompts observed on calls, edited in the app, or
        managed by config-as-code. Setting the same content twice is a no-op (no new
        version). Roark does not run your agent and no metric reads this prompt: it is
        stored and versioned for your reference.

        Args:
          prompt: The prompt content to set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._put(
            f"/v1/agent/{agent_id}/prompts",
            body=maybe_transform({"prompt": prompt}, agent_prompt_update_params.AgentPromptUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentPromptUpdateResponse,
        )

    def list(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentPromptListResponse:
        """Returns the agent's prompt lineages.

        Each lineage is an independent version
        history, labelled by its `source` (USER, API, CONFIG, or a provider
        integration). `prompt` is the current content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agent/{agent_id}/prompts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentPromptListResponse,
        )

    def list_versions(
        self,
        prompt_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentPromptListVersionsResponse:
        """
        Returns the full version history of a single prompt lineage, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agent/{agent_id}/prompts/{prompt_id}/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentPromptListVersionsResponse,
        )


class AsyncAgentPromptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentPromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentPromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentPromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAgentPromptResourceWithStreamingResponse(self)

    async def update(
        self,
        agent_id: str,
        *,
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentPromptUpdateResponse:
        """Sets the agent's API-managed prompt.

        This is its own version history (`source:
        API_MANAGED`), separate from prompts observed on calls, edited in the app, or
        managed by config-as-code. Setting the same content twice is a no-op (no new
        version). Roark does not run your agent and no metric reads this prompt: it is
        stored and versioned for your reference.

        Args:
          prompt: The prompt content to set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._put(
            f"/v1/agent/{agent_id}/prompts",
            body=await async_maybe_transform({"prompt": prompt}, agent_prompt_update_params.AgentPromptUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentPromptUpdateResponse,
        )

    async def list(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentPromptListResponse:
        """Returns the agent's prompt lineages.

        Each lineage is an independent version
        history, labelled by its `source` (USER, API, CONFIG, or a provider
        integration). `prompt` is the current content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agent/{agent_id}/prompts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentPromptListResponse,
        )

    async def list_versions(
        self,
        prompt_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentPromptListVersionsResponse:
        """
        Returns the full version history of a single prompt lineage, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agent/{agent_id}/prompts/{prompt_id}/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentPromptListVersionsResponse,
        )


class AgentPromptResourceWithRawResponse:
    def __init__(self, agent_prompt: AgentPromptResource) -> None:
        self._agent_prompt = agent_prompt

        self.update = to_raw_response_wrapper(
            agent_prompt.update,
        )
        self.list = to_raw_response_wrapper(
            agent_prompt.list,
        )
        self.list_versions = to_raw_response_wrapper(
            agent_prompt.list_versions,
        )


class AsyncAgentPromptResourceWithRawResponse:
    def __init__(self, agent_prompt: AsyncAgentPromptResource) -> None:
        self._agent_prompt = agent_prompt

        self.update = async_to_raw_response_wrapper(
            agent_prompt.update,
        )
        self.list = async_to_raw_response_wrapper(
            agent_prompt.list,
        )
        self.list_versions = async_to_raw_response_wrapper(
            agent_prompt.list_versions,
        )


class AgentPromptResourceWithStreamingResponse:
    def __init__(self, agent_prompt: AgentPromptResource) -> None:
        self._agent_prompt = agent_prompt

        self.update = to_streamed_response_wrapper(
            agent_prompt.update,
        )
        self.list = to_streamed_response_wrapper(
            agent_prompt.list,
        )
        self.list_versions = to_streamed_response_wrapper(
            agent_prompt.list_versions,
        )


class AsyncAgentPromptResourceWithStreamingResponse:
    def __init__(self, agent_prompt: AsyncAgentPromptResource) -> None:
        self._agent_prompt = agent_prompt

        self.update = async_to_streamed_response_wrapper(
            agent_prompt.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agent_prompt.list,
        )
        self.list_versions = async_to_streamed_response_wrapper(
            agent_prompt.list_versions,
        )
