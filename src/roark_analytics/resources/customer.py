# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    customer_list_params,
    customer_create_field_params,
    customer_update_field_params,
    customer_update_notes_params,
    customer_set_attribute_params,
    customer_list_conversations_params,
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
from ..types.customer_list_response import CustomerListResponse
from ..types.customer_delete_response import CustomerDeleteResponse
from ..types.customer_get_by_id_response import CustomerGetByIDResponse
from ..types.customer_list_fields_response import CustomerListFieldsResponse
from ..types.customer_create_field_response import CustomerCreateFieldResponse
from ..types.customer_delete_field_response import CustomerDeleteFieldResponse
from ..types.customer_update_field_response import CustomerUpdateFieldResponse
from ..types.customer_update_notes_response import CustomerUpdateNotesResponse
from ..types.customer_set_attribute_response import CustomerSetAttributeResponse
from ..types.customer_clear_attribute_response import CustomerClearAttributeResponse
from ..types.customer_unlock_attribute_response import CustomerUnlockAttributeResponse
from ..types.customer_list_conversations_response import CustomerListConversationsResponse

__all__ = ["CustomerResource", "AsyncCustomerResource"]


class CustomerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return CustomerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return CustomerResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        agent_id: str | Omit = omit,
        field_key: str | Omit = omit,
        field_operator: Literal["EQUALS", "NOT_EQUALS", "CONTAINS", "STARTS_WITH", "IS_SET", "IS_NOT_SET"]
        | Omit = omit,
        field_value: str | Omit = omit,
        include_no_data: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        modality: Literal["voice", "chat", "call"] | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerListResponse:
        """Returns the people who have talked to your agents in this project.

        Customers we
        hold nothing about beyond their identifier are left out unless includeNoData is
        true.

        Args:
          field_key: Filter by this field, a key from GET /v1/customer/fields. Use with fieldOperator
              and, unless checking presence, fieldValue.

          field_operator: How fieldValue is compared, ignoring case. NOT_EQUALS includes customers without
              the field.

          include_no_data: Include customers we hold nothing about beyond their identifier. Defaults to
              false.

          sort_by: lastSeenAt (the default), firstSeenAt, conversationCount, voiceCount, chatCount,
              talkTimeMs or displayName, or field.<key> (for example field.COMPANY) to sort by
              a field's value. Field keys come from GET /v1/customer/fields. Customers without
              a value sort last.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/customer",
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
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=CustomerListResponse,
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
    ) -> CustomerDeleteResponse:
        """
        Permanently removes the customer, with their fields, evidence and notes.
        Conversations are kept. A new conversation from the same identifier starts a new
        customer.

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
            f"/v1/customer/{customer_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerDeleteResponse,
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
    ) -> CustomerClearAttributeResponse:
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
            f"/v1/customer/{customer_profile_id}/attributes/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerClearAttributeResponse,
        )

    def create_field(
        self,
        *,
        extract: bool,
        key: str,
        label: str,
        value_type: Literal["TEXT", "NUMBER", "BOOLEAN", "DATE", "PHONE_NUMBER", "EMAIL", "CURRENCY"],
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerCreateFieldResponse:
        """Adds a field of your project's own.

        With extract on, conversations fill it from
        what customers say, guided by its description.

        Args:
          extract: Whether conversations fill this field

          key: Starts with a letter; letters, numbers and underscores only. Fixed once created.

          description: What the agent listens for in a conversation. Required when extract is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/customer/fields",
            body=maybe_transform(
                {
                    "extract": extract,
                    "key": key,
                    "label": label,
                    "value_type": value_type,
                    "description": description,
                },
                customer_create_field_params.CustomerCreateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerCreateFieldResponse,
        )

    def delete_field(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerDeleteFieldResponse:
        """Deletes a field of your project's own.

        Its values stop showing on customers. A
        built-in field cannot be deleted; turn it off instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._delete(
            f"/v1/customer/fields/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerDeleteFieldResponse,
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
    ) -> CustomerGetByIDResponse:
        """
        Get a customer

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
            f"/v1/customer/{customer_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerGetByIDResponse,
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
    ) -> CustomerListConversationsResponse:
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
            f"/v1/customer/{customer_profile_id}/conversations",
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
                    customer_list_conversations_params.CustomerListConversationsParams,
                ),
            ),
            cast_to=CustomerListConversationsResponse,
        )

    def list_fields(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerListFieldsResponse:
        """The fields this project's customers can hold, in display order.

        Use a field's
        key to filter, sort and set attributes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/customer/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerListFieldsResponse,
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
    ) -> CustomerSetAttributeResponse:
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
            f"/v1/customer/{customer_profile_id}/attributes/{key}",
            body=maybe_transform({"value": value}, customer_set_attribute_params.CustomerSetAttributeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSetAttributeResponse,
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
    ) -> CustomerUnlockAttributeResponse:
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
            f"/v1/customer/{customer_profile_id}/attributes/{key}/unlock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerUnlockAttributeResponse,
        )

    def update_field(
        self,
        key: str,
        *,
        description: Optional[str] | Omit = omit,
        extract: bool | Omit = omit,
        label: str | Omit = omit,
        value_type: Literal["TEXT", "NUMBER", "BOOLEAN", "DATE", "PHONE_NUMBER", "EMAIL", "CURRENCY"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerUpdateFieldResponse:
        """Changes a field.

        A built-in field can only be turned on or off for your project;
        any field of your project's own can change everything but its key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._patch(
            f"/v1/customer/fields/{key}",
            body=maybe_transform(
                {
                    "description": description,
                    "extract": extract,
                    "label": label,
                    "value_type": value_type,
                },
                customer_update_field_params.CustomerUpdateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerUpdateFieldResponse,
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
    ) -> CustomerUpdateNotesResponse:
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
            f"/v1/customer/{customer_profile_id}/notes",
            body=maybe_transform({"notes": notes}, customer_update_notes_params.CustomerUpdateNotesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerUpdateNotesResponse,
        )


class AsyncCustomerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncCustomerResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        agent_id: str | Omit = omit,
        field_key: str | Omit = omit,
        field_operator: Literal["EQUALS", "NOT_EQUALS", "CONTAINS", "STARTS_WITH", "IS_SET", "IS_NOT_SET"]
        | Omit = omit,
        field_value: str | Omit = omit,
        include_no_data: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        modality: Literal["voice", "chat", "call"] | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerListResponse:
        """Returns the people who have talked to your agents in this project.

        Customers we
        hold nothing about beyond their identifier are left out unless includeNoData is
        true.

        Args:
          field_key: Filter by this field, a key from GET /v1/customer/fields. Use with fieldOperator
              and, unless checking presence, fieldValue.

          field_operator: How fieldValue is compared, ignoring case. NOT_EQUALS includes customers without
              the field.

          include_no_data: Include customers we hold nothing about beyond their identifier. Defaults to
              false.

          sort_by: lastSeenAt (the default), firstSeenAt, conversationCount, voiceCount, chatCount,
              talkTimeMs or displayName, or field.<key> (for example field.COMPANY) to sort by
              a field's value. Field keys come from GET /v1/customer/fields. Customers without
              a value sort last.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/customer",
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
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=CustomerListResponse,
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
    ) -> CustomerDeleteResponse:
        """
        Permanently removes the customer, with their fields, evidence and notes.
        Conversations are kept. A new conversation from the same identifier starts a new
        customer.

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
            f"/v1/customer/{customer_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerDeleteResponse,
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
    ) -> CustomerClearAttributeResponse:
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
            f"/v1/customer/{customer_profile_id}/attributes/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerClearAttributeResponse,
        )

    async def create_field(
        self,
        *,
        extract: bool,
        key: str,
        label: str,
        value_type: Literal["TEXT", "NUMBER", "BOOLEAN", "DATE", "PHONE_NUMBER", "EMAIL", "CURRENCY"],
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerCreateFieldResponse:
        """Adds a field of your project's own.

        With extract on, conversations fill it from
        what customers say, guided by its description.

        Args:
          extract: Whether conversations fill this field

          key: Starts with a letter; letters, numbers and underscores only. Fixed once created.

          description: What the agent listens for in a conversation. Required when extract is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/customer/fields",
            body=await async_maybe_transform(
                {
                    "extract": extract,
                    "key": key,
                    "label": label,
                    "value_type": value_type,
                    "description": description,
                },
                customer_create_field_params.CustomerCreateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerCreateFieldResponse,
        )

    async def delete_field(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerDeleteFieldResponse:
        """Deletes a field of your project's own.

        Its values stop showing on customers. A
        built-in field cannot be deleted; turn it off instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._delete(
            f"/v1/customer/fields/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerDeleteFieldResponse,
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
    ) -> CustomerGetByIDResponse:
        """
        Get a customer

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
            f"/v1/customer/{customer_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerGetByIDResponse,
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
    ) -> CustomerListConversationsResponse:
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
            f"/v1/customer/{customer_profile_id}/conversations",
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
                    customer_list_conversations_params.CustomerListConversationsParams,
                ),
            ),
            cast_to=CustomerListConversationsResponse,
        )

    async def list_fields(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerListFieldsResponse:
        """The fields this project's customers can hold, in display order.

        Use a field's
        key to filter, sort and set attributes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/customer/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerListFieldsResponse,
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
    ) -> CustomerSetAttributeResponse:
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
            f"/v1/customer/{customer_profile_id}/attributes/{key}",
            body=await async_maybe_transform(
                {"value": value}, customer_set_attribute_params.CustomerSetAttributeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSetAttributeResponse,
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
    ) -> CustomerUnlockAttributeResponse:
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
            f"/v1/customer/{customer_profile_id}/attributes/{key}/unlock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerUnlockAttributeResponse,
        )

    async def update_field(
        self,
        key: str,
        *,
        description: Optional[str] | Omit = omit,
        extract: bool | Omit = omit,
        label: str | Omit = omit,
        value_type: Literal["TEXT", "NUMBER", "BOOLEAN", "DATE", "PHONE_NUMBER", "EMAIL", "CURRENCY"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerUpdateFieldResponse:
        """Changes a field.

        A built-in field can only be turned on or off for your project;
        any field of your project's own can change everything but its key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._patch(
            f"/v1/customer/fields/{key}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "extract": extract,
                    "label": label,
                    "value_type": value_type,
                },
                customer_update_field_params.CustomerUpdateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerUpdateFieldResponse,
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
    ) -> CustomerUpdateNotesResponse:
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
            f"/v1/customer/{customer_profile_id}/notes",
            body=await async_maybe_transform({"notes": notes}, customer_update_notes_params.CustomerUpdateNotesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerUpdateNotesResponse,
        )


