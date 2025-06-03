# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import EvaluationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        evaluation = client.evaluations.create(
            evaluators=["string"],
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        evaluation = client.evaluations.create(
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
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.evaluations.with_raw_response.create(
            evaluators=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.evaluations.with_streaming_response.create(
            evaluators=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluations.create(
            evaluators=["string"],
        )
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        evaluation = await async_client.evaluations.create(
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
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.evaluations.with_raw_response.create(
            evaluators=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.evaluations.with_streaming_response.create(
            evaluators=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluationCreateResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True
