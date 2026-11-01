# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    AgentDraftGetResponse,
    AgentDraftCreateResponse,
    AgentDraftDeleteResponse,
    AgentDraftUpdateResponse,
    AgentDraftPublishResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgentDraft:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        agent_draft = client.agent_draft.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentDraftCreateResponse, agent_draft, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        agent_draft = client.agent_draft.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentDraftCreateResponse, agent_draft, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.agent_draft.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = response.parse()
        assert_matches_type(AgentDraftCreateResponse, agent_draft, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.agent_draft.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = response.parse()
            assert_matches_type(AgentDraftCreateResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent_draft.with_raw_response.create(
                agent_id="",
            )

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        agent_draft = client.agent_draft.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settings={},
        )
        assert_matches_type(AgentDraftUpdateResponse, agent_draft, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        agent_draft = client.agent_draft.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settings={
                "background_noise": "NONE",
                "background_noise_url": "https://example.com",
                "background_noise_volume": 0,
                "call_max_duration_seconds": 30,
                "call_silence_timeout_seconds": 5,
                "chat_inactivity_timeout_seconds": 60,
                "chat_max_duration_seconds": 30,
                "end_call_goodbye_message": "x",
                "end_detection_phrases": ["x"],
                "end_detection_reasons": ["x"],
                "first_message": "x",
                "first_message_audio_url": "https://example.com",
                "first_message_mode": "SPEAK_TEXT",
                "idle_max_count": 1,
                "idle_messages": ["x"],
                "idle_timeout_seconds": 1,
                "interruption_mode": "ALLOW",
                "language": "xx",
                "modalities": ["call"],
                "sub_agents": [
                    {
                        "handoffs": [
                            {"description": "x", "history": "SHARED", "note": "x", "once": True, "to": "main"}
                        ],
                        "is_initial": True,
                        "key": "main",
                        "model_configs": [
                            {
                                "llm": [{"model": "x", "provider": "OPENAI", "max_tokens": 1, "temperature": 0}],
                                "stt": [
                                    {
                                        "model": "x",
                                        "provider": "DEEPGRAM",
                                        "endpointing_ms": 10,
                                        "keyterms": ["x"],
                                        "smart_format": True,
                                        "turn_detection": "pipeline",
                                    }
                                ],
                                "tts": [
                                    {
                                        "model": "x",
                                        "provider": "CARTESIA",
                                        "voice_id": "x",
                                        "similarity_boost": 0,
                                        "speed": 0.5,
                                        "stability": 0,
                                    }
                                ],
                                "type": "CASCADE",
                            }
                        ],
                        "name": "x",
                        "system_prompt": "x",
                        "tools": [{"pinned_version": 1, "tool_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                    }
                ],
                "vad_start_secs": 0,
                "vad_stop_secs": 0,
            },
            expected_revision=1,
        )
        assert_matches_type(AgentDraftUpdateResponse, agent_draft, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.agent_draft.with_raw_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settings={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = response.parse()
        assert_matches_type(AgentDraftUpdateResponse, agent_draft, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.agent_draft.with_streaming_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settings={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = response.parse()
            assert_matches_type(AgentDraftUpdateResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent_draft.with_raw_response.update(
                agent_id="",
                settings={},
            )

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        agent_draft = client.agent_draft.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentDraftDeleteResponse, agent_draft, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.agent_draft.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = response.parse()
        assert_matches_type(AgentDraftDeleteResponse, agent_draft, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.agent_draft.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = response.parse()
            assert_matches_type(AgentDraftDeleteResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent_draft.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Roark) -> None:
        agent_draft = client.agent_draft.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentDraftGetResponse, agent_draft, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Roark) -> None:
        response = client.agent_draft.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = response.parse()
        assert_matches_type(AgentDraftGetResponse, agent_draft, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Roark) -> None:
        with client.agent_draft.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = response.parse()
            assert_matches_type(AgentDraftGetResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent_draft.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_publish(self, client: Roark) -> None:
        agent_draft = client.agent_draft.publish(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_revision=1,
        )
        assert_matches_type(AgentDraftPublishResponse, agent_draft, path=["response"])

    @parametrize
    def test_method_publish_with_all_params(self, client: Roark) -> None:
        agent_draft = client.agent_draft.publish(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_revision=1,
            summary="x",
        )
        assert_matches_type(AgentDraftPublishResponse, agent_draft, path=["response"])

    @parametrize
    def test_raw_response_publish(self, client: Roark) -> None:
        response = client.agent_draft.with_raw_response.publish(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_revision=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = response.parse()
        assert_matches_type(AgentDraftPublishResponse, agent_draft, path=["response"])

    @parametrize
    def test_streaming_response_publish(self, client: Roark) -> None:
        with client.agent_draft.with_streaming_response.publish(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_revision=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = response.parse()
            assert_matches_type(AgentDraftPublishResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_publish(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent_draft.with_raw_response.publish(
                agent_id="",
                expected_revision=1,
            )


class TestAsyncAgentDraft:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        agent_draft = await async_client.agent_draft.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentDraftCreateResponse, agent_draft, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_draft = await async_client.agent_draft.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentDraftCreateResponse, agent_draft, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_draft.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = await response.parse()
        assert_matches_type(AgentDraftCreateResponse, agent_draft, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_draft.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = await response.parse()
            assert_matches_type(AgentDraftCreateResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent_draft.with_raw_response.create(
                agent_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        agent_draft = await async_client.agent_draft.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settings={},
        )
        assert_matches_type(AgentDraftUpdateResponse, agent_draft, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_draft = await async_client.agent_draft.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settings={
                "background_noise": "NONE",
                "background_noise_url": "https://example.com",
                "background_noise_volume": 0,
                "call_max_duration_seconds": 30,
                "call_silence_timeout_seconds": 5,
                "chat_inactivity_timeout_seconds": 60,
                "chat_max_duration_seconds": 30,
                "end_call_goodbye_message": "x",
                "end_detection_phrases": ["x"],
                "end_detection_reasons": ["x"],
                "first_message": "x",
                "first_message_audio_url": "https://example.com",
                "first_message_mode": "SPEAK_TEXT",
                "idle_max_count": 1,
                "idle_messages": ["x"],
                "idle_timeout_seconds": 1,
                "interruption_mode": "ALLOW",
                "language": "xx",
                "modalities": ["call"],
                "sub_agents": [
                    {
                        "handoffs": [
                            {"description": "x", "history": "SHARED", "note": "x", "once": True, "to": "main"}
                        ],
                        "is_initial": True,
                        "key": "main",
                        "model_configs": [
                            {
                                "llm": [{"model": "x", "provider": "OPENAI", "max_tokens": 1, "temperature": 0}],
                                "stt": [
                                    {
                                        "model": "x",
                                        "provider": "DEEPGRAM",
                                        "endpointing_ms": 10,
                                        "keyterms": ["x"],
                                        "smart_format": True,
                                        "turn_detection": "pipeline",
                                    }
                                ],
                                "tts": [
                                    {
                                        "model": "x",
                                        "provider": "CARTESIA",
                                        "voice_id": "x",
                                        "similarity_boost": 0,
                                        "speed": 0.5,
                                        "stability": 0,
                                    }
                                ],
                                "type": "CASCADE",
                            }
                        ],
                        "name": "x",
                        "system_prompt": "x",
                        "tools": [{"pinned_version": 1, "tool_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                    }
                ],
                "vad_start_secs": 0,
                "vad_stop_secs": 0,
            },
            expected_revision=1,
        )
        assert_matches_type(AgentDraftUpdateResponse, agent_draft, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_draft.with_raw_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settings={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = await response.parse()
        assert_matches_type(AgentDraftUpdateResponse, agent_draft, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_draft.with_streaming_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settings={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = await response.parse()
            assert_matches_type(AgentDraftUpdateResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent_draft.with_raw_response.update(
                agent_id="",
                settings={},
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        agent_draft = await async_client.agent_draft.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentDraftDeleteResponse, agent_draft, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_draft.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = await response.parse()
        assert_matches_type(AgentDraftDeleteResponse, agent_draft, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_draft.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = await response.parse()
            assert_matches_type(AgentDraftDeleteResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent_draft.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncRoark) -> None:
        agent_draft = await async_client.agent_draft.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentDraftGetResponse, agent_draft, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_draft.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = await response.parse()
        assert_matches_type(AgentDraftGetResponse, agent_draft, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_draft.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = await response.parse()
            assert_matches_type(AgentDraftGetResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent_draft.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_publish(self, async_client: AsyncRoark) -> None:
        agent_draft = await async_client.agent_draft.publish(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_revision=1,
        )
        assert_matches_type(AgentDraftPublishResponse, agent_draft, path=["response"])

    @parametrize
    async def test_method_publish_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_draft = await async_client.agent_draft.publish(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_revision=1,
            summary="x",
        )
        assert_matches_type(AgentDraftPublishResponse, agent_draft, path=["response"])

    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_draft.with_raw_response.publish(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_revision=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_draft = await response.parse()
        assert_matches_type(AgentDraftPublishResponse, agent_draft, path=["response"])

    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_draft.with_streaming_response.publish(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expected_revision=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_draft = await response.parse()
            assert_matches_type(AgentDraftPublishResponse, agent_draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_publish(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent_draft.with_raw_response.publish(
                agent_id="",
                expected_revision=1,
            )
