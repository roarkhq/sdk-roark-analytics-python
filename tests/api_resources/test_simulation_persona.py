# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationPersonaListResponse,
    SimulationPersonaCreateResponse,
    SimulationPersonaUpdateResponse,
    SimulationPersonaGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationPersona:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        simulation_persona = client.simulation_persona.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        )
        assert_matches_type(SimulationPersonaCreateResponse, simulation_persona, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        simulation_persona = client.simulation_persona.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
            background_noise="NONE",
            backstory_prompt="A busy professional calling during lunch break",
            base_emotion="NEUTRAL",
            confirmation_style="EXPLICIT",
            description="description",
            has_disfluencies=True,
            idle_message_max_spoken_count=1,
            idle_message_reset_count_on_user_speech_enabled=True,
            idle_messages=["string"],
            idle_timeout_seconds=5,
            intent_clarity="CLEAR",
            memory_reliability="HIGH",
            properties={
                "age": "bar",
                "zipCode": "bar",
                "occupation": "bar",
            },
            response_timing="RELAXED",
            secondary_language="EN",
            speech_clarity="CLEAR",
            speech_pace="SLOW",
        )
        assert_matches_type(SimulationPersonaCreateResponse, simulation_persona, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.simulation_persona.with_raw_response.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_persona = response.parse()
        assert_matches_type(SimulationPersonaCreateResponse, simulation_persona, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.simulation_persona.with_streaming_response.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_persona = response.parse()
            assert_matches_type(SimulationPersonaCreateResponse, simulation_persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        simulation_persona = client.simulation_persona.update(
            persona_id="personaId",
        )
        assert_matches_type(SimulationPersonaUpdateResponse, simulation_persona, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        simulation_persona = client.simulation_persona.update(
            persona_id="personaId",
            accent="US",
            background_noise="NONE",
            backstory_prompt="A busy professional calling during lunch break",
            base_emotion="NEUTRAL",
            confirmation_style="EXPLICIT",
            description="description",
            gender="MALE",
            has_disfluencies=True,
            idle_message_max_spoken_count=1,
            idle_message_reset_count_on_user_speech_enabled=True,
            idle_messages=["string"],
            idle_timeout_seconds=5,
            intent_clarity="CLEAR",
            language="EN",
            memory_reliability="HIGH",
            name="name",
            properties={
                "age": "bar",
                "zipCode": "bar",
                "occupation": "bar",
            },
            response_timing="RELAXED",
            secondary_language="EN",
            speech_clarity="CLEAR",
            speech_pace="SLOW",
        )
        assert_matches_type(SimulationPersonaUpdateResponse, simulation_persona, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.simulation_persona.with_raw_response.update(
            persona_id="personaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_persona = response.parse()
        assert_matches_type(SimulationPersonaUpdateResponse, simulation_persona, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.simulation_persona.with_streaming_response.update(
            persona_id="personaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_persona = response.parse()
            assert_matches_type(SimulationPersonaUpdateResponse, simulation_persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `persona_id` but received ''"):
            client.simulation_persona.with_raw_response.update(
                persona_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        simulation_persona = client.simulation_persona.list()
        assert_matches_type(SimulationPersonaListResponse, simulation_persona, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        simulation_persona = client.simulation_persona.list(
            after="after",
            limit=1,
            search_text="searchText",
        )
        assert_matches_type(SimulationPersonaListResponse, simulation_persona, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.simulation_persona.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_persona = response.parse()
        assert_matches_type(SimulationPersonaListResponse, simulation_persona, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.simulation_persona.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_persona = response.parse()
            assert_matches_type(SimulationPersonaListResponse, simulation_persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        simulation_persona = client.simulation_persona.get_by_id(
            "personaId",
        )
        assert_matches_type(SimulationPersonaGetByIDResponse, simulation_persona, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.simulation_persona.with_raw_response.get_by_id(
            "personaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_persona = response.parse()
        assert_matches_type(SimulationPersonaGetByIDResponse, simulation_persona, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.simulation_persona.with_streaming_response.get_by_id(
            "personaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_persona = response.parse()
            assert_matches_type(SimulationPersonaGetByIDResponse, simulation_persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `persona_id` but received ''"):
            client.simulation_persona.with_raw_response.get_by_id(
                "",
            )


class TestAsyncSimulationPersona:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        simulation_persona = await async_client.simulation_persona.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        )
        assert_matches_type(SimulationPersonaCreateResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_persona = await async_client.simulation_persona.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
            background_noise="NONE",
            backstory_prompt="A busy professional calling during lunch break",
            base_emotion="NEUTRAL",
            confirmation_style="EXPLICIT",
            description="description",
            has_disfluencies=True,
            idle_message_max_spoken_count=1,
            idle_message_reset_count_on_user_speech_enabled=True,
            idle_messages=["string"],
            idle_timeout_seconds=5,
            intent_clarity="CLEAR",
            memory_reliability="HIGH",
            properties={
                "age": "bar",
                "zipCode": "bar",
                "occupation": "bar",
            },
            response_timing="RELAXED",
            secondary_language="EN",
            speech_clarity="CLEAR",
            speech_pace="SLOW",
        )
        assert_matches_type(SimulationPersonaCreateResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_persona.with_raw_response.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_persona = await response.parse()
        assert_matches_type(SimulationPersonaCreateResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_persona.with_streaming_response.create(
            accent="US",
            gender="MALE",
            language="EN",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_persona = await response.parse()
            assert_matches_type(SimulationPersonaCreateResponse, simulation_persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        simulation_persona = await async_client.simulation_persona.update(
            persona_id="personaId",
        )
        assert_matches_type(SimulationPersonaUpdateResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_persona = await async_client.simulation_persona.update(
            persona_id="personaId",
            accent="US",
            background_noise="NONE",
            backstory_prompt="A busy professional calling during lunch break",
            base_emotion="NEUTRAL",
            confirmation_style="EXPLICIT",
            description="description",
            gender="MALE",
            has_disfluencies=True,
            idle_message_max_spoken_count=1,
            idle_message_reset_count_on_user_speech_enabled=True,
            idle_messages=["string"],
            idle_timeout_seconds=5,
            intent_clarity="CLEAR",
            language="EN",
            memory_reliability="HIGH",
            name="name",
            properties={
                "age": "bar",
                "zipCode": "bar",
                "occupation": "bar",
            },
            response_timing="RELAXED",
            secondary_language="EN",
            speech_clarity="CLEAR",
            speech_pace="SLOW",
        )
        assert_matches_type(SimulationPersonaUpdateResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_persona.with_raw_response.update(
            persona_id="personaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_persona = await response.parse()
        assert_matches_type(SimulationPersonaUpdateResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_persona.with_streaming_response.update(
            persona_id="personaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_persona = await response.parse()
            assert_matches_type(SimulationPersonaUpdateResponse, simulation_persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `persona_id` but received ''"):
            await async_client.simulation_persona.with_raw_response.update(
                persona_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        simulation_persona = await async_client.simulation_persona.list()
        assert_matches_type(SimulationPersonaListResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_persona = await async_client.simulation_persona.list(
            after="after",
            limit=1,
            search_text="searchText",
        )
        assert_matches_type(SimulationPersonaListResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_persona.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_persona = await response.parse()
        assert_matches_type(SimulationPersonaListResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_persona.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_persona = await response.parse()
            assert_matches_type(SimulationPersonaListResponse, simulation_persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        simulation_persona = await async_client.simulation_persona.get_by_id(
            "personaId",
        )
        assert_matches_type(SimulationPersonaGetByIDResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_persona.with_raw_response.get_by_id(
            "personaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_persona = await response.parse()
        assert_matches_type(SimulationPersonaGetByIDResponse, simulation_persona, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_persona.with_streaming_response.get_by_id(
            "personaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_persona = await response.parse()
            assert_matches_type(SimulationPersonaGetByIDResponse, simulation_persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `persona_id` but received ''"):
            await async_client.simulation_persona.with_raw_response.get_by_id(
                "",
            )