class CustomerResourceWithRawResponse:
    def __init__(self, customer: CustomerResource) -> None:
        self._customer = customer

        self.list = to_raw_response_wrapper(
            customer.list,
        )
        self.delete = to_raw_response_wrapper(
            customer.delete,
        )
        self.clear_attribute = to_raw_response_wrapper(
            customer.clear_attribute,
        )
        self.create_field = to_raw_response_wrapper(
            customer.create_field,
        )
        self.delete_field = to_raw_response_wrapper(
            customer.delete_field,
        )
        self.get_by_id = to_raw_response_wrapper(
            customer.get_by_id,
        )
        self.list_conversations = to_raw_response_wrapper(
            customer.list_conversations,
        )
        self.list_fields = to_raw_response_wrapper(
            customer.list_fields,
        )
        self.set_attribute = to_raw_response_wrapper(
            customer.set_attribute,
        )
        self.unlock_attribute = to_raw_response_wrapper(
            customer.unlock_attribute,
        )
        self.update_field = to_raw_response_wrapper(
            customer.update_field,
        )
        self.update_notes = to_raw_response_wrapper(
            customer.update_notes,
        )


class AsyncCustomerResourceWithRawResponse:
    def __init__(self, customer: AsyncCustomerResource) -> None:
        self._customer = customer

        self.list = async_to_raw_response_wrapper(
            customer.list,
        )
        self.delete = async_to_raw_response_wrapper(
            customer.delete,
        )
        self.clear_attribute = async_to_raw_response_wrapper(
            customer.clear_attribute,
        )
        self.create_field = async_to_raw_response_wrapper(
            customer.create_field,
        )
        self.delete_field = async_to_raw_response_wrapper(
            customer.delete_field,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            customer.get_by_id,
        )
        self.list_conversations = async_to_raw_response_wrapper(
            customer.list_conversations,
        )
        self.list_fields = async_to_raw_response_wrapper(
            customer.list_fields,
        )
        self.set_attribute = async_to_raw_response_wrapper(
            customer.set_attribute,
        )
        self.unlock_attribute = async_to_raw_response_wrapper(
            customer.unlock_attribute,
        )
        self.update_field = async_to_raw_response_wrapper(
            customer.update_field,
        )
        self.update_notes = async_to_raw_response_wrapper(
            customer.update_notes,
        )


