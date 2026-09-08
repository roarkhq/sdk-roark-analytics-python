# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import SimulationTemplateListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationTemplate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        simulation_template = client.simulation_template.list()
        assert_matches_type(SimulationTemplateListResponse, simulation_template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.simulation_template.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_template = response.parse()
        assert_matches_type(SimulationTemplateListResponse, simulation_template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.simulation_template.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_template = response.parse()
            assert_matches_type(SimulationTemplateListResponse, simulation_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimulationTemplate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        simulation_template = await async_client.simulation_template.list()
        assert_matches_type(SimulationTemplateListResponse, simulation_template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_template.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_template = await response.parse()
        assert_matches_type(SimulationTemplateListResponse, simulation_template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_template.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_template = await response.parse()
            assert_matches_type(SimulationTemplateListResponse, simulation_template, path=["response"])

        assert cast(Any, response.is_closed) is True
