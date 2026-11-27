# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    AgentConnectionListResponse,
    AgentConnectionCreateResponse,
    AgentConnectionDeleteResponse,
    AgentConnectionUpdateResponse,
    AgentConnectionGetByIDResponse,
    AgentConnectionDiscoverResponse,
    AgentConnectionListBackfillsResponse,
    AgentConnectionListProvidersResponse,
    AgentConnectionCancelBackfillResponse,
    AgentConnectionCreateBackfillResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgentConnection:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="RETELL",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="RETELL",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            capabilities=["PULL_AGENTS"],
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            api_key="x",
            name="Production Retell",
            provider="RETELL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            api_key="x",
            name="Production Retell",
            provider="RETELL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="VAPI",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="VAPI",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            capabilities=["PULL_AGENTS"],
            outbound_request_body_template={"foo": "string"},
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            api_key="x",
            name="Production Retell",
            provider="VAPI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            api_key="x",
            name="Production Retell",
            provider="VAPI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="ELEVEN_LABS",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="ELEVEN_LABS",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            capabilities=["PULL_AGENTS"],
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            api_key="x",
            name="Production Retell",
            provider="ELEVEN_LABS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            api_key="x",
            name="Production Retell",
            provider="ELEVEN_LABS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_4(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="BLAND",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="BLAND",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            capabilities=["PULL_AGENTS"],
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            api_key="x",
            name="Production Retell",
            provider="BLAND",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            api_key="x",
            name="Production Retell",
            provider="BLAND",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_5(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            provider="LEAPING",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            provider="LEAPING",
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_5(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            provider="LEAPING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_5(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            provider="LEAPING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_6(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            api_secret="x",
            name="Production Retell",
            provider="LIVEKIT",
            url="wss://acme.livekit.cloud",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            api_secret="x",
            name="Production Retell",
            provider="LIVEKIT",
            url="wss://acme.livekit.cloud",
            agent_names=["x"],
            agent_scope="ALL",
            endpoint={
                "auto_create_room": True,
                "auto_create_room_metadata": {"foo": "string"},
                "environment": "x",
                "room_creation_url": "https://example.com",
            },
            metadata_egress_strategy="EAGER",
            metadata_filtering_enabled=True,
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_6(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            api_key="x",
            api_secret="x",
            name="Production Retell",
            provider="LIVEKIT",
            url="wss://acme.livekit.cloud",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_6(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            api_key="x",
            api_secret="x",
            name="Production Retell",
            provider="LIVEKIT",
            url="wss://acme.livekit.cloud",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_7(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            name="Production Retell",
            provider="LIVEKIT_SELF_HOSTED",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            name="Production Retell",
            provider="LIVEKIT_SELF_HOSTED",
            observer_api_key_name="x",
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_7(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            name="Production Retell",
            provider="LIVEKIT_SELF_HOSTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_7(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            name="Production Retell",
            provider="LIVEKIT_SELF_HOSTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_8(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            name="Production Retell",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            name="Production Retell",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
            append_agent_id=True,
            auth_token="x",
            base_signaling_url="https://bot.example.com/api/offer",
            observer_api_key_name="x",
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_8(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            name="Production Retell",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_8(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            name="Production Retell",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_9(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            name="Production Retell",
            provider="PIPECAT_CLOUD_INTEGRATION",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            name="Production Retell",
            provider="PIPECAT_CLOUD_INTEGRATION",
            observer_api_key_name="x",
            pcc_public_key="x",
            pcc_room_properties={"foo": "string"},
            pcc_start_body={"foo": "string"},
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_9(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            name="Production Retell",
            provider="PIPECAT_CLOUD_INTEGRATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_9(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            name="Production Retell",
            provider="PIPECAT_CLOUD_INTEGRATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_10(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            app_id="x",
            env_name="production",
            name="Production Retell",
            provider="KORE",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            api_key="x",
            app_id="x",
            env_name="production",
            name="Production Retell",
            provider="KORE",
            base_url="https://example.com",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_10(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            api_key="x",
            app_id="x",
            env_name="production",
            name="Production Retell",
            provider="KORE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_10(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            api_key="x",
            app_id="x",
            env_name="production",
            name="Production Retell",
            provider="KORE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_11(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            provider="GOOGLE_CES",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
            },
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_11(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create(
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            provider="GOOGLE_CES",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
                "universe_domain": "universe_domain",
            },
            version_id="x",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_overload_11(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create(
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            provider="GOOGLE_CES",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_11(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create(
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            provider="GOOGLE_CES",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_1(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="RETELL",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="RETELL",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            capabilities=["PULL_AGENTS"],
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="RETELL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="RETELL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.agent_connection.with_raw_response.update(
                connection_id="",
                provider="RETELL",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="VAPI",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="VAPI",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            capabilities=["PULL_AGENTS"],
            name="Production Retell",
            outbound_request_body_template={"foo": "string"},
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="VAPI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="VAPI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_3(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="ELEVEN_LABS",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="ELEVEN_LABS",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            capabilities=["PULL_AGENTS"],
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="ELEVEN_LABS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="ELEVEN_LABS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_4(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="BLAND",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="BLAND",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            capabilities=["PULL_AGENTS"],
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_4(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="BLAND",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_4(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="BLAND",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_5(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LEAPING",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LEAPING",
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_5(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LEAPING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_5(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LEAPING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_6(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT",
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            api_secret="x",
            metadata_egress_strategy="EAGER",
            metadata_filtering_enabled=True,
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
            url="wss://acme.livekit.cloud",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_6(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_6(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_7(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT_SELF_HOSTED",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT_SELF_HOSTED",
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_7(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT_SELF_HOSTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_7(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT_SELF_HOSTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_8(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
            append_agent_id=True,
            auth_token="x",
            base_signaling_url="https://bot.example.com/api/offer",
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_8(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_8(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_9(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_CLOUD_INTEGRATION",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_9(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_CLOUD_INTEGRATION",
            name="Production Retell",
            pcc_public_key="x",
            pcc_room_properties={"foo": "string"},
            pcc_start_body={"foo": "string"},
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_9(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_CLOUD_INTEGRATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_9(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_CLOUD_INTEGRATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_10(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="KORE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_10(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="KORE",
            api_key="x",
            app_id="x",
            base_url="https://example.com",
            env_name="production",
            name="Production Retell",
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_10(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="KORE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_10(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="KORE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_11(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="GOOGLE_CES",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_11(self, client: Roark) -> None:
        agent_connection = client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="GOOGLE_CES",
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            status="ACTIVE",
            version_id="x",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
                "universe_domain": "universe_domain",
            },
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_update_overload_11(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="GOOGLE_CES",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_11(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="GOOGLE_CES",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        agent_connection = client.agent_connection.list()
        assert_matches_type(AgentConnectionListResponse, agent_connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        agent_connection = client.agent_connection.list(
            provider="RETELL",
        )
        assert_matches_type(AgentConnectionListResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionListResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionListResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        agent_connection = client.agent_connection.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentConnectionDeleteResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionDeleteResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionDeleteResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.agent_connection.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_cancel_backfill(self, client: Roark) -> None:
        agent_connection = client.agent_connection.cancel_backfill(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentConnectionCancelBackfillResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_cancel_backfill(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.cancel_backfill(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCancelBackfillResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_cancel_backfill(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.cancel_backfill(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCancelBackfillResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel_backfill(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `backfill_id` but received ''"):
            client.agent_connection.with_raw_response.cancel_backfill(
                "",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.agent_connection.with_raw_response.cancel_backfill(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
            )

    @parametrize
    def test_method_create_backfill(self, client: Roark) -> None:
        agent_connection = client.agent_connection.create_backfill(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_calls=250,
        )
        assert_matches_type(AgentConnectionCreateBackfillResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_create_backfill(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.create_backfill(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_calls=250,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionCreateBackfillResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_backfill(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.create_backfill(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_calls=250,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionCreateBackfillResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_backfill(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.agent_connection.with_raw_response.create_backfill(
                connection_id="",
                max_calls=250,
            )

    @parametrize
    def test_method_discover(self, client: Roark) -> None:
        agent_connection = client.agent_connection.discover(
            api_key="x",
            provider="RETELL",
        )
        assert_matches_type(AgentConnectionDiscoverResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_discover(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.discover(
            api_key="x",
            provider="RETELL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionDiscoverResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_discover(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.discover(
            api_key="x",
            provider="RETELL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionDiscoverResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        agent_connection = client.agent_connection.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentConnectionGetByIDResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionGetByIDResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionGetByIDResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.agent_connection.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_list_backfills(self, client: Roark) -> None:
        agent_connection = client.agent_connection.list_backfills(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentConnectionListBackfillsResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_list_backfills(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.list_backfills(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionListBackfillsResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_list_backfills(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.list_backfills(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionListBackfillsResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_backfills(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.agent_connection.with_raw_response.list_backfills(
                "",
            )

    @parametrize
    def test_method_list_providers(self, client: Roark) -> None:
        agent_connection = client.agent_connection.list_providers()
        assert_matches_type(AgentConnectionListProvidersResponse, agent_connection, path=["response"])

    @parametrize
    def test_raw_response_list_providers(self, client: Roark) -> None:
        response = client.agent_connection.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = response.parse()
        assert_matches_type(AgentConnectionListProvidersResponse, agent_connection, path=["response"])

    @parametrize
    def test_streaming_response_list_providers(self, client: Roark) -> None:
        with client.agent_connection.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = response.parse()
            assert_matches_type(AgentConnectionListProvidersResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgentConnection:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="RETELL",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="RETELL",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            capabilities=["PULL_AGENTS"],
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            api_key="x",
            name="Production Retell",
            provider="RETELL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            api_key="x",
            name="Production Retell",
            provider="RETELL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="VAPI",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="VAPI",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            capabilities=["PULL_AGENTS"],
            outbound_request_body_template={"foo": "string"},
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            api_key="x",
            name="Production Retell",
            provider="VAPI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            api_key="x",
            name="Production Retell",
            provider="VAPI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="ELEVEN_LABS",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="ELEVEN_LABS",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            capabilities=["PULL_AGENTS"],
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            api_key="x",
            name="Production Retell",
            provider="ELEVEN_LABS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            api_key="x",
            name="Production Retell",
            provider="ELEVEN_LABS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="BLAND",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            name="Production Retell",
            provider="BLAND",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            capabilities=["PULL_AGENTS"],
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            api_key="x",
            name="Production Retell",
            provider="BLAND",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            api_key="x",
            name="Production Retell",
            provider="BLAND",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            provider="LEAPING",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            provider="LEAPING",
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            provider="LEAPING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            provider="LEAPING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            api_secret="x",
            name="Production Retell",
            provider="LIVEKIT",
            url="wss://acme.livekit.cloud",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            api_secret="x",
            name="Production Retell",
            provider="LIVEKIT",
            url="wss://acme.livekit.cloud",
            agent_names=["x"],
            agent_scope="ALL",
            endpoint={
                "auto_create_room": True,
                "auto_create_room_metadata": {"foo": "string"},
                "environment": "x",
                "room_creation_url": "https://example.com",
            },
            metadata_egress_strategy="EAGER",
            metadata_filtering_enabled=True,
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            api_key="x",
            api_secret="x",
            name="Production Retell",
            provider="LIVEKIT",
            url="wss://acme.livekit.cloud",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            api_key="x",
            api_secret="x",
            name="Production Retell",
            provider="LIVEKIT",
            url="wss://acme.livekit.cloud",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            name="Production Retell",
            provider="LIVEKIT_SELF_HOSTED",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            name="Production Retell",
            provider="LIVEKIT_SELF_HOSTED",
            observer_api_key_name="x",
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            name="Production Retell",
            provider="LIVEKIT_SELF_HOSTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            name="Production Retell",
            provider="LIVEKIT_SELF_HOSTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            name="Production Retell",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            name="Production Retell",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
            append_agent_id=True,
            auth_token="x",
            base_signaling_url="https://bot.example.com/api/offer",
            observer_api_key_name="x",
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            name="Production Retell",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            name="Production Retell",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            name="Production Retell",
            provider="PIPECAT_CLOUD_INTEGRATION",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            name="Production Retell",
            provider="PIPECAT_CLOUD_INTEGRATION",
            observer_api_key_name="x",
            pcc_public_key="x",
            pcc_room_properties={"foo": "string"},
            pcc_start_body={"foo": "string"},
            sampling_rate=1,
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            name="Production Retell",
            provider="PIPECAT_CLOUD_INTEGRATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_9(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            name="Production Retell",
            provider="PIPECAT_CLOUD_INTEGRATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            app_id="x",
            env_name="production",
            name="Production Retell",
            provider="KORE",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_10(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            api_key="x",
            app_id="x",
            env_name="production",
            name="Production Retell",
            provider="KORE",
            base_url="https://example.com",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            api_key="x",
            app_id="x",
            env_name="production",
            name="Production Retell",
            provider="KORE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_10(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            api_key="x",
            app_id="x",
            env_name="production",
            name="Production Retell",
            provider="KORE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_11(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            provider="GOOGLE_CES",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
            },
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_11(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create(
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            provider="GOOGLE_CES",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
                "universe_domain": "universe_domain",
            },
            version_id="x",
        )
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_11(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create(
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            provider="GOOGLE_CES",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_11(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create(
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            provider="GOOGLE_CES",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="RETELL",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="RETELL",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            capabilities=["PULL_AGENTS"],
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="RETELL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="RETELL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.agent_connection.with_raw_response.update(
                connection_id="",
                provider="RETELL",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="VAPI",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="VAPI",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            capabilities=["PULL_AGENTS"],
            name="Production Retell",
            outbound_request_body_template={"foo": "string"},
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="VAPI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="VAPI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="ELEVEN_LABS",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="ELEVEN_LABS",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            capabilities=["PULL_AGENTS"],
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="ELEVEN_LABS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="ELEVEN_LABS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="BLAND",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="BLAND",
            agent_ids=["x"],
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            capabilities=["PULL_AGENTS"],
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="BLAND",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="BLAND",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LEAPING",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LEAPING",
            agent_ids=["x"],
            api_key="x",
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LEAPING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LEAPING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT",
            agent_names=["x"],
            agent_scope="ALL",
            api_key="x",
            api_secret="x",
            metadata_egress_strategy="EAGER",
            metadata_filtering_enabled=True,
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
            url="wss://acme.livekit.cloud",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT_SELF_HOSTED",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT_SELF_HOSTED",
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT_SELF_HOSTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="LIVEKIT_SELF_HOSTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
            append_agent_id=True,
            auth_token="x",
            base_signaling_url="https://bot.example.com/api/offer",
            name="Production Retell",
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_SELF_HOSTED_INTEGRATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_9(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_CLOUD_INTEGRATION",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_9(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_CLOUD_INTEGRATION",
            name="Production Retell",
            pcc_public_key="x",
            pcc_room_properties={"foo": "string"},
            pcc_start_body={"foo": "string"},
            sampling_rate=1,
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_9(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_CLOUD_INTEGRATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_9(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="PIPECAT_CLOUD_INTEGRATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_10(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="KORE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_10(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="KORE",
            api_key="x",
            app_id="x",
            base_url="https://example.com",
            env_name="production",
            name="Production Retell",
            status="ACTIVE",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_10(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="KORE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_10(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="KORE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_11(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="GOOGLE_CES",
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_11(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="GOOGLE_CES",
            app_id="x",
            deployment_id="x",
            location="us",
            name="Production Retell",
            status="ACTIVE",
            version_id="x",
            wif_config={
                "audience": "audience",
                "credential_source": {
                    "environment_id": "environment_id",
                    "region_url": "region_url",
                    "regional_cred_verification_url": "regional_cred_verification_url",
                    "url": "url",
                },
                "service_account_impersonation_url": "service_account_impersonation_url",
                "subject_token_type": "subject_token_type",
                "token_url": "token_url",
                "type": "external_account",
                "universe_domain": "universe_domain",
            },
        )
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_11(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="GOOGLE_CES",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_11(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.update(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="GOOGLE_CES",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionUpdateResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.list()
        assert_matches_type(AgentConnectionListResponse, agent_connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.list(
            provider="RETELL",
        )
        assert_matches_type(AgentConnectionListResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionListResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionListResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentConnectionDeleteResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionDeleteResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionDeleteResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.agent_connection.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_cancel_backfill(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.cancel_backfill(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentConnectionCancelBackfillResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_cancel_backfill(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.cancel_backfill(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCancelBackfillResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_cancel_backfill(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.cancel_backfill(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCancelBackfillResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel_backfill(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `backfill_id` but received ''"):
            await async_client.agent_connection.with_raw_response.cancel_backfill(
                "",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.agent_connection.with_raw_response.cancel_backfill(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
            )

    @parametrize
    async def test_method_create_backfill(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.create_backfill(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_calls=250,
        )
        assert_matches_type(AgentConnectionCreateBackfillResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_backfill(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.create_backfill(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_calls=250,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionCreateBackfillResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_backfill(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.create_backfill(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_calls=250,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionCreateBackfillResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_backfill(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.agent_connection.with_raw_response.create_backfill(
                connection_id="",
                max_calls=250,
            )

    @parametrize
    async def test_method_discover(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.discover(
            api_key="x",
            provider="RETELL",
        )
        assert_matches_type(AgentConnectionDiscoverResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_discover(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.discover(
            api_key="x",
            provider="RETELL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionDiscoverResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_discover(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.discover(
            api_key="x",
            provider="RETELL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionDiscoverResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentConnectionGetByIDResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionGetByIDResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionGetByIDResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.agent_connection.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_list_backfills(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.list_backfills(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentConnectionListBackfillsResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_list_backfills(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.list_backfills(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionListBackfillsResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list_backfills(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.list_backfills(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionListBackfillsResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_backfills(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.agent_connection.with_raw_response.list_backfills(
                "",
            )

    @parametrize
    async def test_method_list_providers(self, async_client: AsyncRoark) -> None:
        agent_connection = await async_client.agent_connection.list_providers()
        assert_matches_type(AgentConnectionListProvidersResponse, agent_connection, path=["response"])

    @parametrize
    async def test_raw_response_list_providers(self, async_client: AsyncRoark) -> None:
        response = await async_client.agent_connection.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_connection = await response.parse()
        assert_matches_type(AgentConnectionListProvidersResponse, agent_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list_providers(self, async_client: AsyncRoark) -> None:
        async with async_client.agent_connection.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_connection = await response.parse()
            assert_matches_type(AgentConnectionListProvidersResponse, agent_connection, path=["response"])

        assert cast(Any, response.is_closed) is True
