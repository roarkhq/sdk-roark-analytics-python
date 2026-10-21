# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    dashboard_create_params,
    dashboard_update_params,
    dashboard_get_data_params,
    dashboard_create_widget_params,
    dashboard_update_widget_params,
    dashboard_get_widget_data_params,
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
from ..types.dashboard_list_response import DashboardListResponse
from ..types.dashboard_create_response import DashboardCreateResponse
from ..types.dashboard_delete_response import DashboardDeleteResponse
from ..types.dashboard_update_response import DashboardUpdateResponse
from ..types.dashboard_get_data_response import DashboardGetDataResponse
from ..types.dashboard_get_by_id_response import DashboardGetByIDResponse
from ..types.dashboard_create_widget_response import DashboardCreateWidgetResponse
from ..types.dashboard_delete_widget_response import DashboardDeleteWidgetResponse
from ..types.dashboard_update_widget_response import DashboardUpdateWidgetResponse
from ..types.dashboard_get_widget_data_response import DashboardGetWidgetDataResponse

__all__ = ["DashboardResource", "AsyncDashboardResource"]


class DashboardResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DashboardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return DashboardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DashboardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return DashboardResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        filters: Iterable[dashboard_create_params.Filter] | Omit = omit,
        is_default: bool | Omit = omit,
        time_range: Union[
            dashboard_create_params.TimeRangeUnionMember0,
            dashboard_create_params.TimeRangeUnionMember1,
            dashboard_create_params.TimeRangeUnionMember2,
            dashboard_create_params.TimeRangeUnionMember3,
        ]
        | Omit = omit,
        widgets: Iterable[dashboard_create_params.Widget] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardCreateResponse:
        """Creates a dashboard with its widgets.

        Each widget is an analytics query (see
        POST /v1/analytics/query) with a name unique on the dashboard, a `display`
        (LINE, NUMBER, RADAR, STACKED_BAR, TABLE) and a `size` (SMALL, MEDIUM, LARGE,
        EXTRA_LARGE). Widgets render top to bottom in the order given. Dashboard
        `filters` apply over every widget and must be conversation-level:
        AGENT_PROPERTY, CALL_PROPERTY, MODALITY, DATASET or METRIC_VALUE. On a field a
        widget already filters, the dashboard's wins.

        Args:
          time_range: The window: LAST n DAYS/WEEKS/MONTHS up to now, a CALENDAR_ALIGNED period
              (TODAY, YESTERDAY, THIS_WEEK, LAST_WEEK, THIS_MONTH, LAST_MONTH, THIS_YEAR,
              LAST_YEAR), FIXED from/to, or SINCE a date. At most 731 days (two years).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/dashboard",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "filters": filters,
                    "is_default": is_default,
                    "time_range": time_range,
                    "widgets": widgets,
                },
                dashboard_create_params.DashboardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardCreateResponse,
        )

    def update(
        self,
        dashboard_id: str,
        *,
        description: str | Omit = omit,
        filters: Iterable[dashboard_update_params.Filter] | Omit = omit,
        is_default: bool | Omit = omit,
        name: str | Omit = omit,
        time_range: Union[
            dashboard_update_params.TimeRangeUnionMember0,
            dashboard_update_params.TimeRangeUnionMember1,
            dashboard_update_params.TimeRangeUnionMember2,
            dashboard_update_params.TimeRangeUnionMember3,
        ]
        | Omit = omit,
        widgets: Iterable[dashboard_update_params.Widget] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardUpdateResponse:
        """Edits a dashboard.

        Omitted fields keep their current value. `widgets`, when
        sent, replaces the list: widgets are matched by name, so a widget that keeps its
        name keeps its id; a new name adds a widget and a name no longer listed removes
        it. To change one widget, PUT /v1/dashboard/{dashboardId}/widget/{widgetId}.

        Args:
          time_range: The window: LAST n DAYS/WEEKS/MONTHS up to now, a CALENDAR_ALIGNED period
              (TODAY, YESTERDAY, THIS_WEEK, LAST_WEEK, THIS_MONTH, LAST_MONTH, THIS_YEAR,
              LAST_YEAR), FIXED from/to, or SINCE a date. At most 731 days (two years).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return self._put(
            f"/v1/dashboard/{dashboard_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "filters": filters,
                    "is_default": is_default,
                    "name": name,
                    "time_range": time_range,
                    "widgets": widgets,
                },
                dashboard_update_params.DashboardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardUpdateResponse,
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
    ) -> DashboardListResponse:
        """Lists the project's dashboards, the default first.

        GET
        /v1/dashboard/{dashboardId} returns the widgets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/dashboard",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardListResponse,
        )

    def delete(
        self,
        dashboard_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardDeleteResponse:
        """Deletes a dashboard and its widgets.

        If it was the default, another dashboard
        becomes the default. A dashboard managed by config as code returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return self._delete(
            f"/v1/dashboard/{dashboard_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardDeleteResponse,
        )

    def create_widget(
        self,
        dashboard_id: str,
        *,
        measures: Iterable[dashboard_create_widget_params.Measure],
        name: str,
        comparison_groups: Iterable[dashboard_create_widget_params.ComparisonGroup] | Omit = omit,
        comparison_mode: Literal["NONE", "PREVIOUS_PERIOD"] | Omit = omit,
        description: str | Omit = omit,
        display: Literal["LINE", "NUMBER", "RADAR", "STACKED_BAR", "TABLE"] | Omit = omit,
        filters: Iterable[dashboard_create_widget_params.MeasureFilter] | Omit = omit,
        interval: Literal["HOUR", "DAY", "WEEK", "MONTH"] | Omit = omit,
        size: Literal["SMALL", "MEDIUM", "LARGE", "EXTRA_LARGE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardCreateWidgetResponse:
        """Adds a widget to the top of a dashboard.

        Its name must be unique on the
        dashboard.

        Args:
          measures: What to aggregate: 1 to 10 measures.

          name: Unique on the dashboard: how the widget is matched on update.

          comparison_groups: Run every measure once per named filter set, e.g. one group per agent.

          comparison_mode: PREVIOUS_PERIOD adds the preceding window of the same length to every series.

          display: Chart type. Defaults to LINE.

          filters: Applied to every measure, on top of each measure's own filters.

          interval: Bucket size. Defaults from the window's length and steps coarser when the window
              would exceed 500 buckets.

          size: Grid width. Defaults to MEDIUM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return self._post(
            f"/v1/dashboard/{dashboard_id}/widget",
            body=maybe_transform(
                {
                    "measures": measures,
                    "name": name,
                    "comparison_groups": comparison_groups,
                    "comparison_mode": comparison_mode,
                    "description": description,
                    "display": display,
                    "filters": filters,
                    "interval": interval,
                    "size": size,
                },
                dashboard_create_widget_params.DashboardCreateWidgetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardCreateWidgetResponse,
        )

    def delete_widget(
        self,
        widget_id: str,
        *,
        dashboard_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardDeleteWidgetResponse:
        """
        Removes a widget from a dashboard.

        Args:
          dashboard_id: The dashboard ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not widget_id:
            raise ValueError(f"Expected a non-empty value for `widget_id` but received {widget_id!r}")
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return self._delete(
            f"/v1/dashboard/{dashboard_id}/widget/{widget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardDeleteWidgetResponse,
        )

    def get_by_id(
        self,
        dashboard_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardGetByIDResponse:
        """
        Returns a dashboard with its widgets top to bottom, each in the shape POST
        /v1/dashboard accepts, so a dashboard can be read, edited and written back.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return self._get(
            f"/v1/dashboard/{dashboard_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardGetByIDResponse,
        )

    def get_data(
        self,
        dashboard_id: str,
        *,
        from_: str | Omit = omit,
        timezone: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardGetDataResponse:
        """
        Runs every widget on the dashboard and returns each one's series, exactly as the
        dashboard shows them: over the dashboard's saved window and with its filters
        applied. Pass `from` (and optionally `to`) to read a different window, and
        `timezone` to align buckets to a zone.

        Args:
          from_: ISO 8601 start. Overrides the saved window; without `to`, runs until now.

          timezone: IANA zone buckets and calendar periods align to. Default UTC.

          to: ISO 8601 end. Requires `from`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return self._get(
            f"/v1/dashboard/{dashboard_id}/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "timezone": timezone,
                        "to": to,
                    },
                    dashboard_get_data_params.DashboardGetDataParams,
                ),
            ),
            cast_to=DashboardGetDataResponse,
        )

    def get_widget_data(
        self,
        widget_id: str,
        *,
        dashboard_id: str,
        from_: str | Omit = omit,
        timezone: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardGetWidgetDataResponse:
        """
        Runs one widget and returns its series, as it reads on its dashboard (the
        dashboard's window and filters). Accepts the same `from` / `to` / `timezone`
        overrides as GET /v1/dashboard/{dashboardId}/data.

        Args:
          from_: ISO 8601 start. Overrides the saved window; without `to`, runs until now.

          timezone: IANA zone buckets and calendar periods align to. Default UTC.

          to: ISO 8601 end. Requires `from`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not widget_id:
            raise ValueError(f"Expected a non-empty value for `widget_id` but received {widget_id!r}")
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return self._get(
            f"/v1/dashboard/{dashboard_id}/widget/{widget_id}/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "timezone": timezone,
                        "to": to,
                    },
                    dashboard_get_widget_data_params.DashboardGetWidgetDataParams,
                ),
            ),
            cast_to=DashboardGetWidgetDataResponse,
        )

    def update_widget(
        self,
        widget_id: str,
        *,
        dashboard_id: str,
        measures: Iterable[dashboard_update_widget_params.Measure],
        name: str,
        comparison_groups: Iterable[dashboard_update_widget_params.ComparisonGroup] | Omit = omit,
        comparison_mode: Literal["NONE", "PREVIOUS_PERIOD"] | Omit = omit,
        description: str | Omit = omit,
        display: Literal["LINE", "NUMBER", "RADAR", "STACKED_BAR", "TABLE"] | Omit = omit,
        filters: Iterable[dashboard_update_widget_params.MeasureFilter] | Omit = omit,
        interval: Literal["HOUR", "DAY", "WEEK", "MONTH"] | Omit = omit,
        size: Literal["SMALL", "MEDIUM", "LARGE", "EXTRA_LARGE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardUpdateWidgetResponse:
        """Replaces a widget's definition.

        It keeps its id and its place on the dashboard.

        Args:
          dashboard_id: The dashboard ID

          measures: What to aggregate: 1 to 10 measures.

          name: Unique on the dashboard: how the widget is matched on update.

          comparison_groups: Run every measure once per named filter set, e.g. one group per agent.

          comparison_mode: PREVIOUS_PERIOD adds the preceding window of the same length to every series.

          display: Chart type. Defaults to LINE.

          filters: Applied to every measure, on top of each measure's own filters.

          interval: Bucket size. Defaults from the window's length and steps coarser when the window
              would exceed 500 buckets.

          size: Grid width. Defaults to MEDIUM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not widget_id:
            raise ValueError(f"Expected a non-empty value for `widget_id` but received {widget_id!r}")
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return self._put(
            f"/v1/dashboard/{dashboard_id}/widget/{widget_id}",
            body=maybe_transform(
                {
                    "measures": measures,
                    "name": name,
                    "comparison_groups": comparison_groups,
                    "comparison_mode": comparison_mode,
                    "description": description,
                    "display": display,
                    "filters": filters,
                    "interval": interval,
                    "size": size,
                },
                dashboard_update_widget_params.DashboardUpdateWidgetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardUpdateWidgetResponse,
        )


class AsyncDashboardResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDashboardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDashboardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDashboardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncDashboardResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        filters: Iterable[dashboard_create_params.Filter] | Omit = omit,
        is_default: bool | Omit = omit,
        time_range: Union[
            dashboard_create_params.TimeRangeUnionMember0,
            dashboard_create_params.TimeRangeUnionMember1,
            dashboard_create_params.TimeRangeUnionMember2,
            dashboard_create_params.TimeRangeUnionMember3,
        ]
        | Omit = omit,
        widgets: Iterable[dashboard_create_params.Widget] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardCreateResponse:
        """Creates a dashboard with its widgets.

        Each widget is an analytics query (see
        POST /v1/analytics/query) with a name unique on the dashboard, a `display`
        (LINE, NUMBER, RADAR, STACKED_BAR, TABLE) and a `size` (SMALL, MEDIUM, LARGE,
        EXTRA_LARGE). Widgets render top to bottom in the order given. Dashboard
        `filters` apply over every widget and must be conversation-level:
        AGENT_PROPERTY, CALL_PROPERTY, MODALITY, DATASET or METRIC_VALUE. On a field a
        widget already filters, the dashboard's wins.

        Args:
          time_range: The window: LAST n DAYS/WEEKS/MONTHS up to now, a CALENDAR_ALIGNED period
              (TODAY, YESTERDAY, THIS_WEEK, LAST_WEEK, THIS_MONTH, LAST_MONTH, THIS_YEAR,
              LAST_YEAR), FIXED from/to, or SINCE a date. At most 731 days (two years).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/dashboard",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "filters": filters,
                    "is_default": is_default,
                    "time_range": time_range,
                    "widgets": widgets,
                },
                dashboard_create_params.DashboardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardCreateResponse,
        )

    async def update(
        self,
        dashboard_id: str,
        *,
        description: str | Omit = omit,
        filters: Iterable[dashboard_update_params.Filter] | Omit = omit,
        is_default: bool | Omit = omit,
        name: str | Omit = omit,
        time_range: Union[
            dashboard_update_params.TimeRangeUnionMember0,
            dashboard_update_params.TimeRangeUnionMember1,
            dashboard_update_params.TimeRangeUnionMember2,
            dashboard_update_params.TimeRangeUnionMember3,
        ]
        | Omit = omit,
        widgets: Iterable[dashboard_update_params.Widget] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardUpdateResponse:
        """Edits a dashboard.

        Omitted fields keep their current value. `widgets`, when
        sent, replaces the list: widgets are matched by name, so a widget that keeps its
        name keeps its id; a new name adds a widget and a name no longer listed removes
        it. To change one widget, PUT /v1/dashboard/{dashboardId}/widget/{widgetId}.

        Args:
          time_range: The window: LAST n DAYS/WEEKS/MONTHS up to now, a CALENDAR_ALIGNED period
              (TODAY, YESTERDAY, THIS_WEEK, LAST_WEEK, THIS_MONTH, LAST_MONTH, THIS_YEAR,
              LAST_YEAR), FIXED from/to, or SINCE a date. At most 731 days (two years).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return await self._put(
            f"/v1/dashboard/{dashboard_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "filters": filters,
                    "is_default": is_default,
                    "name": name,
                    "time_range": time_range,
                    "widgets": widgets,
                },
                dashboard_update_params.DashboardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardUpdateResponse,
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
    ) -> DashboardListResponse:
        """Lists the project's dashboards, the default first.

        GET
        /v1/dashboard/{dashboardId} returns the widgets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/dashboard",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardListResponse,
        )

    async def delete(
        self,
        dashboard_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardDeleteResponse:
        """Deletes a dashboard and its widgets.

        If it was the default, another dashboard
        becomes the default. A dashboard managed by config as code returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return await self._delete(
            f"/v1/dashboard/{dashboard_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardDeleteResponse,
        )

    async def create_widget(
        self,
        dashboard_id: str,
        *,
        measures: Iterable[dashboard_create_widget_params.Measure],
        name: str,
        comparison_groups: Iterable[dashboard_create_widget_params.ComparisonGroup] | Omit = omit,
        comparison_mode: Literal["NONE", "PREVIOUS_PERIOD"] | Omit = omit,
        description: str | Omit = omit,
        display: Literal["LINE", "NUMBER", "RADAR", "STACKED_BAR", "TABLE"] | Omit = omit,
        filters: Iterable[dashboard_create_widget_params.MeasureFilter] | Omit = omit,
        interval: Literal["HOUR", "DAY", "WEEK", "MONTH"] | Omit = omit,
        size: Literal["SMALL", "MEDIUM", "LARGE", "EXTRA_LARGE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardCreateWidgetResponse:
        """Adds a widget to the top of a dashboard.

        Its name must be unique on the
        dashboard.

        Args:
          measures: What to aggregate: 1 to 10 measures.

          name: Unique on the dashboard: how the widget is matched on update.

          comparison_groups: Run every measure once per named filter set, e.g. one group per agent.

          comparison_mode: PREVIOUS_PERIOD adds the preceding window of the same length to every series.

          display: Chart type. Defaults to LINE.

          filters: Applied to every measure, on top of each measure's own filters.

          interval: Bucket size. Defaults from the window's length and steps coarser when the window
              would exceed 500 buckets.

          size: Grid width. Defaults to MEDIUM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return await self._post(
            f"/v1/dashboard/{dashboard_id}/widget",
            body=await async_maybe_transform(
                {
                    "measures": measures,
                    "name": name,
                    "comparison_groups": comparison_groups,
                    "comparison_mode": comparison_mode,
                    "description": description,
                    "display": display,
                    "filters": filters,
                    "interval": interval,
                    "size": size,
                },
                dashboard_create_widget_params.DashboardCreateWidgetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardCreateWidgetResponse,
        )

    async def delete_widget(
        self,
        widget_id: str,
        *,
        dashboard_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardDeleteWidgetResponse:
        """
        Removes a widget from a dashboard.

        Args:
          dashboard_id: The dashboard ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not widget_id:
            raise ValueError(f"Expected a non-empty value for `widget_id` but received {widget_id!r}")
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return await self._delete(
            f"/v1/dashboard/{dashboard_id}/widget/{widget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardDeleteWidgetResponse,
        )

    async def get_by_id(
        self,
        dashboard_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardGetByIDResponse:
        """
        Returns a dashboard with its widgets top to bottom, each in the shape POST
        /v1/dashboard accepts, so a dashboard can be read, edited and written back.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return await self._get(
            f"/v1/dashboard/{dashboard_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardGetByIDResponse,
        )

    async def get_data(
        self,
        dashboard_id: str,
        *,
        from_: str | Omit = omit,
        timezone: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardGetDataResponse:
        """
        Runs every widget on the dashboard and returns each one's series, exactly as the
        dashboard shows them: over the dashboard's saved window and with its filters
        applied. Pass `from` (and optionally `to`) to read a different window, and
        `timezone` to align buckets to a zone.

        Args:
          from_: ISO 8601 start. Overrides the saved window; without `to`, runs until now.

          timezone: IANA zone buckets and calendar periods align to. Default UTC.

          to: ISO 8601 end. Requires `from`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return await self._get(
            f"/v1/dashboard/{dashboard_id}/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "timezone": timezone,
                        "to": to,
                    },
                    dashboard_get_data_params.DashboardGetDataParams,
                ),
            ),
            cast_to=DashboardGetDataResponse,
        )

    async def get_widget_data(
        self,
        widget_id: str,
        *,
        dashboard_id: str,
        from_: str | Omit = omit,
        timezone: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardGetWidgetDataResponse:
        """
        Runs one widget and returns its series, as it reads on its dashboard (the
        dashboard's window and filters). Accepts the same `from` / `to` / `timezone`
        overrides as GET /v1/dashboard/{dashboardId}/data.

        Args:
          from_: ISO 8601 start. Overrides the saved window; without `to`, runs until now.

          timezone: IANA zone buckets and calendar periods align to. Default UTC.

          to: ISO 8601 end. Requires `from`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not widget_id:
            raise ValueError(f"Expected a non-empty value for `widget_id` but received {widget_id!r}")
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return await self._get(
            f"/v1/dashboard/{dashboard_id}/widget/{widget_id}/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "timezone": timezone,
                        "to": to,
                    },
                    dashboard_get_widget_data_params.DashboardGetWidgetDataParams,
                ),
            ),
            cast_to=DashboardGetWidgetDataResponse,
        )

    async def update_widget(
        self,
        widget_id: str,
        *,
        dashboard_id: str,
        measures: Iterable[dashboard_update_widget_params.Measure],
        name: str,
        comparison_groups: Iterable[dashboard_update_widget_params.ComparisonGroup] | Omit = omit,
        comparison_mode: Literal["NONE", "PREVIOUS_PERIOD"] | Omit = omit,
        description: str | Omit = omit,
        display: Literal["LINE", "NUMBER", "RADAR", "STACKED_BAR", "TABLE"] | Omit = omit,
        filters: Iterable[dashboard_update_widget_params.MeasureFilter] | Omit = omit,
        interval: Literal["HOUR", "DAY", "WEEK", "MONTH"] | Omit = omit,
        size: Literal["SMALL", "MEDIUM", "LARGE", "EXTRA_LARGE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardUpdateWidgetResponse:
        """Replaces a widget's definition.

        It keeps its id and its place on the dashboard.

        Args:
          dashboard_id: The dashboard ID

          measures: What to aggregate: 1 to 10 measures.

          name: Unique on the dashboard: how the widget is matched on update.

          comparison_groups: Run every measure once per named filter set, e.g. one group per agent.

          comparison_mode: PREVIOUS_PERIOD adds the preceding window of the same length to every series.

          display: Chart type. Defaults to LINE.

          filters: Applied to every measure, on top of each measure's own filters.

          interval: Bucket size. Defaults from the window's length and steps coarser when the window
              would exceed 500 buckets.

          size: Grid width. Defaults to MEDIUM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not widget_id:
            raise ValueError(f"Expected a non-empty value for `widget_id` but received {widget_id!r}")
        if not dashboard_id:
            raise ValueError(f"Expected a non-empty value for `dashboard_id` but received {dashboard_id!r}")
        return await self._put(
            f"/v1/dashboard/{dashboard_id}/widget/{widget_id}",
            body=await async_maybe_transform(
                {
                    "measures": measures,
                    "name": name,
                    "comparison_groups": comparison_groups,
                    "comparison_mode": comparison_mode,
                    "description": description,
                    "display": display,
                    "filters": filters,
                    "interval": interval,
                    "size": size,
                },
                dashboard_update_widget_params.DashboardUpdateWidgetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardUpdateWidgetResponse,
        )


class DashboardResourceWithRawResponse:
    def __init__(self, dashboard: DashboardResource) -> None:
        self._dashboard = dashboard

        self.create = to_raw_response_wrapper(
            dashboard.create,
        )
        self.update = to_raw_response_wrapper(
            dashboard.update,
        )
        self.list = to_raw_response_wrapper(
            dashboard.list,
        )
        self.delete = to_raw_response_wrapper(
            dashboard.delete,
        )
        self.create_widget = to_raw_response_wrapper(
            dashboard.create_widget,
        )
        self.delete_widget = to_raw_response_wrapper(
            dashboard.delete_widget,
        )
        self.get_by_id = to_raw_response_wrapper(
            dashboard.get_by_id,
        )
        self.get_data = to_raw_response_wrapper(
            dashboard.get_data,
        )
        self.get_widget_data = to_raw_response_wrapper(
            dashboard.get_widget_data,
        )
        self.update_widget = to_raw_response_wrapper(
            dashboard.update_widget,
        )


class AsyncDashboardResourceWithRawResponse:
    def __init__(self, dashboard: AsyncDashboardResource) -> None:
        self._dashboard = dashboard

        self.create = async_to_raw_response_wrapper(
            dashboard.create,
        )
        self.update = async_to_raw_response_wrapper(
            dashboard.update,
        )
        self.list = async_to_raw_response_wrapper(
            dashboard.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dashboard.delete,
        )
        self.create_widget = async_to_raw_response_wrapper(
            dashboard.create_widget,
        )
        self.delete_widget = async_to_raw_response_wrapper(
            dashboard.delete_widget,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            dashboard.get_by_id,
        )
        self.get_data = async_to_raw_response_wrapper(
            dashboard.get_data,
        )
        self.get_widget_data = async_to_raw_response_wrapper(
            dashboard.get_widget_data,
        )
        self.update_widget = async_to_raw_response_wrapper(
            dashboard.update_widget,
        )


class DashboardResourceWithStreamingResponse:
    def __init__(self, dashboard: DashboardResource) -> None:
        self._dashboard = dashboard

        self.create = to_streamed_response_wrapper(
            dashboard.create,
        )
        self.update = to_streamed_response_wrapper(
            dashboard.update,
        )
        self.list = to_streamed_response_wrapper(
            dashboard.list,
        )
        self.delete = to_streamed_response_wrapper(
            dashboard.delete,
        )
        self.create_widget = to_streamed_response_wrapper(
            dashboard.create_widget,
        )
        self.delete_widget = to_streamed_response_wrapper(
            dashboard.delete_widget,
        )
        self.get_by_id = to_streamed_response_wrapper(
            dashboard.get_by_id,
        )
        self.get_data = to_streamed_response_wrapper(
            dashboard.get_data,
        )
        self.get_widget_data = to_streamed_response_wrapper(
            dashboard.get_widget_data,
        )
        self.update_widget = to_streamed_response_wrapper(
            dashboard.update_widget,
        )


class AsyncDashboardResourceWithStreamingResponse:
    def __init__(self, dashboard: AsyncDashboardResource) -> None:
        self._dashboard = dashboard

        self.create = async_to_streamed_response_wrapper(
            dashboard.create,
        )
        self.update = async_to_streamed_response_wrapper(
            dashboard.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dashboard.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dashboard.delete,
        )
        self.create_widget = async_to_streamed_response_wrapper(
            dashboard.create_widget,
        )
        self.delete_widget = async_to_streamed_response_wrapper(
            dashboard.delete_widget,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            dashboard.get_by_id,
        )
        self.get_data = async_to_streamed_response_wrapper(
            dashboard.get_data,
        )
        self.get_widget_data = async_to_streamed_response_wrapper(
            dashboard.get_widget_data,
        )
        self.update_widget = async_to_streamed_response_wrapper(
            dashboard.update_widget,
        )
