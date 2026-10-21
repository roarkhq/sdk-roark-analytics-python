# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    AnalyticsQueryResponse,
    AnalyticsGetSchemaResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_schema(self, client: Roark) -> None:
        analytics = client.analytics.get_schema()
        assert_matches_type(AnalyticsGetSchemaResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_get_schema(self, client: Roark) -> None:
        response = client.analytics.with_raw_response.get_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetSchemaResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_get_schema(self, client: Roark) -> None:
        with client.analytics.with_streaming_response.get_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetSchemaResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Roark) -> None:
        analytics = client.analytics.query(
            measures=[{}],
        )
        assert_matches_type(AnalyticsQueryResponse, analytics, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Roark) -> None:
        analytics = client.analytics.query(
            measures=[
                {
                    "aggregation": "COUNT",
                    "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                    "color": "GREEN",
                    "distinct_by": "NONE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}
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
            comparison_groups=[
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
            ],
            comparison_mode="NONE",
            filters=[{"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}],
            include_buckets=True,
            interval="HOUR",
            time_range={"type": "LAST", "unit": "DAYS", "value": 1},
            timezone="x",
        )
        assert_matches_type(AnalyticsQueryResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Roark) -> None:
        response = client.analytics.with_raw_response.query(
            measures=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsQueryResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Roark) -> None:
        with client.analytics.with_streaming_response.query(
            measures=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsQueryResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_schema(self, async_client: AsyncRoark) -> None:
        analytics = await async_client.analytics.get_schema()
        assert_matches_type(AnalyticsGetSchemaResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_get_schema(self, async_client: AsyncRoark) -> None:
        response = await async_client.analytics.with_raw_response.get_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetSchemaResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_get_schema(self, async_client: AsyncRoark) -> None:
        async with async_client.analytics.with_streaming_response.get_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetSchemaResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncRoark) -> None:
        analytics = await async_client.analytics.query(
            measures=[{}],
        )
        assert_matches_type(AnalyticsQueryResponse, analytics, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncRoark) -> None:
        analytics = await async_client.analytics.query(
            measures=[
                {
                    "aggregation": "COUNT",
                    "breakdown": {"type": "METRIC_PROPERTY", "property": "property"},
                    "color": "GREEN",
                    "distinct_by": "NONE",
                    "filters": [
                        {"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}
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
            comparison_groups=[
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
                {
                    "filters": [
                        {"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}
                    ],
                    "name": "x",
                    "color": "GREEN",
                },
            ],
            comparison_mode="NONE",
            filters=[{"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}],
            include_buckets=True,
            interval="HOUR",
            time_range={"type": "LAST", "unit": "DAYS", "value": 1},
            timezone="x",
        )
        assert_matches_type(AnalyticsQueryResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncRoark) -> None:
        response = await async_client.analytics.with_raw_response.query(
            measures=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsQueryResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncRoark) -> None:
        async with async_client.analytics.with_streaming_response.query(
            measures=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsQueryResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True
