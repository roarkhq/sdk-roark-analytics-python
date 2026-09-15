# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    BenchmarkGetTargetResponse,
    BenchmarkListSuitesResponse,
    BenchmarkListMetricsResponse,
    BenchmarkGetLeaderboardResponse,
    BenchmarkListTargetHistoryResponse,
    BenchmarkListTargetScoreSamplesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBenchmark:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_leaderboard(self, client: Roark) -> None:
        benchmark = client.benchmark.get_leaderboard(
            suite="x",
        )
        assert_matches_type(BenchmarkGetLeaderboardResponse, benchmark, path=["response"])

    @parametrize
    def test_method_get_leaderboard_with_all_params(self, client: Roark) -> None:
        benchmark = client.benchmark.get_leaderboard(
            suite="x",
            condition_key="conditionKey",
            limit=1,
            metrics="metrics",
            offset=0,
            order="asc",
            sort_by="x",
            suite_version="x",
        )
        assert_matches_type(BenchmarkGetLeaderboardResponse, benchmark, path=["response"])

    @parametrize
    def test_raw_response_get_leaderboard(self, client: Roark) -> None:
        response = client.benchmark.with_raw_response.get_leaderboard(
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(BenchmarkGetLeaderboardResponse, benchmark, path=["response"])

    @parametrize
    def test_streaming_response_get_leaderboard(self, client: Roark) -> None:
        with client.benchmark.with_streaming_response.get_leaderboard(
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(BenchmarkGetLeaderboardResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_target(self, client: Roark) -> None:
        benchmark = client.benchmark.get_target(
            target_key="targetKey",
            suite="x",
        )
        assert_matches_type(BenchmarkGetTargetResponse, benchmark, path=["response"])

    @parametrize
    def test_method_get_target_with_all_params(self, client: Roark) -> None:
        benchmark = client.benchmark.get_target(
            target_key="targetKey",
            suite="x",
            publication_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            suite_version="x",
        )
        assert_matches_type(BenchmarkGetTargetResponse, benchmark, path=["response"])

    @parametrize
    def test_raw_response_get_target(self, client: Roark) -> None:
        response = client.benchmark.with_raw_response.get_target(
            target_key="targetKey",
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(BenchmarkGetTargetResponse, benchmark, path=["response"])

    @parametrize
    def test_streaming_response_get_target(self, client: Roark) -> None:
        with client.benchmark.with_streaming_response.get_target(
            target_key="targetKey",
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(BenchmarkGetTargetResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_target(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_key` but received ''"):
            client.benchmark.with_raw_response.get_target(
                target_key="",
                suite="x",
            )

    @parametrize
    def test_method_list_metrics(self, client: Roark) -> None:
        benchmark = client.benchmark.list_metrics(
            suite="x",
        )
        assert_matches_type(BenchmarkListMetricsResponse, benchmark, path=["response"])

    @parametrize
    def test_method_list_metrics_with_all_params(self, client: Roark) -> None:
        benchmark = client.benchmark.list_metrics(
            suite="x",
            suite_version="x",
        )
        assert_matches_type(BenchmarkListMetricsResponse, benchmark, path=["response"])

    @parametrize
    def test_raw_response_list_metrics(self, client: Roark) -> None:
        response = client.benchmark.with_raw_response.list_metrics(
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(BenchmarkListMetricsResponse, benchmark, path=["response"])

    @parametrize
    def test_streaming_response_list_metrics(self, client: Roark) -> None:
        with client.benchmark.with_streaming_response.list_metrics(
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(BenchmarkListMetricsResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_suites(self, client: Roark) -> None:
        benchmark = client.benchmark.list_suites()
        assert_matches_type(BenchmarkListSuitesResponse, benchmark, path=["response"])

    @parametrize
    def test_raw_response_list_suites(self, client: Roark) -> None:
        response = client.benchmark.with_raw_response.list_suites()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(BenchmarkListSuitesResponse, benchmark, path=["response"])

    @parametrize
    def test_streaming_response_list_suites(self, client: Roark) -> None:
        with client.benchmark.with_streaming_response.list_suites() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(BenchmarkListSuitesResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_target_history(self, client: Roark) -> None:
        benchmark = client.benchmark.list_target_history(
            target_key="targetKey",
            suite="x",
        )
        assert_matches_type(BenchmarkListTargetHistoryResponse, benchmark, path=["response"])

    @parametrize
    def test_method_list_target_history_with_all_params(self, client: Roark) -> None:
        benchmark = client.benchmark.list_target_history(
            target_key="targetKey",
            suite="x",
            limit=1,
            offset=0,
            suite_version="x",
        )
        assert_matches_type(BenchmarkListTargetHistoryResponse, benchmark, path=["response"])

    @parametrize
    def test_raw_response_list_target_history(self, client: Roark) -> None:
        response = client.benchmark.with_raw_response.list_target_history(
            target_key="targetKey",
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(BenchmarkListTargetHistoryResponse, benchmark, path=["response"])

    @parametrize
    def test_streaming_response_list_target_history(self, client: Roark) -> None:
        with client.benchmark.with_streaming_response.list_target_history(
            target_key="targetKey",
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(BenchmarkListTargetHistoryResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_target_history(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_key` but received ''"):
            client.benchmark.with_raw_response.list_target_history(
                target_key="",
                suite="x",
            )

    @parametrize
    def test_method_list_target_score_samples(self, client: Roark) -> None:
        benchmark = client.benchmark.list_target_score_samples(
            target_key="targetKey",
            suite="x",
        )
        assert_matches_type(BenchmarkListTargetScoreSamplesResponse, benchmark, path=["response"])

    @parametrize
    def test_method_list_target_score_samples_with_all_params(self, client: Roark) -> None:
        benchmark = client.benchmark.list_target_score_samples(
            target_key="targetKey",
            suite="x",
            condition_key="conditionKey",
            limit=1,
            metric_key="x",
            offset=0,
            suite_version="x",
        )
        assert_matches_type(BenchmarkListTargetScoreSamplesResponse, benchmark, path=["response"])

    @parametrize
    def test_raw_response_list_target_score_samples(self, client: Roark) -> None:
        response = client.benchmark.with_raw_response.list_target_score_samples(
            target_key="targetKey",
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(BenchmarkListTargetScoreSamplesResponse, benchmark, path=["response"])

    @parametrize
    def test_streaming_response_list_target_score_samples(self, client: Roark) -> None:
        with client.benchmark.with_streaming_response.list_target_score_samples(
            target_key="targetKey",
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(BenchmarkListTargetScoreSamplesResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_target_score_samples(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_key` but received ''"):
            client.benchmark.with_raw_response.list_target_score_samples(
                target_key="",
                suite="x",
            )


class TestAsyncBenchmark:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_leaderboard(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.get_leaderboard(
            suite="x",
        )
        assert_matches_type(BenchmarkGetLeaderboardResponse, benchmark, path=["response"])

    @parametrize
    async def test_method_get_leaderboard_with_all_params(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.get_leaderboard(
            suite="x",
            condition_key="conditionKey",
            limit=1,
            metrics="metrics",
            offset=0,
            order="asc",
            sort_by="x",
            suite_version="x",
        )
        assert_matches_type(BenchmarkGetLeaderboardResponse, benchmark, path=["response"])

    @parametrize
    async def test_raw_response_get_leaderboard(self, async_client: AsyncRoark) -> None:
        response = await async_client.benchmark.with_raw_response.get_leaderboard(
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(BenchmarkGetLeaderboardResponse, benchmark, path=["response"])

    @parametrize
    async def test_streaming_response_get_leaderboard(self, async_client: AsyncRoark) -> None:
        async with async_client.benchmark.with_streaming_response.get_leaderboard(
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(BenchmarkGetLeaderboardResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_target(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.get_target(
            target_key="targetKey",
            suite="x",
        )
        assert_matches_type(BenchmarkGetTargetResponse, benchmark, path=["response"])

    @parametrize
    async def test_method_get_target_with_all_params(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.get_target(
            target_key="targetKey",
            suite="x",
            publication_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            suite_version="x",
        )
        assert_matches_type(BenchmarkGetTargetResponse, benchmark, path=["response"])

    @parametrize
    async def test_raw_response_get_target(self, async_client: AsyncRoark) -> None:
        response = await async_client.benchmark.with_raw_response.get_target(
            target_key="targetKey",
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(BenchmarkGetTargetResponse, benchmark, path=["response"])

    @parametrize
    async def test_streaming_response_get_target(self, async_client: AsyncRoark) -> None:
        async with async_client.benchmark.with_streaming_response.get_target(
            target_key="targetKey",
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(BenchmarkGetTargetResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_target(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_key` but received ''"):
            await async_client.benchmark.with_raw_response.get_target(
                target_key="",
                suite="x",
            )

    @parametrize
    async def test_method_list_metrics(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.list_metrics(
            suite="x",
        )
        assert_matches_type(BenchmarkListMetricsResponse, benchmark, path=["response"])

    @parametrize
    async def test_method_list_metrics_with_all_params(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.list_metrics(
            suite="x",
            suite_version="x",
        )
        assert_matches_type(BenchmarkListMetricsResponse, benchmark, path=["response"])

    @parametrize
    async def test_raw_response_list_metrics(self, async_client: AsyncRoark) -> None:
        response = await async_client.benchmark.with_raw_response.list_metrics(
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(BenchmarkListMetricsResponse, benchmark, path=["response"])

    @parametrize
    async def test_streaming_response_list_metrics(self, async_client: AsyncRoark) -> None:
        async with async_client.benchmark.with_streaming_response.list_metrics(
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(BenchmarkListMetricsResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_suites(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.list_suites()
        assert_matches_type(BenchmarkListSuitesResponse, benchmark, path=["response"])

    @parametrize
    async def test_raw_response_list_suites(self, async_client: AsyncRoark) -> None:
        response = await async_client.benchmark.with_raw_response.list_suites()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(BenchmarkListSuitesResponse, benchmark, path=["response"])

    @parametrize
    async def test_streaming_response_list_suites(self, async_client: AsyncRoark) -> None:
        async with async_client.benchmark.with_streaming_response.list_suites() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(BenchmarkListSuitesResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_target_history(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.list_target_history(
            target_key="targetKey",
            suite="x",
        )
        assert_matches_type(BenchmarkListTargetHistoryResponse, benchmark, path=["response"])

    @parametrize
    async def test_method_list_target_history_with_all_params(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.list_target_history(
            target_key="targetKey",
            suite="x",
            limit=1,
            offset=0,
            suite_version="x",
        )
        assert_matches_type(BenchmarkListTargetHistoryResponse, benchmark, path=["response"])

    @parametrize
    async def test_raw_response_list_target_history(self, async_client: AsyncRoark) -> None:
        response = await async_client.benchmark.with_raw_response.list_target_history(
            target_key="targetKey",
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(BenchmarkListTargetHistoryResponse, benchmark, path=["response"])

    @parametrize
    async def test_streaming_response_list_target_history(self, async_client: AsyncRoark) -> None:
        async with async_client.benchmark.with_streaming_response.list_target_history(
            target_key="targetKey",
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(BenchmarkListTargetHistoryResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_target_history(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_key` but received ''"):
            await async_client.benchmark.with_raw_response.list_target_history(
                target_key="",
                suite="x",
            )

    @parametrize
    async def test_method_list_target_score_samples(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.list_target_score_samples(
            target_key="targetKey",
            suite="x",
        )
        assert_matches_type(BenchmarkListTargetScoreSamplesResponse, benchmark, path=["response"])

    @parametrize
    async def test_method_list_target_score_samples_with_all_params(self, async_client: AsyncRoark) -> None:
        benchmark = await async_client.benchmark.list_target_score_samples(
            target_key="targetKey",
            suite="x",
            condition_key="conditionKey",
            limit=1,
            metric_key="x",
            offset=0,
            suite_version="x",
        )
        assert_matches_type(BenchmarkListTargetScoreSamplesResponse, benchmark, path=["response"])

    @parametrize
    async def test_raw_response_list_target_score_samples(self, async_client: AsyncRoark) -> None:
        response = await async_client.benchmark.with_raw_response.list_target_score_samples(
            target_key="targetKey",
            suite="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(BenchmarkListTargetScoreSamplesResponse, benchmark, path=["response"])

    @parametrize
    async def test_streaming_response_list_target_score_samples(self, async_client: AsyncRoark) -> None:
        async with async_client.benchmark.with_streaming_response.list_target_score_samples(
            target_key="targetKey",
            suite="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(BenchmarkListTargetScoreSamplesResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_target_score_samples(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_key` but received ''"):
            await async_client.benchmark.with_raw_response.list_target_score_samples(
                target_key="",
                suite="x",
            )