class CustomerResourceWithStreamingResponse:
    def __init__(self, customer: CustomerResource) -> None:
        self._customer = customer

        self.list = to_streamed_response_wrapper(
            customer.list,
        )
        self.delete = to_streamed_response_wrapper(
            customer.delete,
        )
        self.clear_attribute = to_streamed_response_wrapper(
            customer.clear_attribute,
        )
        self.create_field = to_streamed_response_wrapper(
            customer.create_field,
        )
        self.delete_field = to_streamed_response_wrapper(
            customer.delete_field,
        )
        self.get_by_id = to_streamed_response_wrapper(
            customer.get_by_id,
        )
        self.list_conversations = to_streamed_response_wrapper(
            customer.list_conversations,
        )
        self.list_fields = to_streamed_response_wrapper(
            customer.list_fields,
        )
        self.set_attribute = to_streamed_response_wrapper(
            customer.set_attribute,
        )
        self.unlock_attribute = to_streamed_response_wrapper(
            customer.unlock_attribute,
        )
        self.update_field = to_streamed_response_wrapper(
            customer.update_field,
        )
        self.update_notes = to_streamed_response_wrapper(
            customer.update_notes,
        )


class AsyncCustomerResourceWithStreamingResponse:
    def __init__(self, customer: AsyncCustomerResource) -> None:
        self._customer = customer

        self.list = async_to_streamed_response_wrapper(
            customer.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            customer.delete,
        )
        self.clear_attribute = async_to_streamed_response_wrapper(
            customer.clear_attribute,
        )
        self.create_field = async_to_streamed_response_wrapper(
            customer.create_field,
        )
        self.delete_field = async_to_streamed_response_wrapper(
            customer.delete_field,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            customer.get_by_id,
        )
        self.list_conversations = async_to_streamed_response_wrapper(
            customer.list_conversations,
        )
        self.list_fields = async_to_streamed_response_wrapper(
            customer.list_fields,
        )
        self.set_attribute = async_to_streamed_response_wrapper(
            customer.set_attribute,
        )
        self.unlock_attribute = async_to_streamed_response_wrapper(
            customer.unlock_attribute,
        )
        self.update_field = async_to_streamed_response_wrapper(
            customer.update_field,
        )
        self.update_notes = async_to_streamed_response_wrapper(
            customer.update_notes,
        )
