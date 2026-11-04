# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    calendar_connection_list_params,
    calendar_connection_create_params,
    calendar_connection_update_params,
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
from ..types.calendar_connection_list_response import CalendarConnectionListResponse
from ..types.calendar_connection_check_response import CalendarConnectionCheckResponse
from ..types.calendar_connection_create_response import CalendarConnectionCreateResponse
from ..types.calendar_connection_delete_response import CalendarConnectionDeleteResponse
from ..types.calendar_connection_update_response import CalendarConnectionUpdateResponse
from ..types.calendar_connection_get_by_id_response import CalendarConnectionGetByIDResponse
from ..types.calendar_connection_get_target_response import CalendarConnectionGetTargetResponse
from ..types.calendar_connection_list_targets_response import CalendarConnectionListTargetsResponse

__all__ = ["CalendarConnectionResource", "AsyncCalendarConnectionResource"]


class CalendarConnectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CalendarConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return CalendarConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalendarConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return CalendarConnectionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        api_key: str,
        label: str,
        provider: Literal["CAL_COM", "GOOGLE", "CALENDLY"],
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionCreateResponse:
        """
        Verifies the credential against the provider and, only if it works, stores it
        encrypted. A credential the provider rejects is a 400 and no connection is
        created: a connection that has never worked would next be exercised by an
        inbound call at 2am, with nobody there to fix it.

        Args:
          api_key: For CAL_COM: a Cal.com API key (starts with `cal_`). It is verified against
              Cal.com before anything is stored, so an invalid key is a 400 and no connection
              is created. Stored encrypted and never returned.

          label: Customer-facing name for this account, unique within the project. Required.

          provider: Who holds the calendar. CAL_COM is the only provider that can be connected
              today; GOOGLE and CALENDLY are described by `capabilities` but not yet
              connectable.

          timezone: The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
              Omit to adopt the provider account’s own timezone. A fixed offset such as
              `-08:00` is rejected: it does not observe DST.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/calendar-connection",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "label": label,
                    "provider": provider,
                    "timezone": timezone,
                },
                calendar_connection_create_params.CalendarConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCreateResponse,
        )

    def update(
        self,
        connection_id: str,
        *,
        api_key: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionUpdateResponse:
        """
        Renames a connection, changes the timezone slots are offered in, or rotates the
        credential. A rotated credential is verified first, and a verified credential
        returns the connection to ACTIVE.

        Args:
          api_key: Rotate the credential. The new key is verified before it is stored, and a
              verified key returns the connection to ACTIVE, which is how a connection
              recovers from INVALID_CREDENTIALS.

          label: Rename the connection.

          timezone: Change the named IANA timezone slots are offered in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._patch(
            f"/v1/calendar-connection/{connection_id}",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "label": label,
                    "timezone": timezone,
                },
                calendar_connection_update_params.CalendarConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        provider: Literal["CAL_COM", "GOOGLE", "CALENDLY"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionListResponse:
        """Returns every calendar connection in the authenticated project, by label.

        A
        project has a handful of these, so the list is not paginated:
        `pagination.hasMore` is always false.

        Args:
          provider: Who holds the calendar. CAL_COM is the only provider that can be connected
              today; GOOGLE and CALENDLY are described by `capabilities` but not yet
              connectable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/calendar-connection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"provider": provider}, calendar_connection_list_params.CalendarConnectionListParams
                ),
            ),
            cast_to=CalendarConnectionListResponse,
        )

    def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionDeleteResponse:
        """Disconnects the calendar and destroys the stored credential.

        A credential the
        customer deleted should stop existing, so this is not an archive. Appointments
        already recorded against the connection are kept, so a booking stays explainable
        after the calendar is disconnected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._delete(
            f"/v1/calendar-connection/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionDeleteResponse,
        )

    def check(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionCheckResponse:
        """
        Re-verifies the stored credential against the provider and records the result on
        the connection. A credential the provider rejects sets `status` to
        INVALID_CREDENTIALS. A provider outage is a 500 and leaves the status untouched:
        being unable to reach the provider is not evidence that the customer’s
        credential is bad.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            f"/v1/calendar-connection/{connection_id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCheckResponse,
        )

    def get_by_id(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionGetByIDResponse:
        """Returns one calendar connection.

        The stored credential is never included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/v1/calendar-connection/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionGetByIDResponse,
        )

    def get_target(
        self,
        target_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionGetTargetResponse:
        """
        The same entry as the list, plus what it demands of a booker.
        `requiresAttendeeEmail` is the field that decides an agent’s design: the
        attendee object itself needs only a name and a timezone, but an event type can
        declare email required, and an agent that cannot collect one simply cannot book
        on it. Read this when configuring a calendar tool, not after a caller is already
        waiting. Costs one provider call more than the list, which is why the list does
        not fold it in.

        Args:
          connection_id: Calendar connection ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/v1/calendar-connection/{connection_id}/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionGetTargetResponse,
        )

    def list_targets(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionListTargetsResponse:
        """
        What an agent can be pointed at on this connection: Cal.com event types today,
        Google calendars when that lands. Read live from the provider, so an event type
        added since you connected is here without reconnecting. Each entry carries a
        `target` ready to put on a calendar tool, so nothing has to assemble one by
        hand.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/v1/calendar-connection/{connection_id}/targets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionListTargetsResponse,
        )


class AsyncCalendarConnectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCalendarConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalendarConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalendarConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncCalendarConnectionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        api_key: str,
        label: str,
        provider: Literal["CAL_COM", "GOOGLE", "CALENDLY"],
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionCreateResponse:
        """
        Verifies the credential against the provider and, only if it works, stores it
        encrypted. A credential the provider rejects is a 400 and no connection is
        created: a connection that has never worked would next be exercised by an
        inbound call at 2am, with nobody there to fix it.

        Args:
          api_key: For CAL_COM: a Cal.com API key (starts with `cal_`). It is verified against
              Cal.com before anything is stored, so an invalid key is a 400 and no connection
              is created. Stored encrypted and never returned.

          label: Customer-facing name for this account, unique within the project. Required.

          provider: Who holds the calendar. CAL_COM is the only provider that can be connected
              today; GOOGLE and CALENDLY are described by `capabilities` but not yet
              connectable.

          timezone: The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
              Omit to adopt the provider account’s own timezone. A fixed offset such as
              `-08:00` is rejected: it does not observe DST.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/calendar-connection",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "label": label,
                    "provider": provider,
                    "timezone": timezone,
                },
                calendar_connection_create_params.CalendarConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCreateResponse,
        )

    async def update(
        self,
        connection_id: str,
        *,
        api_key: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionUpdateResponse:
        """
        Renames a connection, changes the timezone slots are offered in, or rotates the
        credential. A rotated credential is verified first, and a verified credential
        returns the connection to ACTIVE.

        Args:
          api_key: Rotate the credential. The new key is verified before it is stored, and a
              verified key returns the connection to ACTIVE, which is how a connection
              recovers from INVALID_CREDENTIALS.

          label: Rename the connection.

          timezone: Change the named IANA timezone slots are offered in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._patch(
            f"/v1/calendar-connection/{connection_id}",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "label": label,
                    "timezone": timezone,
                },
                calendar_connection_update_params.CalendarConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionUpdateResponse,
        )

    async def list(
        self,
        *,
        provider: Literal["CAL_COM", "GOOGLE", "CALENDLY"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionListResponse:
        """Returns every calendar connection in the authenticated project, by label.

        A
        project has a handful of these, so the list is not paginated:
        `pagination.hasMore` is always false.

        Args:
          provider: Who holds the calendar. CAL_COM is the only provider that can be connected
              today; GOOGLE and CALENDLY are described by `capabilities` but not yet
              connectable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/calendar-connection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"provider": provider}, calendar_connection_list_params.CalendarConnectionListParams
                ),
            ),
            cast_to=CalendarConnectionListResponse,
        )

    async def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionDeleteResponse:
        """Disconnects the calendar and destroys the stored credential.

        A credential the
        customer deleted should stop existing, so this is not an archive. Appointments
        already recorded against the connection are kept, so a booking stays explainable
        after the calendar is disconnected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._delete(
            f"/v1/calendar-connection/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionDeleteResponse,
        )

    async def check(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionCheckResponse:
        """
        Re-verifies the stored credential against the provider and records the result on
        the connection. A credential the provider rejects sets `status` to
        INVALID_CREDENTIALS. A provider outage is a 500 and leaves the status untouched:
        being unable to reach the provider is not evidence that the customer’s
        credential is bad.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            f"/v1/calendar-connection/{connection_id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCheckResponse,
        )

    async def get_by_id(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionGetByIDResponse:
        """Returns one calendar connection.

        The stored credential is never included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/v1/calendar-connection/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionGetByIDResponse,
        )

    async def get_target(
        self,
        target_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionGetTargetResponse:
        """
        The same entry as the list, plus what it demands of a booker.
        `requiresAttendeeEmail` is the field that decides an agent’s design: the
        attendee object itself needs only a name and a timezone, but an event type can
        declare email required, and an agent that cannot collect one simply cannot book
        on it. Read this when configuring a calendar tool, not after a caller is already
        waiting. Costs one provider call more than the list, which is why the list does
        not fold it in.

        Args:
          connection_id: Calendar connection ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/v1/calendar-connection/{connection_id}/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionGetTargetResponse,
        )

    async def list_targets(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionListTargetsResponse:
        """
        What an agent can be pointed at on this connection: Cal.com event types today,
        Google calendars when that lands. Read live from the provider, so an event type
        added since you connected is here without reconnecting. Each entry carries a
        `target` ready to put on a calendar tool, so nothing has to assemble one by
        hand.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/v1/calendar-connection/{connection_id}/targets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionListTargetsResponse,
        )


class CalendarConnectionResourceWithRawResponse:
    def __init__(self, calendar_connection: CalendarConnectionResource) -> None:
        self._calendar_connection = calendar_connection

        self.create = to_raw_response_wrapper(
            calendar_connection.create,
        )
        self.update = to_raw_response_wrapper(
            calendar_connection.update,
        )
        self.list = to_raw_response_wrapper(
            calendar_connection.list,
        )
        self.delete = to_raw_response_wrapper(
            calendar_connection.delete,
        )
        self.check = to_raw_response_wrapper(
            calendar_connection.check,
        )
        self.get_by_id = to_raw_response_wrapper(
            calendar_connection.get_by_id,
        )
        self.get_target = to_raw_response_wrapper(
            calendar_connection.get_target,
        )
        self.list_targets = to_raw_response_wrapper(
            calendar_connection.list_targets,
        )


class AsyncCalendarConnectionResourceWithRawResponse:
    def __init__(self, calendar_connection: AsyncCalendarConnectionResource) -> None:
        self._calendar_connection = calendar_connection

        self.create = async_to_raw_response_wrapper(
            calendar_connection.create,
        )
        self.update = async_to_raw_response_wrapper(
            calendar_connection.update,
        )
        self.list = async_to_raw_response_wrapper(
            calendar_connection.list,
        )
        self.delete = async_to_raw_response_wrapper(
            calendar_connection.delete,
        )
        self.check = async_to_raw_response_wrapper(
            calendar_connection.check,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            calendar_connection.get_by_id,
        )
        self.get_target = async_to_raw_response_wrapper(
            calendar_connection.get_target,
        )
        self.list_targets = async_to_raw_response_wrapper(
            calendar_connection.list_targets,
        )


class CalendarConnectionResourceWithStreamingResponse:
    def __init__(self, calendar_connection: CalendarConnectionResource) -> None:
        self._calendar_connection = calendar_connection

        self.create = to_streamed_response_wrapper(
            calendar_connection.create,
        )
        self.update = to_streamed_response_wrapper(
            calendar_connection.update,
        )
        self.list = to_streamed_response_wrapper(
            calendar_connection.list,
        )
        self.delete = to_streamed_response_wrapper(
            calendar_connection.delete,
        )
        self.check = to_streamed_response_wrapper(
            calendar_connection.check,
        )
        self.get_by_id = to_streamed_response_wrapper(
            calendar_connection.get_by_id,
        )
        self.get_target = to_streamed_response_wrapper(
            calendar_connection.get_target,
        )
        self.list_targets = to_streamed_response_wrapper(
            calendar_connection.list_targets,
        )


class AsyncCalendarConnectionResourceWithStreamingResponse:
    def __init__(self, calendar_connection: AsyncCalendarConnectionResource) -> None:
        self._calendar_connection = calendar_connection

        self.create = async_to_streamed_response_wrapper(
            calendar_connection.create,
        )
        self.update = async_to_streamed_response_wrapper(
            calendar_connection.update,
        )
        self.list = async_to_streamed_response_wrapper(
            calendar_connection.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            calendar_connection.delete,
        )
        self.check = async_to_streamed_response_wrapper(
            calendar_connection.check,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            calendar_connection.get_by_id,
        )
        self.get_target = async_to_streamed_response_wrapper(
            calendar_connection.get_target,
        )
        self.list_targets = async_to_streamed_response_wrapper(
            calendar_connection.list_targets,
        )
