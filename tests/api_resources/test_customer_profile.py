# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    CustomerProfileListResponse,
    CustomerProfileDeleteResponse,
    CustomerProfileGetByIDResponse,
    CustomerProfileUpdateNotesResponse,
    CustomerProfileSetAttributeResponse,
    CustomerProfileClearAttributeResponse,
    CustomerProfileUnlockAttributeResponse,
    CustomerProfileListConversationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomerProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        customer_profile = client.customer_profile.list()
        assert_matches_type(CustomerProfileListResponse, customer_profile, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        customer_profile = client.customer_profile.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            field_key="FULL_NAME",
            field_operator="EQUALS",
            field_value="x",
            include_no_data="true",
            limit=1,
            modality="call",
            page=1,
            search="search",
            sort_by="lastSeenAt",
            sort_direction="asc",
        )
        assert_matches_type(CustomerProfileListResponse, customer_profile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.customer_profile.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = response.parse()
        assert_matches_type(CustomerProfileListResponse, customer_profile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.customer_profile.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = response.parse()
            assert_matches_type(CustomerProfileListResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        customer_profile = client.customer_profile.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerProfileDeleteResponse, customer_profile, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.customer_profile.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = response.parse()
        assert_matches_type(CustomerProfileDeleteResponse, customer_profile, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.customer_profile.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = response.parse()
            assert_matches_type(CustomerProfileDeleteResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer_profile.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_clear_attribute(self, client: Roark) -> None:
        customer_profile = client.customer_profile.clear_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerProfileClearAttributeResponse, customer_profile, path=["response"])

    @parametrize
    def test_raw_response_clear_attribute(self, client: Roark) -> None:
        response = client.customer_profile.with_raw_response.clear_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = response.parse()
        assert_matches_type(CustomerProfileClearAttributeResponse, customer_profile, path=["response"])

    @parametrize
    def test_streaming_response_clear_attribute(self, client: Roark) -> None:
        with client.customer_profile.with_streaming_response.clear_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = response.parse()
            assert_matches_type(CustomerProfileClearAttributeResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_clear_attribute(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.customer_profile.with_raw_response.clear_attribute(
                "",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer_profile.with_raw_response.clear_attribute(
                "FULL_NAME",
                customer_profile_id="",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        customer_profile = client.customer_profile.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerProfileGetByIDResponse, customer_profile, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.customer_profile.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = response.parse()
        assert_matches_type(CustomerProfileGetByIDResponse, customer_profile, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.customer_profile.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = response.parse()
            assert_matches_type(CustomerProfileGetByIDResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer_profile.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_list_conversations(self, client: Roark) -> None:
        customer_profile = client.customer_profile.list_conversations(
            customer_profile_id="customerProfileId",
        )
        assert_matches_type(CustomerProfileListConversationsResponse, customer_profile, path=["response"])

    @parametrize
    def test_method_list_conversations_with_all_params(self, client: Roark) -> None:
        customer_profile = client.customer_profile.list_conversations(
            customer_profile_id="customerProfileId",
            limit=1,
            page=1,
        )
        assert_matches_type(CustomerProfileListConversationsResponse, customer_profile, path=["response"])

    @parametrize
    def test_raw_response_list_conversations(self, client: Roark) -> None:
        response = client.customer_profile.with_raw_response.list_conversations(
            customer_profile_id="customerProfileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = response.parse()
        assert_matches_type(CustomerProfileListConversationsResponse, customer_profile, path=["response"])

    @parametrize
    def test_streaming_response_list_conversations(self, client: Roark) -> None:
        with client.customer_profile.with_streaming_response.list_conversations(
            customer_profile_id="customerProfileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = response.parse()
            assert_matches_type(CustomerProfileListConversationsResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_conversations(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer_profile.with_raw_response.list_conversations(
                customer_profile_id="",
            )

    @parametrize
    def test_method_set_attribute(self, client: Roark) -> None:
        customer_profile = client.customer_profile.set_attribute(
            key="FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )
        assert_matches_type(CustomerProfileSetAttributeResponse, customer_profile, path=["response"])

    @parametrize
    def test_raw_response_set_attribute(self, client: Roark) -> None:
        response = client.customer_profile.with_raw_response.set_attribute(
            key="FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = response.parse()
        assert_matches_type(CustomerProfileSetAttributeResponse, customer_profile, path=["response"])

    @parametrize
    def test_streaming_response_set_attribute(self, client: Roark) -> None:
        with client.customer_profile.with_streaming_response.set_attribute(
            key="FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = response.parse()
            assert_matches_type(CustomerProfileSetAttributeResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_attribute(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.customer_profile.with_raw_response.set_attribute(
                key="",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                value="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer_profile.with_raw_response.set_attribute(
                key="FULL_NAME",
                customer_profile_id="",
                value="x",
            )

    @parametrize
    def test_method_unlock_attribute(self, client: Roark) -> None:
        customer_profile = client.customer_profile.unlock_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerProfileUnlockAttributeResponse, customer_profile, path=["response"])

    @parametrize
    def test_raw_response_unlock_attribute(self, client: Roark) -> None:
        response = client.customer_profile.with_raw_response.unlock_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = response.parse()
        assert_matches_type(CustomerProfileUnlockAttributeResponse, customer_profile, path=["response"])

    @parametrize
    def test_streaming_response_unlock_attribute(self, client: Roark) -> None:
        with client.customer_profile.with_streaming_response.unlock_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = response.parse()
            assert_matches_type(CustomerProfileUnlockAttributeResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unlock_attribute(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.customer_profile.with_raw_response.unlock_attribute(
                "",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer_profile.with_raw_response.unlock_attribute(
                "FULL_NAME",
                customer_profile_id="",
            )

    @parametrize
    def test_method_update_notes(self, client: Roark) -> None:
        customer_profile = client.customer_profile.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )
        assert_matches_type(CustomerProfileUpdateNotesResponse, customer_profile, path=["response"])

    @parametrize
    def test_raw_response_update_notes(self, client: Roark) -> None:
        response = client.customer_profile.with_raw_response.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = response.parse()
        assert_matches_type(CustomerProfileUpdateNotesResponse, customer_profile, path=["response"])

    @parametrize
    def test_streaming_response_update_notes(self, client: Roark) -> None:
        with client.customer_profile.with_streaming_response.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = response.parse()
            assert_matches_type(CustomerProfileUpdateNotesResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_notes(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer_profile.with_raw_response.update_notes(
                customer_profile_id="",
                notes="notes",
            )


class TestAsyncCustomerProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.list()
        assert_matches_type(CustomerProfileListResponse, customer_profile, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            field_key="FULL_NAME",
            field_operator="EQUALS",
            field_value="x",
            include_no_data="true",
            limit=1,
            modality="call",
            page=1,
            search="search",
            sort_by="lastSeenAt",
            sort_direction="asc",
        )
        assert_matches_type(CustomerProfileListResponse, customer_profile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_profile.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = await response.parse()
        assert_matches_type(CustomerProfileListResponse, customer_profile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_profile.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = await response.parse()
            assert_matches_type(CustomerProfileListResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerProfileDeleteResponse, customer_profile, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_profile.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = await response.parse()
        assert_matches_type(CustomerProfileDeleteResponse, customer_profile, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_profile.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = await response.parse()
            assert_matches_type(CustomerProfileDeleteResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer_profile.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_clear_attribute(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.clear_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerProfileClearAttributeResponse, customer_profile, path=["response"])

    @parametrize
    async def test_raw_response_clear_attribute(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_profile.with_raw_response.clear_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = await response.parse()
        assert_matches_type(CustomerProfileClearAttributeResponse, customer_profile, path=["response"])

    @parametrize
    async def test_streaming_response_clear_attribute(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_profile.with_streaming_response.clear_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = await response.parse()
            assert_matches_type(CustomerProfileClearAttributeResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_clear_attribute(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.customer_profile.with_raw_response.clear_attribute(
                "",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer_profile.with_raw_response.clear_attribute(
                "FULL_NAME",
                customer_profile_id="",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerProfileGetByIDResponse, customer_profile, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_profile.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = await response.parse()
        assert_matches_type(CustomerProfileGetByIDResponse, customer_profile, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_profile.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = await response.parse()
            assert_matches_type(CustomerProfileGetByIDResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer_profile.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_list_conversations(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.list_conversations(
            customer_profile_id="customerProfileId",
        )
        assert_matches_type(CustomerProfileListConversationsResponse, customer_profile, path=["response"])

    @parametrize
    async def test_method_list_conversations_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.list_conversations(
            customer_profile_id="customerProfileId",
            limit=1,
            page=1,
        )
        assert_matches_type(CustomerProfileListConversationsResponse, customer_profile, path=["response"])

    @parametrize
    async def test_raw_response_list_conversations(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_profile.with_raw_response.list_conversations(
            customer_profile_id="customerProfileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = await response.parse()
        assert_matches_type(CustomerProfileListConversationsResponse, customer_profile, path=["response"])

    @parametrize
    async def test_streaming_response_list_conversations(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_profile.with_streaming_response.list_conversations(
            customer_profile_id="customerProfileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = await response.parse()
            assert_matches_type(CustomerProfileListConversationsResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_conversations(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer_profile.with_raw_response.list_conversations(
                customer_profile_id="",
            )

    @parametrize
    async def test_method_set_attribute(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.set_attribute(
            key="FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )
        assert_matches_type(CustomerProfileSetAttributeResponse, customer_profile, path=["response"])

    @parametrize
    async def test_raw_response_set_attribute(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_profile.with_raw_response.set_attribute(
            key="FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = await response.parse()
        assert_matches_type(CustomerProfileSetAttributeResponse, customer_profile, path=["response"])

    @parametrize
    async def test_streaming_response_set_attribute(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_profile.with_streaming_response.set_attribute(
            key="FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = await response.parse()
            assert_matches_type(CustomerProfileSetAttributeResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_attribute(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.customer_profile.with_raw_response.set_attribute(
                key="",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                value="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer_profile.with_raw_response.set_attribute(
                key="FULL_NAME",
                customer_profile_id="",
                value="x",
            )

    @parametrize
    async def test_method_unlock_attribute(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.unlock_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerProfileUnlockAttributeResponse, customer_profile, path=["response"])

    @parametrize
    async def test_raw_response_unlock_attribute(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_profile.with_raw_response.unlock_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = await response.parse()
        assert_matches_type(CustomerProfileUnlockAttributeResponse, customer_profile, path=["response"])

    @parametrize
    async def test_streaming_response_unlock_attribute(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_profile.with_streaming_response.unlock_attribute(
            "FULL_NAME",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = await response.parse()
            assert_matches_type(CustomerProfileUnlockAttributeResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unlock_attribute(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.customer_profile.with_raw_response.unlock_attribute(
                "",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer_profile.with_raw_response.unlock_attribute(
                "FULL_NAME",
                customer_profile_id="",
            )

    @parametrize
    async def test_method_update_notes(self, async_client: AsyncRoark) -> None:
        customer_profile = await async_client.customer_profile.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )
        assert_matches_type(CustomerProfileUpdateNotesResponse, customer_profile, path=["response"])

    @parametrize
    async def test_raw_response_update_notes(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_profile.with_raw_response.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_profile = await response.parse()
        assert_matches_type(CustomerProfileUpdateNotesResponse, customer_profile, path=["response"])

    @parametrize
    async def test_streaming_response_update_notes(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_profile.with_streaming_response.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_profile = await response.parse()
            assert_matches_type(CustomerProfileUpdateNotesResponse, customer_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_notes(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer_profile.with_raw_response.update_notes(
                customer_profile_id="",
                notes="notes",
            )
