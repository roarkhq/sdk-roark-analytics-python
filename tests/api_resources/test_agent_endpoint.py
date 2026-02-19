# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    AgentEndpointListResponse,
    AgentEndpointCreateResponse,
    AgentEndpointUpdateResponse,
    AgentEndpointGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgentEndpoint:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        agent_endpoint = client.agent_endpoint.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="INCOMING",
            value="value",
        )
        assert_matches_type(AgentEndpointCreateResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        agent_endpoint = client.agent_endpoint.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="INCOMING",
            value="value",
            environment="environment",
            outbound_dial_http_request_definition_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            outbound_dial_type="NONE",
        )
        assert_matches_type(AgentEndpointCreateResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.agent_endpoint.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="INCOMING",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_endpoint = response.parse()
        assert_matches_type(AgentEndpointCreateResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.agent_endpoint.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="INCOMING",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_endpoint = response.parse()
            assert_matches_type(AgentEndpointCreateResponse, agent_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        agent_endpoint = client.agent_endpoint.update(
            endpoint_id="endpointId",
        )
        assert_matches_type(AgentEndpointUpdateResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        agent_endpoint = client.agent_endpoint.update(
            endpoint_id="endpointId",
            environment="environment",
            outbound_dial_http_request_definition_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            outbound_dial_type="NONE",
        )
        assert_matches_type(AgentEndpointUpdateResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.agent_endpoint.with_raw_response.update(
            endpoint_id="endpointId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_endpoint = response.parse()
        assert_matches_type(AgentEndpointUpdateResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.agent_endpoint.with_streaming_response.update(
            endpoint_id="endpointId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_endpoint = response.parse()
            assert_matches_type(AgentEndpointUpdateResponse, agent_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint_id` but received ''"):
            client.agent_endpoint.with_raw_response.update(
                endpoint_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        agent_endpoint = client.agent_endpoint.list()
        assert_matches_type(AgentEndpointListResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        agent_endpoint = client.agent_endpoint.list(
            after="after",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            search_text="searchText",
        )
        assert_matches_type(AgentEndpointListResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.agent_endpoint.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_endpoint = response.parse()
        assert_matches_type(AgentEndpointListResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.agent_endpoint.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_endpoint = response.parse()
            assert_matches_type(AgentEndpointListResponse, agent_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        agent_endpoint = client.agent_endpoint.get_by_id(
            "endpointId",
        )
        assert_matches_type(AgentEndpointGetByIDResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.agent_endpoint.with_raw_response.get_by_id(
            "endpointId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_endpoint = response.parse()
        assert_matches_type(AgentEndpointGetByIDResponse, agent_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.agent_endpoint.with_streaming_response.get_by_id(
            "endpointId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_endpoint = response.parse()
            assert_matches_type(AgentEndpointGetByIDResponse, agent_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint_id` but received ''"):
            client.agent_endpoint.with_raw_response.get_by_id(
                "",
            )


class TestAsyncAgentEndpoint:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        agent_endpoint = await async_client.agent_endpoint.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="INCOMING",
            value="value",
        )
        assert_matches_type(AgentEndpointCreateResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_endpoint = await async_client.agent_endpoint.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="INCOMING",
            value="value",
            environment="environment",
            outbound_dial_http_request_definition_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            outbound_dial_type="NONE",
        )
        assert_matches_type(AgentEndpointCreateResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_endpoint.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="INCOMING",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_endpoint = await response.parse()
        assert_matches_type(AgentEndpointCreateResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_endpoint.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="INCOMING",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_endpoint = await response.parse()
            assert_matches_type(AgentEndpointCreateResponse, agent_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        agent_endpoint = await async_client.agent_endpoint.update(
            endpoint_id="endpointId",
        )
        assert_matches_type(AgentEndpointUpdateResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_endpoint = await async_client.agent_endpoint.update(
            endpoint_id="endpointId",
            environment="environment",
            outbound_dial_http_request_definition_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            outbound_dial_type="NONE",
        )
        assert_matches_type(AgentEndpointUpdateResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_endpoint.with_raw_response.update(
            endpoint_id="endpointId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_endpoint = await response.parse()
        assert_matches_type(AgentEndpointUpdateResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_endpoint.with_streaming_response.update(
            endpoint_id="endpointId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_endpoint = await response.parse()
            assert_matches_type(AgentEndpointUpdateResponse, agent_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint_id` but received ''"):
            await async_client.agent_endpoint.with_raw_response.update(
                endpoint_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        agent_endpoint = await async_client.agent_endpoint.list()
        assert_matches_type(AgentEndpointListResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_endpoint = await async_client.agent_endpoint.list(
            after="after",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            search_text="searchText",
        )
        assert_matches_type(AgentEndpointListResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_endpoint.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_endpoint = await response.parse()
        assert_matches_type(AgentEndpointListResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_endpoint.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_endpoint = await response.parse()
            assert_matches_type(AgentEndpointListResponse, agent_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        agent_endpoint = await async_client.agent_endpoint.get_by_id(
            "endpointId",
        )
        assert_matches_type(AgentEndpointGetByIDResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_endpoint.with_raw_response.get_by_id(
            "endpointId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_endpoint = await response.parse()
        assert_matches_type(AgentEndpointGetByIDResponse, agent_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_endpoint.with_streaming_response.get_by_id(
            "endpointId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_endpoint = await response.parse()
            assert_matches_type(AgentEndpointGetByIDResponse, agent_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint_id` but received ''"):
            await async_client.agent_endpoint.with_raw_response.get_by_id(
                "",
            )
