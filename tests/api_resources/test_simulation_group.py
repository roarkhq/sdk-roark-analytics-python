# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationGroupRunResponse,
    SimulationGroupListResponse,
    SimulationGroupCreateResponse,
    SimulationGroupDeleteResponse,
    SimulationGroupUpdateResponse,
    SimulationGroupGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationGroup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        simulation_group = client.simulation_group.create(
            name="Release regression",
            simulation_run_plan_ids=["3c1d2e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "6d7e8f9a-0b1c-4d2e-9f3a-4b5c6d7e8f9a"],
        )
        assert_matches_type(SimulationGroupCreateResponse, simulation_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        simulation_group = client.simulation_group.create(
            name="Release regression",
            simulation_run_plan_ids=["3c1d2e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "6d7e8f9a-0b1c-4d2e-9f3a-4b5c6d7e8f9a"],
            description="description",
            notifications={
                "email": {"enabled": True, "recipients": ["qa-lead@example.com"]},
                "slack": [{"channel_id": "C07ABCDEF12", "channel_name": "qa-reports"}],
            },
        )
        assert_matches_type(SimulationGroupCreateResponse, simulation_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.simulation_group.with_raw_response.create(
            name="Release regression",
            simulation_run_plan_ids=["3c1d2e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "6d7e8f9a-0b1c-4d2e-9f3a-4b5c6d7e8f9a"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = response.parse()
        assert_matches_type(SimulationGroupCreateResponse, simulation_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.simulation_group.with_streaming_response.create(
            name="Release regression",
            simulation_run_plan_ids=["3c1d2e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "6d7e8f9a-0b1c-4d2e-9f3a-4b5c6d7e8f9a"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = response.parse()
            assert_matches_type(SimulationGroupCreateResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        simulation_group = client.simulation_group.update(
            group_id="2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )
        assert_matches_type(SimulationGroupUpdateResponse, simulation_group, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        simulation_group = client.simulation_group.update(
            group_id="2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
            description="description",
            name="x",
            notifications={
                "email": {"enabled": True, "recipients": ["qa-lead@example.com"]},
                "slack": [{"channel_id": "C07ABCDEF12", "channel_name": "qa-reports"}],
            },
            simulation_run_plan_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SimulationGroupUpdateResponse, simulation_group, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.simulation_group.with_raw_response.update(
            group_id="2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = response.parse()
        assert_matches_type(SimulationGroupUpdateResponse, simulation_group, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.simulation_group.with_streaming_response.update(
            group_id="2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = response.parse()
            assert_matches_type(SimulationGroupUpdateResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.simulation_group.with_raw_response.update(
                group_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        simulation_group = client.simulation_group.list()
        assert_matches_type(SimulationGroupListResponse, simulation_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        simulation_group = client.simulation_group.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SimulationGroupListResponse, simulation_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.simulation_group.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = response.parse()
        assert_matches_type(SimulationGroupListResponse, simulation_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.simulation_group.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = response.parse()
            assert_matches_type(SimulationGroupListResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        simulation_group = client.simulation_group.delete(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )
        assert_matches_type(SimulationGroupDeleteResponse, simulation_group, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.simulation_group.with_raw_response.delete(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = response.parse()
        assert_matches_type(SimulationGroupDeleteResponse, simulation_group, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.simulation_group.with_streaming_response.delete(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = response.parse()
            assert_matches_type(SimulationGroupDeleteResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.simulation_group.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        simulation_group = client.simulation_group.get_by_id(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )
        assert_matches_type(SimulationGroupGetByIDResponse, simulation_group, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.simulation_group.with_raw_response.get_by_id(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = response.parse()
        assert_matches_type(SimulationGroupGetByIDResponse, simulation_group, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.simulation_group.with_streaming_response.get_by_id(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = response.parse()
            assert_matches_type(SimulationGroupGetByIDResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.simulation_group.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_run(self, client: Roark) -> None:
        simulation_group = client.simulation_group.run(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )
        assert_matches_type(SimulationGroupRunResponse, simulation_group, path=["response"])

    @parametrize
    def test_raw_response_run(self, client: Roark) -> None:
        response = client.simulation_group.with_raw_response.run(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = response.parse()
        assert_matches_type(SimulationGroupRunResponse, simulation_group, path=["response"])

    @parametrize
    def test_streaming_response_run(self, client: Roark) -> None:
        with client.simulation_group.with_streaming_response.run(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = response.parse()
            assert_matches_type(SimulationGroupRunResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.simulation_group.with_raw_response.run(
                "",
            )


class TestAsyncSimulationGroup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        simulation_group = await async_client.simulation_group.create(
            name="Release regression",
            simulation_run_plan_ids=["3c1d2e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "6d7e8f9a-0b1c-4d2e-9f3a-4b5c6d7e8f9a"],
        )
        assert_matches_type(SimulationGroupCreateResponse, simulation_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_group = await async_client.simulation_group.create(
            name="Release regression",
            simulation_run_plan_ids=["3c1d2e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "6d7e8f9a-0b1c-4d2e-9f3a-4b5c6d7e8f9a"],
            description="description",
            notifications={
                "email": {"enabled": True, "recipients": ["qa-lead@example.com"]},
                "slack": [{"channel_id": "C07ABCDEF12", "channel_name": "qa-reports"}],
            },
        )
        assert_matches_type(SimulationGroupCreateResponse, simulation_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_group.with_raw_response.create(
            name="Release regression",
            simulation_run_plan_ids=["3c1d2e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "6d7e8f9a-0b1c-4d2e-9f3a-4b5c6d7e8f9a"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = await response.parse()
        assert_matches_type(SimulationGroupCreateResponse, simulation_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_group.with_streaming_response.create(
            name="Release regression",
            simulation_run_plan_ids=["3c1d2e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "6d7e8f9a-0b1c-4d2e-9f3a-4b5c6d7e8f9a"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = await response.parse()
            assert_matches_type(SimulationGroupCreateResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        simulation_group = await async_client.simulation_group.update(
            group_id="2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )
        assert_matches_type(SimulationGroupUpdateResponse, simulation_group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_group = await async_client.simulation_group.update(
            group_id="2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
            description="description",
            name="x",
            notifications={
                "email": {"enabled": True, "recipients": ["qa-lead@example.com"]},
                "slack": [{"channel_id": "C07ABCDEF12", "channel_name": "qa-reports"}],
            },
            simulation_run_plan_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SimulationGroupUpdateResponse, simulation_group, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_group.with_raw_response.update(
            group_id="2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = await response.parse()
        assert_matches_type(SimulationGroupUpdateResponse, simulation_group, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_group.with_streaming_response.update(
            group_id="2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = await response.parse()
            assert_matches_type(SimulationGroupUpdateResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.simulation_group.with_raw_response.update(
                group_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        simulation_group = await async_client.simulation_group.list()
        assert_matches_type(SimulationGroupListResponse, simulation_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_group = await async_client.simulation_group.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SimulationGroupListResponse, simulation_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_group.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = await response.parse()
        assert_matches_type(SimulationGroupListResponse, simulation_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_group.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = await response.parse()
            assert_matches_type(SimulationGroupListResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        simulation_group = await async_client.simulation_group.delete(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )
        assert_matches_type(SimulationGroupDeleteResponse, simulation_group, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_group.with_raw_response.delete(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = await response.parse()
        assert_matches_type(SimulationGroupDeleteResponse, simulation_group, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_group.with_streaming_response.delete(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = await response.parse()
            assert_matches_type(SimulationGroupDeleteResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.simulation_group.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        simulation_group = await async_client.simulation_group.get_by_id(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )
        assert_matches_type(SimulationGroupGetByIDResponse, simulation_group, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_group.with_raw_response.get_by_id(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = await response.parse()
        assert_matches_type(SimulationGroupGetByIDResponse, simulation_group, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_group.with_streaming_response.get_by_id(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = await response.parse()
            assert_matches_type(SimulationGroupGetByIDResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.simulation_group.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_run(self, async_client: AsyncRoark) -> None:
        simulation_group = await async_client.simulation_group.run(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )
        assert_matches_type(SimulationGroupRunResponse, simulation_group, path=["response"])

    @parametrize
    async def test_raw_response_run(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_group.with_raw_response.run(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_group = await response.parse()
        assert_matches_type(SimulationGroupRunResponse, simulation_group, path=["response"])

    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_group.with_streaming_response.run(
            "2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_group = await response.parse()
            assert_matches_type(SimulationGroupRunResponse, simulation_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.simulation_group.with_raw_response.run(
                "",
            )
