# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    CallListResponse,
    CallCreateResponse,
    CallGetByIDResponse,
    CallListMetricsResponse,
    CallListSentimentRunsResponse,
    CallListEvaluationRunsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCall:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        call = client.call.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            recording_url="https://example.com",
            started_at="startedAt",
        )
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        call = client.call.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            recording_url="https://example.com",
            started_at="startedAt",
            agent={
                "roark_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "endpoint": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                "prompt": {"resolved_prompt": "resolvedPrompt"},
            },
            agents=[
                {
                    "roark_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "endpoint": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "prompt": {"resolved_prompt": "resolvedPrompt"},
                }
            ],
            customer={
                "phone_number_e164": "phoneNumberE164",
                "label": "label",
            },
            customers=[
                {
                    "phone_number_e164": "phoneNumberE164",
                    "label": "label",
                }
            ],
            ended_status="PARTICIPANTS_DID_NOT_SPEAK",
            properties={"foo": "bar"},
            stereo_recording_url="https://example.com",
            tool_invocations=[
                {
                    "name": "name",
                    "parameters": {
                        "foo": {
                            "description": "description",
                            "type": "string",
                            "value": {},
                        }
                    },
                    "result": "string",
                    "start_offset_ms": 0,
                    "agent": {
                        "custom_id": "customId",
                        "roark_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "description": "description",
                    "end_offset_ms": 0,
                }
            ],
            transcript=[
                {
                    "end_offset_ms": 0,
                    "role": "AGENT",
                    "start_offset_ms": 0,
                    "text": "x",
                    "agent": {
                        "custom_id": "customId",
                        "roark_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "language_code": "languageCode",
                }
            ],
        )
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.call.with_raw_response.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            recording_url="https://example.com",
            started_at="startedAt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.call.with_streaming_response.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            recording_url="https://example.com",
            started_at="startedAt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallCreateResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        call = client.call.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        call = client.call.list(
            after="eyJpZCI6IjU1MGU4NDAwLWUyOWItNDFkNC1hNzE2LTQ0NjY1NTQ0MDAwMCIsImNyZWF0ZWRBdCI6IjIwMjQtMDEtMTVUMTA6MDA6MDAuMDAwWiJ9",
            limit=20,
            search_text="billing inquiry",
            sort_by="createdAt",
            sort_direction="desc",
            status="ENDED",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.call.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.call.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        call = client.call.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallGetByIDResponse, call, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.call.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetByIDResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.call.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetByIDResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_list_evaluation_runs(self, client: Roark) -> None:
        call = client.call.list_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallListEvaluationRunsResponse, call, path=["response"])

    @parametrize
    def test_raw_response_list_evaluation_runs(self, client: Roark) -> None:
        response = client.call.with_raw_response.list_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListEvaluationRunsResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_list_evaluation_runs(self, client: Roark) -> None:
        with client.call.with_streaming_response.list_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListEvaluationRunsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_evaluation_runs(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.list_evaluation_runs(
                "",
            )

    @parametrize
    def test_method_list_metrics(self, client: Roark) -> None:
        call = client.call.list_metrics(
            call_id="callId",
        )
        assert_matches_type(CallListMetricsResponse, call, path=["response"])

    @parametrize
    def test_method_list_metrics_with_all_params(self, client: Roark) -> None:
        call = client.call.list_metrics(
            call_id="callId",
            flatten="flatten",
        )
        assert_matches_type(CallListMetricsResponse, call, path=["response"])

    @parametrize
    def test_raw_response_list_metrics(self, client: Roark) -> None:
        response = client.call.with_raw_response.list_metrics(
            call_id="callId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListMetricsResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_list_metrics(self, client: Roark) -> None:
        with client.call.with_streaming_response.list_metrics(
            call_id="callId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListMetricsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_metrics(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.list_metrics(
                call_id="",
            )

    @parametrize
    def test_method_list_sentiment_runs(self, client: Roark) -> None:
        call = client.call.list_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallListSentimentRunsResponse, call, path=["response"])

    @parametrize
    def test_raw_response_list_sentiment_runs(self, client: Roark) -> None:
        response = client.call.with_raw_response.list_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListSentimentRunsResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_list_sentiment_runs(self, client: Roark) -> None:
        with client.call.with_streaming_response.list_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListSentimentRunsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_sentiment_runs(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.list_sentiment_runs(
                "",
            )


class TestAsyncCall:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            recording_url="https://example.com",
            started_at="startedAt",
        )
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            recording_url="https://example.com",
            started_at="startedAt",
            agent={
                "roark_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "endpoint": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                "prompt": {"resolved_prompt": "resolvedPrompt"},
            },
            agents=[
                {
                    "roark_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "endpoint": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "prompt": {"resolved_prompt": "resolvedPrompt"},
                }
            ],
            customer={
                "phone_number_e164": "phoneNumberE164",
                "label": "label",
            },
            customers=[
                {
                    "phone_number_e164": "phoneNumberE164",
                    "label": "label",
                }
            ],
            ended_status="PARTICIPANTS_DID_NOT_SPEAK",
            properties={"foo": "bar"},
            stereo_recording_url="https://example.com",
            tool_invocations=[
                {
                    "name": "name",
                    "parameters": {
                        "foo": {
                            "description": "description",
                            "type": "string",
                            "value": {},
                        }
                    },
                    "result": "string",
                    "start_offset_ms": 0,
                    "agent": {
                        "custom_id": "customId",
                        "roark_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "description": "description",
                    "end_offset_ms": 0,
                }
            ],
            transcript=[
                {
                    "end_offset_ms": 0,
                    "role": "AGENT",
                    "start_offset_ms": 0,
                    "text": "x",
                    "agent": {
                        "custom_id": "customId",
                        "roark_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "language_code": "languageCode",
                }
            ],
        )
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            recording_url="https://example.com",
            started_at="startedAt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallCreateResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            recording_url="https://example.com",
            started_at="startedAt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallCreateResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.list(
            after="eyJpZCI6IjU1MGU4NDAwLWUyOWItNDFkNC1hNzE2LTQ0NjY1NTQ0MDAwMCIsImNyZWF0ZWRBdCI6IjIwMjQtMDEtMTVUMTA6MDA6MDAuMDAwWiJ9",
            limit=20,
            search_text="billing inquiry",
            sort_by="createdAt",
            sort_direction="desc",
            status="ENDED",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallGetByIDResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetByIDResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetByIDResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_list_evaluation_runs(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.list_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallListEvaluationRunsResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_list_evaluation_runs(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.list_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListEvaluationRunsResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_list_evaluation_runs(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.list_evaluation_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListEvaluationRunsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_evaluation_runs(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.list_evaluation_runs(
                "",
            )

    @parametrize
    async def test_method_list_metrics(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.list_metrics(
            call_id="callId",
        )
        assert_matches_type(CallListMetricsResponse, call, path=["response"])

    @parametrize
    async def test_method_list_metrics_with_all_params(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.list_metrics(
            call_id="callId",
            flatten="flatten",
        )
        assert_matches_type(CallListMetricsResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_list_metrics(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.list_metrics(
            call_id="callId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListMetricsResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_list_metrics(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.list_metrics(
            call_id="callId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListMetricsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_metrics(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.list_metrics(
                call_id="",
            )

    @parametrize
    async def test_method_list_sentiment_runs(self, async_client: AsyncRoark) -> None:
        call = await async_client.call.list_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallListSentimentRunsResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_list_sentiment_runs(self, async_client: AsyncRoark) -> None:
        response = await async_client.call.with_raw_response.list_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListSentimentRunsResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_list_sentiment_runs(self, async_client: AsyncRoark) -> None:
        async with async_client.call.with_streaming_response.list_sentiment_runs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListSentimentRunsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_sentiment_runs(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.list_sentiment_runs(
                "",
            )
