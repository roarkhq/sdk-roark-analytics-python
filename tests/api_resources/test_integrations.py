# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    IntegrationCreateVapiCallResponse,
    IntegrationCreateRetellCallResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_retell_call(self, client: Roark) -> None:
        integration = client.integrations.create_retell_call(
            retell_call_ended_payload={
                "event": "bar",
                "call": "bar",
            },
        )
        assert_matches_type(IntegrationCreateRetellCallResponse, integration, path=["response"])

    @parametrize
    def test_method_create_retell_call_with_all_params(self, client: Roark) -> None:
        integration = client.integrations.create_retell_call(
            retell_call_ended_payload={
                "event": "bar",
                "call": "bar",
            },
            properties={
                "business_name": "bar",
                "business_id": "bar",
            },
            skip_already_imported=True,
        )
        assert_matches_type(IntegrationCreateRetellCallResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_create_retell_call(self, client: Roark) -> None:
        response = client.integrations.with_raw_response.create_retell_call(
            retell_call_ended_payload={
                "event": "bar",
                "call": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationCreateRetellCallResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_create_retell_call(self, client: Roark) -> None:
        with client.integrations.with_streaming_response.create_retell_call(
            retell_call_ended_payload={
                "event": "bar",
                "call": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationCreateRetellCallResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_vapi_call(self, client: Roark) -> None:
        integration = client.integrations.create_vapi_call(
            vapi_end_of_call_report_payload={
                "call": "bar",
                "type": "bar",
                "status": "bar",
                "assistant": "bar",
                "customer": "bar",
                "phoneNumber": "bar",
                "artifact": "bar",
                "startedAt": "bar",
                "endedAt": "bar",
                "endedReason": "bar",
            },
        )
        assert_matches_type(IntegrationCreateVapiCallResponse, integration, path=["response"])

    @parametrize
    def test_method_create_vapi_call_with_all_params(self, client: Roark) -> None:
        integration = client.integrations.create_vapi_call(
            vapi_end_of_call_report_payload={
                "call": "bar",
                "type": "bar",
                "status": "bar",
                "assistant": "bar",
                "customer": "bar",
                "phoneNumber": "bar",
                "artifact": "bar",
                "startedAt": "bar",
                "endedAt": "bar",
                "endedReason": "bar",
            },
            properties={
                "business_name": "bar",
                "business_id": "bar",
            },
            skip_already_imported=True,
        )
        assert_matches_type(IntegrationCreateVapiCallResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_create_vapi_call(self, client: Roark) -> None:
        response = client.integrations.with_raw_response.create_vapi_call(
            vapi_end_of_call_report_payload={
                "call": "bar",
                "type": "bar",
                "status": "bar",
                "assistant": "bar",
                "customer": "bar",
                "phoneNumber": "bar",
                "artifact": "bar",
                "startedAt": "bar",
                "endedAt": "bar",
                "endedReason": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationCreateVapiCallResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_create_vapi_call(self, client: Roark) -> None:
        with client.integrations.with_streaming_response.create_vapi_call(
            vapi_end_of_call_report_payload={
                "call": "bar",
                "type": "bar",
                "status": "bar",
                "assistant": "bar",
                "customer": "bar",
                "phoneNumber": "bar",
                "artifact": "bar",
                "startedAt": "bar",
                "endedAt": "bar",
                "endedReason": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationCreateVapiCallResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_retell_call(self, async_client: AsyncRoark) -> None:
        integration = await async_client.integrations.create_retell_call(
            retell_call_ended_payload={
                "event": "bar",
                "call": "bar",
            },
        )
        assert_matches_type(IntegrationCreateRetellCallResponse, integration, path=["response"])

    @parametrize
    async def test_method_create_retell_call_with_all_params(self, async_client: AsyncRoark) -> None:
        integration = await async_client.integrations.create_retell_call(
            retell_call_ended_payload={
                "event": "bar",
                "call": "bar",
            },
            properties={
                "business_name": "bar",
                "business_id": "bar",
            },
            skip_already_imported=True,
        )
        assert_matches_type(IntegrationCreateRetellCallResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_create_retell_call(self, async_client: AsyncRoark) -> None:
        response = await async_client.integrations.with_raw_response.create_retell_call(
            retell_call_ended_payload={
                "event": "bar",
                "call": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationCreateRetellCallResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_create_retell_call(self, async_client: AsyncRoark) -> None:
        async with async_client.integrations.with_streaming_response.create_retell_call(
            retell_call_ended_payload={
                "event": "bar",
                "call": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationCreateRetellCallResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_vapi_call(self, async_client: AsyncRoark) -> None:
        integration = await async_client.integrations.create_vapi_call(
            vapi_end_of_call_report_payload={
                "call": "bar",
                "type": "bar",
                "status": "bar",
                "assistant": "bar",
                "customer": "bar",
                "phoneNumber": "bar",
                "artifact": "bar",
                "startedAt": "bar",
                "endedAt": "bar",
                "endedReason": "bar",
            },
        )
        assert_matches_type(IntegrationCreateVapiCallResponse, integration, path=["response"])

    @parametrize
    async def test_method_create_vapi_call_with_all_params(self, async_client: AsyncRoark) -> None:
        integration = await async_client.integrations.create_vapi_call(
            vapi_end_of_call_report_payload={
                "call": "bar",
                "type": "bar",
                "status": "bar",
                "assistant": "bar",
                "customer": "bar",
                "phoneNumber": "bar",
                "artifact": "bar",
                "startedAt": "bar",
                "endedAt": "bar",
                "endedReason": "bar",
            },
            properties={
                "business_name": "bar",
                "business_id": "bar",
            },
            skip_already_imported=True,
        )
        assert_matches_type(IntegrationCreateVapiCallResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_create_vapi_call(self, async_client: AsyncRoark) -> None:
        response = await async_client.integrations.with_raw_response.create_vapi_call(
            vapi_end_of_call_report_payload={
                "call": "bar",
                "type": "bar",
                "status": "bar",
                "assistant": "bar",
                "customer": "bar",
                "phoneNumber": "bar",
                "artifact": "bar",
                "startedAt": "bar",
                "endedAt": "bar",
                "endedReason": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationCreateVapiCallResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_create_vapi_call(self, async_client: AsyncRoark) -> None:
        async with async_client.integrations.with_streaming_response.create_vapi_call(
            vapi_end_of_call_report_payload={
                "call": "bar",
                "type": "bar",
                "status": "bar",
                "assistant": "bar",
                "customer": "bar",
                "phoneNumber": "bar",
                "artifact": "bar",
                "startedAt": "bar",
                "endedAt": "bar",
                "endedReason": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationCreateVapiCallResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True
