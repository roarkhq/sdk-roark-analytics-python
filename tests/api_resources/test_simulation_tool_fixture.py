# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationToolFixtureListResponse,
    SimulationToolFixtureCreateResponse,
    SimulationToolFixtureDeleteResponse,
    SimulationToolFixtureUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationToolFixture:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        simulation_tool_fixture = client.simulation_tool_fixture.create(
            tool_name="lookup_availability",
        )
        assert_matches_type(SimulationToolFixtureCreateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        simulation_tool_fixture = client.simulation_tool_fixture.create(
            tool_name="lookup_availability",
            customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Forces the no-availability branch",
            enabled=True,
            response={"slots": []},
        )
        assert_matches_type(SimulationToolFixtureCreateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.simulation_tool_fixture.with_raw_response.create(
            tool_name="lookup_availability",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_tool_fixture = response.parse()
        assert_matches_type(SimulationToolFixtureCreateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.simulation_tool_fixture.with_streaming_response.create(
            tool_name="lookup_availability",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_tool_fixture = response.parse()
            assert_matches_type(SimulationToolFixtureCreateResponse, simulation_tool_fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        simulation_tool_fixture = client.simulation_tool_fixture.update(
            fixture_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationToolFixtureUpdateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        simulation_tool_fixture = client.simulation_tool_fixture.update(
            fixture_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            enabled=True,
            response="response",
        )
        assert_matches_type(SimulationToolFixtureUpdateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.simulation_tool_fixture.with_raw_response.update(
            fixture_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_tool_fixture = response.parse()
        assert_matches_type(SimulationToolFixtureUpdateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.simulation_tool_fixture.with_streaming_response.update(
            fixture_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_tool_fixture = response.parse()
            assert_matches_type(SimulationToolFixtureUpdateResponse, simulation_tool_fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fixture_id` but received ''"):
            client.simulation_tool_fixture.with_raw_response.update(
                fixture_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        simulation_tool_fixture = client.simulation_tool_fixture.list()
        assert_matches_type(SimulationToolFixtureListResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        simulation_tool_fixture = client.simulation_tool_fixture.list(
            tool_name="toolName",
        )
        assert_matches_type(SimulationToolFixtureListResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.simulation_tool_fixture.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_tool_fixture = response.parse()
        assert_matches_type(SimulationToolFixtureListResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.simulation_tool_fixture.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_tool_fixture = response.parse()
            assert_matches_type(SimulationToolFixtureListResponse, simulation_tool_fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        simulation_tool_fixture = client.simulation_tool_fixture.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationToolFixtureDeleteResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.simulation_tool_fixture.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_tool_fixture = response.parse()
        assert_matches_type(SimulationToolFixtureDeleteResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.simulation_tool_fixture.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_tool_fixture = response.parse()
            assert_matches_type(SimulationToolFixtureDeleteResponse, simulation_tool_fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fixture_id` but received ''"):
            client.simulation_tool_fixture.with_raw_response.delete(
                "",
            )


class TestAsyncSimulationToolFixture:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        simulation_tool_fixture = await async_client.simulation_tool_fixture.create(
            tool_name="lookup_availability",
        )
        assert_matches_type(SimulationToolFixtureCreateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_tool_fixture = await async_client.simulation_tool_fixture.create(
            tool_name="lookup_availability",
            customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Forces the no-availability branch",
            enabled=True,
            response={"slots": []},
        )
        assert_matches_type(SimulationToolFixtureCreateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_tool_fixture.with_raw_response.create(
            tool_name="lookup_availability",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_tool_fixture = await response.parse()
        assert_matches_type(SimulationToolFixtureCreateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_tool_fixture.with_streaming_response.create(
            tool_name="lookup_availability",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_tool_fixture = await response.parse()
            assert_matches_type(SimulationToolFixtureCreateResponse, simulation_tool_fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        simulation_tool_fixture = await async_client.simulation_tool_fixture.update(
            fixture_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationToolFixtureUpdateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_tool_fixture = await async_client.simulation_tool_fixture.update(
            fixture_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            enabled=True,
            response="response",
        )
        assert_matches_type(SimulationToolFixtureUpdateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_tool_fixture.with_raw_response.update(
            fixture_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_tool_fixture = await response.parse()
        assert_matches_type(SimulationToolFixtureUpdateResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_tool_fixture.with_streaming_response.update(
            fixture_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_tool_fixture = await response.parse()
            assert_matches_type(SimulationToolFixtureUpdateResponse, simulation_tool_fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fixture_id` but received ''"):
            await async_client.simulation_tool_fixture.with_raw_response.update(
                fixture_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        simulation_tool_fixture = await async_client.simulation_tool_fixture.list()
        assert_matches_type(SimulationToolFixtureListResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_tool_fixture = await async_client.simulation_tool_fixture.list(
            tool_name="toolName",
        )
        assert_matches_type(SimulationToolFixtureListResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_tool_fixture.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_tool_fixture = await response.parse()
        assert_matches_type(SimulationToolFixtureListResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_tool_fixture.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_tool_fixture = await response.parse()
            assert_matches_type(SimulationToolFixtureListResponse, simulation_tool_fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        simulation_tool_fixture = await async_client.simulation_tool_fixture.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationToolFixtureDeleteResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_tool_fixture.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_tool_fixture = await response.parse()
        assert_matches_type(SimulationToolFixtureDeleteResponse, simulation_tool_fixture, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_tool_fixture.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_tool_fixture = await response.parse()
            assert_matches_type(SimulationToolFixtureDeleteResponse, simulation_tool_fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fixture_id` but received ''"):
            await async_client.simulation_tool_fixture.with_raw_response.delete(
                "",
            )
