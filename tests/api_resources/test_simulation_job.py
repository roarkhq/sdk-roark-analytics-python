# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationJobGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationJob:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        simulation_job = client.simulation_job.get_by_id(
            "7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f",
        )
        assert_matches_type(SimulationJobGetByIDResponse, simulation_job, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.simulation_job.with_raw_response.get_by_id(
            "7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_job = response.parse()
        assert_matches_type(SimulationJobGetByIDResponse, simulation_job, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.simulation_job.with_streaming_response.get_by_id(
            "7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_job = response.parse()
            assert_matches_type(SimulationJobGetByIDResponse, simulation_job, path=["response"])

        assert cast(Any, response.is_closed) is True

class TestAsyncSimulationJob:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        simulation_job = await async_client.simulation_job.get_by_id(
            "7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f",
        )
        assert_matches_type(SimulationJobGetByIDResponse, simulation_job, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_job.with_raw_response.get_by_id(
            "7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_job = await response.parse()
        assert_matches_type(SimulationJobGetByIDResponse, simulation_job, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_job.with_streaming_response.get_by_id(
            "7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_job = await response.parse()
            assert_matches_type(SimulationJobGetByIDResponse, simulation_job, path=["response"])

        assert cast(Any, response.is_closed) is True
