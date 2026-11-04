# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    CalendarConnectionListResponse,
    CalendarConnectionCheckResponse,
    CalendarConnectionCreateResponse,
    CalendarConnectionDeleteResponse,
    CalendarConnectionUpdateResponse,
    CalendarConnectionGetByIDResponse,
    CalendarConnectionGetTargetResponse,
    CalendarConnectionListTargetsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalendarConnection:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.create(
            api_key="x",
            label="x",
            provider="CAL_COM",
        )
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.create(
            api_key="x",
            label="x",
            provider="CAL_COM",
            timezone="x",
        )
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.calendar_connection.with_raw_response.create(
            api_key="x",
            label="x",
            provider="CAL_COM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.calendar_connection.with_streaming_response.create(
            api_key="x",
            label="x",
            provider="CAL_COM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.update(
            connection_id="connectionId",
        )
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.update(
            connection_id="connectionId",
            api_key="x",
            label="x",
            timezone="x",
        )
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.calendar_connection.with_raw_response.update(
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.calendar_connection.with_streaming_response.update(
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.calendar_connection.with_raw_response.update(
                connection_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.list()
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.list(
            provider="CAL_COM",
        )
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.calendar_connection.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.calendar_connection.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.delete(
            "connectionId",
        )
        assert_matches_type(CalendarConnectionDeleteResponse, calendar_connection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.calendar_connection.with_raw_response.delete(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionDeleteResponse, calendar_connection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.calendar_connection.with_streaming_response.delete(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionDeleteResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.calendar_connection.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_check(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.check(
            "connectionId",
        )
        assert_matches_type(CalendarConnectionCheckResponse, calendar_connection, path=["response"])

    @parametrize
    def test_raw_response_check(self, client: Roark) -> None:
        response = client.calendar_connection.with_raw_response.check(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionCheckResponse, calendar_connection, path=["response"])

    @parametrize
    def test_streaming_response_check(self, client: Roark) -> None:
        with client.calendar_connection.with_streaming_response.check(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionCheckResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_check(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.calendar_connection.with_raw_response.check(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.get_by_id(
            "connectionId",
        )
        assert_matches_type(CalendarConnectionGetByIDResponse, calendar_connection, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.calendar_connection.with_raw_response.get_by_id(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionGetByIDResponse, calendar_connection, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.calendar_connection.with_streaming_response.get_by_id(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionGetByIDResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.calendar_connection.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_get_target(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.get_target(
            "targetId",
            connection_id="connectionId",
        )
        assert_matches_type(CalendarConnectionGetTargetResponse, calendar_connection, path=["response"])

    @parametrize
    def test_raw_response_get_target(self, client: Roark) -> None:
        response = client.calendar_connection.with_raw_response.get_target(
            "targetId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionGetTargetResponse, calendar_connection, path=["response"])

    @parametrize
    def test_streaming_response_get_target(self, client: Roark) -> None:
        with client.calendar_connection.with_streaming_response.get_target(
            "targetId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionGetTargetResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_target(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            client.calendar_connection.with_raw_response.get_target(
                "",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.calendar_connection.with_raw_response.get_target(
                "targetId",
                connection_id="",
            )

    @parametrize
    def test_method_list_targets(self, client: Roark) -> None:
        calendar_connection = client.calendar_connection.list_targets(
            "connectionId",
        )
        assert_matches_type(CalendarConnectionListTargetsResponse, calendar_connection, path=["response"])

    @parametrize
    def test_raw_response_list_targets(self, client: Roark) -> None:
        response = client.calendar_connection.with_raw_response.list_targets(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionListTargetsResponse, calendar_connection, path=["response"])

    @parametrize
    def test_streaming_response_list_targets(self, client: Roark) -> None:
        with client.calendar_connection.with_streaming_response.list_targets(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionListTargetsResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_targets(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.calendar_connection.with_raw_response.list_targets(
                "",
            )


class TestAsyncCalendarConnection:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.create(
            api_key="x",
            label="x",
            provider="CAL_COM",
        )
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.create(
            api_key="x",
            label="x",
            provider="CAL_COM",
            timezone="x",
        )
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.calendar_connection.with_raw_response.create(
            api_key="x",
            label="x",
            provider="CAL_COM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.calendar_connection.with_streaming_response.create(
            api_key="x",
            label="x",
            provider="CAL_COM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.update(
            connection_id="connectionId",
        )
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.update(
            connection_id="connectionId",
            api_key="x",
            label="x",
            timezone="x",
        )
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.calendar_connection.with_raw_response.update(
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.calendar_connection.with_streaming_response.update(
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.calendar_connection.with_raw_response.update(
                connection_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.list()
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.list(
            provider="CAL_COM",
        )
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.calendar_connection.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.calendar_connection.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.delete(
            "connectionId",
        )
        assert_matches_type(CalendarConnectionDeleteResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.calendar_connection.with_raw_response.delete(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionDeleteResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.calendar_connection.with_streaming_response.delete(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionDeleteResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.calendar_connection.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_check(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.check(
            "connectionId",
        )
        assert_matches_type(CalendarConnectionCheckResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_raw_response_check(self, async_client: AsyncRoark) -> None:
        response = await async_client.calendar_connection.with_raw_response.check(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionCheckResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncRoark) -> None:
        async with async_client.calendar_connection.with_streaming_response.check(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionCheckResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_check(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.calendar_connection.with_raw_response.check(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.get_by_id(
            "connectionId",
        )
        assert_matches_type(CalendarConnectionGetByIDResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.calendar_connection.with_raw_response.get_by_id(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionGetByIDResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.calendar_connection.with_streaming_response.get_by_id(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionGetByIDResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.calendar_connection.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_get_target(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.get_target(
            "targetId",
            connection_id="connectionId",
        )
        assert_matches_type(CalendarConnectionGetTargetResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_raw_response_get_target(self, async_client: AsyncRoark) -> None:
        response = await async_client.calendar_connection.with_raw_response.get_target(
            "targetId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionGetTargetResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_streaming_response_get_target(self, async_client: AsyncRoark) -> None:
        async with async_client.calendar_connection.with_streaming_response.get_target(
            "targetId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionGetTargetResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_target(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            await async_client.calendar_connection.with_raw_response.get_target(
                "",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.calendar_connection.with_raw_response.get_target(
                "targetId",
                connection_id="",
            )

    @parametrize
    async def test_method_list_targets(self, async_client: AsyncRoark) -> None:
        calendar_connection = await async_client.calendar_connection.list_targets(
            "connectionId",
        )
        assert_matches_type(CalendarConnectionListTargetsResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_raw_response_list_targets(self, async_client: AsyncRoark) -> None:
        response = await async_client.calendar_connection.with_raw_response.list_targets(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionListTargetsResponse, calendar_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list_targets(self, async_client: AsyncRoark) -> None:
        async with async_client.calendar_connection.with_streaming_response.list_targets(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionListTargetsResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_targets(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.calendar_connection.with_raw_response.list_targets(
                "",
            )
