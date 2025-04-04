# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import CallAnalysisCreateResponse, CallAnalysisRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallAnalysis:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        call_analysis = client.call_analysis.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            participants=[{"role": "AGENT"}, {"role": "AGENT"}],
            recording_url="https://example.com/recording.wav",
            started_at="2025-04-04T17:46:46.039Z",
        )
        assert_matches_type(CallAnalysisCreateResponse, call_analysis, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        call_analysis = client.call_analysis.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            participants=[
                {
                    "role": "AGENT",
                    "is_simulated": True,
                    "name": "Sales Agent",
                    "phone_number": "+15551234567",
                    "spoke_first": True,
                },
                {
                    "role": "AGENT",
                    "is_simulated": True,
                    "name": "John Doe",
                    "phone_number": "+15557654321",
                    "spoke_first": False,
                },
            ],
            recording_url="https://example.com/recording.wav",
            started_at="2025-04-04T17:46:46.039Z",
            ended_reason="endedReason",
            is_test=False,
            properties={
                "business_name": "bar",
                "business_id": "bar",
            },
            retell_call_id="retellCallId",
            stereo_recording_url="https://example.com",
            tool_invocations=[
                {
                    "name": "getDentalAppointments",
                    "parameters": {},
                    "result": {"appointments": "bar"},
                    "start_offset_ms": 2000,
                    "description": "Get available dental appointments",
                    "end_offset_ms": 0,
                },
                {
                    "name": "bookAppointment",
                    "parameters": {
                        "patientName": "John Doe",
                        "patientPhone": "+1234567890",
                        "appointmentType": {
                            "description": "Type of dental appointment",
                            "type": "string",
                            "value": "cleaning",
                        },
                    },
                    "result": "Success",
                    "start_offset_ms": 7000,
                    "description": "Book an appointment for the client",
                    "end_offset_ms": 0,
                },
            ],
            vapi_call_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallAnalysisCreateResponse, call_analysis, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.call_analysis.with_raw_response.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            participants=[{"role": "AGENT"}, {"role": "AGENT"}],
            recording_url="https://example.com/recording.wav",
            started_at="2025-04-04T17:46:46.039Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_analysis = response.parse()
        assert_matches_type(CallAnalysisCreateResponse, call_analysis, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.call_analysis.with_streaming_response.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            participants=[{"role": "AGENT"}, {"role": "AGENT"}],
            recording_url="https://example.com/recording.wav",
            started_at="2025-04-04T17:46:46.039Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_analysis = response.parse()
            assert_matches_type(CallAnalysisCreateResponse, call_analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Roark) -> None:
        call_analysis = client.call_analysis.retrieve(
            "jobId",
        )
        assert_matches_type(CallAnalysisRetrieveResponse, call_analysis, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Roark) -> None:
        response = client.call_analysis.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_analysis = response.parse()
        assert_matches_type(CallAnalysisRetrieveResponse, call_analysis, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Roark) -> None:
        with client.call_analysis.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_analysis = response.parse()
            assert_matches_type(CallAnalysisRetrieveResponse, call_analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.call_analysis.with_raw_response.retrieve(
                "",
            )


class TestAsyncCallAnalysis:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        call_analysis = await async_client.call_analysis.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            participants=[{"role": "AGENT"}, {"role": "AGENT"}],
            recording_url="https://example.com/recording.wav",
            started_at="2025-04-04T17:46:46.039Z",
        )
        assert_matches_type(CallAnalysisCreateResponse, call_analysis, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        call_analysis = await async_client.call_analysis.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            participants=[
                {
                    "role": "AGENT",
                    "is_simulated": True,
                    "name": "Sales Agent",
                    "phone_number": "+15551234567",
                    "spoke_first": True,
                },
                {
                    "role": "AGENT",
                    "is_simulated": True,
                    "name": "John Doe",
                    "phone_number": "+15557654321",
                    "spoke_first": False,
                },
            ],
            recording_url="https://example.com/recording.wav",
            started_at="2025-04-04T17:46:46.039Z",
            ended_reason="endedReason",
            is_test=False,
            properties={
                "business_name": "bar",
                "business_id": "bar",
            },
            retell_call_id="retellCallId",
            stereo_recording_url="https://example.com",
            tool_invocations=[
                {
                    "name": "getDentalAppointments",
                    "parameters": {},
                    "result": {"appointments": "bar"},
                    "start_offset_ms": 2000,
                    "description": "Get available dental appointments",
                    "end_offset_ms": 0,
                },
                {
                    "name": "bookAppointment",
                    "parameters": {
                        "patientName": "John Doe",
                        "patientPhone": "+1234567890",
                        "appointmentType": {
                            "description": "Type of dental appointment",
                            "type": "string",
                            "value": "cleaning",
                        },
                    },
                    "result": "Success",
                    "start_offset_ms": 7000,
                    "description": "Book an appointment for the client",
                    "end_offset_ms": 0,
                },
            ],
            vapi_call_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CallAnalysisCreateResponse, call_analysis, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.call_analysis.with_raw_response.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            participants=[{"role": "AGENT"}, {"role": "AGENT"}],
            recording_url="https://example.com/recording.wav",
            started_at="2025-04-04T17:46:46.039Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_analysis = await response.parse()
        assert_matches_type(CallAnalysisCreateResponse, call_analysis, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.call_analysis.with_streaming_response.create(
            call_direction="INBOUND",
            interface_type="PHONE",
            participants=[{"role": "AGENT"}, {"role": "AGENT"}],
            recording_url="https://example.com/recording.wav",
            started_at="2025-04-04T17:46:46.039Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_analysis = await response.parse()
            assert_matches_type(CallAnalysisCreateResponse, call_analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRoark) -> None:
        call_analysis = await async_client.call_analysis.retrieve(
            "jobId",
        )
        assert_matches_type(CallAnalysisRetrieveResponse, call_analysis, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRoark) -> None:
        response = await async_client.call_analysis.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_analysis = await response.parse()
        assert_matches_type(CallAnalysisRetrieveResponse, call_analysis, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRoark) -> None:
        async with async_client.call_analysis.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_analysis = await response.parse()
            assert_matches_type(CallAnalysisRetrieveResponse, call_analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.call_analysis.with_raw_response.retrieve(
                "",
            )
