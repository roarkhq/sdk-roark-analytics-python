# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    MeGetResponse,
    MeListAPIKeysResponse,
    MeCreateAPIKeyResponse,
    MeRevokeAPIKeyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_api_key(self, client: Roark) -> None:
        me = client.me.create_api_key(
            name="CI deploy gate",
        )
        assert_matches_type(MeCreateAPIKeyResponse, me, path=["response"])

    @parametrize
    def test_method_create_api_key_with_all_params(self, client: Roark) -> None:
        me = client.me.create_api_key(
            name="CI deploy gate",
            expires_at="2026-12-31T23:59:59.000Z",
            permissions=["call:read", "metric:read"],
            project_id="projectId",
            scopes=["READ"],
        )
        assert_matches_type(MeCreateAPIKeyResponse, me, path=["response"])

    @parametrize
    def test_raw_response_create_api_key(self, client: Roark) -> None:
        response = client.me.with_raw_response.create_api_key(
            name="CI deploy gate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeCreateAPIKeyResponse, me, path=["response"])

    @parametrize
    def test_streaming_response_create_api_key(self, client: Roark) -> None:
        with client.me.with_streaming_response.create_api_key(
            name="CI deploy gate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeCreateAPIKeyResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Roark) -> None:
        me = client.me.get()
        assert_matches_type(MeGetResponse, me, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Roark) -> None:
        response = client.me.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeGetResponse, me, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Roark) -> None:
        with client.me.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeGetResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_api_keys(self, client: Roark) -> None:
        me = client.me.list_api_keys()
        assert_matches_type(MeListAPIKeysResponse, me, path=["response"])

    @parametrize
    def test_method_list_api_keys_with_all_params(self, client: Roark) -> None:
        me = client.me.list_api_keys(
            status="ACTIVE",
        )
        assert_matches_type(MeListAPIKeysResponse, me, path=["response"])

    @parametrize
    def test_raw_response_list_api_keys(self, client: Roark) -> None:
        response = client.me.with_raw_response.list_api_keys()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeListAPIKeysResponse, me, path=["response"])

    @parametrize
    def test_streaming_response_list_api_keys(self, client: Roark) -> None:
        with client.me.with_streaming_response.list_api_keys() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeListAPIKeysResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_revoke_api_key(self, client: Roark) -> None:
        me = client.me.revoke_api_key(
            "id",
        )
        assert_matches_type(MeRevokeAPIKeyResponse, me, path=["response"])

    @parametrize
    def test_raw_response_revoke_api_key(self, client: Roark) -> None:
        response = client.me.with_raw_response.revoke_api_key(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeRevokeAPIKeyResponse, me, path=["response"])

    @parametrize
    def test_streaming_response_revoke_api_key(self, client: Roark) -> None:
        with client.me.with_streaming_response.revoke_api_key(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeRevokeAPIKeyResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke_api_key(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.me.with_raw_response.revoke_api_key(
                "",
            )


class TestAsyncMe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_api_key(self, async_client: AsyncRoark) -> None:
        me = await async_client.me.create_api_key(
            name="CI deploy gate",
        )
        assert_matches_type(MeCreateAPIKeyResponse, me, path=["response"])

    @parametrize
    async def test_method_create_api_key_with_all_params(self, async_client: AsyncRoark) -> None:
        me = await async_client.me.create_api_key(
            name="CI deploy gate",
            expires_at="2026-12-31T23:59:59.000Z",
            permissions=["call:read", "metric:read"],
            project_id="projectId",
            scopes=["READ"],
        )
        assert_matches_type(MeCreateAPIKeyResponse, me, path=["response"])

    @parametrize
    async def test_raw_response_create_api_key(self, async_client: AsyncRoark) -> None:
        response = await async_client.me.with_raw_response.create_api_key(
            name="CI deploy gate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeCreateAPIKeyResponse, me, path=["response"])

    @parametrize
    async def test_streaming_response_create_api_key(self, async_client: AsyncRoark) -> None:
        async with async_client.me.with_streaming_response.create_api_key(
            name="CI deploy gate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeCreateAPIKeyResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncRoark) -> None:
        me = await async_client.me.get()
        assert_matches_type(MeGetResponse, me, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncRoark) -> None:
        response = await async_client.me.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeGetResponse, me, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncRoark) -> None:
        async with async_client.me.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeGetResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_api_keys(self, async_client: AsyncRoark) -> None:
        me = await async_client.me.list_api_keys()
        assert_matches_type(MeListAPIKeysResponse, me, path=["response"])

    @parametrize
    async def test_method_list_api_keys_with_all_params(self, async_client: AsyncRoark) -> None:
        me = await async_client.me.list_api_keys(
            status="ACTIVE",
        )
        assert_matches_type(MeListAPIKeysResponse, me, path=["response"])

    @parametrize
    async def test_raw_response_list_api_keys(self, async_client: AsyncRoark) -> None:
        response = await async_client.me.with_raw_response.list_api_keys()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeListAPIKeysResponse, me, path=["response"])

    @parametrize
    async def test_streaming_response_list_api_keys(self, async_client: AsyncRoark) -> None:
        async with async_client.me.with_streaming_response.list_api_keys() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeListAPIKeysResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_revoke_api_key(self, async_client: AsyncRoark) -> None:
        me = await async_client.me.revoke_api_key(
            "id",
        )
        assert_matches_type(MeRevokeAPIKeyResponse, me, path=["response"])

    @parametrize
    async def test_raw_response_revoke_api_key(self, async_client: AsyncRoark) -> None:
        response = await async_client.me.with_raw_response.revoke_api_key(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeRevokeAPIKeyResponse, me, path=["response"])

    @parametrize
    async def test_streaming_response_revoke_api_key(self, async_client: AsyncRoark) -> None:
        async with async_client.me.with_streaming_response.revoke_api_key(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeRevokeAPIKeyResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke_api_key(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.me.with_raw_response.revoke_api_key(
                "",
            )
