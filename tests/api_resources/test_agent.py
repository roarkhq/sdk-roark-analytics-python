# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    AgentListResponse,
    AgentCreateResponse,
    AgentUpdateResponse,
    AgentGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        agent = client.agent.create(
            name="x",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        agent = client.agent.create(
            name="x",
            custom_id="customId",
            description="description",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.agent.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.agent.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        agent = client.agent.update(
            agent_id="agentId",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        agent = client.agent.update(
            agent_id="agentId",
            description="description",
            name="x",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.agent.with_raw_response.update(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.agent.with_streaming_response.update(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        agent = client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        agent = client.agent.list(
            after="after",
            limit=1,
            search_text="searchText",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        agent = client.agent.get_by_id(
            "agentId",
        )
        assert_matches_type(AgentGetByIDResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.agent.with_raw_response.get_by_id(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentGetByIDResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.agent.with_streaming_response.get_by_id(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentGetByIDResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.get_by_id(
                "",
            )


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        agent = await async_client.agent.create(
            name="x",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        agent = await async_client.agent.create(
            name="x",
            custom_id="customId",
            description="description",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.agent.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        agent = await async_client.agent.update(
            agent_id="agentId",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        agent = await async_client.agent.update(
            agent_id="agentId",
            description="description",
            name="x",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent.with_raw_response.update(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.agent.with_streaming_response.update(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        agent = await async_client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        agent = await async_client.agent.list(
            after="after",
            limit=1,
            search_text="searchText",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        agent = await async_client.agent.get_by_id(
            "agentId",
        )
        assert_matches_type(AgentGetByIDResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent.with_raw_response.get_by_id(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentGetByIDResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.agent.with_streaming_response.get_by_id(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentGetByIDResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.get_by_id(
                "",
            )
