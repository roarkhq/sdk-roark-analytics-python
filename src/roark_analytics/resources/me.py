# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import me_list_api_keys_params, me_create_api_key_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.me_get_response import MeGetResponse
from ..types.me_list_api_keys_response import MeListAPIKeysResponse
from ..types.me_create_api_key_response import MeCreateAPIKeyResponse
from ..types.me_revoke_api_key_response import MeRevokeAPIKeyResponse

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return MeResourceWithStreamingResponse(self)

    def create_api_key(
        self,
        *,
        name: str,
        expires_at: str | Omit = omit,
        permissions: SequenceNotStr[str] | Omit = omit,
        project_id: str | Omit = omit,
        scopes: List[Literal["READ", "WRITE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeCreateAPIKeyResponse:
        """Mints a credential that acts as you, for a CLI or an automation.

        The key value
        is returned exactly once, in the `key` field: capture it now, it is unreadable
        afterwards. Requires a personal credential (a project API key is refused) and
        admin on the project the credential defaults to. The new credential can never
        exceed the one that created it: not in scope, not in permissions, and not in
        lifetime. Omit a field to copy it from the calling credential.

        Args:
          name: A label you will recognise later. It is the only thing that tells two
              credentials apart in the list you revoke from.

          expires_at: ISO 8601 expiry. Defaults to the calling credential's own expiry (no expiry, for
              a `roark auth login` credential) and may not outlive it, so a short-lived
              connector credential cannot mint a permanent one.

          permissions: Granular 'resource:action' permissions. Defaults to the calling credential's own
              set, and can never exceed it. A ceiling, not an entitlement: the holder still
              only reaches what their project membership allows.

          project_id: Project the credential assumes when a request sends no X-Roark-Project-Id
              header. Defaults to the calling credential's own default project. You must be an
              admin of whichever project is used.

          scopes: Coarse tier. Defaults to the calling credential's own tier, and can never exceed
              it: a READ credential cannot mint a WRITE one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/me/api-keys",
            body=maybe_transform(
                {
                    "name": name,
                    "expires_at": expires_at,
                    "permissions": permissions,
                    "project_id": project_id,
                    "scopes": scopes,
                },
                me_create_api_key_params.MeCreateAPIKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeCreateAPIKeyResponse,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeGetResponse:
        """
        Returns the scope of the credential making the request, the organization it acts
        in, its default project (if any) and the permissions it was granted. Works for
        both project-scoped API keys and user-scoped credentials from the CLI or an MCP
        connector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeGetResponse,
        )

    def list_api_keys(
        self,
        *,
        status: Literal["ACTIVE", "REVOKED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeListAPIKeysResponse:
        """
        Returns the credentials that act as you: the ones created in the dashboard, from
        `roark auth login`, and MCP connectors. Requires a personal credential; a
        project API key is refused. Defaults to ACTIVE, pass ?status=REVOKED to see
        revoked ones. The key value itself is never returned.

        Args:
          status: Filter by status. Defaults to ACTIVE.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/me/api-keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, me_list_api_keys_params.MeListAPIKeysParams),
            ),
            cast_to=MeListAPIKeysResponse,
        )

    def revoke_api_key(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeRevokeAPIKeyResponse:
        """Revokes a credential that acts as you.

        It stops working immediately. A
        credential may revoke itself, which is what `roark auth logout` does. Repeating
        the call is safe; an unknown id, or one belonging to someone else, answers 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/me/api-keys/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeRevokeAPIKeyResponse,
        )


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncMeResourceWithStreamingResponse(self)

    async def create_api_key(
        self,
        *,
        name: str,
        expires_at: str | Omit = omit,
        permissions: SequenceNotStr[str] | Omit = omit,
        project_id: str | Omit = omit,
        scopes: List[Literal["READ", "WRITE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeCreateAPIKeyResponse:
        """Mints a credential that acts as you, for a CLI or an automation.

        The key value
        is returned exactly once, in the `key` field: capture it now, it is unreadable
        afterwards. Requires a personal credential (a project API key is refused) and
        admin on the project the credential defaults to. The new credential can never
        exceed the one that created it: not in scope, not in permissions, and not in
        lifetime. Omit a field to copy it from the calling credential.

        Args:
          name: A label you will recognise later. It is the only thing that tells two
              credentials apart in the list you revoke from.

          expires_at: ISO 8601 expiry. Defaults to the calling credential's own expiry (no expiry, for
              a `roark auth login` credential) and may not outlive it, so a short-lived
              connector credential cannot mint a permanent one.

          permissions: Granular 'resource:action' permissions. Defaults to the calling credential's own
              set, and can never exceed it. A ceiling, not an entitlement: the holder still
              only reaches what their project membership allows.

          project_id: Project the credential assumes when a request sends no X-Roark-Project-Id
              header. Defaults to the calling credential's own default project. You must be an
              admin of whichever project is used.

          scopes: Coarse tier. Defaults to the calling credential's own tier, and can never exceed
              it: a READ credential cannot mint a WRITE one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/me/api-keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "expires_at": expires_at,
                    "permissions": permissions,
                    "project_id": project_id,
                    "scopes": scopes,
                },
                me_create_api_key_params.MeCreateAPIKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeCreateAPIKeyResponse,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeGetResponse:
        """
        Returns the scope of the credential making the request, the organization it acts
        in, its default project (if any) and the permissions it was granted. Works for
        both project-scoped API keys and user-scoped credentials from the CLI or an MCP
        connector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeGetResponse,
        )

    async def list_api_keys(
        self,
        *,
        status: Literal["ACTIVE", "REVOKED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeListAPIKeysResponse:
        """
        Returns the credentials that act as you: the ones created in the dashboard, from
        `roark auth login`, and MCP connectors. Requires a personal credential; a
        project API key is refused. Defaults to ACTIVE, pass ?status=REVOKED to see
        revoked ones. The key value itself is never returned.

        Args:
          status: Filter by status. Defaults to ACTIVE.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/me/api-keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, me_list_api_keys_params.MeListAPIKeysParams),
            ),
            cast_to=MeListAPIKeysResponse,
        )

    async def revoke_api_key(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeRevokeAPIKeyResponse:
        """Revokes a credential that acts as you.

        It stops working immediately. A
        credential may revoke itself, which is what `roark auth logout` does. Repeating
        the call is safe; an unknown id, or one belonging to someone else, answers 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/me/api-keys/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeRevokeAPIKeyResponse,
        )


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.create_api_key = to_raw_response_wrapper(
            me.create_api_key,
        )
        self.get = to_raw_response_wrapper(
            me.get,
        )
        self.list_api_keys = to_raw_response_wrapper(
            me.list_api_keys,
        )
        self.revoke_api_key = to_raw_response_wrapper(
            me.revoke_api_key,
        )


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.create_api_key = async_to_raw_response_wrapper(
            me.create_api_key,
        )
        self.get = async_to_raw_response_wrapper(
            me.get,
        )
        self.list_api_keys = async_to_raw_response_wrapper(
            me.list_api_keys,
        )
        self.revoke_api_key = async_to_raw_response_wrapper(
            me.revoke_api_key,
        )


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.create_api_key = to_streamed_response_wrapper(
            me.create_api_key,
        )
        self.get = to_streamed_response_wrapper(
            me.get,
        )
        self.list_api_keys = to_streamed_response_wrapper(
            me.list_api_keys,
        )
        self.revoke_api_key = to_streamed_response_wrapper(
            me.revoke_api_key,
        )


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.create_api_key = async_to_streamed_response_wrapper(
            me.create_api_key,
        )
        self.get = async_to_streamed_response_wrapper(
            me.get,
        )
        self.list_api_keys = async_to_streamed_response_wrapper(
            me.list_api_keys,
        )
        self.revoke_api_key = async_to_streamed_response_wrapper(
            me.revoke_api_key,
        )
