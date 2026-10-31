# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    AgentVersionListResponse,
    AgentVersionGetByIDResponse,
    AgentVersionRollbackResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgentVersion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        agent_version = client.agent_version.list(
            agent_id="agentId",
        )
        assert_matches_type(AgentVersionListResponse, agent_version, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        agent_version = client.agent_version.list(
            agent_id="agentId",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(AgentVersionListResponse, agent_version, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.agent_version.with_raw_response.list(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_version = response.parse()
        assert_matches_type(AgentVersionListResponse, agent_version, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.agent_version.with_streaming_response.list(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_version = response.parse()
            assert_matches_type(AgentVersionListResponse, agent_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent_version.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        agent_version = client.agent_version.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentVersionGetByIDResponse, agent_version, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.agent_version.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_version = response.parse()
        assert_matches_type(AgentVersionGetByIDResponse, agent_version, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.agent_version.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_version = response.parse()
            assert_matches_type(AgentVersionGetByIDResponse, agent_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.agent_version.with_raw_response.get_by_id(
                "",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent_version.with_raw_response.get_by_id(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

    @parametrize
    def test_method_rollback(self, client: Roark) -> None:
        agent_version = client.agent_version.rollback(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentVersionRollbackResponse, agent_version, path=["response"])

    @parametrize
    def test_method_rollback_with_all_params(self, client: Roark) -> None:
        agent_version = client.agent_version.rollback(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_live_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="x",
        )
        assert_matches_type(AgentVersionRollbackResponse, agent_version, path=["response"])

    @parametrize
    def test_raw_response_rollback(self, client: Roark) -> None:
        response = client.agent_version.with_raw_response.rollback(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_version = response.parse()
        assert_matches_type(AgentVersionRollbackResponse, agent_version, path=["response"])

    @parametrize
    def test_streaming_response_rollback(self, client: Roark) -> None:
        with client.agent_version.with_streaming_response.rollback(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_version = response.parse()
            assert_matches_type(AgentVersionRollbackResponse, agent_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rollback(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.agent_version.with_raw_response.rollback(
                version_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent_version.with_raw_response.rollback(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )


class TestAsyncAgentVersion:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        agent_version = await async_client.agent_version.list(
            agent_id="agentId",
        )
        assert_matches_type(AgentVersionListResponse, agent_version, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_version = await async_client.agent_version.list(
            agent_id="agentId",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(AgentVersionListResponse, agent_version, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_version.with_raw_response.list(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_version = await response.parse()
        assert_matches_type(AgentVersionListResponse, agent_version, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_version.with_streaming_response.list(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_version = await response.parse()
            assert_matches_type(AgentVersionListResponse, agent_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent_version.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        agent_version = await async_client.agent_version.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentVersionGetByIDResponse, agent_version, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_version.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_version = await response.parse()
        assert_matches_type(AgentVersionGetByIDResponse, agent_version, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_version.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_version = await response.parse()
            assert_matches_type(AgentVersionGetByIDResponse, agent_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.agent_version.with_raw_response.get_by_id(
                "",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent_version.with_raw_response.get_by_id(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

    @parametrize
    async def test_method_rollback(self, async_client: AsyncRoark) -> None:
        agent_version = await async_client.agent_version.rollback(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentVersionRollbackResponse, agent_version, path=["response"])

    @parametrize
    async def test_method_rollback_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_version = await async_client.agent_version.rollback(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_live_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="x",
        )
        assert_matches_type(AgentVersionRollbackResponse, agent_version, path=["response"])

    @parametrize
    async def test_raw_response_rollback(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_version.with_raw_response.rollback(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_version = await response.parse()
        assert_matches_type(AgentVersionRollbackResponse, agent_version, path=["response"])

    @parametrize
    async def test_streaming_response_rollback(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_version.with_streaming_response.rollback(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_version = await response.parse()
            assert_matches_type(AgentVersionRollbackResponse, agent_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rollback(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.agent_version.with_raw_response.rollback(
                version_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent_version.with_raw_response.rollback(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )
