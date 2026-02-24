# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    MetricCollectionJobListResponse,
    MetricCollectionJobCreateResponse,
    MetricCollectionJobGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetricCollectionJob:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        metric_collection_job = client.metric_collection_job.create(
            call_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(MetricCollectionJobCreateResponse, metric_collection_job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.metric_collection_job.with_raw_response.create(
            call_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_collection_job = response.parse()
        assert_matches_type(MetricCollectionJobCreateResponse, metric_collection_job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.metric_collection_job.with_streaming_response.create(
            call_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_collection_job = response.parse()
            assert_matches_type(MetricCollectionJobCreateResponse, metric_collection_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        metric_collection_job = client.metric_collection_job.list()
        assert_matches_type(MetricCollectionJobListResponse, metric_collection_job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        metric_collection_job = client.metric_collection_job.list(
            after="after",
            limit=20,
            status="PENDING",
        )
        assert_matches_type(MetricCollectionJobListResponse, metric_collection_job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.metric_collection_job.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_collection_job = response.parse()
        assert_matches_type(MetricCollectionJobListResponse, metric_collection_job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.metric_collection_job.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_collection_job = response.parse()
            assert_matches_type(MetricCollectionJobListResponse, metric_collection_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        metric_collection_job = client.metric_collection_job.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetricCollectionJobGetByIDResponse, metric_collection_job, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.metric_collection_job.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_collection_job = response.parse()
        assert_matches_type(MetricCollectionJobGetByIDResponse, metric_collection_job, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.metric_collection_job.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_collection_job = response.parse()
            assert_matches_type(MetricCollectionJobGetByIDResponse, metric_collection_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.metric_collection_job.with_raw_response.get_by_id(
                "",
            )


class TestAsyncMetricCollectionJob:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        metric_collection_job = await async_client.metric_collection_job.create(
            call_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(MetricCollectionJobCreateResponse, metric_collection_job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_collection_job.with_raw_response.create(
            call_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_collection_job = await response.parse()
        assert_matches_type(MetricCollectionJobCreateResponse, metric_collection_job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_collection_job.with_streaming_response.create(
            call_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_collection_job = await response.parse()
            assert_matches_type(MetricCollectionJobCreateResponse, metric_collection_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        metric_collection_job = await async_client.metric_collection_job.list()
        assert_matches_type(MetricCollectionJobListResponse, metric_collection_job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        metric_collection_job = await async_client.metric_collection_job.list(
            after="after",
            limit=20,
            status="PENDING",
        )
        assert_matches_type(MetricCollectionJobListResponse, metric_collection_job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_collection_job.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_collection_job = await response.parse()
        assert_matches_type(MetricCollectionJobListResponse, metric_collection_job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_collection_job.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_collection_job = await response.parse()
            assert_matches_type(MetricCollectionJobListResponse, metric_collection_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        metric_collection_job = await async_client.metric_collection_job.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetricCollectionJobGetByIDResponse, metric_collection_job, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_collection_job.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_collection_job = await response.parse()
        assert_matches_type(MetricCollectionJobGetByIDResponse, metric_collection_job, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_collection_job.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_collection_job = await response.parse()
            assert_matches_type(MetricCollectionJobGetByIDResponse, metric_collection_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.metric_collection_job.with_raw_response.get_by_id(
                "",
            )
