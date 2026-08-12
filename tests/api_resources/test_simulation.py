# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import SimulationRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_run_overload_1(self, client: Roark) -> None:
        simulation = client.simulation.run(
            plan={
                "agent_endpoints": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
                "direction": "OUTBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{}],
            },
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_1(self, client: Roark) -> None:
        simulation = client.simulation.run(
            plan={
                "agent_endpoints": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
                "direction": "OUTBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "metric_id": "x",
                        "slug": "customer_satisfaction",
                    }
                ],
                "description": "A run plan for testing inbound calls",
                "end_call_phrases": ["goodbye"],
                "end_call_reasons": ["Order has been confirmed by the agent"],
                "execution_mode": "PARALLEL",
                "flows": [
                    {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "edge_cases": "ALL",
                        "happy_path": True,
                        "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "variables": {"foo": "string"},
                    }
                ],
                "iteration_count": 1,
                "max_concurrent_jobs": 5,
                "name": "Billing regression",
                "personas": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "scenarios": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "variables": {
                            "customerName": "John Doe",
                            "appointmentDate": "2024-02-15",
                        },
                    }
                ],
                "silence_timeout_seconds": 30,
            },
            save_as_plan=True,
            variables={"orderNumber": "12345"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_run_overload_1(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.run(
            plan={
                "agent_endpoints": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
                "direction": "OUTBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{}],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_1(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.run(
            plan={
                "agent_endpoints": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
                "direction": "OUTBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{}],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationRunResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_overload_2(self, client: Roark) -> None:
        simulation = client.simulation.run(
            plan_id="3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c",
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_2(self, client: Roark) -> None:
        simulation = client.simulation.run(
            plan_id="3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c",
            variables={"orderNumber": "99887"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_run_overload_2(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.run(
            plan_id="3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_2(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.run(
            plan_id="3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationRunResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimulation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_run_overload_1(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            plan={
                "agent_endpoints": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
                "direction": "OUTBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{}],
            },
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_1(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            plan={
                "agent_endpoints": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
                "direction": "OUTBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "metric_id": "x",
                        "slug": "customer_satisfaction",
                    }
                ],
                "description": "A run plan for testing inbound calls",
                "end_call_phrases": ["goodbye"],
                "end_call_reasons": ["Order has been confirmed by the agent"],
                "execution_mode": "PARALLEL",
                "flows": [
                    {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "edge_cases": "ALL",
                        "happy_path": True,
                        "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "variables": {"foo": "string"},
                    }
                ],
                "iteration_count": 1,
                "max_concurrent_jobs": 5,
                "name": "Billing regression",
                "personas": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "scenarios": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "variables": {
                            "customerName": "John Doe",
                            "appointmentDate": "2024-02-15",
                        },
                    }
                ],
                "silence_timeout_seconds": 30,
            },
            save_as_plan=True,
            variables={"orderNumber": "12345"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.run(
            plan={
                "agent_endpoints": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
                "direction": "OUTBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{}],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_1(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.run(
            plan={
                "agent_endpoints": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
                "direction": "OUTBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{}],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationRunResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_overload_2(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            plan_id="3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c",
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_2(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            plan_id="3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c",
            variables={"orderNumber": "99887"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.run(
            plan_id="3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.run(
            plan_id="3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationRunResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True
