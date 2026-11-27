# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    calendar_connection_list_params,
    calendar_connection_create_params,
    calendar_connection_update_params,
    calendar_connection_create_target_params,
    calendar_connection_update_target_params,
    calendar_connection_start_google_oauth_params,
    calendar_connection_start_calendly_oauth_params,
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
from ..types.calendar_connection_create_target_response import CalendarConnectionCreateTargetResponse
from ..types.calendar_connection_delete_target_response import CalendarConnectionDeleteTargetResponse
from ..types.calendar_connection_update_target_response import CalendarConnectionUpdateTargetResponse
from ..types.calendar_connection_list_calendars_response import CalendarConnectionListCalendarsResponse
from ..types.calendar_connection_start_google_oauth_response import CalendarConnectionStartGoogleOauthResponse
from ..types.calendar_connection_start_calendly_oauth_response import CalendarConnectionStartCalendlyOauthResponse

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
        provider: Literal["CAL_COM", "GOOGLE", "CALENDLY", "GO_HIGH_LEVEL"],
        go_high_level_location: Optional[str] | Omit = omit,
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
          api_key: The provider account’s API key. For CAL_COM, a Cal.com API key (starts with
              `cal_`). For GO_HIGH_LEVEL, a sub-account Private Integration Token, which must
              carry the `calendars.readonly`, `calendars/events.readonly`,
              `calendars/events.write`, `contacts.readonly`, `contacts.write` and
              `locations.readonly` scopes. It is verified against the provider before anything
              is stored, so an invalid key is a 400 and no connection is created. Stored
              encrypted and never returned.

          label: Customer-facing name for this account, unique within the project. Required.

          provider: Who holds the calendar. CAL_COM and GO_HIGH_LEVEL are connected with a key,
              GO_HIGH_LEVEL also needing the sub-account the key belongs to; GOOGLE and
              CALENDLY are connected by consent, through `POST
              /v1/connections/calendar/google/authorize-url` and `POST
              /v1/connections/calendar/calendly/authorize-url`.

          go_high_level_location: Required for GO_HIGH_LEVEL and ignored by every other provider: the sub-account
              the token belongs to, for example `ve9EPM428h8vShlRW1KT`. A Private Integration
              Token does not name its own sub-account and every calendar call needs one, so
              the two are stored and verified together: a token minted in a different
              sub-account is a 400.

          timezone: The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
              Omit to adopt the provider account’s own timezone. A fixed offset such as
              `-08:00` is rejected: it does not observe DST.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connections/calendar",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "label": label,
                    "provider": provider,
                    "go_high_level_location": go_high_level_location,
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
        go_high_level_location: Optional[str] | Omit = omit,
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

          go_high_level_location: Only with `apiKey`, and only for GO_HIGH_LEVEL: the sub-account the rotated
              token belongs to. Required there because the token and the sub-account are one
              credential, so a rotation has to name both.

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
            f"/v1/connections/calendar/{connection_id}",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "go_high_level_location": go_high_level_location,
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
        provider: Literal["CAL_COM", "GOOGLE", "CALENDLY", "GO_HIGH_LEVEL"] | Omit = omit,
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
          provider: Who holds the calendar. CAL_COM and GO_HIGH_LEVEL are connected with a key,
              GO_HIGH_LEVEL also needing the sub-account the key belongs to; GOOGLE and
              CALENDLY are connected by consent, through `POST
              /v1/connections/calendar/google/authorize-url` and `POST
              /v1/connections/calendar/calendly/authorize-url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/connections/calendar",
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
        after the calendar is disconnected. Refused with a 409 while a calendar tool is
        still bound to the connection, naming the tools: point them at another calendar,
        or delete them, first. A dangling binding would otherwise be found by whoever
        next tried to ship the agent, who is not the person who disconnected the
        calendar.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._delete(
            f"/v1/connections/calendar/{connection_id}",
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
            f"/v1/connections/calendar/{connection_id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCheckResponse,
        )

    def create_target(
        self,
        connection_id: str,
        *,
        calendar_id: str,
        duration_minutes: int,
        name: str,
        all_day_events_block: Optional[bool] | Omit = omit,
        buffer_after_minutes: Optional[int] | Omit = omit,
        buffer_before_minutes: Optional[int] | Omit = omit,
        horizon_days: Optional[int] | Omit = omit,
        hours: Optional[Iterable[calendar_connection_create_target_params.Hour]] | Omit = omit,
        min_notice_minutes: Optional[int] | Omit = omit,
        slot_interval_minutes: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionCreateTargetResponse:
        """Only for a connection whose `capabilities.roarkOwnsBookingPolicy` is true.

        A
        calendar with no scheduling of its own has nothing an agent can be pointed at,
        so the thing a calendar tool books into is created here: the calendar, how long
        an appointment runs, and the hours it is offered in. The policy and the hours
        are written together, because a target with no hours offers nothing. Refused if
        the calendar is one the account can only read.

        Args:
          calendar_id: The calendar to write appointments to, from `GET
              /v1/connections/calendar/{connectionId}/calendars`. `primary` is accepted and
              stored as the account’s own id.

          name: Unique within the connection, and how a config file refers to this target.
              Letters, digits, spaces, _ or -.

          all_day_events_block: Whether an all-day event closes the day. Defaults to true, because a calendar
              marks all-day events free unless their creator says otherwise and a public
              holiday entered as one would otherwise be bookable.

          buffer_before_minutes: Dead time before an appointment, counted as busy when a slot is offered.
              Defaults to 0.

          horizon_days: How far ahead appointments may be made. Defaults to 30.

          hours: The windows of the week appointments are offered in. Omit to adopt Monday to
              Friday, 09:00 to 17:00. A target with no windows offers nothing at all, which
              reads to a caller as a permanently full diary.

          min_notice_minutes: How soon from now an appointment may be made. Defaults to 120.

          slot_interval_minutes: The grid slots are offered on. Defaults to the duration, which gives
              back-to-back appointments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            f"/v1/connections/calendar/{connection_id}/targets",
            body=maybe_transform(
                {
                    "calendar_id": calendar_id,
                    "duration_minutes": duration_minutes,
                    "name": name,
                    "all_day_events_block": all_day_events_block,
                    "buffer_after_minutes": buffer_after_minutes,
                    "buffer_before_minutes": buffer_before_minutes,
                    "horizon_days": horizon_days,
                    "hours": hours,
                    "min_notice_minutes": min_notice_minutes,
                    "slot_interval_minutes": slot_interval_minutes,
                },
                calendar_connection_create_target_params.CalendarConnectionCreateTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCreateTargetResponse,
        )

    def delete_target(
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
    ) -> CalendarConnectionDeleteTargetResponse:
        """Refused while a calendar tool still books into it, naming the tools.

        A dangling
        binding would otherwise be found by whoever next tried to ship the agent, who is
        not the person who deleted the target. Appointments already recorded against it
        are kept.

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
        return self._delete(
            f"/v1/connections/calendar/{connection_id}/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionDeleteTargetResponse,
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
            f"/v1/connections/calendar/{connection_id}",
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
            f"/v1/connections/calendar/{connection_id}/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionGetTargetResponse,
        )

    def list_calendars(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionListCalendarsResponse:
        """
        Only for a connection whose `capabilities.roarkOwnsBookingPolicy` is true: on a
        scheduling system the bookable things already exist and `GET /targets` returns
        them. Calendars the account can only read are left out rather than listed and
        refused: one would answer availability perfectly well and then fail the booking,
        mid-call, with a caller on the line.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/v1/connections/calendar/{connection_id}/calendars",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionListCalendarsResponse,
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
            f"/v1/connections/calendar/{connection_id}/targets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionListTargetsResponse,
        )

    def start_calendly_oauth(
        self,
        *,
        calendar_connection_id: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionStartCalendlyOauthResponse:
        """Returns a URL to open in a browser.

        Calendly has no credential a request body
        can carry, so connecting one is two steps: ask for this URL, let the customer
        consent, and Roark finishes the rest server-side (it exchanges the code,
        verifies the credential, reads the account’s own timezone when none was given,
        and stores the connection). Nothing is created until the customer consents, and
        a link that is not used expires. Read the result with `GET
        /v1/connections/calendar?provider=CALENDLY`.

        Args:
          calendar_connection_id: Reconnect an existing connection instead of creating one: the consent screen
              replaces that connection’s credential in place, so every tool bound to it keeps
              working. Use this when a connection reports `INVALID_CREDENTIALS`. The
              connection’s existing name and timezone are kept, so `label` is ignored when
              this is set.

          label: Customer-facing name for the connection, unique within the project. Required
              unless `calendarConnectionId` is set, and decided now because the consent screen
              has nowhere to carry it.

          timezone: The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
              Omit to adopt the Calendly account’s own. A fixed offset such as `-08:00` is
              rejected: it does not observe DST.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connections/calendar/calendly/authorize-url",
            body=maybe_transform(
                {
                    "calendar_connection_id": calendar_connection_id,
                    "label": label,
                    "timezone": timezone,
                },
                calendar_connection_start_calendly_oauth_params.CalendarConnectionStartCalendlyOauthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionStartCalendlyOauthResponse,
        )

    def start_google_oauth(
        self,
        *,
        calendar_connection_id: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        login_hint: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionStartGoogleOauthResponse:
        """Returns a URL to open in a browser.

        Google has no credential a request body can
        carry, so connecting one is two steps: ask for this URL, let the customer
        consent, and Roark finishes the rest server-side (it exchanges the code,
        verifies that both calendar permissions were granted, reads the account’s own
        timezone when none was given, and stores the connection). Nothing is created
        until the customer consents, and a link that is not used expires. Read the
        result with `GET /v1/connections/calendar?provider=GOOGLE`.

        Args:
          calendar_connection_id: Reconnect an existing connection instead of creating one: the consent screen
              replaces that connection’s credential in place, so every tool bound to it keeps
              working. Use this when a connection reports `INVALID_CREDENTIALS`. The
              connection’s existing name and timezone are kept, so `label` is ignored when
              this is set.

          label: Customer-facing name for the connection, unique within the project. Required
              unless `calendarConnectionId` is set, and decided now because the consent screen
              has nowhere to carry it.

          login_hint: The Google account to preselect on the consent screen. A hint only: it is
              ignored if the user is signed into another account, and nothing is authorized by
              it.

          timezone: The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
              Omit to adopt the Google account’s own. A fixed offset such as `-08:00` is
              rejected: it does not observe DST.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connections/calendar/google/authorize-url",
            body=maybe_transform(
                {
                    "calendar_connection_id": calendar_connection_id,
                    "label": label,
                    "login_hint": login_hint,
                    "timezone": timezone,
                },
                calendar_connection_start_google_oauth_params.CalendarConnectionStartGoogleOauthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionStartGoogleOauthResponse,
        )

    def update_target(
        self,
        target_id: str,
        *,
        connection_id: str,
        all_day_events_block: Optional[bool] | Omit = omit,
        buffer_after_minutes: Optional[int] | Omit = omit,
        buffer_before_minutes: Optional[int] | Omit = omit,
        duration_minutes: int | Omit = omit,
        horizon_days: Optional[int] | Omit = omit,
        hours: Optional[Iterable[calendar_connection_update_target_params.Hour]] | Omit = omit,
        min_notice_minutes: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        slot_interval_minutes: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionUpdateTargetResponse:
        """
        Changes what agents ALREADY PUBLISHED against this target book, with no new tool
        version, the same thing editing a Cal.com event type on cal.com does. `hours`
        replaces the whole week when present, because a rota is described as a week and
        a partial update of one window has no meaning anybody would expect. The calendar
        cannot be changed: it is the target’s identity for the booking ledger, so moving
        it would orphan every appointment made on the old one.

        Args:
          connection_id: Calendar connection ID

          all_day_events_block: Whether an all-day event closes the day. Defaults to true, because a calendar
              marks all-day events free unless their creator says otherwise and a public
              holiday entered as one would otherwise be bookable.

          buffer_before_minutes: Dead time before an appointment, counted as busy when a slot is offered.
              Defaults to 0.

          horizon_days: How far ahead appointments may be made. Defaults to 30.

          hours: The windows of the week appointments are offered in. Omit to adopt Monday to
              Friday, 09:00 to 17:00. A target with no windows offers nothing at all, which
              reads to a caller as a permanently full diary.

          min_notice_minutes: How soon from now an appointment may be made. Defaults to 120.

          name: Unique within the connection, and how a config file refers to this target.
              Letters, digits, spaces, _ or -.

          slot_interval_minutes: The grid slots are offered on. Defaults to the duration, which gives
              back-to-back appointments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._put(
            f"/v1/connections/calendar/{connection_id}/targets/{target_id}",
            body=maybe_transform(
                {
                    "all_day_events_block": all_day_events_block,
                    "buffer_after_minutes": buffer_after_minutes,
                    "buffer_before_minutes": buffer_before_minutes,
                    "duration_minutes": duration_minutes,
                    "horizon_days": horizon_days,
                    "hours": hours,
                    "min_notice_minutes": min_notice_minutes,
                    "name": name,
                    "slot_interval_minutes": slot_interval_minutes,
                },
                calendar_connection_update_target_params.CalendarConnectionUpdateTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionUpdateTargetResponse,
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
        provider: Literal["CAL_COM", "GOOGLE", "CALENDLY", "GO_HIGH_LEVEL"],
        go_high_level_location: Optional[str] | Omit = omit,
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
          api_key: The provider account’s API key. For CAL_COM, a Cal.com API key (starts with
              `cal_`). For GO_HIGH_LEVEL, a sub-account Private Integration Token, which must
              carry the `calendars.readonly`, `calendars/events.readonly`,
              `calendars/events.write`, `contacts.readonly`, `contacts.write` and
              `locations.readonly` scopes. It is verified against the provider before anything
              is stored, so an invalid key is a 400 and no connection is created. Stored
              encrypted and never returned.

          label: Customer-facing name for this account, unique within the project. Required.

          provider: Who holds the calendar. CAL_COM and GO_HIGH_LEVEL are connected with a key,
              GO_HIGH_LEVEL also needing the sub-account the key belongs to; GOOGLE and
              CALENDLY are connected by consent, through `POST
              /v1/connections/calendar/google/authorize-url` and `POST
              /v1/connections/calendar/calendly/authorize-url`.

          go_high_level_location: Required for GO_HIGH_LEVEL and ignored by every other provider: the sub-account
              the token belongs to, for example `ve9EPM428h8vShlRW1KT`. A Private Integration
              Token does not name its own sub-account and every calendar call needs one, so
              the two are stored and verified together: a token minted in a different
              sub-account is a 400.

          timezone: The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
              Omit to adopt the provider account’s own timezone. A fixed offset such as
              `-08:00` is rejected: it does not observe DST.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connections/calendar",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "label": label,
                    "provider": provider,
                    "go_high_level_location": go_high_level_location,
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
        go_high_level_location: Optional[str] | Omit = omit,
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

          go_high_level_location: Only with `apiKey`, and only for GO_HIGH_LEVEL: the sub-account the rotated
              token belongs to. Required there because the token and the sub-account are one
              credential, so a rotation has to name both.

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
            f"/v1/connections/calendar/{connection_id}",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "go_high_level_location": go_high_level_location,
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
        provider: Literal["CAL_COM", "GOOGLE", "CALENDLY", "GO_HIGH_LEVEL"] | Omit = omit,
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
          provider: Who holds the calendar. CAL_COM and GO_HIGH_LEVEL are connected with a key,
              GO_HIGH_LEVEL also needing the sub-account the key belongs to; GOOGLE and
              CALENDLY are connected by consent, through `POST
              /v1/connections/calendar/google/authorize-url` and `POST
              /v1/connections/calendar/calendly/authorize-url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/connections/calendar",
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
        after the calendar is disconnected. Refused with a 409 while a calendar tool is
        still bound to the connection, naming the tools: point them at another calendar,
        or delete them, first. A dangling binding would otherwise be found by whoever
        next tried to ship the agent, who is not the person who disconnected the
        calendar.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._delete(
            f"/v1/connections/calendar/{connection_id}",
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
            f"/v1/connections/calendar/{connection_id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCheckResponse,
        )

    async def create_target(
        self,
        connection_id: str,
        *,
        calendar_id: str,
        duration_minutes: int,
        name: str,
        all_day_events_block: Optional[bool] | Omit = omit,
        buffer_after_minutes: Optional[int] | Omit = omit,
        buffer_before_minutes: Optional[int] | Omit = omit,
        horizon_days: Optional[int] | Omit = omit,
        hours: Optional[Iterable[calendar_connection_create_target_params.Hour]] | Omit = omit,
        min_notice_minutes: Optional[int] | Omit = omit,
        slot_interval_minutes: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionCreateTargetResponse:
        """Only for a connection whose `capabilities.roarkOwnsBookingPolicy` is true.

        A
        calendar with no scheduling of its own has nothing an agent can be pointed at,
        so the thing a calendar tool books into is created here: the calendar, how long
        an appointment runs, and the hours it is offered in. The policy and the hours
        are written together, because a target with no hours offers nothing. Refused if
        the calendar is one the account can only read.

        Args:
          calendar_id: The calendar to write appointments to, from `GET
              /v1/connections/calendar/{connectionId}/calendars`. `primary` is accepted and
              stored as the account’s own id.

          name: Unique within the connection, and how a config file refers to this target.
              Letters, digits, spaces, _ or -.

          all_day_events_block: Whether an all-day event closes the day. Defaults to true, because a calendar
              marks all-day events free unless their creator says otherwise and a public
              holiday entered as one would otherwise be bookable.

          buffer_before_minutes: Dead time before an appointment, counted as busy when a slot is offered.
              Defaults to 0.

          horizon_days: How far ahead appointments may be made. Defaults to 30.

          hours: The windows of the week appointments are offered in. Omit to adopt Monday to
              Friday, 09:00 to 17:00. A target with no windows offers nothing at all, which
              reads to a caller as a permanently full diary.

          min_notice_minutes: How soon from now an appointment may be made. Defaults to 120.

          slot_interval_minutes: The grid slots are offered on. Defaults to the duration, which gives
              back-to-back appointments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            f"/v1/connections/calendar/{connection_id}/targets",
            body=await async_maybe_transform(
                {
                    "calendar_id": calendar_id,
                    "duration_minutes": duration_minutes,
                    "name": name,
                    "all_day_events_block": all_day_events_block,
                    "buffer_after_minutes": buffer_after_minutes,
                    "buffer_before_minutes": buffer_before_minutes,
                    "horizon_days": horizon_days,
                    "hours": hours,
                    "min_notice_minutes": min_notice_minutes,
                    "slot_interval_minutes": slot_interval_minutes,
                },
                calendar_connection_create_target_params.CalendarConnectionCreateTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCreateTargetResponse,
        )

    async def delete_target(
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
    ) -> CalendarConnectionDeleteTargetResponse:
        """Refused while a calendar tool still books into it, naming the tools.

        A dangling
        binding would otherwise be found by whoever next tried to ship the agent, who is
        not the person who deleted the target. Appointments already recorded against it
        are kept.

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
        return await self._delete(
            f"/v1/connections/calendar/{connection_id}/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionDeleteTargetResponse,
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
            f"/v1/connections/calendar/{connection_id}",
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
            f"/v1/connections/calendar/{connection_id}/targets/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionGetTargetResponse,
        )

    async def list_calendars(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionListCalendarsResponse:
        """
        Only for a connection whose `capabilities.roarkOwnsBookingPolicy` is true: on a
        scheduling system the bookable things already exist and `GET /targets` returns
        them. Calendars the account can only read are left out rather than listed and
        refused: one would answer availability perfectly well and then fail the booking,
        mid-call, with a caller on the line.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/v1/connections/calendar/{connection_id}/calendars",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionListCalendarsResponse,
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
            f"/v1/connections/calendar/{connection_id}/targets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionListTargetsResponse,
        )

    async def start_calendly_oauth(
        self,
        *,
        calendar_connection_id: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionStartCalendlyOauthResponse:
        """Returns a URL to open in a browser.

        Calendly has no credential a request body
        can carry, so connecting one is two steps: ask for this URL, let the customer
        consent, and Roark finishes the rest server-side (it exchanges the code,
        verifies the credential, reads the account’s own timezone when none was given,
        and stores the connection). Nothing is created until the customer consents, and
        a link that is not used expires. Read the result with `GET
        /v1/connections/calendar?provider=CALENDLY`.

        Args:
          calendar_connection_id: Reconnect an existing connection instead of creating one: the consent screen
              replaces that connection’s credential in place, so every tool bound to it keeps
              working. Use this when a connection reports `INVALID_CREDENTIALS`. The
              connection’s existing name and timezone are kept, so `label` is ignored when
              this is set.

          label: Customer-facing name for the connection, unique within the project. Required
              unless `calendarConnectionId` is set, and decided now because the consent screen
              has nowhere to carry it.

          timezone: The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
              Omit to adopt the Calendly account’s own. A fixed offset such as `-08:00` is
              rejected: it does not observe DST.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connections/calendar/calendly/authorize-url",
            body=await async_maybe_transform(
                {
                    "calendar_connection_id": calendar_connection_id,
                    "label": label,
                    "timezone": timezone,
                },
                calendar_connection_start_calendly_oauth_params.CalendarConnectionStartCalendlyOauthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionStartCalendlyOauthResponse,
        )

    async def start_google_oauth(
        self,
        *,
        calendar_connection_id: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        login_hint: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionStartGoogleOauthResponse:
        """Returns a URL to open in a browser.

        Google has no credential a request body can
        carry, so connecting one is two steps: ask for this URL, let the customer
        consent, and Roark finishes the rest server-side (it exchanges the code,
        verifies that both calendar permissions were granted, reads the account’s own
        timezone when none was given, and stores the connection). Nothing is created
        until the customer consents, and a link that is not used expires. Read the
        result with `GET /v1/connections/calendar?provider=GOOGLE`.

        Args:
          calendar_connection_id: Reconnect an existing connection instead of creating one: the consent screen
              replaces that connection’s credential in place, so every tool bound to it keeps
              working. Use this when a connection reports `INVALID_CREDENTIALS`. The
              connection’s existing name and timezone are kept, so `label` is ignored when
              this is set.

          label: Customer-facing name for the connection, unique within the project. Required
              unless `calendarConnectionId` is set, and decided now because the consent screen
              has nowhere to carry it.

          login_hint: The Google account to preselect on the consent screen. A hint only: it is
              ignored if the user is signed into another account, and nothing is authorized by
              it.

          timezone: The named IANA timezone to offer slots in, for example `America/Los_Angeles`.
              Omit to adopt the Google account’s own. A fixed offset such as `-08:00` is
              rejected: it does not observe DST.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connections/calendar/google/authorize-url",
            body=await async_maybe_transform(
                {
                    "calendar_connection_id": calendar_connection_id,
                    "label": label,
                    "login_hint": login_hint,
                    "timezone": timezone,
                },
                calendar_connection_start_google_oauth_params.CalendarConnectionStartGoogleOauthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionStartGoogleOauthResponse,
        )

    async def update_target(
        self,
        target_id: str,
        *,
        connection_id: str,
        all_day_events_block: Optional[bool] | Omit = omit,
        buffer_after_minutes: Optional[int] | Omit = omit,
        buffer_before_minutes: Optional[int] | Omit = omit,
        duration_minutes: int | Omit = omit,
        horizon_days: Optional[int] | Omit = omit,
        hours: Optional[Iterable[calendar_connection_update_target_params.Hour]] | Omit = omit,
        min_notice_minutes: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        slot_interval_minutes: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionUpdateTargetResponse:
        """
        Changes what agents ALREADY PUBLISHED against this target book, with no new tool
        version, the same thing editing a Cal.com event type on cal.com does. `hours`
        replaces the whole week when present, because a rota is described as a week and
        a partial update of one window has no meaning anybody would expect. The calendar
        cannot be changed: it is the target’s identity for the booking ledger, so moving
        it would orphan every appointment made on the old one.

        Args:
          connection_id: Calendar connection ID

          all_day_events_block: Whether an all-day event closes the day. Defaults to true, because a calendar
              marks all-day events free unless their creator says otherwise and a public
              holiday entered as one would otherwise be bookable.

          buffer_before_minutes: Dead time before an appointment, counted as busy when a slot is offered.
              Defaults to 0.

          horizon_days: How far ahead appointments may be made. Defaults to 30.

          hours: The windows of the week appointments are offered in. Omit to adopt Monday to
              Friday, 09:00 to 17:00. A target with no windows offers nothing at all, which
              reads to a caller as a permanently full diary.

          min_notice_minutes: How soon from now an appointment may be made. Defaults to 120.

          name: Unique within the connection, and how a config file refers to this target.
              Letters, digits, spaces, _ or -.

          slot_interval_minutes: The grid slots are offered on. Defaults to the duration, which gives
              back-to-back appointments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._put(
            f"/v1/connections/calendar/{connection_id}/targets/{target_id}",
            body=await async_maybe_transform(
                {
                    "all_day_events_block": all_day_events_block,
                    "buffer_after_minutes": buffer_after_minutes,
                    "buffer_before_minutes": buffer_before_minutes,
                    "duration_minutes": duration_minutes,
                    "horizon_days": horizon_days,
                    "hours": hours,
                    "min_notice_minutes": min_notice_minutes,
                    "name": name,
                    "slot_interval_minutes": slot_interval_minutes,
                },
                calendar_connection_update_target_params.CalendarConnectionUpdateTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionUpdateTargetResponse,
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
        self.create_target = to_raw_response_wrapper(
            calendar_connection.create_target,
        )
        self.delete_target = to_raw_response_wrapper(
            calendar_connection.delete_target,
        )
        self.get_by_id = to_raw_response_wrapper(
            calendar_connection.get_by_id,
        )
        self.get_target = to_raw_response_wrapper(
            calendar_connection.get_target,
        )
        self.list_calendars = to_raw_response_wrapper(
            calendar_connection.list_calendars,
        )
        self.list_targets = to_raw_response_wrapper(
            calendar_connection.list_targets,
        )
        self.start_calendly_oauth = to_raw_response_wrapper(
            calendar_connection.start_calendly_oauth,
        )
        self.start_google_oauth = to_raw_response_wrapper(
            calendar_connection.start_google_oauth,
        )
        self.update_target = to_raw_response_wrapper(
            calendar_connection.update_target,
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
        self.create_target = async_to_raw_response_wrapper(
            calendar_connection.create_target,
        )
        self.delete_target = async_to_raw_response_wrapper(
            calendar_connection.delete_target,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            calendar_connection.get_by_id,
        )
        self.get_target = async_to_raw_response_wrapper(
            calendar_connection.get_target,
        )
        self.list_calendars = async_to_raw_response_wrapper(
            calendar_connection.list_calendars,
        )
        self.list_targets = async_to_raw_response_wrapper(
            calendar_connection.list_targets,
        )
        self.start_calendly_oauth = async_to_raw_response_wrapper(
            calendar_connection.start_calendly_oauth,
        )
        self.start_google_oauth = async_to_raw_response_wrapper(
            calendar_connection.start_google_oauth,
        )
        self.update_target = async_to_raw_response_wrapper(
            calendar_connection.update_target,
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
        self.create_target = to_streamed_response_wrapper(
            calendar_connection.create_target,
        )
        self.delete_target = to_streamed_response_wrapper(
            calendar_connection.delete_target,
        )
        self.get_by_id = to_streamed_response_wrapper(
            calendar_connection.get_by_id,
        )
        self.get_target = to_streamed_response_wrapper(
            calendar_connection.get_target,
        )
        self.list_calendars = to_streamed_response_wrapper(
            calendar_connection.list_calendars,
        )
        self.list_targets = to_streamed_response_wrapper(
            calendar_connection.list_targets,
        )
        self.start_calendly_oauth = to_streamed_response_wrapper(
            calendar_connection.start_calendly_oauth,
        )
        self.start_google_oauth = to_streamed_response_wrapper(
            calendar_connection.start_google_oauth,
        )
        self.update_target = to_streamed_response_wrapper(
            calendar_connection.update_target,
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
        self.create_target = async_to_streamed_response_wrapper(
            calendar_connection.create_target,
        )
        self.delete_target = async_to_streamed_response_wrapper(
            calendar_connection.delete_target,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            calendar_connection.get_by_id,
        )
        self.get_target = async_to_streamed_response_wrapper(
            calendar_connection.get_target,
        )
        self.list_calendars = async_to_streamed_response_wrapper(
            calendar_connection.list_calendars,
        )
        self.list_targets = async_to_streamed_response_wrapper(
            calendar_connection.list_targets,
        )
        self.start_calendly_oauth = async_to_streamed_response_wrapper(
            calendar_connection.start_calendly_oauth,
        )
        self.start_google_oauth = async_to_streamed_response_wrapper(
            calendar_connection.start_google_oauth,
        )
        self.update_target = async_to_streamed_response_wrapper(
            calendar_connection.update_target,
        )
