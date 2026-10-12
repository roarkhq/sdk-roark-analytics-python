# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationRunGroupListResponse,
    SimulationRunGroupCreateResponse,
    SimulationRunGroupDeleteResponse,
    SimulationRunGroupGetByIDResponse,
    SimulationRunGroupRegenerateReportResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationRunGroup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        simulation_run_group = client.simulation_run_group.create()
        assert_matches_type(SimulationRunGroupCreateResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        simulation_run_group = client.simulation_run_group.create(
            name="Release 4.2 regression",
            simulation_run_plan_ids=["7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f", "9a8b7c6d-5e4f-4a3b-8c2d-1e0f9a8b7c6d"],
            simulation_run_plan_job_ids=[
                "7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f",
                "9a8b7c6d-5e4f-4a3b-8c2d-1e0f9a8b7c6d",
            ],
        )
        assert_matches_type(SimulationRunGroupCreateResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.simulation_run_group.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = response.parse()
        assert_matches_type(SimulationRunGroupCreateResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.simulation_run_group.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = response.parse()
            assert_matches_type(SimulationRunGroupCreateResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        simulation_run_group = client.simulation_run_group.list()
        assert_matches_type(SimulationRunGroupListResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        simulation_run_group = client.simulation_run_group.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SimulationRunGroupListResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.simulation_run_group.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = response.parse()
        assert_matches_type(SimulationRunGroupListResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.simulation_run_group.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = response.parse()
            assert_matches_type(SimulationRunGroupListResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        simulation_run_group = client.simulation_run_group.delete(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )
        assert_matches_type(SimulationRunGroupDeleteResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.simulation_run_group.with_raw_response.delete(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = response.parse()
        assert_matches_type(SimulationRunGroupDeleteResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.simulation_run_group.with_streaming_response.delete(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = response.parse()
            assert_matches_type(SimulationRunGroupDeleteResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.simulation_run_group.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        simulation_run_group = client.simulation_run_group.get_by_id(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )
        assert_matches_type(SimulationRunGroupGetByIDResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.simulation_run_group.with_raw_response.get_by_id(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = response.parse()
        assert_matches_type(SimulationRunGroupGetByIDResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.simulation_run_group.with_streaming_response.get_by_id(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = response.parse()
            assert_matches_type(SimulationRunGroupGetByIDResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.simulation_run_group.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_regenerate_report(self, client: Roark) -> None:
        simulation_run_group = client.simulation_run_group.regenerate_report(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )
        assert_matches_type(SimulationRunGroupRegenerateReportResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_raw_response_regenerate_report(self, client: Roark) -> None:
        response = client.simulation_run_group.with_raw_response.regenerate_report(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = response.parse()
        assert_matches_type(SimulationRunGroupRegenerateReportResponse, simulation_run_group, path=["response"])

    @parametrize
    def test_streaming_response_regenerate_report(self, client: Roark) -> None:
        with client.simulation_run_group.with_streaming_response.regenerate_report(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = response.parse()
            assert_matches_type(SimulationRunGroupRegenerateReportResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_regenerate_report(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.simulation_run_group.with_raw_response.regenerate_report(
                "",
            )


class TestAsyncSimulationRunGroup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        simulation_run_group = await async_client.simulation_run_group.create()
        assert_matches_type(SimulationRunGroupCreateResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_run_group = await async_client.simulation_run_group.create(
            name="Release 4.2 regression",
            simulation_run_plan_ids=["7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f", "9a8b7c6d-5e4f-4a3b-8c2d-1e0f9a8b7c6d"],
            simulation_run_plan_job_ids=[
                "7f3e4d2c-8a91-4b5c-9e6f-1a2b3c4d5e6f",
                "9a8b7c6d-5e4f-4a3b-8c2d-1e0f9a8b7c6d",
            ],
        )
        assert_matches_type(SimulationRunGroupCreateResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_group.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = await response.parse()
        assert_matches_type(SimulationRunGroupCreateResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_group.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = await response.parse()
            assert_matches_type(SimulationRunGroupCreateResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        simulation_run_group = await async_client.simulation_run_group.list()
        assert_matches_type(SimulationRunGroupListResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_run_group = await async_client.simulation_run_group.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SimulationRunGroupListResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_group.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = await response.parse()
        assert_matches_type(SimulationRunGroupListResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_group.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = await response.parse()
            assert_matches_type(SimulationRunGroupListResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        simulation_run_group = await async_client.simulation_run_group.delete(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )
        assert_matches_type(SimulationRunGroupDeleteResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_group.with_raw_response.delete(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = await response.parse()
        assert_matches_type(SimulationRunGroupDeleteResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_group.with_streaming_response.delete(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = await response.parse()
            assert_matches_type(SimulationRunGroupDeleteResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.simulation_run_group.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        simulation_run_group = await async_client.simulation_run_group.get_by_id(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )
        assert_matches_type(SimulationRunGroupGetByIDResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_group.with_raw_response.get_by_id(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = await response.parse()
        assert_matches_type(SimulationRunGroupGetByIDResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_group.with_streaming_response.get_by_id(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = await response.parse()
            assert_matches_type(SimulationRunGroupGetByIDResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.simulation_run_group.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_regenerate_report(self, async_client: AsyncRoark) -> None:
        simulation_run_group = await async_client.simulation_run_group.regenerate_report(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )
        assert_matches_type(SimulationRunGroupRegenerateReportResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_raw_response_regenerate_report(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_group.with_raw_response.regenerate_report(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_group = await response.parse()
        assert_matches_type(SimulationRunGroupRegenerateReportResponse, simulation_run_group, path=["response"])

    @parametrize
    async def test_streaming_response_regenerate_report(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_group.with_streaming_response.regenerate_report(
            "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_group = await response.parse()
            assert_matches_type(SimulationRunGroupRegenerateReportResponse, simulation_run_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_regenerate_report(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.simulation_run_group.with_raw_response.regenerate_report(
                "",
            )
