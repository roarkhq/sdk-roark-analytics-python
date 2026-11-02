# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    live_report_run_params,
    live_report_list_params,
    live_report_create_params,
    live_report_update_params,
    live_report_list_documents_params,
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
from ..types.live_report_run_response import LiveReportRunResponse
from ..types.live_report_list_response import LiveReportListResponse
from ..types.live_report_create_response import LiveReportCreateResponse
from ..types.live_report_delete_response import LiveReportDeleteResponse
from ..types.live_report_update_response import LiveReportUpdateResponse
from ..types.live_report_get_by_id_response import LiveReportGetByIDResponse
from ..types.live_report_get_document_response import LiveReportGetDocumentResponse
from ..types.live_report_list_documents_response import LiveReportListDocumentsResponse

__all__ = ["LiveReportResource", "AsyncLiveReportResource"]


class LiveReportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiveReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return LiveReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return LiveReportResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        agent_id: Optional[str] | Omit = omit,
        cadence: Literal["DAILY", "WEEKLY", "MONTHLY"] | Omit = omit,
        dashboard_id: Optional[str] | Omit = omit,
        delivery_hour: int | Omit = omit,
        description: Optional[str] | Omit = omit,
        filters: Iterable[live_report_create_params.Filter] | Omit = omit,
        generate_now: bool | Omit = omit,
        include_transcript_excerpts: bool | Omit = omit,
        notifications: live_report_create_params.Notification | Omit = omit,
        status: Literal["ACTIVE", "PAUSED"] | Omit = omit,
        targets: Iterable[live_report_create_params.Target] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportCreateResponse:
        """Saves a report on the project's live calls.

        Simulations are never included.
        Targets are analytics measures held to a bar: a threshold metric is read as its
        pass rate (`value` is a percentage, 0-100, held AT_LEAST by default); a numeric
        metric as its average (held AT_MOST by default). Every target is read for the
        period and the period before it, so the report says whether each was met and how
        it moved. Scheduled reports are written `deliveryHour` hours into the day after
        each period ends in `timezone` (a week runs Monday to Sunday), then emailed and
        posted per `notifications`. With `generateNow` (the default) the report for the
        latest closed period is written right away and not sent.

        Args:
          generate_now: Write the report for the latest closed period right away. Default true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/live-report",
            body=maybe_transform(
                {
                    "name": name,
                    "agent_id": agent_id,
                    "cadence": cadence,
                    "dashboard_id": dashboard_id,
                    "delivery_hour": delivery_hour,
                    "description": description,
                    "filters": filters,
                    "generate_now": generate_now,
                    "include_transcript_excerpts": include_transcript_excerpts,
                    "notifications": notifications,
                    "status": status,
                    "targets": targets,
                    "timezone": timezone,
                },
                live_report_create_params.LiveReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportCreateResponse,
        )

    def update(
        self,
        report_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        cadence: Literal["DAILY", "WEEKLY", "MONTHLY"] | Omit = omit,
        dashboard_id: Optional[str] | Omit = omit,
        delivery_hour: int | Omit = omit,
        description: Optional[str] | Omit = omit,
        filters: Iterable[live_report_update_params.Filter] | Omit = omit,
        include_transcript_excerpts: bool | Omit = omit,
        name: str | Omit = omit,
        notifications: live_report_update_params.Notification | Omit = omit,
        status: Literal["ACTIVE", "PAUSED"] | Omit = omit,
        targets: Iterable[live_report_update_params.Target] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportUpdateResponse:
        """Changes the fields sent.

        Set `status` to PAUSED to stop scheduled reports.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._patch(
            f"/v1/live-report/{report_id}",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "cadence": cadence,
                    "dashboard_id": dashboard_id,
                    "delivery_hour": delivery_hour,
                    "description": description,
                    "filters": filters,
                    "include_transcript_excerpts": include_transcript_excerpts,
                    "name": name,
                    "notifications": notifications,
                    "status": status,
                    "targets": targets,
                    "timezone": timezone,
                },
                live_report_update_params.LiveReportUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportListResponse:
        """
        Lists the project's saved live call reports, newest first.

        Args:
          limit: Page size, at most 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/live-report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    live_report_list_params.LiveReportListParams,
                ),
            ),
            cast_to=LiveReportListResponse,
        )

    def delete(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportDeleteResponse:
        """
        Deletes the report and stops its scheduled reports.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._delete(
            f"/v1/live-report/{report_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportDeleteResponse,
        )

    def get_by_id(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportGetByIDResponse:
        """
        Get a live report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._get(
            f"/v1/live-report/{report_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportGetByIDResponse,
        )

    def get_document(
        self,
        document_id: str,
        *,
        report_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportGetDocumentResponse:
        """Returns one written report.

        `document` is null until `status` is READY. Theme
        excerpts and grader quotes (call transcript text) are included only for keys
        with transcript:read.

        Args:
          report_id: The live report ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._get(
            f"/v1/live-report/{report_id}/document/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportGetDocumentResponse,
        )

    def list_documents(
        self,
        report_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportListDocumentsResponse:
        """
        Lists a report's documents, newest period first.

        Args:
          limit: Page size, at most 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._get(
            f"/v1/live-report/{report_id}/document",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    live_report_list_documents_params.LiveReportListDocumentsParams,
                ),
            ),
            cast_to=LiveReportListDocumentsResponse,
        )

    def run(
        self,
        report_id: str,
        *,
        period_end: str | Omit = omit,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportRunResponse:
        """
        Writes the report now, for its latest closed period or a custom window
        (`periodStart` + `periodEnd`, at most 92 days, ended). Returns 202 with the
        document in PENDING; poll GET /v1/live-report/{reportId}/document/{documentId}
        until `status` is READY or FAILED (typically a few minutes). An identical
        request already in flight is returned as-is. A generated document is not
        emailed.

        Args:
          period_end: ISO 8601 end (exclusive) of a custom window. Requires periodStart.

          period_start: ISO 8601 start of a custom window. Omit both for the latest closed period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._post(
            f"/v1/live-report/{report_id}/generate",
            body=maybe_transform(
                {
                    "period_end": period_end,
                    "period_start": period_start,
                },
                live_report_run_params.LiveReportRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportRunResponse,
        )


class AsyncLiveReportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiveReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLiveReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncLiveReportResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        agent_id: Optional[str] | Omit = omit,
        cadence: Literal["DAILY", "WEEKLY", "MONTHLY"] | Omit = omit,
        dashboard_id: Optional[str] | Omit = omit,
        delivery_hour: int | Omit = omit,
        description: Optional[str] | Omit = omit,
        filters: Iterable[live_report_create_params.Filter] | Omit = omit,
        generate_now: bool | Omit = omit,
        include_transcript_excerpts: bool | Omit = omit,
        notifications: live_report_create_params.Notification | Omit = omit,
        status: Literal["ACTIVE", "PAUSED"] | Omit = omit,
        targets: Iterable[live_report_create_params.Target] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportCreateResponse:
        """Saves a report on the project's live calls.

        Simulations are never included.
        Targets are analytics measures held to a bar: a threshold metric is read as its
        pass rate (`value` is a percentage, 0-100, held AT_LEAST by default); a numeric
        metric as its average (held AT_MOST by default). Every target is read for the
        period and the period before it, so the report says whether each was met and how
        it moved. Scheduled reports are written `deliveryHour` hours into the day after
        each period ends in `timezone` (a week runs Monday to Sunday), then emailed and
        posted per `notifications`. With `generateNow` (the default) the report for the
        latest closed period is written right away and not sent.

        Args:
          generate_now: Write the report for the latest closed period right away. Default true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/live-report",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "agent_id": agent_id,
                    "cadence": cadence,
                    "dashboard_id": dashboard_id,
                    "delivery_hour": delivery_hour,
                    "description": description,
                    "filters": filters,
                    "generate_now": generate_now,
                    "include_transcript_excerpts": include_transcript_excerpts,
                    "notifications": notifications,
                    "status": status,
                    "targets": targets,
                    "timezone": timezone,
                },
                live_report_create_params.LiveReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportCreateResponse,
        )

    async def update(
        self,
        report_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        cadence: Literal["DAILY", "WEEKLY", "MONTHLY"] | Omit = omit,
        dashboard_id: Optional[str] | Omit = omit,
        delivery_hour: int | Omit = omit,
        description: Optional[str] | Omit = omit,
        filters: Iterable[live_report_update_params.Filter] | Omit = omit,
        include_transcript_excerpts: bool | Omit = omit,
        name: str | Omit = omit,
        notifications: live_report_update_params.Notification | Omit = omit,
        status: Literal["ACTIVE", "PAUSED"] | Omit = omit,
        targets: Iterable[live_report_update_params.Target] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportUpdateResponse:
        """Changes the fields sent.

        Set `status` to PAUSED to stop scheduled reports.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._patch(
            f"/v1/live-report/{report_id}",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "cadence": cadence,
                    "dashboard_id": dashboard_id,
                    "delivery_hour": delivery_hour,
                    "description": description,
                    "filters": filters,
                    "include_transcript_excerpts": include_transcript_excerpts,
                    "name": name,
                    "notifications": notifications,
                    "status": status,
                    "targets": targets,
                    "timezone": timezone,
                },
                live_report_update_params.LiveReportUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportListResponse:
        """
        Lists the project's saved live call reports, newest first.

        Args:
          limit: Page size, at most 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/live-report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    live_report_list_params.LiveReportListParams,
                ),
            ),
            cast_to=LiveReportListResponse,
        )

    async def delete(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportDeleteResponse:
        """
        Deletes the report and stops its scheduled reports.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._delete(
            f"/v1/live-report/{report_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportDeleteResponse,
        )

    async def get_by_id(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportGetByIDResponse:
        """
        Get a live report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._get(
            f"/v1/live-report/{report_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportGetByIDResponse,
        )

    async def get_document(
        self,
        document_id: str,
        *,
        report_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportGetDocumentResponse:
        """Returns one written report.

        `document` is null until `status` is READY. Theme
        excerpts and grader quotes (call transcript text) are included only for keys
        with transcript:read.

        Args:
          report_id: The live report ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._get(
            f"/v1/live-report/{report_id}/document/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportGetDocumentResponse,
        )

    async def list_documents(
        self,
        report_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportListDocumentsResponse:
        """
        Lists a report's documents, newest period first.

        Args:
          limit: Page size, at most 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._get(
            f"/v1/live-report/{report_id}/document",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    live_report_list_documents_params.LiveReportListDocumentsParams,
                ),
            ),
            cast_to=LiveReportListDocumentsResponse,
        )

    async def run(
        self,
        report_id: str,
        *,
        period_end: str | Omit = omit,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveReportRunResponse:
        """
        Writes the report now, for its latest closed period or a custom window
        (`periodStart` + `periodEnd`, at most 92 days, ended). Returns 202 with the
        document in PENDING; poll GET /v1/live-report/{reportId}/document/{documentId}
        until `status` is READY or FAILED (typically a few minutes). An identical
        request already in flight is returned as-is. A generated document is not
        emailed.

        Args:
          period_end: ISO 8601 end (exclusive) of a custom window. Requires periodStart.

          period_start: ISO 8601 start of a custom window. Omit both for the latest closed period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._post(
            f"/v1/live-report/{report_id}/generate",
            body=await async_maybe_transform(
                {
                    "period_end": period_end,
                    "period_start": period_start,
                },
                live_report_run_params.LiveReportRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveReportRunResponse,
        )


class LiveReportResourceWithRawResponse:
    def __init__(self, live_report: LiveReportResource) -> None:
        self._live_report = live_report

        self.create = to_raw_response_wrapper(
            live_report.create,
        )
        self.update = to_raw_response_wrapper(
            live_report.update,
        )
        self.list = to_raw_response_wrapper(
            live_report.list,
        )
        self.delete = to_raw_response_wrapper(
            live_report.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            live_report.get_by_id,
        )
        self.get_document = to_raw_response_wrapper(
            live_report.get_document,
        )
        self.list_documents = to_raw_response_wrapper(
            live_report.list_documents,
        )
        self.run = to_raw_response_wrapper(
            live_report.run,
        )


class AsyncLiveReportResourceWithRawResponse:
    def __init__(self, live_report: AsyncLiveReportResource) -> None:
        self._live_report = live_report

        self.create = async_to_raw_response_wrapper(
            live_report.create,
        )
        self.update = async_to_raw_response_wrapper(
            live_report.update,
        )
        self.list = async_to_raw_response_wrapper(
            live_report.list,
        )
        self.delete = async_to_raw_response_wrapper(
            live_report.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            live_report.get_by_id,
        )
        self.get_document = async_to_raw_response_wrapper(
            live_report.get_document,
        )
        self.list_documents = async_to_raw_response_wrapper(
            live_report.list_documents,
        )
        self.run = async_to_raw_response_wrapper(
            live_report.run,
        )


class LiveReportResourceWithStreamingResponse:
    def __init__(self, live_report: LiveReportResource) -> None:
        self._live_report = live_report

        self.create = to_streamed_response_wrapper(
            live_report.create,
        )
        self.update = to_streamed_response_wrapper(
            live_report.update,
        )
        self.list = to_streamed_response_wrapper(
            live_report.list,
        )
        self.delete = to_streamed_response_wrapper(
            live_report.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            live_report.get_by_id,
        )
        self.get_document = to_streamed_response_wrapper(
            live_report.get_document,
        )
        self.list_documents = to_streamed_response_wrapper(
            live_report.list_documents,
        )
        self.run = to_streamed_response_wrapper(
            live_report.run,
        )


class AsyncLiveReportResourceWithStreamingResponse:
    def __init__(self, live_report: AsyncLiveReportResource) -> None:
        self._live_report = live_report

        self.create = async_to_streamed_response_wrapper(
            live_report.create,
        )
        self.update = async_to_streamed_response_wrapper(
            live_report.update,
        )
        self.list = async_to_streamed_response_wrapper(
            live_report.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            live_report.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            live_report.get_by_id,
        )
        self.get_document = async_to_streamed_response_wrapper(
            live_report.get_document,
        )
        self.list_documents = async_to_streamed_response_wrapper(
            live_report.list_documents,
        )
        self.run = async_to_streamed_response_wrapper(
            live_report.run,
        )
