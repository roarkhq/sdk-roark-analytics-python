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
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{}],
            },
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_1(self, client: Roark) -> None:
        simulation = client.simulation.run(
            plan={
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "metric_id": "x", "slug": "x"}],
                "description": "A run plan for testing inbound calls",
                "end_call_phrases": ["goodbye"],
                "end_call_reasons": ["Order has been confirmed by the agent"],
                "execution_mode": "PARALLEL",
                "flows": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "edge_cases": "ALL",
                        "happy_path": True,
                        "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "variables": {"customer_name": "John Doe", "appointment_date": "2024-02-15"},
                    }
                ],
                "iteration_count": 1,
                "max_concurrent_jobs": 5,
                "name": "Billing regression",
                "personas": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "scenarios": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "variables": {"customer_name": "John Doe", "appointment_date": "2024-02-15"},
                    }
                ],
                "silence_timeout_seconds": 30,
            },
            save_as_plan=True,
            variables={"order_number": "12345", "environment": "staging"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_run_overload_1(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.run(
            plan={
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
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
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
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
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_2(self, client: Roark) -> None:
        simulation = client.simulation.run(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            variables={"order_number": "12345", "environment": "staging"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_run_overload_2(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.run(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_2(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.run(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{}],
            },
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_1(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            plan={
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
                "max_simulation_duration_seconds": 300,
                "metrics": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "metric_id": "x", "slug": "x"}],
                "description": "A run plan for testing inbound calls",
                "end_call_phrases": ["goodbye"],
                "end_call_reasons": ["Order has been confirmed by the agent"],
                "execution_mode": "PARALLEL",
                "flows": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "edge_cases": "ALL",
                        "happy_path": True,
                        "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "variables": {"customer_name": "John Doe", "appointment_date": "2024-02-15"},
                    }
                ],
                "iteration_count": 1,
                "max_concurrent_jobs": 5,
                "name": "Billing regression",
                "personas": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "scenarios": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "variables": {"customer_name": "John Doe", "appointment_date": "2024-02-15"},
                    }
                ],
                "silence_timeout_seconds": 30,
            },
            save_as_plan=True,
            variables={"order_number": "12345", "environment": "staging"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.run(
            plan={
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
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
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
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
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_2(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            variables={"order_number": "12345", "environment": "staging"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.run(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.run(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationRunResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True
