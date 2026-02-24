# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationRunPlanListResponse,
    SimulationRunPlanCreateResponse,
    SimulationRunPlanDeleteResponse,
    SimulationRunPlanUpdateResponse,
    SimulationRunPlanGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationRunPlan:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        simulation_run_plan = client.simulation_run_plan.create(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            max_simulation_duration_seconds=300,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="My Run Plan",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(SimulationRunPlanCreateResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        simulation_run_plan = client.simulation_run_plan.create(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            max_simulation_duration_seconds=300,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="My Run Plan",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "variables": {
                        "customerName": "John Doe",
                        "appointmentDate": "2024-02-15",
                    },
                }
            ],
            auto_run=False,
            description="A run plan for testing inbound calls",
            end_call_phrases=["goodbye"],
            execution_mode="PARALLEL",
            iteration_count=1,
            max_concurrent_jobs=5,
            silence_timeout_seconds=30,
        )
        assert_matches_type(SimulationRunPlanCreateResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.simulation_run_plan.with_raw_response.create(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            max_simulation_duration_seconds=300,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="My Run Plan",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = response.parse()
        assert_matches_type(SimulationRunPlanCreateResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.simulation_run_plan.with_streaming_response.create(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            max_simulation_duration_seconds=300,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="My Run Plan",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = response.parse()
            assert_matches_type(SimulationRunPlanCreateResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        simulation_run_plan = client.simulation_run_plan.update(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationRunPlanUpdateResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        simulation_run_plan = client.simulation_run_plan.update(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            description="description",
            direction="INBOUND",
            end_call_phrases=["string"],
            execution_mode="PARALLEL",
            iteration_count=1,
            max_concurrent_jobs=1,
            max_simulation_duration_seconds=1,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="x",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "variables": {"foo": "string"},
                }
            ],
            silence_timeout_seconds=1,
        )
        assert_matches_type(SimulationRunPlanUpdateResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.simulation_run_plan.with_raw_response.update(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = response.parse()
        assert_matches_type(SimulationRunPlanUpdateResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.simulation_run_plan.with_streaming_response.update(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = response.parse()
            assert_matches_type(SimulationRunPlanUpdateResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.simulation_run_plan.with_raw_response.update(
                plan_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        simulation_run_plan = client.simulation_run_plan.list()
        assert_matches_type(SimulationRunPlanListResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        simulation_run_plan = client.simulation_run_plan.list(
            after="after",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=20,
            search_text="searchText",
        )
        assert_matches_type(SimulationRunPlanListResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.simulation_run_plan.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = response.parse()
        assert_matches_type(SimulationRunPlanListResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.simulation_run_plan.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = response.parse()
            assert_matches_type(SimulationRunPlanListResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        simulation_run_plan = client.simulation_run_plan.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationRunPlanDeleteResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.simulation_run_plan.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = response.parse()
        assert_matches_type(SimulationRunPlanDeleteResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.simulation_run_plan.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = response.parse()
            assert_matches_type(SimulationRunPlanDeleteResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.simulation_run_plan.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        simulation_run_plan = client.simulation_run_plan.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationRunPlanGetByIDResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.simulation_run_plan.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = response.parse()
        assert_matches_type(SimulationRunPlanGetByIDResponse, simulation_run_plan, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.simulation_run_plan.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = response.parse()
            assert_matches_type(SimulationRunPlanGetByIDResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.simulation_run_plan.with_raw_response.get_by_id(
                "",
            )


class TestAsyncSimulationRunPlan:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        simulation_run_plan = await async_client.simulation_run_plan.create(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            max_simulation_duration_seconds=300,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="My Run Plan",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(SimulationRunPlanCreateResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_run_plan = await async_client.simulation_run_plan.create(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            max_simulation_duration_seconds=300,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="My Run Plan",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "variables": {
                        "customerName": "John Doe",
                        "appointmentDate": "2024-02-15",
                    },
                }
            ],
            auto_run=False,
            description="A run plan for testing inbound calls",
            end_call_phrases=["goodbye"],
            execution_mode="PARALLEL",
            iteration_count=1,
            max_concurrent_jobs=5,
            silence_timeout_seconds=30,
        )
        assert_matches_type(SimulationRunPlanCreateResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_plan.with_raw_response.create(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            max_simulation_duration_seconds=300,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="My Run Plan",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = await response.parse()
        assert_matches_type(SimulationRunPlanCreateResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_plan.with_streaming_response.create(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            max_simulation_duration_seconds=300,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="My Run Plan",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = await response.parse()
            assert_matches_type(SimulationRunPlanCreateResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        simulation_run_plan = await async_client.simulation_run_plan.update(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationRunPlanUpdateResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_run_plan = await async_client.simulation_run_plan.update(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            description="description",
            direction="INBOUND",
            end_call_phrases=["string"],
            execution_mode="PARALLEL",
            iteration_count=1,
            max_concurrent_jobs=1,
            max_simulation_duration_seconds=1,
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="x",
            personas=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            scenarios=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "variables": {"foo": "string"},
                }
            ],
            silence_timeout_seconds=1,
        )
        assert_matches_type(SimulationRunPlanUpdateResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_plan.with_raw_response.update(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = await response.parse()
        assert_matches_type(SimulationRunPlanUpdateResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_plan.with_streaming_response.update(
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = await response.parse()
            assert_matches_type(SimulationRunPlanUpdateResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.simulation_run_plan.with_raw_response.update(
                plan_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        simulation_run_plan = await async_client.simulation_run_plan.list()
        assert_matches_type(SimulationRunPlanListResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_run_plan = await async_client.simulation_run_plan.list(
            after="after",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=20,
            search_text="searchText",
        )
        assert_matches_type(SimulationRunPlanListResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_plan.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = await response.parse()
        assert_matches_type(SimulationRunPlanListResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_plan.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = await response.parse()
            assert_matches_type(SimulationRunPlanListResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        simulation_run_plan = await async_client.simulation_run_plan.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationRunPlanDeleteResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_plan.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = await response.parse()
        assert_matches_type(SimulationRunPlanDeleteResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_plan.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = await response.parse()
            assert_matches_type(SimulationRunPlanDeleteResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.simulation_run_plan.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        simulation_run_plan = await async_client.simulation_run_plan.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationRunPlanGetByIDResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_run_plan.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_run_plan = await response.parse()
        assert_matches_type(SimulationRunPlanGetByIDResponse, simulation_run_plan, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_run_plan.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_run_plan = await response.parse()
            assert_matches_type(SimulationRunPlanGetByIDResponse, simulation_run_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.simulation_run_plan.with_raw_response.get_by_id(
                "",
            )
