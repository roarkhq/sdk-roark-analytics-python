# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import ConfigApplyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_apply(self, client: Roark) -> None:
        config = client.config.apply(
            resources=[
                {
                    "kind": "agent",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(ConfigApplyResponse, config, path=["response"])

    @parametrize
    def test_method_apply_with_all_params(self, client: Roark) -> None:
        config = client.config.apply(
            resources=[
                {
                    "kind": "agent",
                    "name": "name",
                    "custom_id": "customId",
                    "description": "description",
                    "endpoints": [
                        {
                            "direction": "INCOMING",
                            "name": "name",
                            "value": "x",
                            "environment": "environment",
                        }
                    ],
                }
            ],
            prune=True,
        )
        assert_matches_type(ConfigApplyResponse, config, path=["response"])

    @parametrize
    def test_raw_response_apply(self, client: Roark) -> None:
        response = client.config.with_raw_response.apply(
            resources=[
                {
                    "kind": "agent",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigApplyResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_apply(self, client: Roark) -> None:
        with client.config.with_streaming_response.apply(
            resources=[
                {
                    "kind": "agent",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigApplyResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_apply(self, async_client: AsyncRoark) -> None:
        config = await async_client.config.apply(
            resources=[
                {
                    "kind": "agent",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(ConfigApplyResponse, config, path=["response"])

    @parametrize
    async def test_method_apply_with_all_params(self, async_client: AsyncRoark) -> None:
        config = await async_client.config.apply(
            resources=[
                {
                    "kind": "agent",
                    "name": "name",
                    "custom_id": "customId",
                    "description": "description",
                    "endpoints": [
                        {
                            "direction": "INCOMING",
                            "name": "name",
                            "value": "x",
                            "environment": "environment",
                        }
                    ],
                }
            ],
            prune=True,
        )
        assert_matches_type(ConfigApplyResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_apply(self, async_client: AsyncRoark) -> None:
        response = await async_client.config.with_raw_response.apply(
            resources=[
                {
                    "kind": "agent",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigApplyResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_apply(self, async_client: AsyncRoark) -> None:
        async with async_client.config.with_streaming_response.apply(
            resources=[
                {
                    "kind": "agent",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigApplyResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
