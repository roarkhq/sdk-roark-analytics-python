# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    CustomerListResponse,
    CustomerDeleteResponse,
    CustomerGetByIDResponse,
    CustomerListFieldsResponse,
    CustomerCreateFieldResponse,
    CustomerDeleteFieldResponse,
    CustomerUpdateFieldResponse,
    CustomerUpdateNotesResponse,
    CustomerSetAttributeResponse,
    CustomerClearAttributeResponse,
    CustomerUnlockAttributeResponse,
    CustomerListConversationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        customer = client.customer.list()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        customer = client.customer.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            field_key="x",
            field_operator="EQUALS",
            field_value="x",
            include_no_data="true",
            limit=1,
            modality="voice",
            page=1,
            search="search",
            sort_by="sortBy",
            sort_direction="asc",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.customer.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.customer.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        customer = client.customer.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerDeleteResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.customer.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerDeleteResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.customer.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerDeleteResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_clear_attribute(self, client: Roark) -> None:
        customer = client.customer.clear_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerClearAttributeResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_clear_attribute(self, client: Roark) -> None:
        response = client.customer.with_raw_response.clear_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerClearAttributeResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_clear_attribute(self, client: Roark) -> None:
        with client.customer.with_streaming_response.clear_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerClearAttributeResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_clear_attribute(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.customer.with_raw_response.clear_attribute(
                "",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer.with_raw_response.clear_attribute(
                "x",
                customer_profile_id="",
            )

    @parametrize
    def test_method_create_field(self, client: Roark) -> None:
        customer = client.customer.create_field(
            extract=True,
            key="plan_tier",
            label="x",
            value_type="TEXT",
        )
        assert_matches_type(CustomerCreateFieldResponse, customer, path=["response"])

    @parametrize
    def test_method_create_field_with_all_params(self, client: Roark) -> None:
        customer = client.customer.create_field(
            extract=True,
            key="plan_tier",
            label="x",
            value_type="TEXT",
            description="x",
        )
        assert_matches_type(CustomerCreateFieldResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_create_field(self, client: Roark) -> None:
        response = client.customer.with_raw_response.create_field(
            extract=True,
            key="plan_tier",
            label="x",
            value_type="TEXT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerCreateFieldResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_create_field(self, client: Roark) -> None:
        with client.customer.with_streaming_response.create_field(
            extract=True,
            key="plan_tier",
            label="x",
            value_type="TEXT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerCreateFieldResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_field(self, client: Roark) -> None:
        customer = client.customer.delete_field(
            "x",
        )
        assert_matches_type(CustomerDeleteFieldResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_delete_field(self, client: Roark) -> None:
        response = client.customer.with_raw_response.delete_field(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerDeleteFieldResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_delete_field(self, client: Roark) -> None:
        with client.customer.with_streaming_response.delete_field(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerDeleteFieldResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_field(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.customer.with_raw_response.delete_field(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        customer = client.customer.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerGetByIDResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.customer.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerGetByIDResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.customer.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerGetByIDResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_list_conversations(self, client: Roark) -> None:
        customer = client.customer.list_conversations(
            customer_profile_id="customerProfileId",
        )
        assert_matches_type(CustomerListConversationsResponse, customer, path=["response"])

    @parametrize
    def test_method_list_conversations_with_all_params(self, client: Roark) -> None:
        customer = client.customer.list_conversations(
            customer_profile_id="customerProfileId",
            limit=1,
            page=1,
        )
        assert_matches_type(CustomerListConversationsResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_list_conversations(self, client: Roark) -> None:
        response = client.customer.with_raw_response.list_conversations(
            customer_profile_id="customerProfileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerListConversationsResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_list_conversations(self, client: Roark) -> None:
        with client.customer.with_streaming_response.list_conversations(
            customer_profile_id="customerProfileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerListConversationsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_conversations(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer.with_raw_response.list_conversations(
                customer_profile_id="",
            )

    @parametrize
    def test_method_list_fields(self, client: Roark) -> None:
        customer = client.customer.list_fields()
        assert_matches_type(CustomerListFieldsResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_list_fields(self, client: Roark) -> None:
        response = client.customer.with_raw_response.list_fields()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerListFieldsResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_list_fields(self, client: Roark) -> None:
        with client.customer.with_streaming_response.list_fields() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerListFieldsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_attribute(self, client: Roark) -> None:
        customer = client.customer.set_attribute(
            key="x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )
        assert_matches_type(CustomerSetAttributeResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_set_attribute(self, client: Roark) -> None:
        response = client.customer.with_raw_response.set_attribute(
            key="x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerSetAttributeResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_set_attribute(self, client: Roark) -> None:
        with client.customer.with_streaming_response.set_attribute(
            key="x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerSetAttributeResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_attribute(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.customer.with_raw_response.set_attribute(
                key="",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                value="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer.with_raw_response.set_attribute(
                key="x",
                customer_profile_id="",
                value="x",
            )

    @parametrize
    def test_method_unlock_attribute(self, client: Roark) -> None:
        customer = client.customer.unlock_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerUnlockAttributeResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_unlock_attribute(self, client: Roark) -> None:
        response = client.customer.with_raw_response.unlock_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerUnlockAttributeResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_unlock_attribute(self, client: Roark) -> None:
        with client.customer.with_streaming_response.unlock_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerUnlockAttributeResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unlock_attribute(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.customer.with_raw_response.unlock_attribute(
                "",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer.with_raw_response.unlock_attribute(
                "x",
                customer_profile_id="",
            )

    @parametrize
    def test_method_update_field(self, client: Roark) -> None:
        customer = client.customer.update_field(
            key="x",
        )
        assert_matches_type(CustomerUpdateFieldResponse, customer, path=["response"])

    @parametrize
    def test_method_update_field_with_all_params(self, client: Roark) -> None:
        customer = client.customer.update_field(
            key="x",
            description="x",
            extract=True,
            label="x",
            value_type="TEXT",
        )
        assert_matches_type(CustomerUpdateFieldResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_update_field(self, client: Roark) -> None:
        response = client.customer.with_raw_response.update_field(
            key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerUpdateFieldResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_update_field(self, client: Roark) -> None:
        with client.customer.with_streaming_response.update_field(
            key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerUpdateFieldResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_field(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.customer.with_raw_response.update_field(
                key="",
            )

    @parametrize
    def test_method_update_notes(self, client: Roark) -> None:
        customer = client.customer.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )
        assert_matches_type(CustomerUpdateNotesResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_update_notes(self, client: Roark) -> None:
        response = client.customer.with_raw_response.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerUpdateNotesResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_update_notes(self, client: Roark) -> None:
        with client.customer.with_streaming_response.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerUpdateNotesResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_notes(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            client.customer.with_raw_response.update_notes(
                customer_profile_id="",
                notes="notes",
            )


class TestAsyncCustomer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.list()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            field_key="x",
            field_operator="EQUALS",
            field_value="x",
            include_no_data="true",
            limit=1,
            modality="voice",
            page=1,
            search="search",
            sort_by="sortBy",
            sort_direction="asc",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerDeleteResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerDeleteResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerDeleteResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_clear_attribute(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.clear_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerClearAttributeResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_clear_attribute(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.clear_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerClearAttributeResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_clear_attribute(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.clear_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerClearAttributeResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_clear_attribute(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.customer.with_raw_response.clear_attribute(
                "",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer.with_raw_response.clear_attribute(
                "x",
                customer_profile_id="",
            )

    @parametrize
    async def test_method_create_field(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.create_field(
            extract=True,
            key="plan_tier",
            label="x",
            value_type="TEXT",
        )
        assert_matches_type(CustomerCreateFieldResponse, customer, path=["response"])

    @parametrize
    async def test_method_create_field_with_all_params(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.create_field(
            extract=True,
            key="plan_tier",
            label="x",
            value_type="TEXT",
            description="x",
        )
        assert_matches_type(CustomerCreateFieldResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_create_field(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.create_field(
            extract=True,
            key="plan_tier",
            label="x",
            value_type="TEXT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerCreateFieldResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create_field(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.create_field(
            extract=True,
            key="plan_tier",
            label="x",
            value_type="TEXT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerCreateFieldResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_field(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.delete_field(
            "x",
        )
        assert_matches_type(CustomerDeleteFieldResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_delete_field(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.delete_field(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerDeleteFieldResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_delete_field(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.delete_field(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerDeleteFieldResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_field(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.customer.with_raw_response.delete_field(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerGetByIDResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerGetByIDResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerGetByIDResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_list_conversations(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.list_conversations(
            customer_profile_id="customerProfileId",
        )
        assert_matches_type(CustomerListConversationsResponse, customer, path=["response"])

    @parametrize
    async def test_method_list_conversations_with_all_params(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.list_conversations(
            customer_profile_id="customerProfileId",
            limit=1,
            page=1,
        )
        assert_matches_type(CustomerListConversationsResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_list_conversations(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.list_conversations(
            customer_profile_id="customerProfileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerListConversationsResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_list_conversations(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.list_conversations(
            customer_profile_id="customerProfileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerListConversationsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_conversations(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer.with_raw_response.list_conversations(
                customer_profile_id="",
            )

    @parametrize
    async def test_method_list_fields(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.list_fields()
        assert_matches_type(CustomerListFieldsResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_list_fields(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.list_fields()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerListFieldsResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_list_fields(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.list_fields() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerListFieldsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_attribute(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.set_attribute(
            key="x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )
        assert_matches_type(CustomerSetAttributeResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_set_attribute(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.set_attribute(
            key="x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerSetAttributeResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_set_attribute(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.set_attribute(
            key="x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerSetAttributeResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_attribute(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.customer.with_raw_response.set_attribute(
                key="",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                value="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer.with_raw_response.set_attribute(
                key="x",
                customer_profile_id="",
                value="x",
            )

    @parametrize
    async def test_method_unlock_attribute(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.unlock_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerUnlockAttributeResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_unlock_attribute(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.unlock_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerUnlockAttributeResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_unlock_attribute(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.unlock_attribute(
            "x",
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerUnlockAttributeResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unlock_attribute(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.customer.with_raw_response.unlock_attribute(
                "",
                customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer.with_raw_response.unlock_attribute(
                "x",
                customer_profile_id="",
            )

    @parametrize
    async def test_method_update_field(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.update_field(
            key="x",
        )
        assert_matches_type(CustomerUpdateFieldResponse, customer, path=["response"])

    @parametrize
    async def test_method_update_field_with_all_params(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.update_field(
            key="x",
            description="x",
            extract=True,
            label="x",
            value_type="TEXT",
        )
        assert_matches_type(CustomerUpdateFieldResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_update_field(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.update_field(
            key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerUpdateFieldResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_update_field(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.update_field(
            key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerUpdateFieldResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_field(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.customer.with_raw_response.update_field(
                key="",
            )

    @parametrize
    async def test_method_update_notes(self, async_client: AsyncRoark) -> None:
        customer = await async_client.customer.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )
        assert_matches_type(CustomerUpdateNotesResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_update_notes(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer.with_raw_response.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerUpdateNotesResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_update_notes(self, async_client: AsyncRoark) -> None:
        async with async_client.customer.with_streaming_response.update_notes(
            customer_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            notes="notes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerUpdateNotesResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_notes(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_profile_id` but received ''"):
            await async_client.customer.with_raw_response.update_notes(
                customer_profile_id="",
                notes="notes",
            )
