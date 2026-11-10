# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    ToolListResponse,
    ToolCreateResponse,
    ToolDeleteResponse,
    ToolUpdateResponse,
    ToolGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTool:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        tool = client.tool.create(
            description="x",
            name="book_appointment",
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        tool = client.tool.create(
            description="x",
            name="book_appointment",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calendar={
                "appointment_types": [
                    {"event_type_id": 0, "name": "checkup", "duration_minutes": 0, "when_to_use": "x"}
                ],
                "calendar_connection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "operation": "CHECK_AVAILABILITY",
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
                "simulate": True,
            },
            expected_result="expectedResult",
            inputs=[{"name": "date", "type": "string", "description": "description", "required": True}],
            invocation_criteria="invocationCriteria",
            mcp={
                "mcp_server_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "tool": "x",
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
            },
            runtime={
                "request": {
                    "url": "https://example.com",
                    "body": "x",
                    "headers": [{"name": "X-Api-Version", "value": "2026-10-01"}],
                    "method": "POST",
                    "timeout_ms": 1000,
                },
                "changes_data": True,
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
                "response_fields": ["x"],
            },
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.tool.with_raw_response.create(
            description="x",
            name="book_appointment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.tool.with_streaming_response.create(
            description="x",
            name="book_appointment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCreateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        tool = client.tool.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="x",
            name="book_appointment",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        tool = client.tool.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="x",
            name="book_appointment",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calendar={
                "appointment_types": [
                    {"event_type_id": 0, "name": "checkup", "duration_minutes": 0, "when_to_use": "x"}
                ],
                "calendar_connection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "operation": "CHECK_AVAILABILITY",
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
                "simulate": True,
            },
            expected_result="expectedResult",
            inputs=[{"name": "date", "type": "string", "description": "description", "required": True}],
            invocation_criteria="invocationCriteria",
            mcp={
                "mcp_server_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "tool": "x",
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
            },
            runtime={
                "request": {
                    "url": "https://example.com",
                    "body": "x",
                    "headers": [{"name": "X-Api-Version", "value": "2026-10-01"}],
                    "method": "POST",
                    "timeout_ms": 1000,
                },
                "changes_data": True,
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
                "response_fields": ["x"],
            },
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.tool.with_raw_response.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="x",
            name="book_appointment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.tool.with_streaming_response.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="x",
            name="book_appointment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolUpdateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tool.with_raw_response.update(
                tool_id="",
                description="x",
                name="book_appointment",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        tool = client.tool.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        tool = client.tool.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_built_in="true",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.tool.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.tool.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        tool = client.tool.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ToolDeleteResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.tool.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolDeleteResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.tool.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolDeleteResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tool.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        tool = client.tool.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ToolGetByIDResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.tool.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolGetByIDResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.tool.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolGetByIDResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tool.with_raw_response.get_by_id(
                "",
            )


class TestAsyncTool:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        tool = await async_client.tool.create(
            description="x",
            name="book_appointment",
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        tool = await async_client.tool.create(
            description="x",
            name="book_appointment",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calendar={
                "appointment_types": [
                    {"event_type_id": 0, "name": "checkup", "duration_minutes": 0, "when_to_use": "x"}
                ],
                "calendar_connection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "operation": "CHECK_AVAILABILITY",
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
                "simulate": True,
            },
            expected_result="expectedResult",
            inputs=[{"name": "date", "type": "string", "description": "description", "required": True}],
            invocation_criteria="invocationCriteria",
            mcp={
                "mcp_server_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "tool": "x",
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
            },
            runtime={
                "request": {
                    "url": "https://example.com",
                    "body": "x",
                    "headers": [{"name": "X-Api-Version", "value": "2026-10-01"}],
                    "method": "POST",
                    "timeout_ms": 1000,
                },
                "changes_data": True,
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
                "response_fields": ["x"],
            },
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.tool.with_raw_response.create(
            description="x",
            name="book_appointment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.tool.with_streaming_response.create(
            description="x",
            name="book_appointment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCreateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        tool = await async_client.tool.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="x",
            name="book_appointment",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        tool = await async_client.tool.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="x",
            name="book_appointment",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calendar={
                "appointment_types": [
                    {"event_type_id": 0, "name": "checkup", "duration_minutes": 0, "when_to_use": "x"}
                ],
                "calendar_connection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "operation": "CHECK_AVAILABILITY",
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
                "simulate": True,
            },
            expected_result="expectedResult",
            inputs=[{"name": "date", "type": "string", "description": "description", "required": True}],
            invocation_criteria="invocationCriteria",
            mcp={
                "mcp_server_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "tool": "x",
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
            },
            runtime={
                "request": {
                    "url": "https://example.com",
                    "body": "x",
                    "headers": [{"name": "X-Api-Version", "value": "2026-10-01"}],
                    "method": "POST",
                    "timeout_ms": 1000,
                },
                "changes_data": True,
                "messages": {"before": "before", "failure": "failure", "slow": "slow"},
                "response_fields": ["x"],
            },
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.tool.with_raw_response.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="x",
            name="book_appointment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.tool.with_streaming_response.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="x",
            name="book_appointment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolUpdateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tool.with_raw_response.update(
                tool_id="",
                description="x",
                name="book_appointment",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        tool = await async_client.tool.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        tool = await async_client.tool.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_built_in="true",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.tool.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.tool.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        tool = await async_client.tool.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ToolDeleteResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.tool.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolDeleteResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.tool.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolDeleteResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tool.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        tool = await async_client.tool.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ToolGetByIDResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.tool.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolGetByIDResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.tool.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolGetByIDResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tool.with_raw_response.get_by_id(
                "",
            )
