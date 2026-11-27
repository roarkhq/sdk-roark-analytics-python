# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationRunResponse,
    SimulationMockToolResponse,
    SimulationGenerateResourcesResponse,
    SimulationGetResourceGenerationResponse,
    SimulationGuideResourceGenerationResponse,
    SimulationListResourceGenerationsResponse,
    SimulationAnswerResourceGenerationResponse,
    SimulationCancelResourceGenerationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_answer_resource_generation(self, client: Roark) -> None:
        simulation = client.simulation.answer_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        )
        assert_matches_type(SimulationAnswerResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_answer_resource_generation(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.answer_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationAnswerResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_answer_resource_generation(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.answer_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationAnswerResourceGenerationResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_answer_resource_generation(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            client.simulation.with_raw_response.answer_resource_generation(
                generation_id="",
                text="x",
            )

    @parametrize
    def test_method_cancel_resource_generation(self, client: Roark) -> None:
        simulation = client.simulation.cancel_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationCancelResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_cancel_resource_generation(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.cancel_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationCancelResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_cancel_resource_generation(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.cancel_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationCancelResourceGenerationResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel_resource_generation(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            client.simulation.with_raw_response.cancel_resource_generation(
                "",
            )

    @parametrize
    def test_method_generate_resources(self, client: Roark) -> None:
        simulation = client.simulation.generate_resources(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SimulationGenerateResourcesResponse, simulation, path=["response"])

    @parametrize
    def test_method_generate_resources_with_all_params(self, client: Roark) -> None:
        simulation = client.simulation.generate_resources(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            agent_endpoint_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            capabilities=["APPOINTMENT_BOOKING"],
            explore={"enabled": True, "max_conversation_minutes": 1, "max_conversations": 1},
            industry="HEALTHCARE",
            industry_description="Funeral services",
            testing_instructions="testingInstructions",
            website_url="https://example.com",
        )
        assert_matches_type(SimulationGenerateResourcesResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_generate_resources(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.generate_resources(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationGenerateResourcesResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_generate_resources(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.generate_resources(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationGenerateResourcesResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_resource_generation(self, client: Roark) -> None:
        simulation = client.simulation.get_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationGetResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_get_resource_generation(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.get_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationGetResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_get_resource_generation(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.get_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationGetResourceGenerationResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_resource_generation(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            client.simulation.with_raw_response.get_resource_generation(
                "",
            )

    @parametrize
    def test_method_guide_resource_generation(self, client: Roark) -> None:
        simulation = client.simulation.guide_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        )
        assert_matches_type(SimulationGuideResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_guide_resource_generation(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.guide_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationGuideResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_guide_resource_generation(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.guide_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationGuideResourceGenerationResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_guide_resource_generation(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            client.simulation.with_raw_response.guide_resource_generation(
                generation_id="",
                text="x",
            )

    @parametrize
    def test_method_list_resource_generations(self, client: Roark) -> None:
        simulation = client.simulation.list_resource_generations()
        assert_matches_type(SimulationListResourceGenerationsResponse, simulation, path=["response"])

    @parametrize
    def test_method_list_resource_generations_with_all_params(self, client: Roark) -> None:
        simulation = client.simulation.list_resource_generations(
            agent_ids="agentIds",
            limit=1,
        )
        assert_matches_type(SimulationListResourceGenerationsResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_list_resource_generations(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.list_resource_generations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationListResourceGenerationsResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_list_resource_generations(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.list_resource_generations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationListResourceGenerationsResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_mock_tool(self, client: Roark) -> None:
        simulation = client.simulation.mock_tool(
            simulation_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_name="book_appointment",
        )
        assert_matches_type(SimulationMockToolResponse, simulation, path=["response"])

    @parametrize
    def test_method_mock_tool_with_all_params(self, client: Roark) -> None:
        simulation = client.simulation.mock_tool(
            simulation_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_name="book_appointment",
            arguments={"date": "2026-10-01", "time": "15:00"},
            session_id="sessionId",
            tool_description="Books an appointment. Args: date (YYYY-MM-DD), time (HH:MM). Returns {confirmationId, status}.",
        )
        assert_matches_type(SimulationMockToolResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_mock_tool(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.mock_tool(
            simulation_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_name="book_appointment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationMockToolResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_mock_tool(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.mock_tool(
            simulation_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_name="book_appointment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationMockToolResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_overload_1(self, client: Roark) -> None:
        simulation = client.simulation.run(
            plan={
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
                "max_simulation_duration_seconds": 300,
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
                "calls_per_second": 0.5,
                "comparison_baseline": "NONE",
                "comparison_property": "BACKGROUND_NOISE",
                "comparison_values": [
                    "NONE",
                    {"value": "OFFICE", "background_noise_volume": 0.6},
                    {"value": "DRIVING", "background_noise_volume": 0.7},
                    {"value": "DRIVING", "background_noise_volume": 1},
                ],
                "description": "A run plan for testing inbound calls",
                "end_call_phrases": ["goodbye"],
                "end_call_reasons": ["Order has been confirmed by the agent"],
                "enrich_with_live_conversation": False,
                "execution_mode": "PARALLEL",
                "flows": [
                    {
                        "edge_cases": "ALL",
                        "happy_path": True,
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "overrides": [
                            {"property": "ACCENT", "value": "IN"},
                            {"property": "BACKGROUND_NOISE", "value": "TRAIN"},
                        ],
                        "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "slug": "sf-prompt-injection",
                        "variables": {"customer_name": "John Doe", "appointment_date": "2024-02-15"},
                    }
                ],
                "include_automatic_metrics": True,
                "include_flow_metrics": True,
                "iteration_count": 1,
                "max_concurrent_jobs": 5,
                "max_no_response_retries": 2,
                "metrics": [
                    {
                        "conversation_source": "SIMULATED",
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "metric_id": "x",
                        "min_pass_rate": 80,
                        "slug": "x",
                    }
                ],
                "name": "Billing regression",
                "no_response_retry_backoff_seconds": 90,
                "personas": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "ramp_up_seconds": 60,
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

    @parametrize
    def test_method_run_overload_3(self, client: Roark) -> None:
        simulation = client.simulation.run(
            plan_config_key="simulationPlan/nightly-screener-suite",
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_3(self, client: Roark) -> None:
        simulation = client.simulation.run(
            plan_config_key="simulationPlan/nightly-screener-suite",
            variables={"order_number": "12345", "environment": "staging"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_run_overload_3(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.run(
            plan_config_key="simulationPlan/nightly-screener-suite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_3(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.run(
            plan_config_key="simulationPlan/nightly-screener-suite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(SimulationRunResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_overload_4(self, client: Roark) -> None:
        simulation = client.simulation.run(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            template="health-check",
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_4(self, client: Roark) -> None:
        simulation = client.simulation.run(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            template="health-check",
            additional_metrics=[{"slug": "call_ended_prematurely"}],
            calls_per_second=0.5,
            comparison_baseline="US",
            comparison_values=["US", "GB", "IN"],
            end_call_phrases=["goodbye"],
            end_call_reasons=["Order has been confirmed by the agent"],
            enrich_with_live_conversation=False,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_mode="PARALLEL",
            flows=[
                {"slug": "sf-prompt-injection", "edge_cases": [{"slug": "data-embedded-injection"}]},
                {"id": "3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c", "happy_path": True},
            ],
            iteration_count=6,
            max_concurrent_jobs=5,
            max_no_response_retries=2,
            max_simulation_duration_seconds=1,
            name="x",
            no_response_retry_backoff_seconds=90,
            persona_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            questions=[{"ask": "What are your holiday hours?", "expect": "We're closed on public holidays."}],
            ramp_up_seconds=60,
            save_as_plan=True,
            silence_timeout_seconds=30,
            variables={"order_number": "12345", "environment": "staging"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_raw_response_run_overload_4(self, client: Roark) -> None:
        response = client.simulation.with_raw_response.run(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            template="health-check",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_4(self, client: Roark) -> None:
        with client.simulation.with_streaming_response.run(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            template="health-check",
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
    async def test_method_answer_resource_generation(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.answer_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        )
        assert_matches_type(SimulationAnswerResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_answer_resource_generation(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.answer_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationAnswerResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_answer_resource_generation(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.answer_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationAnswerResourceGenerationResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_answer_resource_generation(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            await async_client.simulation.with_raw_response.answer_resource_generation(
                generation_id="",
                text="x",
            )

    @parametrize
    async def test_method_cancel_resource_generation(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.cancel_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationCancelResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_cancel_resource_generation(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.cancel_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationCancelResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_cancel_resource_generation(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.cancel_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationCancelResourceGenerationResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel_resource_generation(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            await async_client.simulation.with_raw_response.cancel_resource_generation(
                "",
            )

    @parametrize
    async def test_method_generate_resources(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.generate_resources(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SimulationGenerateResourcesResponse, simulation, path=["response"])

    @parametrize
    async def test_method_generate_resources_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.generate_resources(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            agent_endpoint_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            capabilities=["APPOINTMENT_BOOKING"],
            explore={"enabled": True, "max_conversation_minutes": 1, "max_conversations": 1},
            industry="HEALTHCARE",
            industry_description="Funeral services",
            testing_instructions="testingInstructions",
            website_url="https://example.com",
        )
        assert_matches_type(SimulationGenerateResourcesResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_generate_resources(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.generate_resources(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationGenerateResourcesResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_generate_resources(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.generate_resources(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationGenerateResourcesResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_resource_generation(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.get_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SimulationGetResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_get_resource_generation(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.get_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationGetResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_get_resource_generation(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.get_resource_generation(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationGetResourceGenerationResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_resource_generation(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            await async_client.simulation.with_raw_response.get_resource_generation(
                "",
            )

    @parametrize
    async def test_method_guide_resource_generation(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.guide_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        )
        assert_matches_type(SimulationGuideResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_guide_resource_generation(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.guide_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationGuideResourceGenerationResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_guide_resource_generation(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.guide_resource_generation(
            generation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationGuideResourceGenerationResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_guide_resource_generation(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            await async_client.simulation.with_raw_response.guide_resource_generation(
                generation_id="",
                text="x",
            )

    @parametrize
    async def test_method_list_resource_generations(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.list_resource_generations()
        assert_matches_type(SimulationListResourceGenerationsResponse, simulation, path=["response"])

    @parametrize
    async def test_method_list_resource_generations_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.list_resource_generations(
            agent_ids="agentIds",
            limit=1,
        )
        assert_matches_type(SimulationListResourceGenerationsResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_list_resource_generations(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.list_resource_generations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationListResourceGenerationsResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_list_resource_generations(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.list_resource_generations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationListResourceGenerationsResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_mock_tool(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.mock_tool(
            simulation_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_name="book_appointment",
        )
        assert_matches_type(SimulationMockToolResponse, simulation, path=["response"])

    @parametrize
    async def test_method_mock_tool_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.mock_tool(
            simulation_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_name="book_appointment",
            arguments={"date": "2026-10-01", "time": "15:00"},
            session_id="sessionId",
            tool_description="Books an appointment. Args: date (YYYY-MM-DD), time (HH:MM). Returns {confirmationId, status}.",
        )
        assert_matches_type(SimulationMockToolResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_mock_tool(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.mock_tool(
            simulation_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_name="book_appointment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationMockToolResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_mock_tool(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.mock_tool(
            simulation_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_name="book_appointment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationMockToolResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_overload_1(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            plan={
                "agent_endpoints": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "direction": "INBOUND",
                "max_simulation_duration_seconds": 300,
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
                "calls_per_second": 0.5,
                "comparison_baseline": "NONE",
                "comparison_property": "BACKGROUND_NOISE",
                "comparison_values": [
                    "NONE",
                    {"value": "OFFICE", "background_noise_volume": 0.6},
                    {"value": "DRIVING", "background_noise_volume": 0.7},
                    {"value": "DRIVING", "background_noise_volume": 1},
                ],
                "description": "A run plan for testing inbound calls",
                "end_call_phrases": ["goodbye"],
                "end_call_reasons": ["Order has been confirmed by the agent"],
                "enrich_with_live_conversation": False,
                "execution_mode": "PARALLEL",
                "flows": [
                    {
                        "edge_cases": "ALL",
                        "happy_path": True,
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "overrides": [
                            {"property": "ACCENT", "value": "IN"},
                            {"property": "BACKGROUND_NOISE", "value": "TRAIN"},
                        ],
                        "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "slug": "sf-prompt-injection",
                        "variables": {"customer_name": "John Doe", "appointment_date": "2024-02-15"},
                    }
                ],
                "include_automatic_metrics": True,
                "include_flow_metrics": True,
                "iteration_count": 1,
                "max_concurrent_jobs": 5,
                "max_no_response_retries": 2,
                "metrics": [
                    {
                        "conversation_source": "SIMULATED",
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "metric_id": "x",
                        "min_pass_rate": 80,
                        "slug": "x",
                    }
                ],
                "name": "Billing regression",
                "no_response_retry_backoff_seconds": 90,
                "personas": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "ramp_up_seconds": 60,
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

    @parametrize
    async def test_method_run_overload_3(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            plan_config_key="simulationPlan/nightly-screener-suite",
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_3(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            plan_config_key="simulationPlan/nightly-screener-suite",
            variables={"order_number": "12345", "environment": "staging"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_3(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.run(
            plan_config_key="simulationPlan/nightly-screener-suite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_3(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.run(
            plan_config_key="simulationPlan/nightly-screener-suite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationRunResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_overload_4(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            template="health-check",
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_4(self, async_client: AsyncRoark) -> None:
        simulation = await async_client.simulation.run(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            template="health-check",
            additional_metrics=[{"slug": "call_ended_prematurely"}],
            calls_per_second=0.5,
            comparison_baseline="US",
            comparison_values=["US", "GB", "IN"],
            end_call_phrases=["goodbye"],
            end_call_reasons=["Order has been confirmed by the agent"],
            enrich_with_live_conversation=False,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_mode="PARALLEL",
            flows=[
                {"slug": "sf-prompt-injection", "edge_cases": [{"slug": "data-embedded-injection"}]},
                {"id": "3a1d5e7c-9b2f-4a6d-8c31-5f7e9d0a2b4c", "happy_path": True},
            ],
            iteration_count=6,
            max_concurrent_jobs=5,
            max_no_response_retries=2,
            max_simulation_duration_seconds=1,
            name="x",
            no_response_retry_backoff_seconds=90,
            persona_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            questions=[{"ask": "What are your holiday hours?", "expect": "We're closed on public holidays."}],
            ramp_up_seconds=60,
            save_as_plan=True,
            silence_timeout_seconds=30,
            variables={"order_number": "12345", "environment": "staging"},
        )
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_4(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation.with_raw_response.run(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            template="health-check",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = await response.parse()
        assert_matches_type(SimulationRunResponse, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_4(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation.with_streaming_response.run(
            agent_endpoints=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            direction="INBOUND",
            template="health-check",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(SimulationRunResponse, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True
