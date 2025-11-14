# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    PersonaCreateResponse,
    PersonaUpdateResponse,
    PersonaFindAllResponse,
    PersonaGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPersona:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        persona = client.persona.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        )
        assert_matches_type(PersonaCreateResponse, persona, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        persona = client.persona.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
            background_noise="NONE",
            backstory_prompt="A busy professional calling during lunch break",
            base_emotion="NEUTRAL",
            confirmation_style="EXPLICIT",
            has_disfluencies=True,
            intent_clarity="CLEAR",
            memory_reliability="HIGH",
            properties={
                "age": "bar",
                "zipCode": "bar",
                "occupation": "bar",
            },
            # TODO: Uncomment when Prism correctly handles null values for nullable enums
            # secondary_language=None,
        )
        assert_matches_type(PersonaCreateResponse, persona, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.persona.with_raw_response.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = response.parse()
        assert_matches_type(PersonaCreateResponse, persona, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.persona.with_streaming_response.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = response.parse()
            assert_matches_type(PersonaCreateResponse, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        persona = client.persona.update(
            persona_id="personaId",
        )
        assert_matches_type(PersonaUpdateResponse, persona, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        persona = client.persona.update(
            persona_id="personaId",
            accent="US",
            background_noise="NONE",
            backstory_prompt="A busy professional calling during lunch break",
            base_emotion="NEUTRAL",
            confirmation_style="EXPLICIT",
            gender="MALE",
            has_disfluencies=True,
            intent_clarity="CLEAR",
            language="EN",
            memory_reliability="HIGH",
            name="name",
            properties={
                "age": "bar",
                "zipCode": "bar",
                "occupation": "bar",
            },
            # TODO: Uncomment when Prism correctly handles null values for nullable enums
            # secondary_language=None,
        )
        assert_matches_type(PersonaUpdateResponse, persona, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.persona.with_raw_response.update(
            persona_id="personaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = response.parse()
        assert_matches_type(PersonaUpdateResponse, persona, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.persona.with_streaming_response.update(
            persona_id="personaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = response.parse()
            assert_matches_type(PersonaUpdateResponse, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `persona_id` but received ''"):
            client.persona.with_raw_response.update(
                persona_id="",
            )

    @parametrize
    def test_method_find_all(self, client: Roark) -> None:
        persona = client.persona.find_all()
        assert_matches_type(PersonaFindAllResponse, persona, path=["response"])

    @parametrize
    def test_method_find_all_with_all_params(self, client: Roark) -> None:
        persona = client.persona.find_all(
            after="after",
            limit=1,
            search_text="searchText",
        )
        assert_matches_type(PersonaFindAllResponse, persona, path=["response"])

    @parametrize
    def test_raw_response_find_all(self, client: Roark) -> None:
        response = client.persona.with_raw_response.find_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = response.parse()
        assert_matches_type(PersonaFindAllResponse, persona, path=["response"])

    @parametrize
    def test_streaming_response_find_all(self, client: Roark) -> None:
        with client.persona.with_streaming_response.find_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = response.parse()
            assert_matches_type(PersonaFindAllResponse, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        persona = client.persona.get_by_id(
            "personaId",
        )
        assert_matches_type(PersonaGetByIDResponse, persona, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.persona.with_raw_response.get_by_id(
            "personaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = response.parse()
        assert_matches_type(PersonaGetByIDResponse, persona, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.persona.with_streaming_response.get_by_id(
            "personaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = response.parse()
            assert_matches_type(PersonaGetByIDResponse, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `persona_id` but received ''"):
            client.persona.with_raw_response.get_by_id(
                "",
            )


class TestAsyncPersona:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        persona = await async_client.persona.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        )
        assert_matches_type(PersonaCreateResponse, persona, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        persona = await async_client.persona.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
            background_noise="NONE",
            backstory_prompt="A busy professional calling during lunch break",
            base_emotion="NEUTRAL",
            confirmation_style="EXPLICIT",
            has_disfluencies=True,
            intent_clarity="CLEAR",
            memory_reliability="HIGH",
            properties={
                "age": "bar",
                "zipCode": "bar",
                "occupation": "bar",
            },
            # TODO: Uncomment when Prism correctly handles null values for nullable enums
            # secondary_language=None,
        )
        assert_matches_type(PersonaCreateResponse, persona, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.persona.with_raw_response.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = await response.parse()
        assert_matches_type(PersonaCreateResponse, persona, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.persona.with_streaming_response.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = await response.parse()
            assert_matches_type(PersonaCreateResponse, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        persona = await async_client.persona.update(
            persona_id="personaId",
        )
        assert_matches_type(PersonaUpdateResponse, persona, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        persona = await async_client.persona.update(
            persona_id="personaId",
            accent="US",
            background_noise="NONE",
            backstory_prompt="A busy professional calling during lunch break",
            base_emotion="NEUTRAL",
            confirmation_style="EXPLICIT",
            gender="MALE",
            has_disfluencies=True,
            intent_clarity="CLEAR",
            language="EN",
            memory_reliability="HIGH",
            name="name",
            properties={
                "age": "bar",
                "zipCode": "bar",
                "occupation": "bar",
            },
            # TODO: Uncomment when Prism correctly handles null values for nullable enums
            # secondary_language=None,
        )
        assert_matches_type(PersonaUpdateResponse, persona, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.persona.with_raw_response.update(
            persona_id="personaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = await response.parse()
        assert_matches_type(PersonaUpdateResponse, persona, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.persona.with_streaming_response.update(
            persona_id="personaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = await response.parse()
            assert_matches_type(PersonaUpdateResponse, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `persona_id` but received ''"):
            await async_client.persona.with_raw_response.update(
                persona_id="",
            )

    @parametrize
    async def test_method_find_all(self, async_client: AsyncRoark) -> None:
        persona = await async_client.persona.find_all()
        assert_matches_type(PersonaFindAllResponse, persona, path=["response"])

    @parametrize
    async def test_method_find_all_with_all_params(self, async_client: AsyncRoark) -> None:
        persona = await async_client.persona.find_all(
            after="after",
            limit=1,
            search_text="searchText",
        )
        assert_matches_type(PersonaFindAllResponse, persona, path=["response"])

    @parametrize
    async def test_raw_response_find_all(self, async_client: AsyncRoark) -> None:
        response = await async_client.persona.with_raw_response.find_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = await response.parse()
        assert_matches_type(PersonaFindAllResponse, persona, path=["response"])

    @parametrize
    async def test_streaming_response_find_all(self, async_client: AsyncRoark) -> None:
        async with async_client.persona.with_streaming_response.find_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = await response.parse()
            assert_matches_type(PersonaFindAllResponse, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        persona = await async_client.persona.get_by_id(
            "personaId",
        )
        assert_matches_type(PersonaGetByIDResponse, persona, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.persona.with_raw_response.get_by_id(
            "personaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = await response.parse()
        assert_matches_type(PersonaGetByIDResponse, persona, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.persona.with_streaming_response.get_by_id(
            "personaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = await response.parse()
            assert_matches_type(PersonaGetByIDResponse, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `persona_id` but received ''"):
            await async_client.persona.with_raw_response.get_by_id(
                "",
            )
