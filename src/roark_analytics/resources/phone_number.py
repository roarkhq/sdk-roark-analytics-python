# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    phone_number_list_params,
    phone_number_create_params,
    phone_number_update_params,
    phone_number_list_available_params,
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
from ..types.phone_number_list_response import PhoneNumberListResponse
from ..types.phone_number_create_response import PhoneNumberCreateResponse
from ..types.phone_number_delete_response import PhoneNumberDeleteResponse
from ..types.phone_number_update_response import PhoneNumberUpdateResponse
from ..types.phone_number_get_allowance_response import PhoneNumberGetAllowanceResponse
from ..types.phone_number_list_available_response import PhoneNumberListAvailableResponse

__all__ = ["PhoneNumberResource", "AsyncPhoneNumberResource"]


class PhoneNumberResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return PhoneNumberResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_id: str | Omit = omit,
        auto_pick: phone_number_create_params.AutoPick | Omit = omit,
        country: Literal["US", "CA"] | Omit = omit,
        e164: str | Omit = omit,
        expect_free: bool | Omit = omit,
        expect_monthly_rent_micros: int | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberCreateResponse:
        """
        Buys a number from the carrier for this project: the one named by e164, or one
        Roark picks to match autoPick (trying the next match if the carrier has just
        sold one). Free inside the plan allowance; past it, the first month of rent is
        charged now and monthly after that.

        Args:
          agent_id: The agent to assign the number to

          auto_pick: Let Roark pick a matching number instead of naming one. Give this or e164.

          country: The country of the number given by e164 (default: US). An auto-picked number
              uses autoPick.country.

          e164: The number to buy, in E.164 format, from a search result. Give this or autoPick.

          expect_free: Whether you expect this number to be free (from the allowance). The purchase is
              refused with 409 if that has changed since you checked.

          expect_monthly_rent_micros: The monthly rent you expect for a paid number, in micros (from the allowance).
              The purchase is refused with 409 if that has changed since you checked.

          name: A label for the number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/phone-number",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "auto_pick": auto_pick,
                    "country": country,
                    "e164": e164,
                    "expect_free": expect_free,
                    "expect_monthly_rent_micros": expect_monthly_rent_micros,
                    "name": name,
                },
                phone_number_create_params.PhoneNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCreateResponse,
        )

    def update(
        self,
        phone_number_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberUpdateResponse:
        """Relabels a number or changes which agent it is assigned to.

        A field left out is
        untouched; null clears it.

        Args:
          agent_id: Agent to assign the number to; null unassigns, omit to leave it alone

          name: New label; null clears it, omit to leave it alone

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return self._put(
            f"/v1/phone-number/{phone_number_id}",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "name": name,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberUpdateResponse,
        )

    def list(
        self,
        *,
        agent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberListResponse:
        """
        Returns the phone numbers the project owns, oldest first, with the agent each is
        assigned to.

        Args:
          agent_id: Only the numbers assigned to this agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/phone-number",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_id": agent_id}, phone_number_list_params.PhoneNumberListParams),
            ),
            cast_to=PhoneNumberListResponse,
        )

    def delete(
        self,
        phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberDeleteResponse:
        """Gives the number back to the carrier.

        This cannot be undone: rent stops today
        and nothing is refunded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return self._delete(
            f"/v1/phone-number/{phone_number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberDeleteResponse,
        )

    def get_allowance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberGetAllowanceResponse:
        """
        Returns how many numbers the organization gets for free, how many it holds, what
        a paid number costs a month, and whether a purchase would be admitted right now.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/phone-number/allowance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberGetAllowanceResponse,
        )

    def list_available(
        self,
        *,
        area_code: str | Omit = omit,
        contains: str | Omit = omit,
        country: Literal["US", "CA"] | Omit = omit,
        limit: int | Omit = omit,
        number_type: Literal["LOCAL", "TOLL_FREE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberListAvailableResponse:
        """
        Returns US or Canadian numbers the carrier has for sale, local or toll-free,
        narrowed by area code or by digits the number must contain. When an area code
        has no numbers, nearby ones are returned flagged bestEffort; an empty list means
        nothing matched. Buy one with POST /v1/phone-number, or let Roark pick with
        autoPick.

        Args:
          area_code: Three-digit area code, or a toll-free prefix such as 800. When it has no
              numbers, nearby ones are returned instead, flagged bestEffort.

          contains: Digits or letters the number must contain (1 to 7, * matches any digit)

          country: ISO 3166-1 alpha-2 country of the number: US or CA

          limit: Maximum number of results (default: 20, max: 100)

          number_type: LOCAL for a number in an area code, TOLL_FREE for one from the shared US and
              Canada toll-free pool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/phone-number/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "area_code": area_code,
                        "contains": contains,
                        "country": country,
                        "limit": limit,
                        "number_type": number_type,
                    },
                    phone_number_list_available_params.PhoneNumberListAvailableParams,
                ),
            ),
            cast_to=PhoneNumberListAvailableResponse,
        )


class AsyncPhoneNumberResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncPhoneNumberResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_id: str | Omit = omit,
        auto_pick: phone_number_create_params.AutoPick | Omit = omit,
        country: Literal["US", "CA"] | Omit = omit,
        e164: str | Omit = omit,
        expect_free: bool | Omit = omit,
        expect_monthly_rent_micros: int | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberCreateResponse:
        """
        Buys a number from the carrier for this project: the one named by e164, or one
        Roark picks to match autoPick (trying the next match if the carrier has just
        sold one). Free inside the plan allowance; past it, the first month of rent is
        charged now and monthly after that.

        Args:
          agent_id: The agent to assign the number to

          auto_pick: Let Roark pick a matching number instead of naming one. Give this or e164.

          country: The country of the number given by e164 (default: US). An auto-picked number
              uses autoPick.country.

          e164: The number to buy, in E.164 format, from a search result. Give this or autoPick.

          expect_free: Whether you expect this number to be free (from the allowance). The purchase is
              refused with 409 if that has changed since you checked.

          expect_monthly_rent_micros: The monthly rent you expect for a paid number, in micros (from the allowance).
              The purchase is refused with 409 if that has changed since you checked.

          name: A label for the number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/phone-number",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "auto_pick": auto_pick,
                    "country": country,
                    "e164": e164,
                    "expect_free": expect_free,
                    "expect_monthly_rent_micros": expect_monthly_rent_micros,
                    "name": name,
                },
                phone_number_create_params.PhoneNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCreateResponse,
        )

    async def update(
        self,
        phone_number_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberUpdateResponse:
        """Relabels a number or changes which agent it is assigned to.

        A field left out is
        untouched; null clears it.

        Args:
          agent_id: Agent to assign the number to; null unassigns, omit to leave it alone

          name: New label; null clears it, omit to leave it alone

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return await self._put(
            f"/v1/phone-number/{phone_number_id}",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "name": name,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberUpdateResponse,
        )

    async def list(
        self,
        *,
        agent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberListResponse:
        """
        Returns the phone numbers the project owns, oldest first, with the agent each is
        assigned to.

        Args:
          agent_id: Only the numbers assigned to this agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/phone-number",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"agent_id": agent_id}, phone_number_list_params.PhoneNumberListParams
                ),
            ),
            cast_to=PhoneNumberListResponse,
        )

    async def delete(
        self,
        phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberDeleteResponse:
        """Gives the number back to the carrier.

        This cannot be undone: rent stops today
        and nothing is refunded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return await self._delete(
            f"/v1/phone-number/{phone_number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberDeleteResponse,
        )

    async def get_allowance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberGetAllowanceResponse:
        """
        Returns how many numbers the organization gets for free, how many it holds, what
        a paid number costs a month, and whether a purchase would be admitted right now.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/phone-number/allowance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberGetAllowanceResponse,
        )

    async def list_available(
        self,
        *,
        area_code: str | Omit = omit,
        contains: str | Omit = omit,
        country: Literal["US", "CA"] | Omit = omit,
        limit: int | Omit = omit,
        number_type: Literal["LOCAL", "TOLL_FREE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberListAvailableResponse:
        """
        Returns US or Canadian numbers the carrier has for sale, local or toll-free,
        narrowed by area code or by digits the number must contain. When an area code
        has no numbers, nearby ones are returned flagged bestEffort; an empty list means
        nothing matched. Buy one with POST /v1/phone-number, or let Roark pick with
        autoPick.

        Args:
          area_code: Three-digit area code, or a toll-free prefix such as 800. When it has no
              numbers, nearby ones are returned instead, flagged bestEffort.

          contains: Digits or letters the number must contain (1 to 7, * matches any digit)

          country: ISO 3166-1 alpha-2 country of the number: US or CA

          limit: Maximum number of results (default: 20, max: 100)

          number_type: LOCAL for a number in an area code, TOLL_FREE for one from the shared US and
              Canada toll-free pool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/phone-number/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "area_code": area_code,
                        "contains": contains,
                        "country": country,
                        "limit": limit,
                        "number_type": number_type,
                    },
                    phone_number_list_available_params.PhoneNumberListAvailableParams,
                ),
            ),
            cast_to=PhoneNumberListAvailableResponse,
        )


