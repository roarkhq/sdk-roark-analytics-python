# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationEnvironmentListResponse,
    SimulationEnvironmentCreateResponse,
    SimulationEnvironmentDeleteResponse,
    SimulationEnvironmentUpdateResponse,
    SimulationEnvironmentGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationEnvironment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        simulation_environment = client.simulation_environment.create(
            background_noise="OFFICE",
            name="Busy call centre",
        )
        assert_matches_type(SimulationEnvironmentCreateResponse, simulation_environment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        simulation_environment = client.simulation_environment.create(
            background_noise="OFFICE",
            name="Busy call centre",
            background_noise_volume=0.3,
            description="Open-plan office at peak hours",
        )
        assert_matches_type(SimulationEnvironmentCreateResponse, simulation_environment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.simulation_environment.with_raw_response.create(
            background_noise="OFFICE",
            name="Busy call centre",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = response.parse()
        assert_matches_type(SimulationEnvironmentCreateResponse, simulation_environment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.simulation_environment.with_streaming_response.create(
            background_noise="OFFICE",
            name="Busy call centre",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = response.parse()
            assert_matches_type(SimulationEnvironmentCreateResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        simulation_environment = client.simulation_environment.update(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationEnvironmentUpdateResponse, simulation_environment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        simulation_environment = client.simulation_environment.update(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            background_noise="OFFICE",
            background_noise_volume=0.3,
            description="Open-plan office at peak hours",
            name="Busy call centre",
        )
        assert_matches_type(SimulationEnvironmentUpdateResponse, simulation_environment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.simulation_environment.with_raw_response.update(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = response.parse()
        assert_matches_type(SimulationEnvironmentUpdateResponse, simulation_environment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.simulation_environment.with_streaming_response.update(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = response.parse()
            assert_matches_type(SimulationEnvironmentUpdateResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.simulation_environment.with_raw_response.update(
                environment_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        simulation_environment = client.simulation_environment.list()
        assert_matches_type(SimulationEnvironmentListResponse, simulation_environment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        simulation_environment = client.simulation_environment.list(
            after="after",
            limit=1,
        )
        assert_matches_type(SimulationEnvironmentListResponse, simulation_environment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.simulation_environment.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = response.parse()
        assert_matches_type(SimulationEnvironmentListResponse, simulation_environment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.simulation_environment.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = response.parse()
            assert_matches_type(SimulationEnvironmentListResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        simulation_environment = client.simulation_environment.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationEnvironmentDeleteResponse, simulation_environment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.simulation_environment.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = response.parse()
        assert_matches_type(SimulationEnvironmentDeleteResponse, simulation_environment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.simulation_environment.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = response.parse()
            assert_matches_type(SimulationEnvironmentDeleteResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.simulation_environment.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        simulation_environment = client.simulation_environment.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationEnvironmentGetByIDResponse, simulation_environment, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.simulation_environment.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = response.parse()
        assert_matches_type(SimulationEnvironmentGetByIDResponse, simulation_environment, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.simulation_environment.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = response.parse()
            assert_matches_type(SimulationEnvironmentGetByIDResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.simulation_environment.with_raw_response.get_by_id(
                "",
            )


class TestAsyncSimulationEnvironment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        simulation_environment = await async_client.simulation_environment.create(
            background_noise="OFFICE",
            name="Busy call centre",
        )
        assert_matches_type(SimulationEnvironmentCreateResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_environment = await async_client.simulation_environment.create(
            background_noise="OFFICE",
            name="Busy call centre",
            background_noise_volume=0.3,
            description="Open-plan office at peak hours",
        )
        assert_matches_type(SimulationEnvironmentCreateResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_environment.with_raw_response.create(
            background_noise="OFFICE",
            name="Busy call centre",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = await response.parse()
        assert_matches_type(SimulationEnvironmentCreateResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_environment.with_streaming_response.create(
            background_noise="OFFICE",
            name="Busy call centre",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = await response.parse()
            assert_matches_type(SimulationEnvironmentCreateResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        simulation_environment = await async_client.simulation_environment.update(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationEnvironmentUpdateResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_environment = await async_client.simulation_environment.update(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            background_noise="OFFICE",
            background_noise_volume=0.3,
            description="Open-plan office at peak hours",
            name="Busy call centre",
        )
        assert_matches_type(SimulationEnvironmentUpdateResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_environment.with_raw_response.update(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = await response.parse()
        assert_matches_type(SimulationEnvironmentUpdateResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_environment.with_streaming_response.update(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = await response.parse()
            assert_matches_type(SimulationEnvironmentUpdateResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.simulation_environment.with_raw_response.update(
                environment_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        simulation_environment = await async_client.simulation_environment.list()
        assert_matches_type(SimulationEnvironmentListResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_environment = await async_client.simulation_environment.list(
            after="after",
            limit=1,
        )
        assert_matches_type(SimulationEnvironmentListResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_environment.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = await response.parse()
        assert_matches_type(SimulationEnvironmentListResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_environment.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = await response.parse()
            assert_matches_type(SimulationEnvironmentListResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        simulation_environment = await async_client.simulation_environment.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationEnvironmentDeleteResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_environment.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = await response.parse()
        assert_matches_type(SimulationEnvironmentDeleteResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_environment.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = await response.parse()
            assert_matches_type(SimulationEnvironmentDeleteResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.simulation_environment.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        simulation_environment = await async_client.simulation_environment.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationEnvironmentGetByIDResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_environment.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_environment = await response.parse()
        assert_matches_type(SimulationEnvironmentGetByIDResponse, simulation_environment, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_environment.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_environment = await response.parse()
            assert_matches_type(SimulationEnvironmentGetByIDResponse, simulation_environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.simulation_environment.with_raw_response.get_by_id(
                "",
            )
