# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    EvaluationGetJobResponse,
    EvaluationCreateJobResponse,
    EvaluationGetJobRunsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_job(self, client: Roark) -> None:
        evaluation = client.evaluation.create_job(
            evaluators=["string"],
        )
        assert_matches_type(EvaluationCreateJobResponse, evaluation, path=["response"])

    @parametrize
    def test_method_create_job_with_all_params(self, client: Roark) -> None:
        evaluation = client.evaluation.create_job(
            evaluators=["string"],
            call={
                "call_direction": "INBOUND",
                "interface_type": "PHONE",
                "participants": [
                    {
                        "role": "AGENT",
                        "is_simulated": True,
                        "name": "x",
                        "phone_number": "xxx",
                        "spoke_first": True,
                    },
                    {
                        "role": "AGENT",
                        "is_simulated": True,
                        "name": "x",
                        "phone_number": "xxx",
                        "spoke_first": True,
                    },
                ],
                "recording_url": "https://example.com",
                "started_at": "startedAt",
                "ended_reason": "endedReason",
                "ended_status": "AGENT_ENDED_CALL",
                "is_test": True,
                "properties": {"foo": "bar"},
                "retell_call_id": "retellCallId",
                "stereo_recording_url": "https://example.com",
                "tool_invocations": [
                    {
                        "name": "name",
                        "parameters": {"foo": "value"},
                        "result": "string",
                        "start_offset_ms": 0,
                        "description": "description",
                        "end_offset_ms": 0,
                    }
                ],
                "vapi_call_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            dataset={
                "calls": [
                    {
                        "call_direction": "INBOUND",
                        "interface_type": "PHONE",
                        "participants": [
                            {
                                "role": "AGENT",
                                "is_simulated": True,
                                "name": "x",
                                "phone_number": "xxx",
                                "spoke_first": True,
                            },
                            {
                                "role": "AGENT",
                                "is_simulated": True,
                                "name": "x",
                                "phone_number": "xxx",
                                "spoke_first": True,
                            },
                        ],
                        "recording_url": "https://example.com",
                        "started_at": "startedAt",
                        "ended_reason": "endedReason",
                        "ended_status": "AGENT_ENDED_CALL",
                        "is_test": True,
                        "properties": {"foo": "bar"},
                        "retell_call_id": "retellCallId",
                        "stereo_recording_url": "https://example.com",
                        "tool_invocations": [
                            {
                                "name": "name",
                                "parameters": {"foo": "value"},
                                "result": "string",
                                "start_offset_ms": 0,
                                "description": "description",
                                "end_offset_ms": 0,
                            }
                        ],
                        "vapi_call_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
                "name": "name",
            },
        )
        assert_matches_type(EvaluationCreateJobResponse, evaluation, path=["response"])

    @parametrize
    def test_raw_response_create_job(self, client: Roark) -> None:
        response = client.evaluation.with_raw_response.create_job(
            evaluators=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluationCreateJobResponse, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_create_job(self, client: Roark) -> None:
        with client.evaluation.with_streaming_response.create_job(
            evaluators=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluationCreateJobResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_evaluator_by_id(self, client: Roark) -> None:
        evaluation = client.evaluation.get_evaluator_by_id(
            "evaluatorId",
        )
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    def test_raw_response_get_evaluator_by_id(self, client: Roark) -> None:
        response = client.evaluation.with_raw_response.get_evaluator_by_id(
            "evaluatorId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_get_evaluator_by_id(self, client: Roark) -> None:
        with client.evaluation.with_streaming_response.get_evaluator_by_id(
            "evaluatorId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(object, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_evaluator_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluator_id` but received ''"):
            client.evaluation.with_raw_response.get_evaluator_by_id(
                "",
            )

    @parametrize
    def test_method_get_evaluators(self, client: Roark) -> None:
        evaluation = client.evaluation.get_evaluators()
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    def test_method_get_evaluators_with_all_params(self, client: Roark) -> None:
        evaluation = client.evaluation.get_evaluators(
            after="after",
            limit="321669910225",
        )
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    def test_raw_response_get_evaluators(self, client: Roark) -> None:
        response = client.evaluation.with_raw_response.get_evaluators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_get_evaluators(self, client: Roark) -> None:
        with client.evaluation.with_streaming_response.get_evaluators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(object, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_job(self, client: Roark) -> None:
        evaluation = client.evaluation.get_job(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EvaluationGetJobResponse, evaluation, path=["response"])

    @parametrize
    def test_raw_response_get_job(self, client: Roark) -> None:
        response = client.evaluation.with_raw_response.get_job(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluationGetJobResponse, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_get_job(self, client: Roark) -> None:
        with client.evaluation.with_streaming_response.get_job(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluationGetJobResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_job(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.evaluation.with_raw_response.get_job(
                "",
            )

    @parametrize
    def test_method_get_job_runs(self, client: Roark) -> None:
        evaluation = client.evaluation.get_job_runs(
            job_id="jobId",
        )
        assert_matches_type(EvaluationGetJobRunsResponse, evaluation, path=["response"])

    @parametrize
    def test_method_get_job_runs_with_all_params(self, client: Roark) -> None:
        evaluation = client.evaluation.get_job_runs(
            job_id="jobId",
            limit="10",
            next_cursor="nextCursor",
        )
        assert_matches_type(EvaluationGetJobRunsResponse, evaluation, path=["response"])

    @parametrize
    def test_raw_response_get_job_runs(self, client: Roark) -> None:
        response = client.evaluation.with_raw_response.get_job_runs(
            job_id="jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluationGetJobRunsResponse, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_get_job_runs(self, client: Roark) -> None:
        with client.evaluation.with_streaming_response.get_job_runs(
            job_id="jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluationGetJobRunsResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_job_runs(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.evaluation.with_raw_response.get_job_runs(
                job_id="",
            )


class TestAsyncEvaluation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_job(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluation.create_job(
            evaluators=["string"],
        )
        assert_matches_type(EvaluationCreateJobResponse, evaluation, path=["response"])

    @parametrize
    async def test_method_create_job_with_all_params(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluation.create_job(
            evaluators=["string"],
            call={
                "call_direction": "INBOUND",
                "interface_type": "PHONE",
                "participants": [
                    {
                        "role": "AGENT",
                        "is_simulated": True,
                        "name": "x",
                        "phone_number": "xxx",
                        "spoke_first": True,
                    },
                    {
                        "role": "AGENT",
                        "is_simulated": True,
                        "name": "x",
                        "phone_number": "xxx",
                        "spoke_first": True,
                    },
                ],
                "recording_url": "https://example.com",
                "started_at": "startedAt",
                "ended_reason": "endedReason",
                "ended_status": "AGENT_ENDED_CALL",
                "is_test": True,
                "properties": {"foo": "bar"},
                "retell_call_id": "retellCallId",
                "stereo_recording_url": "https://example.com",
                "tool_invocations": [
                    {
                        "name": "name",
                        "parameters": {"foo": "value"},
                        "result": "string",
                        "start_offset_ms": 0,
                        "description": "description",
                        "end_offset_ms": 0,
                    }
                ],
                "vapi_call_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            dataset={
                "calls": [
                    {
                        "call_direction": "INBOUND",
                        "interface_type": "PHONE",
                        "participants": [
                            {
                                "role": "AGENT",
                                "is_simulated": True,
                                "name": "x",
                                "phone_number": "xxx",
                                "spoke_first": True,
                            },
                            {
                                "role": "AGENT",
                                "is_simulated": True,
                                "name": "x",
                                "phone_number": "xxx",
                                "spoke_first": True,
                            },
                        ],
                        "recording_url": "https://example.com",
                        "started_at": "startedAt",
                        "ended_reason": "endedReason",
                        "ended_status": "AGENT_ENDED_CALL",
                        "is_test": True,
                        "properties": {"foo": "bar"},
                        "retell_call_id": "retellCallId",
                        "stereo_recording_url": "https://example.com",
                        "tool_invocations": [
                            {
                                "name": "name",
                                "parameters": {"foo": "value"},
                                "result": "string",
                                "start_offset_ms": 0,
                                "description": "description",
                                "end_offset_ms": 0,
                            }
                        ],
                        "vapi_call_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
                "name": "name",
            },
        )
        assert_matches_type(EvaluationCreateJobResponse, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_create_job(self, async_client: AsyncRoark) -> None:
        response = await async_client.evaluation.with_raw_response.create_job(
            evaluators=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluationCreateJobResponse, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_create_job(self, async_client: AsyncRoark) -> None:
        async with async_client.evaluation.with_streaming_response.create_job(
            evaluators=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluationCreateJobResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_evaluator_by_id(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluation.get_evaluator_by_id(
            "evaluatorId",
        )
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_get_evaluator_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.evaluation.with_raw_response.get_evaluator_by_id(
            "evaluatorId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_get_evaluator_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.evaluation.with_streaming_response.get_evaluator_by_id(
            "evaluatorId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(object, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_evaluator_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluator_id` but received ''"):
            await async_client.evaluation.with_raw_response.get_evaluator_by_id(
                "",
            )

    @parametrize
    async def test_method_get_evaluators(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluation.get_evaluators()
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    async def test_method_get_evaluators_with_all_params(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluation.get_evaluators(
            after="after",
            limit="321669910225",
        )
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_get_evaluators(self, async_client: AsyncRoark) -> None:
        response = await async_client.evaluation.with_raw_response.get_evaluators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(object, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_get_evaluators(self, async_client: AsyncRoark) -> None:
        async with async_client.evaluation.with_streaming_response.get_evaluators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(object, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_job(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluation.get_job(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EvaluationGetJobResponse, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_get_job(self, async_client: AsyncRoark) -> None:
        response = await async_client.evaluation.with_raw_response.get_job(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluationGetJobResponse, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_get_job(self, async_client: AsyncRoark) -> None:
        async with async_client.evaluation.with_streaming_response.get_job(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluationGetJobResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_job(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.evaluation.with_raw_response.get_job(
                "",
            )

    @parametrize
    async def test_method_get_job_runs(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluation.get_job_runs(
            job_id="jobId",
        )
        assert_matches_type(EvaluationGetJobRunsResponse, evaluation, path=["response"])

    @parametrize
    async def test_method_get_job_runs_with_all_params(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluation.get_job_runs(
            job_id="jobId",
            limit="10",
            next_cursor="nextCursor",
        )
        assert_matches_type(EvaluationGetJobRunsResponse, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_get_job_runs(self, async_client: AsyncRoark) -> None:
        response = await async_client.evaluation.with_raw_response.get_job_runs(
            job_id="jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluationGetJobRunsResponse, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_get_job_runs(self, async_client: AsyncRoark) -> None:
        async with async_client.evaluation.with_streaming_response.get_job_runs(
            job_id="jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluationGetJobRunsResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_job_runs(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.evaluation.with_raw_response.get_job_runs(
                job_id="",
            )