class PhoneNumberResourceWithRawResponse:
    def __init__(self, phone_number: PhoneNumberResource) -> None:
        self._phone_number = phone_number

        self.create = to_raw_response_wrapper(
            phone_number.create,
        )
        self.update = to_raw_response_wrapper(
            phone_number.update,
        )
        self.list = to_raw_response_wrapper(
            phone_number.list,
        )
        self.delete = to_raw_response_wrapper(
            phone_number.delete,
        )
        self.get_allowance = to_raw_response_wrapper(
            phone_number.get_allowance,
        )
        self.list_available = to_raw_response_wrapper(
            phone_number.list_available,
        )


class AsyncPhoneNumberResourceWithRawResponse:
    def __init__(self, phone_number: AsyncPhoneNumberResource) -> None:
        self._phone_number = phone_number

        self.create = async_to_raw_response_wrapper(
            phone_number.create,
        )
        self.update = async_to_raw_response_wrapper(
            phone_number.update,
        )
        self.list = async_to_raw_response_wrapper(
            phone_number.list,
        )
        self.delete = async_to_raw_response_wrapper(
            phone_number.delete,
        )
        self.get_allowance = async_to_raw_response_wrapper(
            phone_number.get_allowance,
        )
        self.list_available = async_to_raw_response_wrapper(
            phone_number.list_available,
        )


class PhoneNumberResourceWithStreamingResponse:
    def __init__(self, phone_number: PhoneNumberResource) -> None:
        self._phone_number = phone_number

        self.create = to_streamed_response_wrapper(
            phone_number.create,
        )
        self.update = to_streamed_response_wrapper(
            phone_number.update,
        )
        self.list = to_streamed_response_wrapper(
            phone_number.list,
        )
        self.delete = to_streamed_response_wrapper(
            phone_number.delete,
        )
        self.get_allowance = to_streamed_response_wrapper(
            phone_number.get_allowance,
        )
        self.list_available = to_streamed_response_wrapper(
            phone_number.list_available,
        )


class AsyncPhoneNumberResourceWithStreamingResponse:
    def __init__(self, phone_number: AsyncPhoneNumberResource) -> None:
        self._phone_number = phone_number

        self.create = async_to_streamed_response_wrapper(
            phone_number.create,
        )
        self.update = async_to_streamed_response_wrapper(
            phone_number.update,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_number.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            phone_number.delete,
        )
        self.get_allowance = async_to_streamed_response_wrapper(
            phone_number.get_allowance,
        )
        self.list_available = async_to_streamed_response_wrapper(
            phone_number.list_available,
        )
