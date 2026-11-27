# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    McpServerListResponse,
    McpServerCreateResponse,
    McpServerDeleteResponse,
    McpServerUpdateResponse,
    McpServerGetByIDResponse,
    McpServerRefreshResponse,
    McpServerDiscoverResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcpServer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        mcp_server = client.mcp_server.create(
            label="CRM",
            url="https://mcp.example.com/mcp",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        mcp_server = client.mcp_server.create(
            label="CRM",
            url="https://mcp.example.com/mcp",
            auth={"type": "NONE"},
            directory_key="x",
            transport="STREAMABLE_HTTP",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.mcp_server.with_raw_response.create(
            label="CRM",
            url="https://mcp.example.com/mcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.mcp_server.with_streaming_response.create(
            label="CRM",
            url="https://mcp.example.com/mcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        mcp_server = client.mcp_server.update(
            server_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        mcp_server = client.mcp_server.update(
            server_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth={"type": "NONE"},
            label="x",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.mcp_server.with_raw_response.update(
            server_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.mcp_server.with_streaming_response.update(
            server_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.mcp_server.with_raw_response.update(
                server_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        mcp_server = client.mcp_server.list()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.mcp_server.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.mcp_server.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        mcp_server = client.mcp_server.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpServerDeleteResponse, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.mcp_server.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerDeleteResponse, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.mcp_server.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerDeleteResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.mcp_server.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_discover(self, client: Roark) -> None:
        mcp_server = client.mcp_server.discover(
            url="https://mcp.example.com/mcp",
        )
        assert_matches_type(McpServerDiscoverResponse, mcp_server, path=["response"])

    @parametrize
    def test_method_discover_with_all_params(self, client: Roark) -> None:
        mcp_server = client.mcp_server.discover(
            url="https://mcp.example.com/mcp",
            auth={"type": "NONE"},
            transport="STREAMABLE_HTTP",
        )
        assert_matches_type(McpServerDiscoverResponse, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_discover(self, client: Roark) -> None:
        response = client.mcp_server.with_raw_response.discover(
            url="https://mcp.example.com/mcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerDiscoverResponse, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_discover(self, client: Roark) -> None:
        with client.mcp_server.with_streaming_response.discover(
            url="https://mcp.example.com/mcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerDiscoverResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        mcp_server = client.mcp_server.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpServerGetByIDResponse, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.mcp_server.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerGetByIDResponse, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.mcp_server.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerGetByIDResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.mcp_server.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_refresh(self, client: Roark) -> None:
        mcp_server = client.mcp_server.refresh(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpServerRefreshResponse, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_refresh(self, client: Roark) -> None:
        response = client.mcp_server.with_raw_response.refresh(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerRefreshResponse, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_refresh(self, client: Roark) -> None:
        with client.mcp_server.with_streaming_response.refresh(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerRefreshResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_refresh(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.mcp_server.with_raw_response.refresh(
                "",
            )


class TestAsyncMcpServer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.create(
            label="CRM",
            url="https://mcp.example.com/mcp",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.create(
            label="CRM",
            url="https://mcp.example.com/mcp",
            auth={"type": "NONE"},
            directory_key="x",
            transport="STREAMABLE_HTTP",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.mcp_server.with_raw_response.create(
            label="CRM",
            url="https://mcp.example.com/mcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.mcp_server.with_streaming_response.create(
            label="CRM",
            url="https://mcp.example.com/mcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.update(
            server_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.update(
            server_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth={"type": "NONE"},
            label="x",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.mcp_server.with_raw_response.update(
            server_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.mcp_server.with_streaming_response.update(
            server_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.mcp_server.with_raw_response.update(
                server_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.list()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.mcp_server.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.mcp_server.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpServerDeleteResponse, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.mcp_server.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerDeleteResponse, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.mcp_server.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerDeleteResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.mcp_server.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_discover(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.discover(
            url="https://mcp.example.com/mcp",
        )
        assert_matches_type(McpServerDiscoverResponse, mcp_server, path=["response"])

    @parametrize
    async def test_method_discover_with_all_params(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.discover(
            url="https://mcp.example.com/mcp",
            auth={"type": "NONE"},
            transport="STREAMABLE_HTTP",
        )
        assert_matches_type(McpServerDiscoverResponse, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_discover(self, async_client: AsyncRoark) -> None:
        response = await async_client.mcp_server.with_raw_response.discover(
            url="https://mcp.example.com/mcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerDiscoverResponse, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_discover(self, async_client: AsyncRoark) -> None:
        async with async_client.mcp_server.with_streaming_response.discover(
            url="https://mcp.example.com/mcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerDiscoverResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpServerGetByIDResponse, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.mcp_server.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerGetByIDResponse, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.mcp_server.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerGetByIDResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.mcp_server.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_refresh(self, async_client: AsyncRoark) -> None:
        mcp_server = await async_client.mcp_server.refresh(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpServerRefreshResponse, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncRoark) -> None:
        response = await async_client.mcp_server.with_raw_response.refresh(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerRefreshResponse, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncRoark) -> None:
        async with async_client.mcp_server.with_streaming_response.refresh(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerRefreshResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_refresh(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.mcp_server.with_raw_response.refresh(
                "",
            )
