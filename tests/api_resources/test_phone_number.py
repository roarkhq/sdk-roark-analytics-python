# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    PhoneNumberListResponse,
    PhoneNumberCreateResponse,
    PhoneNumberDeleteResponse,
    PhoneNumberUpdateResponse,
    PhoneNumberGetAllowanceResponse,
    PhoneNumberListAvailableResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumber:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        phone_number = client.phone_number.create()
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        phone_number = client.phone_number.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auto_pick={"area_code": "415", "contains": "555", "country": "US", "number_type": "LOCAL"},
            country="US",
            e164="+14155550123",
            expect_free=True,
            expect_monthly_rent_micros=2000000,
            name="x",
        )
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.phone_number.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.phone_number.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        phone_number = client.phone_number.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        phone_number = client.phone_number.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.phone_number.with_raw_response.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.phone_number.with_streaming_response.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.phone_number.with_raw_response.update(
                phone_number_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        phone_number = client.phone_number.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        phone_number = client.phone_number.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.phone_number.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.phone_number.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        phone_number = client.phone_number.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.phone_number.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.phone_number.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.phone_number.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_allowance(self, client: Roark) -> None:
        phone_number = client.phone_number.get_allowance()
        assert_matches_type(PhoneNumberGetAllowanceResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_get_allowance(self, client: Roark) -> None:
        response = client.phone_number.with_raw_response.get_allowance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberGetAllowanceResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_get_allowance(self, client: Roark) -> None:
        with client.phone_number.with_streaming_response.get_allowance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberGetAllowanceResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_available(self, client: Roark) -> None:
        phone_number = client.phone_number.list_available()
        assert_matches_type(PhoneNumberListAvailableResponse, phone_number, path=["response"])

    @parametrize
    def test_method_list_available_with_all_params(self, client: Roark) -> None:
        phone_number = client.phone_number.list_available(
            area_code="415",
            contains="555",
            country="US",
            limit=1,
            number_type="LOCAL",
        )
        assert_matches_type(PhoneNumberListAvailableResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_list_available(self, client: Roark) -> None:
        response = client.phone_number.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberListAvailableResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_list_available(self, client: Roark) -> None:
        with client.phone_number.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberListAvailableResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhoneNumber:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.create()
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auto_pick={"area_code": "415", "contains": "555", "country": "US", "number_type": "LOCAL"},
            country="US",
            e164="+14155550123",
            expect_free=True,
            expect_monthly_rent_micros=2000000,
            name="x",
        )
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.phone_number.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.phone_number.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.phone_number.with_raw_response.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.phone_number.with_streaming_response.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.phone_number.with_raw_response.update(
                phone_number_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.phone_number.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.phone_number.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.phone_number.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.phone_number.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.phone_number.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_allowance(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.get_allowance()
        assert_matches_type(PhoneNumberGetAllowanceResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_get_allowance(self, async_client: AsyncRoark) -> None:
        response = await async_client.phone_number.with_raw_response.get_allowance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberGetAllowanceResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_get_allowance(self, async_client: AsyncRoark) -> None:
        async with async_client.phone_number.with_streaming_response.get_allowance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberGetAllowanceResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_available(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.list_available()
        assert_matches_type(PhoneNumberListAvailableResponse, phone_number, path=["response"])

    @parametrize
    async def test_method_list_available_with_all_params(self, async_client: AsyncRoark) -> None:
        phone_number = await async_client.phone_number.list_available(
            area_code="415",
            contains="555",
            country="US",
            limit=1,
            number_type="LOCAL",
        )
        assert_matches_type(PhoneNumberListAvailableResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_list_available(self, async_client: AsyncRoark) -> None:
        response = await async_client.phone_number.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberListAvailableResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_list_available(self, async_client: AsyncRoark) -> None:
        async with async_client.phone_number.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberListAvailableResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True
