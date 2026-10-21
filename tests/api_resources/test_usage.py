# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import UsageGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Roark) -> None:
        usage = client.usage.get(
            from_="2026-09-01T00:00:00Z",
            to="2026-10-01T00:00:00Z",
        )
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Roark) -> None:
        usage = client.usage.get(
            from_="2026-09-01T00:00:00Z",
            to="2026-10-01T00:00:00Z",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Roark) -> None:
        response = client.usage.with_raw_response.get(
            from_="2026-09-01T00:00:00Z",
            to="2026-10-01T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Roark) -> None:
        with client.usage.with_streaming_response.get(
            from_="2026-09-01T00:00:00Z",
            to="2026-10-01T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncRoark) -> None:
        usage = await async_client.usage.get(
            from_="2026-09-01T00:00:00Z",
            to="2026-10-01T00:00:00Z",
        )
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncRoark) -> None:
        usage = await async_client.usage.get(
            from_="2026-09-01T00:00:00Z",
            to="2026-10-01T00:00:00Z",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncRoark) -> None:
        response = await async_client.usage.with_raw_response.get(
            from_="2026-09-01T00:00:00Z",
            to="2026-10-01T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncRoark) -> None:
        async with async_client.usage.with_streaming_response.get(
            from_="2026-09-01T00:00:00Z",
            to="2026-10-01T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
