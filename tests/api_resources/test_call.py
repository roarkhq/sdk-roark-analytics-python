# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    CallGetByIDResponse,
    CallGetMetricsResponse,
    CallGetSentimentRunsResponse,
    CallGetEvaluationRunsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCall:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        call = client.call.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallGetByIDResponse, call, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.call.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetByIDResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.call.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetByIDResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_get_evaluation_runs(self, client: Roark) -> None:
        call = client.call.get_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallGetEvaluationRunsResponse, call, path=["response"])

    @parametrize
    def test_raw_response_get_evaluation_runs(self, client: Roark) -> None:
        response = client.call.with_raw_response.get_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetEvaluationRunsResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_get_evaluation_runs(self, client: Roark) -> None:
        with client.call.with_streaming_response.get_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetEvaluationRunsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_evaluation_runs(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.get_evaluation_runs(
                "",
            )

    @parametrize
    def test_method_get_metrics(self, client: Roark) -> None:
        call = client.call.get_metrics(
            call_id="callId",
        )
        assert_matches_type(CallGetMetricsResponse, call, path=["response"])

    @parametrize
    def test_method_get_metrics_with_all_params(self, client: Roark) -> None:
        call = client.call.get_metrics(
            call_id="callId",
            flatten="flatten",
        )
        assert_matches_type(CallGetMetricsResponse, call, path=["response"])

    @parametrize
    def test_raw_response_get_metrics(self, client: Roark) -> None:
        response = client.call.with_raw_response.get_metrics(
            call_id="callId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetMetricsResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_get_metrics(self, client: Roark) -> None:
        with client.call.with_streaming_response.get_metrics(
            call_id="callId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetMetricsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_metrics(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.get_metrics(
                call_id="",
            )

    @parametrize
    def test_method_get_sentiment_runs(self, client: Roark) -> None:
        call = client.call.get_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallGetSentimentRunsResponse, call, path=["response"])

    @parametrize
    def test_raw_response_get_sentiment_runs(self, client: Roark) -> None:
        response = client.call.with_raw_response.get_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetSentimentRunsResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_get_sentiment_runs(self, client: Roark) -> None:
        with client.call.with_streaming_response.get_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetSentimentRunsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_sentiment_runs(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.get_sentiment_runs(
                "",
            )


class TestAsyncCall:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallGetByIDResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetByIDResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetByIDResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_get_evaluation_runs(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.get_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallGetEvaluationRunsResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_get_evaluation_runs(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.get_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetEvaluationRunsResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_get_evaluation_runs(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.get_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetEvaluationRunsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_evaluation_runs(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.get_evaluation_runs(
                "",
            )

    @parametrize
    async def test_method_get_metrics(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.get_metrics(
            call_id="callId",
        )
        assert_matches_type(CallGetMetricsResponse, call, path=["response"])

    @parametrize
    async def test_method_get_metrics_with_all_params(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.get_metrics(
            call_id="callId",
            flatten="flatten",
        )
        assert_matches_type(CallGetMetricsResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_get_metrics(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.get_metrics(
            call_id="callId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetMetricsResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_get_metrics(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.get_metrics(
            call_id="callId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetMetricsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_metrics(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.get_metrics(
                call_id="",
            )

    @parametrize
    async def test_method_get_sentiment_runs(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.get_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallGetSentimentRunsResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_get_sentiment_runs(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.get_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetSentimentRunsResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_get_sentiment_runs(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.get_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetSentimentRunsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_sentiment_runs(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.get_sentiment_runs(
                "",
            )
