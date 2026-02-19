# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    HTTPRequestDefinitionListResponse,
    HTTPRequestDefinitionCreateResponse,
    HTTPRequestDefinitionUpdateResponse,
    HTTPRequestDefinitionGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHTTPRequestDefinition:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        http_request_definition = client.http_request_definition.create(
            scope="AGENT_OUTBOUND_DIAL",
            url="https://example.com",
        )
        assert_matches_type(HTTPRequestDefinitionCreateResponse, http_request_definition, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        http_request_definition = client.http_request_definition.create(
            scope="AGENT_OUTBOUND_DIAL",
            url="https://example.com",
            body="string",
            description="description",
            headers={"foo": "string"},
            method="POST",
        )
        assert_matches_type(HTTPRequestDefinitionCreateResponse, http_request_definition, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.http_request_definition.with_raw_response.create(
            scope="AGENT_OUTBOUND_DIAL",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_request_definition = response.parse()
        assert_matches_type(HTTPRequestDefinitionCreateResponse, http_request_definition, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.http_request_definition.with_streaming_response.create(
            scope="AGENT_OUTBOUND_DIAL",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_request_definition = response.parse()
            assert_matches_type(HTTPRequestDefinitionCreateResponse, http_request_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        http_request_definition = client.http_request_definition.update(
            definition_id="definitionId",
        )
        assert_matches_type(HTTPRequestDefinitionUpdateResponse, http_request_definition, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        http_request_definition = client.http_request_definition.update(
            definition_id="definitionId",
            body="string",
            description="description",
            headers={"foo": "string"},
            method="POST",
            url="https://example.com",
        )
        assert_matches_type(HTTPRequestDefinitionUpdateResponse, http_request_definition, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.http_request_definition.with_raw_response.update(
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_request_definition = response.parse()
        assert_matches_type(HTTPRequestDefinitionUpdateResponse, http_request_definition, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.http_request_definition.with_streaming_response.update(
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_request_definition = response.parse()
            assert_matches_type(HTTPRequestDefinitionUpdateResponse, http_request_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.http_request_definition.with_raw_response.update(
                definition_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        http_request_definition = client.http_request_definition.list()
        assert_matches_type(HTTPRequestDefinitionListResponse, http_request_definition, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        http_request_definition = client.http_request_definition.list(
            after="after",
            limit=1,
        )
        assert_matches_type(HTTPRequestDefinitionListResponse, http_request_definition, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.http_request_definition.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_request_definition = response.parse()
        assert_matches_type(HTTPRequestDefinitionListResponse, http_request_definition, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.http_request_definition.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_request_definition = response.parse()
            assert_matches_type(HTTPRequestDefinitionListResponse, http_request_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        http_request_definition = client.http_request_definition.get_by_id(
            "definitionId",
        )
        assert_matches_type(HTTPRequestDefinitionGetByIDResponse, http_request_definition, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.http_request_definition.with_raw_response.get_by_id(
            "definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_request_definition = response.parse()
        assert_matches_type(HTTPRequestDefinitionGetByIDResponse, http_request_definition, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.http_request_definition.with_streaming_response.get_by_id(
            "definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_request_definition = response.parse()
            assert_matches_type(HTTPRequestDefinitionGetByIDResponse, http_request_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.http_request_definition.with_raw_response.get_by_id(
                "",
            )


class TestAsyncHTTPRequestDefinition:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        http_request_definition = await async_client.http_request_definition.create(
            scope="AGENT_OUTBOUND_DIAL",
            url="https://example.com",
        )
        assert_matches_type(HTTPRequestDefinitionCreateResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        http_request_definition = await async_client.http_request_definition.create(
            scope="AGENT_OUTBOUND_DIAL",
            url="https://example.com",
            body="string",
            description="description",
            headers={"foo": "string"},
            method="POST",
        )
        assert_matches_type(HTTPRequestDefinitionCreateResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.http_request_definition.with_raw_response.create(
            scope="AGENT_OUTBOUND_DIAL",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_request_definition = await response.parse()
        assert_matches_type(HTTPRequestDefinitionCreateResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.http_request_definition.with_streaming_response.create(
            scope="AGENT_OUTBOUND_DIAL",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_request_definition = await response.parse()
            assert_matches_type(HTTPRequestDefinitionCreateResponse, http_request_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        http_request_definition = await async_client.http_request_definition.update(
            definition_id="definitionId",
        )
        assert_matches_type(HTTPRequestDefinitionUpdateResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        http_request_definition = await async_client.http_request_definition.update(
            definition_id="definitionId",
            body="string",
            description="description",
            headers={"foo": "string"},
            method="POST",
            url="https://example.com",
        )
        assert_matches_type(HTTPRequestDefinitionUpdateResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.http_request_definition.with_raw_response.update(
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_request_definition = await response.parse()
        assert_matches_type(HTTPRequestDefinitionUpdateResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.http_request_definition.with_streaming_response.update(
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_request_definition = await response.parse()
            assert_matches_type(HTTPRequestDefinitionUpdateResponse, http_request_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.http_request_definition.with_raw_response.update(
                definition_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        http_request_definition = await async_client.http_request_definition.list()
        assert_matches_type(HTTPRequestDefinitionListResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        http_request_definition = await async_client.http_request_definition.list(
            after="after",
            limit=1,
        )
        assert_matches_type(HTTPRequestDefinitionListResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.http_request_definition.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_request_definition = await response.parse()
        assert_matches_type(HTTPRequestDefinitionListResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.http_request_definition.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_request_definition = await response.parse()
            assert_matches_type(HTTPRequestDefinitionListResponse, http_request_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        http_request_definition = await async_client.http_request_definition.get_by_id(
            "definitionId",
        )
        assert_matches_type(HTTPRequestDefinitionGetByIDResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.http_request_definition.with_raw_response.get_by_id(
            "definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_request_definition = await response.parse()
        assert_matches_type(HTTPRequestDefinitionGetByIDResponse, http_request_definition, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.http_request_definition.with_streaming_response.get_by_id(
            "definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_request_definition = await response.parse()
            assert_matches_type(HTTPRequestDefinitionGetByIDResponse, http_request_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.http_request_definition.with_raw_response.get_by_id(
                "",
            )
