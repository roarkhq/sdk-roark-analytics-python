# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    CustomerFlowFolderListResponse,
    CustomerFlowFolderCreateResponse,
    CustomerFlowFolderDeleteResponse,
    CustomerFlowFolderUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomerFlowFolder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        customer_flow_folder = client.customer_flow_folder.create(
            name="x",
        )
        assert_matches_type(CustomerFlowFolderCreateResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        customer_flow_folder = client.customer_flow_folder.create(
            name="x",
            color="GREEN",
            description="description",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowFolderCreateResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.customer_flow_folder.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_folder = response.parse()
        assert_matches_type(CustomerFlowFolderCreateResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.customer_flow_folder.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_folder = response.parse()
            assert_matches_type(CustomerFlowFolderCreateResponse, customer_flow_folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        customer_flow_folder = client.customer_flow_folder.update(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowFolderUpdateResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        customer_flow_folder = client.customer_flow_folder.update(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            color="GREEN",
            description="description",
            name="x",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowFolderUpdateResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.customer_flow_folder.with_raw_response.update(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_folder = response.parse()
        assert_matches_type(CustomerFlowFolderUpdateResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.customer_flow_folder.with_streaming_response.update(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_folder = response.parse()
            assert_matches_type(CustomerFlowFolderUpdateResponse, customer_flow_folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.customer_flow_folder.with_raw_response.update(
                folder_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        customer_flow_folder = client.customer_flow_folder.list()
        assert_matches_type(CustomerFlowFolderListResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.customer_flow_folder.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_folder = response.parse()
        assert_matches_type(CustomerFlowFolderListResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.customer_flow_folder.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_folder = response.parse()
            assert_matches_type(CustomerFlowFolderListResponse, customer_flow_folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        customer_flow_folder = client.customer_flow_folder.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowFolderDeleteResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.customer_flow_folder.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_folder = response.parse()
        assert_matches_type(CustomerFlowFolderDeleteResponse, customer_flow_folder, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.customer_flow_folder.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_folder = response.parse()
            assert_matches_type(CustomerFlowFolderDeleteResponse, customer_flow_folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.customer_flow_folder.with_raw_response.delete(
                "",
            )


class TestAsyncCustomerFlowFolder:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        customer_flow_folder = await async_client.customer_flow_folder.create(
            name="x",
        )
        assert_matches_type(CustomerFlowFolderCreateResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_flow_folder = await async_client.customer_flow_folder.create(
            name="x",
            color="GREEN",
            description="description",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowFolderCreateResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow_folder.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_folder = await response.parse()
        assert_matches_type(CustomerFlowFolderCreateResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow_folder.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_folder = await response.parse()
            assert_matches_type(CustomerFlowFolderCreateResponse, customer_flow_folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        customer_flow_folder = await async_client.customer_flow_folder.update(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowFolderUpdateResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_flow_folder = await async_client.customer_flow_folder.update(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            color="GREEN",
            description="description",
            name="x",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowFolderUpdateResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow_folder.with_raw_response.update(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_folder = await response.parse()
        assert_matches_type(CustomerFlowFolderUpdateResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow_folder.with_streaming_response.update(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_folder = await response.parse()
            assert_matches_type(CustomerFlowFolderUpdateResponse, customer_flow_folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.customer_flow_folder.with_raw_response.update(
                folder_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        customer_flow_folder = await async_client.customer_flow_folder.list()
        assert_matches_type(CustomerFlowFolderListResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow_folder.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_folder = await response.parse()
        assert_matches_type(CustomerFlowFolderListResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow_folder.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_folder = await response.parse()
            assert_matches_type(CustomerFlowFolderListResponse, customer_flow_folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        customer_flow_folder = await async_client.customer_flow_folder.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowFolderDeleteResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow_folder.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_folder = await response.parse()
        assert_matches_type(CustomerFlowFolderDeleteResponse, customer_flow_folder, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow_folder.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_folder = await response.parse()
            assert_matches_type(CustomerFlowFolderDeleteResponse, customer_flow_folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.customer_flow_folder.with_raw_response.delete(
                "",
            )
