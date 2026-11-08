# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    customer_profile_list_params,
    customer_profile_update_notes_params,
    customer_profile_set_attribute_params,
    customer_profile_list_conversations_params,
)
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
from ..types.customer_profile_list_response import CustomerProfileListResponse
from ..types.customer_profile_delete_response import CustomerProfileDeleteResponse
from ..types.customer_profile_get_by_id_response import CustomerProfileGetByIDResponse
from ..types.customer_profile_update_notes_response import CustomerProfileUpdateNotesResponse
from ..types.customer_profile_set_attribute_response import CustomerProfileSetAttributeResponse
from ..types.customer_profile_clear_attribute_response import CustomerProfileClearAttributeResponse
from ..types.customer_profile_unlock_attribute_response import CustomerProfileUnlockAttributeResponse
from ..types.customer_profile_list_conversations_response import CustomerProfileListConversationsResponse

__all__ = ["CustomerProfileResource", "AsyncCustomerProfileResource"]


class CustomerProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomerProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return CustomerProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return CustomerProfileResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        agent_id: str | Omit = omit,
        field_key: Literal[
            "FULL_NAME",
            "PREFERRED_NAME",
            "ACCOUNT_ID",
            "COMPANY",
            "JOB_TITLE",
            "EMAIL",
            "ALTERNATE_PHONE",
            "AGE",
            "GENDER",
            "LANGUAGE",
            "LOCATION",
            "TIMEZONE",
            "BEST_TIME_TO_REACH",
            "PREFERRED_CHANNEL",
        ]
        | Omit = omit,
        field_operator: Literal["EQUALS", "NOT_EQUALS", "CONTAINS", "STARTS_WITH", "IS_SET", "IS_NOT_SET"]
        | Omit = omit,
        field_value: str | Omit = omit,
        include_no_data: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        modality: Literal["call", "chat"] | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal[
            "lastSeenAt",
            "firstSeenAt",
            "conversationCount",
            "voiceCount",
            "chatCount",
            "talkTimeMs",
            "displayName",
            "field.FULL_NAME",
            "field.PREFERRED_NAME",
            "field.ACCOUNT_ID",
            "field.COMPANY",
            "field.JOB_TITLE",
            "field.EMAIL",
            "field.ALTERNATE_PHONE",
            "field.AGE",
            "field.GENDER",
            "field.LANGUAGE",
            "field.LOCATION",
            "field.TIMEZONE",
            "field.BEST_TIME_TO_REACH",
            "field.PREFERRED_CHANNEL",
        ]
        | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileListResponse:
        """Returns the people who have talked to your agents in this project.

        Customers we
        hold nothing about beyond their identifier are left out unless includeNoData is
        true.

        Args:
          field_key: Filter by this field. Use with fieldOperator and, unless checking presence,
              fieldValue.

          field_operator: How fieldValue is compared, ignoring case. NOT_EQUALS includes customers without
              the field.

          include_no_data: Include customers we hold nothing about beyond their identifier. Defaults to
              false.

          sort_by: A column, or field.<KEY> (for example field.COMPANY) to sort by a field's value.
              Customers without a value sort last.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/customer-profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "field_key": field_key,
                        "field_operator": field_operator,
                        "field_value": field_value,
                        "include_no_data": include_no_data,
                        "limit": limit,
                        "modality": modality,
                        "page": page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    customer_profile_list_params.CustomerProfileListParams,
                ),
            ),
            cast_to=CustomerProfileListResponse,
        )

    def delete(
        self,
        customer_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileDeleteResponse:
        """Permanently removes the profile, its fields, evidence and notes.

        Conversations
        are kept. A new conversation from the same identifier creates a new profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return self._delete(
            f"/v1/customer-profile/{customer_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileDeleteResponse,
        )

    def clear_attribute(
        self,
        key: str,
        *,
        customer_profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileClearAttributeResponse:
        """
        Removes the value and any lock, so a later conversation can fill it again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return self._delete(
            f"/v1/customer-profile/{customer_profile_id}/attributes/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileClearAttributeResponse,
        )

    def get_by_id(
        self,
        customer_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileGetByIDResponse:
        """
        Get a customer profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return self._get(
            f"/v1/customer-profile/{customer_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileGetByIDResponse,
        )

    def list_conversations(
        self,
        customer_profile_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileListConversationsResponse:
        """
        Calls and chats with this customer, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return self._get(
            f"/v1/customer-profile/{customer_profile_id}/conversations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    customer_profile_list_conversations_params.CustomerProfileListConversationsParams,
                ),
            ),
            cast_to=CustomerProfileListConversationsResponse,
        )

    def set_attribute(
        self,
        key: str,
        *,
        customer_profile_id: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileSetAttributeResponse:
        """
        Sets the value and locks the field, so newer conversations cannot change it.

        Args:
          value: The new value. Setting a field locks it, so newer conversations cannot change
              it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return self._put(
            f"/v1/customer-profile/{customer_profile_id}/attributes/{key}",
            body=maybe_transform(
                {"value": value}, customer_profile_set_attribute_params.CustomerProfileSetAttributeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileSetAttributeResponse,
        )

    def unlock_attribute(
        self,
        key: str,
        *,
        customer_profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileUnlockAttributeResponse:
        """Lets newer conversations change this field again.

        The current value stays until
        one does.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return self._post(
            f"/v1/customer-profile/{customer_profile_id}/attributes/{key}/unlock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileUnlockAttributeResponse,
        )

    def update_notes(
        self,
        customer_profile_id: str,
        *,
        notes: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileUpdateNotesResponse:
        """Replaces your team's shared notes.

        Null or empty clears them. The last save
        wins.

        Args:
          notes: Replaces the existing notes. Null or empty clears them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return self._put(
            f"/v1/customer-profile/{customer_profile_id}/notes",
            body=maybe_transform(
                {"notes": notes}, customer_profile_update_notes_params.CustomerProfileUpdateNotesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileUpdateNotesResponse,
        )


class AsyncCustomerProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomerProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncCustomerProfileResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        agent_id: str | Omit = omit,
        field_key: Literal[
            "FULL_NAME",
            "PREFERRED_NAME",
            "ACCOUNT_ID",
            "COMPANY",
            "JOB_TITLE",
            "EMAIL",
            "ALTERNATE_PHONE",
            "AGE",
            "GENDER",
            "LANGUAGE",
            "LOCATION",
            "TIMEZONE",
            "BEST_TIME_TO_REACH",
            "PREFERRED_CHANNEL",
        ]
        | Omit = omit,
        field_operator: Literal["EQUALS", "NOT_EQUALS", "CONTAINS", "STARTS_WITH", "IS_SET", "IS_NOT_SET"]
        | Omit = omit,
        field_value: str | Omit = omit,
        include_no_data: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        modality: Literal["call", "chat"] | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal[
            "lastSeenAt",
            "firstSeenAt",
            "conversationCount",
            "voiceCount",
            "chatCount",
            "talkTimeMs",
            "displayName",
            "field.FULL_NAME",
            "field.PREFERRED_NAME",
            "field.ACCOUNT_ID",
            "field.COMPANY",
            "field.JOB_TITLE",
            "field.EMAIL",
            "field.ALTERNATE_PHONE",
            "field.AGE",
            "field.GENDER",
            "field.LANGUAGE",
            "field.LOCATION",
            "field.TIMEZONE",
            "field.BEST_TIME_TO_REACH",
            "field.PREFERRED_CHANNEL",
        ]
        | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileListResponse:
        """Returns the people who have talked to your agents in this project.

        Customers we
        hold nothing about beyond their identifier are left out unless includeNoData is
        true.

        Args:
          field_key: Filter by this field. Use with fieldOperator and, unless checking presence,
              fieldValue.

          field_operator: How fieldValue is compared, ignoring case. NOT_EQUALS includes customers without
              the field.

          include_no_data: Include customers we hold nothing about beyond their identifier. Defaults to
              false.

          sort_by: A column, or field.<KEY> (for example field.COMPANY) to sort by a field's value.
              Customers without a value sort last.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/customer-profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "field_key": field_key,
                        "field_operator": field_operator,
                        "field_value": field_value,
                        "include_no_data": include_no_data,
                        "limit": limit,
                        "modality": modality,
                        "page": page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    customer_profile_list_params.CustomerProfileListParams,
                ),
            ),
            cast_to=CustomerProfileListResponse,
        )

    async def delete(
        self,
        customer_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileDeleteResponse:
        """Permanently removes the profile, its fields, evidence and notes.

        Conversations
        are kept. A new conversation from the same identifier creates a new profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return await self._delete(
            f"/v1/customer-profile/{customer_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileDeleteResponse,
        )

    async def clear_attribute(
        self,
        key: str,
        *,
        customer_profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileClearAttributeResponse:
        """
        Removes the value and any lock, so a later conversation can fill it again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return await self._delete(
            f"/v1/customer-profile/{customer_profile_id}/attributes/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileClearAttributeResponse,
        )

    async def get_by_id(
        self,
        customer_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileGetByIDResponse:
        """
        Get a customer profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return await self._get(
            f"/v1/customer-profile/{customer_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileGetByIDResponse,
        )

    async def list_conversations(
        self,
        customer_profile_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileListConversationsResponse:
        """
        Calls and chats with this customer, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return await self._get(
            f"/v1/customer-profile/{customer_profile_id}/conversations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    customer_profile_list_conversations_params.CustomerProfileListConversationsParams,
                ),
            ),
            cast_to=CustomerProfileListConversationsResponse,
        )

    async def set_attribute(
        self,
        key: str,
        *,
        customer_profile_id: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileSetAttributeResponse:
        """
        Sets the value and locks the field, so newer conversations cannot change it.

        Args:
          value: The new value. Setting a field locks it, so newer conversations cannot change
              it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return await self._put(
            f"/v1/customer-profile/{customer_profile_id}/attributes/{key}",
            body=await async_maybe_transform(
                {"value": value}, customer_profile_set_attribute_params.CustomerProfileSetAttributeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileSetAttributeResponse,
        )

    async def unlock_attribute(
        self,
        key: str,
        *,
        customer_profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileUnlockAttributeResponse:
        """Lets newer conversations change this field again.

        The current value stays until
        one does.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return await self._post(
            f"/v1/customer-profile/{customer_profile_id}/attributes/{key}/unlock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileUnlockAttributeResponse,
        )

    async def update_notes(
        self,
        customer_profile_id: str,
        *,
        notes: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerProfileUpdateNotesResponse:
        """Replaces your team's shared notes.

        Null or empty clears them. The last save
        wins.

        Args:
          notes: Replaces the existing notes. Null or empty clears them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_profile_id` but received {customer_profile_id!r}"
            )
        return await self._put(
            f"/v1/customer-profile/{customer_profile_id}/notes",
            body=await async_maybe_transform(
                {"notes": notes}, customer_profile_update_notes_params.CustomerProfileUpdateNotesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerProfileUpdateNotesResponse,
        )


class CustomerProfileResourceWithRawResponse:
    def __init__(self, customer_profile: CustomerProfileResource) -> None:
        self._customer_profile = customer_profile

        self.list = to_raw_response_wrapper(
            customer_profile.list,
        )
        self.delete = to_raw_response_wrapper(
            customer_profile.delete,
        )
        self.clear_attribute = to_raw_response_wrapper(
            customer_profile.clear_attribute,
        )
        self.get_by_id = to_raw_response_wrapper(
            customer_profile.get_by_id,
        )
        self.list_conversations = to_raw_response_wrapper(
            customer_profile.list_conversations,
        )
        self.set_attribute = to_raw_response_wrapper(
            customer_profile.set_attribute,
        )
        self.unlock_attribute = to_raw_response_wrapper(
            customer_profile.unlock_attribute,
        )
        self.update_notes = to_raw_response_wrapper(
            customer_profile.update_notes,
        )


class AsyncCustomerProfileResourceWithRawResponse:
    def __init__(self, customer_profile: AsyncCustomerProfileResource) -> None:
        self._customer_profile = customer_profile

        self.list = async_to_raw_response_wrapper(
            customer_profile.list,
        )
        self.delete = async_to_raw_response_wrapper(
            customer_profile.delete,
        )
        self.clear_attribute = async_to_raw_response_wrapper(
            customer_profile.clear_attribute,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            customer_profile.get_by_id,
        )
        self.list_conversations = async_to_raw_response_wrapper(
            customer_profile.list_conversations,
        )
        self.set_attribute = async_to_raw_response_wrapper(
            customer_profile.set_attribute,
        )
        self.unlock_attribute = async_to_raw_response_wrapper(
            customer_profile.unlock_attribute,
        )
        self.update_notes = async_to_raw_response_wrapper(
            customer_profile.update_notes,
        )


class CustomerProfileResourceWithStreamingResponse:
    def __init__(self, customer_profile: CustomerProfileResource) -> None:
        self._customer_profile = customer_profile

        self.list = to_streamed_response_wrapper(
            customer_profile.list,
        )
        self.delete = to_streamed_response_wrapper(
            customer_profile.delete,
        )
        self.clear_attribute = to_streamed_response_wrapper(
            customer_profile.clear_attribute,
        )
        self.get_by_id = to_streamed_response_wrapper(
            customer_profile.get_by_id,
        )
        self.list_conversations = to_streamed_response_wrapper(
            customer_profile.list_conversations,
        )
        self.set_attribute = to_streamed_response_wrapper(
            customer_profile.set_attribute,
        )
        self.unlock_attribute = to_streamed_response_wrapper(
            customer_profile.unlock_attribute,
        )
        self.update_notes = to_streamed_response_wrapper(
            customer_profile.update_notes,
        )


class AsyncCustomerProfileResourceWithStreamingResponse:
    def __init__(self, customer_profile: AsyncCustomerProfileResource) -> None:
        self._customer_profile = customer_profile

        self.list = async_to_streamed_response_wrapper(
            customer_profile.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            customer_profile.delete,
        )
        self.clear_attribute = async_to_streamed_response_wrapper(
            customer_profile.clear_attribute,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            customer_profile.get_by_id,
        )
        self.list_conversations = async_to_streamed_response_wrapper(
            customer_profile.list_conversations,
        )
        self.set_attribute = async_to_streamed_response_wrapper(
            customer_profile.set_attribute,
        )
        self.unlock_attribute = async_to_streamed_response_wrapper(
            customer_profile.unlock_attribute,
        )
        self.update_notes = async_to_streamed_response_wrapper(
            customer_profile.update_notes,
        )
