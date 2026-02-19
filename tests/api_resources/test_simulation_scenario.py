# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationScenarioListResponse,
    SimulationScenarioCreateResponse,
    SimulationScenarioDeleteResponse,
    SimulationScenarioUpdateResponse,
    SimulationScenarioGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationScenario:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        simulation_scenario = client.simulation_scenario.create(
            name="x",
            steps=[
                {
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        )
        assert_matches_type(SimulationScenarioCreateResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.simulation_scenario.with_raw_response.create(
            name="x",
            steps=[
                {
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = response.parse()
        assert_matches_type(SimulationScenarioCreateResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.simulation_scenario.with_streaming_response.create(
            name="x",
            steps=[
                {
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = response.parse()
            assert_matches_type(SimulationScenarioCreateResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        simulation_scenario = client.simulation_scenario.update(
            scenario_id="scenarioId",
            step_changes=[
                {
                    "action": "create",
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        )
        assert_matches_type(SimulationScenarioUpdateResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        simulation_scenario = client.simulation_scenario.update(
            scenario_id="scenarioId",
            step_changes=[
                {
                    "action": "create",
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
            name="x",
        )
        assert_matches_type(SimulationScenarioUpdateResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.simulation_scenario.with_raw_response.update(
            scenario_id="scenarioId",
            step_changes=[
                {
                    "action": "create",
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = response.parse()
        assert_matches_type(SimulationScenarioUpdateResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.simulation_scenario.with_streaming_response.update(
            scenario_id="scenarioId",
            step_changes=[
                {
                    "action": "create",
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = response.parse()
            assert_matches_type(SimulationScenarioUpdateResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scenario_id` but received ''"):
            client.simulation_scenario.with_raw_response.update(
                scenario_id="",
                step_changes=[
                    {
                        "action": "create",
                        "content": "content",
                        "type": "AGENT_TURN",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        simulation_scenario = client.simulation_scenario.list()
        assert_matches_type(SimulationScenarioListResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        simulation_scenario = client.simulation_scenario.list(
            after="after",
            limit=1,
        )
        assert_matches_type(SimulationScenarioListResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.simulation_scenario.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = response.parse()
        assert_matches_type(SimulationScenarioListResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.simulation_scenario.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = response.parse()
            assert_matches_type(SimulationScenarioListResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        simulation_scenario = client.simulation_scenario.delete(
            "scenarioId",
        )
        assert_matches_type(SimulationScenarioDeleteResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.simulation_scenario.with_raw_response.delete(
            "scenarioId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = response.parse()
        assert_matches_type(SimulationScenarioDeleteResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.simulation_scenario.with_streaming_response.delete(
            "scenarioId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = response.parse()
            assert_matches_type(SimulationScenarioDeleteResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scenario_id` but received ''"):
            client.simulation_scenario.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        simulation_scenario = client.simulation_scenario.get_by_id(
            "scenarioId",
        )
        assert_matches_type(SimulationScenarioGetByIDResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.simulation_scenario.with_raw_response.get_by_id(
            "scenarioId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = response.parse()
        assert_matches_type(SimulationScenarioGetByIDResponse, simulation_scenario, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.simulation_scenario.with_streaming_response.get_by_id(
            "scenarioId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = response.parse()
            assert_matches_type(SimulationScenarioGetByIDResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scenario_id` but received ''"):
            client.simulation_scenario.with_raw_response.get_by_id(
                "",
            )


class TestAsyncSimulationScenario:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        simulation_scenario = await async_client.simulation_scenario.create(
            name="x",
            steps=[
                {
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        )
        assert_matches_type(SimulationScenarioCreateResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_scenario.with_raw_response.create(
            name="x",
            steps=[
                {
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = await response.parse()
        assert_matches_type(SimulationScenarioCreateResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_scenario.with_streaming_response.create(
            name="x",
            steps=[
                {
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = await response.parse()
            assert_matches_type(SimulationScenarioCreateResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        simulation_scenario = await async_client.simulation_scenario.update(
            scenario_id="scenarioId",
            step_changes=[
                {
                    "action": "create",
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        )
        assert_matches_type(SimulationScenarioUpdateResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_scenario = await async_client.simulation_scenario.update(
            scenario_id="scenarioId",
            step_changes=[
                {
                    "action": "create",
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
            name="x",
        )
        assert_matches_type(SimulationScenarioUpdateResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_scenario.with_raw_response.update(
            scenario_id="scenarioId",
            step_changes=[
                {
                    "action": "create",
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = await response.parse()
        assert_matches_type(SimulationScenarioUpdateResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_scenario.with_streaming_response.update(
            scenario_id="scenarioId",
            step_changes=[
                {
                    "action": "create",
                    "content": "content",
                    "type": "AGENT_TURN",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = await response.parse()
            assert_matches_type(SimulationScenarioUpdateResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scenario_id` but received ''"):
            await async_client.simulation_scenario.with_raw_response.update(
                scenario_id="",
                step_changes=[
                    {
                        "action": "create",
                        "content": "content",
                        "type": "AGENT_TURN",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        simulation_scenario = await async_client.simulation_scenario.list()
        assert_matches_type(SimulationScenarioListResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_scenario = await async_client.simulation_scenario.list(
            after="after",
            limit=1,
        )
        assert_matches_type(SimulationScenarioListResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_scenario.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = await response.parse()
        assert_matches_type(SimulationScenarioListResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_scenario.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = await response.parse()
            assert_matches_type(SimulationScenarioListResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        simulation_scenario = await async_client.simulation_scenario.delete(
            "scenarioId",
        )
        assert_matches_type(SimulationScenarioDeleteResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_scenario.with_raw_response.delete(
            "scenarioId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = await response.parse()
        assert_matches_type(SimulationScenarioDeleteResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_scenario.with_streaming_response.delete(
            "scenarioId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = await response.parse()
            assert_matches_type(SimulationScenarioDeleteResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scenario_id` but received ''"):
            await async_client.simulation_scenario.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        simulation_scenario = await async_client.simulation_scenario.get_by_id(
            "scenarioId",
        )
        assert_matches_type(SimulationScenarioGetByIDResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_scenario.with_raw_response.get_by_id(
            "scenarioId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_scenario = await response.parse()
        assert_matches_type(SimulationScenarioGetByIDResponse, simulation_scenario, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_scenario.with_streaming_response.get_by_id(
            "scenarioId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_scenario = await response.parse()
            assert_matches_type(SimulationScenarioGetByIDResponse, simulation_scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scenario_id` but received ''"):
            await async_client.simulation_scenario.with_raw_response.get_by_id(
                "",
            )
