# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    AgentConfigListResponse,
    AgentConfigUpdateResponse,
    AgentConfigGetByIDResponse,
    AgentConfigPromoteResponse,
    AgentConfigResolveResponse,
    AgentConfigDeleteStagingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgentConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        agent_config = client.agent_config.update(
            key="x",
            channel="production",
            document={"foo": "string"},
        )
        assert_matches_type(AgentConfigUpdateResponse, agent_config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        agent_config = client.agent_config.update(
            key="x",
            channel="production",
            document={"foo": "string"},
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
        )
        assert_matches_type(AgentConfigUpdateResponse, agent_config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.agent_config.with_raw_response.update(
            key="x",
            channel="production",
            document={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = response.parse()
        assert_matches_type(AgentConfigUpdateResponse, agent_config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.agent_config.with_streaming_response.update(
            key="x",
            channel="production",
            document={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = response.parse()
            assert_matches_type(AgentConfigUpdateResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.agent_config.with_raw_response.update(
                key="",
                channel="production",
                document={"foo": "string"},
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        agent_config = client.agent_config.list()
        assert_matches_type(AgentConfigListResponse, agent_config, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.agent_config.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = response.parse()
        assert_matches_type(AgentConfigListResponse, agent_config, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.agent_config.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = response.parse()
            assert_matches_type(AgentConfigListResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_staging(self, client: Roark) -> None:
        agent_config = client.agent_config.delete_staging(
            "x",
        )
        assert_matches_type(AgentConfigDeleteStagingResponse, agent_config, path=["response"])

    @parametrize
    def test_raw_response_delete_staging(self, client: Roark) -> None:
        response = client.agent_config.with_raw_response.delete_staging(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = response.parse()
        assert_matches_type(AgentConfigDeleteStagingResponse, agent_config, path=["response"])

    @parametrize
    def test_streaming_response_delete_staging(self, client: Roark) -> None:
        with client.agent_config.with_streaming_response.delete_staging(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = response.parse()
            assert_matches_type(AgentConfigDeleteStagingResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_staging(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.agent_config.with_raw_response.delete_staging(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        agent_config = client.agent_config.get_by_id(
            "x",
        )
        assert_matches_type(AgentConfigGetByIDResponse, agent_config, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.agent_config.with_raw_response.get_by_id(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = response.parse()
        assert_matches_type(AgentConfigGetByIDResponse, agent_config, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.agent_config.with_streaming_response.get_by_id(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = response.parse()
            assert_matches_type(AgentConfigGetByIDResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.agent_config.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_promote(self, client: Roark) -> None:
        agent_config = client.agent_config.promote(
            "x",
        )
        assert_matches_type(AgentConfigPromoteResponse, agent_config, path=["response"])

    @parametrize
    def test_raw_response_promote(self, client: Roark) -> None:
        response = client.agent_config.with_raw_response.promote(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = response.parse()
        assert_matches_type(AgentConfigPromoteResponse, agent_config, path=["response"])

    @parametrize
    def test_streaming_response_promote(self, client: Roark) -> None:
        with client.agent_config.with_streaming_response.promote(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = response.parse()
            assert_matches_type(AgentConfigPromoteResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_promote(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.agent_config.with_raw_response.promote(
                "",
            )

    @parametrize
    def test_method_resolve(self, client: Roark) -> None:
        agent_config = client.agent_config.resolve(
            key="x",
        )
        assert_matches_type(AgentConfigResolveResponse, agent_config, path=["response"])

    @parametrize
    def test_method_resolve_with_all_params(self, client: Roark) -> None:
        agent_config = client.agent_config.resolve(
            key="x",
            defaults={"system_prompt": "You are a helpful receptionist.", "model": "gpt-4.1", "temperature": 0.4},
            session={"called_number": "+15559870000", "caller_number": "+15551230000", "session_id": "sessionId"},
        )
        assert_matches_type(AgentConfigResolveResponse, agent_config, path=["response"])

    @parametrize
    def test_raw_response_resolve(self, client: Roark) -> None:
        response = client.agent_config.with_raw_response.resolve(
            key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = response.parse()
        assert_matches_type(AgentConfigResolveResponse, agent_config, path=["response"])

    @parametrize
    def test_streaming_response_resolve(self, client: Roark) -> None:
        with client.agent_config.with_streaming_response.resolve(
            key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = response.parse()
            assert_matches_type(AgentConfigResolveResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resolve(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.agent_config.with_raw_response.resolve(
                key="",
            )


class TestAsyncAgentConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        agent_config = await async_client.agent_config.update(
            key="x",
            channel="production",
            document={"foo": "string"},
        )
        assert_matches_type(AgentConfigUpdateResponse, agent_config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_config = await async_client.agent_config.update(
            key="x",
            channel="production",
            document={"foo": "string"},
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
        )
        assert_matches_type(AgentConfigUpdateResponse, agent_config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_config.with_raw_response.update(
            key="x",
            channel="production",
            document={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = await response.parse()
        assert_matches_type(AgentConfigUpdateResponse, agent_config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_config.with_streaming_response.update(
            key="x",
            channel="production",
            document={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = await response.parse()
            assert_matches_type(AgentConfigUpdateResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.agent_config.with_raw_response.update(
                key="",
                channel="production",
                document={"foo": "string"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        agent_config = await async_client.agent_config.list()
        assert_matches_type(AgentConfigListResponse, agent_config, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_config.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = await response.parse()
        assert_matches_type(AgentConfigListResponse, agent_config, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_config.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = await response.parse()
            assert_matches_type(AgentConfigListResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_staging(self, async_client: AsyncRoark) -> None:
        agent_config = await async_client.agent_config.delete_staging(
            "x",
        )
        assert_matches_type(AgentConfigDeleteStagingResponse, agent_config, path=["response"])

    @parametrize
    async def test_raw_response_delete_staging(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_config.with_raw_response.delete_staging(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = await response.parse()
        assert_matches_type(AgentConfigDeleteStagingResponse, agent_config, path=["response"])

    @parametrize
    async def test_streaming_response_delete_staging(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_config.with_streaming_response.delete_staging(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = await response.parse()
            assert_matches_type(AgentConfigDeleteStagingResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_staging(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.agent_config.with_raw_response.delete_staging(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        agent_config = await async_client.agent_config.get_by_id(
            "x",
        )
        assert_matches_type(AgentConfigGetByIDResponse, agent_config, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_config.with_raw_response.get_by_id(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = await response.parse()
        assert_matches_type(AgentConfigGetByIDResponse, agent_config, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_config.with_streaming_response.get_by_id(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = await response.parse()
            assert_matches_type(AgentConfigGetByIDResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.agent_config.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_promote(self, async_client: AsyncRoark) -> None:
        agent_config = await async_client.agent_config.promote(
            "x",
        )
        assert_matches_type(AgentConfigPromoteResponse, agent_config, path=["response"])

    @parametrize
    async def test_raw_response_promote(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_config.with_raw_response.promote(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = await response.parse()
        assert_matches_type(AgentConfigPromoteResponse, agent_config, path=["response"])

    @parametrize
    async def test_streaming_response_promote(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_config.with_streaming_response.promote(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = await response.parse()
            assert_matches_type(AgentConfigPromoteResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_promote(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.agent_config.with_raw_response.promote(
                "",
            )

    @parametrize
    async def test_method_resolve(self, async_client: AsyncRoark) -> None:
        agent_config = await async_client.agent_config.resolve(
            key="x",
        )
        assert_matches_type(AgentConfigResolveResponse, agent_config, path=["response"])

    @parametrize
    async def test_method_resolve_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_config = await async_client.agent_config.resolve(
            key="x",
            defaults={"system_prompt": "You are a helpful receptionist.", "model": "gpt-4.1", "temperature": 0.4},
            session={"called_number": "+15559870000", "caller_number": "+15551230000", "session_id": "sessionId"},
        )
        assert_matches_type(AgentConfigResolveResponse, agent_config, path=["response"])

    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_config.with_raw_response.resolve(
            key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_config = await response.parse()
        assert_matches_type(AgentConfigResolveResponse, agent_config, path=["response"])

    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_config.with_streaming_response.resolve(
            key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_config = await response.parse()
            assert_matches_type(AgentConfigResolveResponse, agent_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resolve(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.agent_config.with_raw_response.resolve(
                key="",
            )
