# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    DashboardListResponse,
    DashboardCreateResponse,
    DashboardDeleteResponse,
    DashboardUpdateResponse,
    DashboardGetByIDResponse,
    DashboardGetDataResponse,
    DashboardCreateWidgetResponse,
    DashboardDeleteWidgetResponse,
    DashboardUpdateWidgetResponse,
    DashboardGetWidgetDataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDashboard:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        dashboard = client.dashboard.create(
            name="x",
        )
        assert_matches_type(DashboardCreateResponse, dashboard, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        dashboard = client.dashboard.create(
            name="x",
            description="description",
            filters=[{"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}],
            is_default=True,
            time_range={"type": "LAST", "unit": "DAYS", "value": 1},
            widgets=[
                {
                    "measures": [
                        {
                            "aggregation": "COUNT",
                            "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                            "color": "GREEN",
                            "distinct_by": "NONE",
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "is_baseline": True,
                            "metric": "x",
                            "nested_aggregation": "COUNT",
                            "nested_aggregation_percentile": 0,
                            "pass_operator": "EQUALS",
                            "pass_value": "string",
                            "percentile": 0,
                            "type": "METRIC",
                        }
                    ],
                    "name": "x",
                    "comparison_groups": [
                        {
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "name": "x",
                            "color": "GREEN",
                        },
                        {
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "name": "x",
                            "color": "GREEN",
                        },
                    ],
                    "comparison_mode": "NONE",
                    "description": "description",
                    "display": "LINE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "interval": "HOUR",
                    "size": "SMALL",
                }
            ],
        )
        assert_matches_type(DashboardCreateResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardCreateResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardCreateResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        dashboard = client.dashboard.update(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )
        assert_matches_type(DashboardUpdateResponse, dashboard, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        dashboard = client.dashboard.update(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            description="description",
            filters=[{"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}],
            is_default=True,
            name="x",
            time_range={"type": "LAST", "unit": "DAYS", "value": 1},
            widgets=[
                {
                    "measures": [
                        {
                            "aggregation": "COUNT",
                            "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                            "color": "GREEN",
                            "distinct_by": "NONE",
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "is_baseline": True,
                            "metric": "x",
                            "nested_aggregation": "COUNT",
                            "nested_aggregation_percentile": 0,
                            "pass_operator": "EQUALS",
                            "pass_value": "string",
                            "percentile": 0,
                            "type": "METRIC",
                        }
                    ],
                    "name": "x",
                    "comparison_groups": [
                        {
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "name": "x",
                            "color": "GREEN",
                        },
                        {
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "name": "x",
                            "color": "GREEN",
                        },
                    ],
                    "comparison_mode": "NONE",
                    "description": "description",
                    "display": "LINE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "interval": "HOUR",
                    "size": "SMALL",
                }
            ],
        )
        assert_matches_type(DashboardUpdateResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.update(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardUpdateResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.update(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardUpdateResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            client.dashboard.with_raw_response.update(
                dashboard_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        dashboard = client.dashboard.list()
        assert_matches_type(DashboardListResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardListResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardListResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        dashboard = client.dashboard.delete(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )
        assert_matches_type(DashboardDeleteResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.delete(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardDeleteResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.delete(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardDeleteResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            client.dashboard.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_widget(self, client: Roark) -> None:
        dashboard = client.dashboard.create_widget(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        )
        assert_matches_type(DashboardCreateWidgetResponse, dashboard, path=["response"])

    @parametrize
    def test_method_create_widget_with_all_params(self, client: Roark) -> None:
        dashboard = client.dashboard.create_widget(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[
                {
                    "aggregation": "COUNT",
                    "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                    "color": "GREEN",
                    "distinct_by": "NONE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "is_baseline": True,
                    "metric": "x",
                    "nested_aggregation": "COUNT",
                    "nested_aggregation_percentile": 0,
                    "pass_operator": "EQUALS",
                    "pass_value": "string",
                    "percentile": 0,
                    "type": "METRIC",
                }
            ],
            name="x",
            comparison_groups=[
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
            ],
            comparison_mode="NONE",
            description="description",
            display="LINE",
            filters=[{"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}],
            interval="HOUR",
            size="SMALL",
        )
        assert_matches_type(DashboardCreateWidgetResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_create_widget(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.create_widget(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardCreateWidgetResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_create_widget(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.create_widget(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardCreateWidgetResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_widget(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            client.dashboard.with_raw_response.create_widget(
                dashboard_id="",
                measures=[{}],
                name="x",
            )

    @parametrize
    def test_method_delete_widget(self, client: Roark) -> None:
        dashboard = client.dashboard.delete_widget(
            "7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )
        assert_matches_type(DashboardDeleteWidgetResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_delete_widget(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.delete_widget(
            "7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardDeleteWidgetResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_delete_widget(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.delete_widget(
            "7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardDeleteWidgetResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_widget(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `widget_id` but received ''"):
            client.dashboard.with_raw_response.delete_widget(
                "",
                dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            client.dashboard.with_raw_response.delete_widget(
                "7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
                dashboard_id="",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        dashboard = client.dashboard.get_by_id(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )
        assert_matches_type(DashboardGetByIDResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.get_by_id(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardGetByIDResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.get_by_id(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardGetByIDResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            client.dashboard.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_get_data(self, client: Roark) -> None:
        dashboard = client.dashboard.get_data(
            dashboard_id="dashboardId",
        )
        assert_matches_type(DashboardGetDataResponse, dashboard, path=["response"])

    @parametrize
    def test_method_get_data_with_all_params(self, client: Roark) -> None:
        dashboard = client.dashboard.get_data(
            dashboard_id="dashboardId",
            from_="2019-12-27T18:11:19.117Z",
            timezone="x",
            to="2019-12-27T18:11:19.117Z",
        )
        assert_matches_type(DashboardGetDataResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_get_data(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.get_data(
            dashboard_id="dashboardId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardGetDataResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_get_data(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.get_data(
            dashboard_id="dashboardId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardGetDataResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_data(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            client.dashboard.with_raw_response.get_data(
                dashboard_id="",
            )

    @parametrize
    def test_method_get_widget_data(self, client: Roark) -> None:
        dashboard = client.dashboard.get_widget_data(
            widget_id="widgetId",
            dashboard_id="dashboardId",
        )
        assert_matches_type(DashboardGetWidgetDataResponse, dashboard, path=["response"])

    @parametrize
    def test_method_get_widget_data_with_all_params(self, client: Roark) -> None:
        dashboard = client.dashboard.get_widget_data(
            widget_id="widgetId",
            dashboard_id="dashboardId",
            from_="2019-12-27T18:11:19.117Z",
            timezone="x",
            to="2019-12-27T18:11:19.117Z",
        )
        assert_matches_type(DashboardGetWidgetDataResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_get_widget_data(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.get_widget_data(
            widget_id="widgetId",
            dashboard_id="dashboardId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardGetWidgetDataResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_get_widget_data(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.get_widget_data(
            widget_id="widgetId",
            dashboard_id="dashboardId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardGetWidgetDataResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_widget_data(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `widget_id` but received ''"):
            client.dashboard.with_raw_response.get_widget_data(
                widget_id="",
                dashboard_id="dashboardId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            client.dashboard.with_raw_response.get_widget_data(
                widget_id="widgetId",
                dashboard_id="",
            )

    @parametrize
    def test_method_update_widget(self, client: Roark) -> None:
        dashboard = client.dashboard.update_widget(
            widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        )
        assert_matches_type(DashboardUpdateWidgetResponse, dashboard, path=["response"])

    @parametrize
    def test_method_update_widget_with_all_params(self, client: Roark) -> None:
        dashboard = client.dashboard.update_widget(
            widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[
                {
                    "aggregation": "COUNT",
                    "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                    "color": "GREEN",
                    "distinct_by": "NONE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "is_baseline": True,
                    "metric": "x",
                    "nested_aggregation": "COUNT",
                    "nested_aggregation_percentile": 0,
                    "pass_operator": "EQUALS",
                    "pass_value": "string",
                    "percentile": 0,
                    "type": "METRIC",
                }
            ],
            name="x",
            comparison_groups=[
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
            ],
            comparison_mode="NONE",
            description="description",
            display="LINE",
            filters=[{"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}],
            interval="HOUR",
            size="SMALL",
        )
        assert_matches_type(DashboardUpdateWidgetResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_update_widget(self, client: Roark) -> None:
        response = client.dashboard.with_raw_response.update_widget(
            widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardUpdateWidgetResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_update_widget(self, client: Roark) -> None:
        with client.dashboard.with_streaming_response.update_widget(
            widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardUpdateWidgetResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_widget(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `widget_id` but received ''"):
            client.dashboard.with_raw_response.update_widget(
                widget_id="",
                dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
                measures=[{}],
                name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            client.dashboard.with_raw_response.update_widget(
                widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
                dashboard_id="",
                measures=[{}],
                name="x",
            )


class TestAsyncDashboard:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.create(
            name="x",
        )
        assert_matches_type(DashboardCreateResponse, dashboard, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.create(
            name="x",
            description="description",
            filters=[{"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}],
            is_default=True,
            time_range={"type": "LAST", "unit": "DAYS", "value": 1},
            widgets=[
                {
                    "measures": [
                        {
                            "aggregation": "COUNT",
                            "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                            "color": "GREEN",
                            "distinct_by": "NONE",
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "is_baseline": True,
                            "metric": "x",
                            "nested_aggregation": "COUNT",
                            "nested_aggregation_percentile": 0,
                            "pass_operator": "EQUALS",
                            "pass_value": "string",
                            "percentile": 0,
                            "type": "METRIC",
                        }
                    ],
                    "name": "x",
                    "comparison_groups": [
                        {
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "name": "x",
                            "color": "GREEN",
                        },
                        {
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "name": "x",
                            "color": "GREEN",
                        },
                    ],
                    "comparison_mode": "NONE",
                    "description": "description",
                    "display": "LINE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "interval": "HOUR",
                    "size": "SMALL",
                }
            ],
        )
        assert_matches_type(DashboardCreateResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardCreateResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardCreateResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.update(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )
        assert_matches_type(DashboardUpdateResponse, dashboard, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.update(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            description="description",
            filters=[{"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}],
            is_default=True,
            name="x",
            time_range={"type": "LAST", "unit": "DAYS", "value": 1},
            widgets=[
                {
                    "measures": [
                        {
                            "aggregation": "COUNT",
                            "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                            "color": "GREEN",
                            "distinct_by": "NONE",
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "is_baseline": True,
                            "metric": "x",
                            "nested_aggregation": "COUNT",
                            "nested_aggregation_percentile": 0,
                            "pass_operator": "EQUALS",
                            "pass_value": "string",
                            "percentile": 0,
                            "type": "METRIC",
                        }
                    ],
                    "name": "x",
                    "comparison_groups": [
                        {
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "name": "x",
                            "color": "GREEN",
                        },
                        {
                            "filters": [
                                {
                                    "type": "METRIC_PROPERTY",
                                    "value": "string",
                                    "operator": "EQUALS",
                                    "property": "property",
                                }
                            ],
                            "name": "x",
                            "color": "GREEN",
                        },
                    ],
                    "comparison_mode": "NONE",
                    "description": "description",
                    "display": "LINE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "interval": "HOUR",
                    "size": "SMALL",
                }
            ],
        )
        assert_matches_type(DashboardUpdateResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.update(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardUpdateResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.update(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardUpdateResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            await async_client.dashboard.with_raw_response.update(
                dashboard_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.list()
        assert_matches_type(DashboardListResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardListResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardListResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.delete(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )
        assert_matches_type(DashboardDeleteResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.delete(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardDeleteResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.delete(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardDeleteResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            await async_client.dashboard.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_widget(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.create_widget(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        )
        assert_matches_type(DashboardCreateWidgetResponse, dashboard, path=["response"])

    @parametrize
    async def test_method_create_widget_with_all_params(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.create_widget(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[
                {
                    "aggregation": "COUNT",
                    "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                    "color": "GREEN",
                    "distinct_by": "NONE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "is_baseline": True,
                    "metric": "x",
                    "nested_aggregation": "COUNT",
                    "nested_aggregation_percentile": 0,
                    "pass_operator": "EQUALS",
                    "pass_value": "string",
                    "percentile": 0,
                    "type": "METRIC",
                }
            ],
            name="x",
            comparison_groups=[
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
            ],
            comparison_mode="NONE",
            description="description",
            display="LINE",
            filters=[{"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}],
            interval="HOUR",
            size="SMALL",
        )
        assert_matches_type(DashboardCreateWidgetResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_create_widget(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.create_widget(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardCreateWidgetResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_create_widget(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.create_widget(
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardCreateWidgetResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_widget(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            await async_client.dashboard.with_raw_response.create_widget(
                dashboard_id="",
                measures=[{}],
                name="x",
            )

    @parametrize
    async def test_method_delete_widget(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.delete_widget(
            "7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )
        assert_matches_type(DashboardDeleteWidgetResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_delete_widget(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.delete_widget(
            "7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardDeleteWidgetResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_delete_widget(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.delete_widget(
            "7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardDeleteWidgetResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_widget(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `widget_id` but received ''"):
            await async_client.dashboard.with_raw_response.delete_widget(
                "",
                dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            await async_client.dashboard.with_raw_response.delete_widget(
                "7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
                dashboard_id="",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.get_by_id(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )
        assert_matches_type(DashboardGetByIDResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.get_by_id(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardGetByIDResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.get_by_id(
            "6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardGetByIDResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            await async_client.dashboard.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_get_data(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.get_data(
            dashboard_id="dashboardId",
        )
        assert_matches_type(DashboardGetDataResponse, dashboard, path=["response"])

    @parametrize
    async def test_method_get_data_with_all_params(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.get_data(
            dashboard_id="dashboardId",
            from_="2019-12-27T18:11:19.117Z",
            timezone="x",
            to="2019-12-27T18:11:19.117Z",
        )
        assert_matches_type(DashboardGetDataResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_get_data(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.get_data(
            dashboard_id="dashboardId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardGetDataResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_get_data(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.get_data(
            dashboard_id="dashboardId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardGetDataResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_data(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            await async_client.dashboard.with_raw_response.get_data(
                dashboard_id="",
            )

    @parametrize
    async def test_method_get_widget_data(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.get_widget_data(
            widget_id="widgetId",
            dashboard_id="dashboardId",
        )
        assert_matches_type(DashboardGetWidgetDataResponse, dashboard, path=["response"])

    @parametrize
    async def test_method_get_widget_data_with_all_params(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.get_widget_data(
            widget_id="widgetId",
            dashboard_id="dashboardId",
            from_="2019-12-27T18:11:19.117Z",
            timezone="x",
            to="2019-12-27T18:11:19.117Z",
        )
        assert_matches_type(DashboardGetWidgetDataResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_get_widget_data(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.get_widget_data(
            widget_id="widgetId",
            dashboard_id="dashboardId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardGetWidgetDataResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_get_widget_data(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.get_widget_data(
            widget_id="widgetId",
            dashboard_id="dashboardId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardGetWidgetDataResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_widget_data(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `widget_id` but received ''"):
            await async_client.dashboard.with_raw_response.get_widget_data(
                widget_id="",
                dashboard_id="dashboardId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            await async_client.dashboard.with_raw_response.get_widget_data(
                widget_id="widgetId",
                dashboard_id="",
            )

    @parametrize
    async def test_method_update_widget(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.update_widget(
            widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        )
        assert_matches_type(DashboardUpdateWidgetResponse, dashboard, path=["response"])

    @parametrize
    async def test_method_update_widget_with_all_params(self, async_client: AsyncRoark) -> None:
        dashboard = await async_client.dashboard.update_widget(
            widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[
                {
                    "aggregation": "COUNT",
                    "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                    "color": "GREEN",
                    "distinct_by": "NONE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "is_baseline": True,
                    "metric": "x",
                    "nested_aggregation": "COUNT",
                    "nested_aggregation_percentile": 0,
                    "pass_operator": "EQUALS",
                    "pass_value": "string",
                    "percentile": 0,
                    "type": "METRIC",
                }
            ],
            name="x",
            comparison_groups=[
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
            ],
            comparison_mode="NONE",
            description="description",
            display="LINE",
            filters=[{"type": "METRIC_PROPERTY", "value": "string", "operator": "EQUALS", "property": "property"}],
            interval="HOUR",
            size="SMALL",
        )
        assert_matches_type(DashboardUpdateWidgetResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_update_widget(self, async_client: AsyncRoark) -> None:
        response = await async_client.dashboard.with_raw_response.update_widget(
            widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardUpdateWidgetResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_update_widget(self, async_client: AsyncRoark) -> None:
        async with async_client.dashboard.with_streaming_response.update_widget(
            widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
            dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
            measures=[{}],
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardUpdateWidgetResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_widget(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `widget_id` but received ''"):
            await async_client.dashboard.with_raw_response.update_widget(
                widget_id="",
                dashboard_id="6f1d2c3b-4a5e-4f60-8b71-9c0d1e2f3a4b",
                measures=[{}],
                name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dashboard_id` but received ''"):
            await async_client.dashboard.with_raw_response.update_widget(
                widget_id="7a8b9c0d-1e2f-4a3b-8c4d-5e6f7a8b9c0d",
                dashboard_id="",
                measures=[{}],
                name="x",
            )
