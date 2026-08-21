# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    CustomerFlowListResponse,
    CustomerFlowCreateResponse,
    CustomerFlowDeleteResponse,
    CustomerFlowUpdateResponse,
    CustomerFlowGetByIDResponse,
    CustomerFlowReplaceGraphResponse,
    CustomerFlowUpdateHappyPathResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomerFlow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Roark) -> None:
        customer_flow = client.customer_flow.create(
            graph=[{"type": "CUSTOMER_FIRST_MESSAGE"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Roark) -> None:
        customer_flow = client.customer_flow.create(
            graph=[
                {
                    "type": "CUSTOMER_FIRST_MESSAGE",
                    "content": "Hi, I need to move my appointment.",
                    "merge_into_node_ids": ["x"],
                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ref": "x",
                    "steps": [],
                }
            ],
            title="Reschedule an appointment",
            type="SCRIPTED",
            agent_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            branching_mode="DETERMINISTIC",
            description="description",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.create(
            graph=[{"type": "CUSTOMER_FIRST_MESSAGE"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.create(
            graph=[{"type": "CUSTOMER_FIRST_MESSAGE"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Roark) -> None:
        customer_flow = client.customer_flow.create(
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            happy_path={
                "environment_id": "d1f5c19d-0000-4000-8000-000000000001",
                "persona_override_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
                "title": "Asks about a charge",
            },
            title="Billing questions",
            type="IMPROV",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Roark) -> None:
        customer_flow = client.customer_flow.create(
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            happy_path={
                "environment_id": "d1f5c19d-0000-4000-8000-000000000001",
                "persona_override_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
                "title": "Asks about a charge",
                "preceded_by_customer_flow_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "preceded_by_customer_flow_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "prompt": "You want to understand a charge on your latest invoice.",
            },
            title="Billing questions",
            type="IMPROV",
            agent_expectations=[{"prompt": "The agent never states an amount it has not verified"}],
            description="description",
            edge_cases=[
                {
                    "title": "Disputes the charge",
                    "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preceded_by_customer_flow_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preceded_by_customer_flow_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "prompt": "You are certain the charge is wrong.",
                }
            ],
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.create(
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            happy_path={
                "environment_id": "d1f5c19d-0000-4000-8000-000000000001",
                "persona_override_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
                "title": "Asks about a charge",
            },
            title="Billing questions",
            type="IMPROV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.create(
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            happy_path={
                "environment_id": "d1f5c19d-0000-4000-8000-000000000001",
                "persona_override_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
                "title": "Asks about a charge",
            },
            title="Billing questions",
            type="IMPROV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        customer_flow = client.customer_flow.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        customer_flow = client.customer_flow.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            branching_mode="DETERMINISTIC",
            description="description",
            title="x",
        )
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.customer_flow.with_raw_response.update(
                flow_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        customer_flow = client.customer_flow.list()
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        customer_flow = client.customer_flow.list(
            after="after",
            include_system="true",
            limit=1,
            search_text="searchText",
            type="SCRIPTED",
        )
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        customer_flow = client.customer_flow.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowDeleteResponse, customer_flow, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowDeleteResponse, customer_flow, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowDeleteResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.customer_flow.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        customer_flow = client.customer_flow.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.customer_flow.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_replace_graph(self, client: Roark) -> None:
        customer_flow = client.customer_flow.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[{"type": "AGENT_TURN"}],
        )
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @parametrize
    def test_method_replace_graph_with_all_params(self, client: Roark) -> None:
        customer_flow = client.customer_flow.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[
                {
                    "type": "AGENT_TURN",
                    "content": "content",
                    "merge_into_node_ids": ["x"],
                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ref": "x",
                    "steps": [],
                }
            ],
            allow_unmerge=True,
        )
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @parametrize
    def test_raw_response_replace_graph(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[{"type": "AGENT_TURN"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @parametrize
    def test_streaming_response_replace_graph(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[{"type": "AGENT_TURN"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace_graph(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.customer_flow.with_raw_response.replace_graph(
                flow_id="",
                graph=[{"type": "AGENT_TURN"}],
            )

    @parametrize
    def test_method_update_happy_path(self, client: Roark) -> None:
        customer_flow = client.customer_flow.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @parametrize
    def test_method_update_happy_path_with_all_params(self, client: Roark) -> None:
        customer_flow = client.customer_flow.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            persona_override_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
            title="x",
        )
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @parametrize
    def test_raw_response_update_happy_path(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @parametrize
    def test_streaming_response_update_happy_path(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_happy_path(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.customer_flow.with_raw_response.update_happy_path(
                flow_id="",
            )


class TestAsyncCustomerFlow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.create(
            graph=[{"type": "CUSTOMER_FIRST_MESSAGE"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.create(
            graph=[
                {
                    "type": "CUSTOMER_FIRST_MESSAGE",
                    "content": "Hi, I need to move my appointment.",
                    "merge_into_node_ids": ["x"],
                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ref": "x",
                    "steps": [],
                }
            ],
            title="Reschedule an appointment",
            type="SCRIPTED",
            agent_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            branching_mode="DETERMINISTIC",
            description="description",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.create(
            graph=[{"type": "CUSTOMER_FIRST_MESSAGE"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.create(
            graph=[{"type": "CUSTOMER_FIRST_MESSAGE"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.create(
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            happy_path={
                "environment_id": "d1f5c19d-0000-4000-8000-000000000001",
                "persona_override_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
                "title": "Asks about a charge",
            },
            title="Billing questions",
            type="IMPROV",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.create(
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            happy_path={
                "environment_id": "d1f5c19d-0000-4000-8000-000000000001",
                "persona_override_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
                "title": "Asks about a charge",
                "preceded_by_customer_flow_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "preceded_by_customer_flow_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "prompt": "You want to understand a charge on your latest invoice.",
            },
            title="Billing questions",
            type="IMPROV",
            agent_expectations=[{"prompt": "The agent never states an amount it has not verified"}],
            description="description",
            edge_cases=[
                {
                    "title": "Disputes the charge",
                    "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preceded_by_customer_flow_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preceded_by_customer_flow_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "prompt": "You are certain the charge is wrong.",
                }
            ],
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.create(
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            happy_path={
                "environment_id": "d1f5c19d-0000-4000-8000-000000000001",
                "persona_override_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
                "title": "Asks about a charge",
            },
            title="Billing questions",
            type="IMPROV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.create(
            agent_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            happy_path={
                "environment_id": "d1f5c19d-0000-4000-8000-000000000001",
                "persona_override_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
                "title": "Asks about a charge",
            },
            title="Billing questions",
            type="IMPROV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            branching_mode="DETERMINISTIC",
            description="description",
            title="x",
        )
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.customer_flow.with_raw_response.update(
                flow_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.list()
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.list(
            after="after",
            include_system="true",
            limit=1,
            search_text="searchText",
            type="SCRIPTED",
        )
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowDeleteResponse, customer_flow, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowDeleteResponse, customer_flow, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowDeleteResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.customer_flow.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.customer_flow.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_replace_graph(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[{"type": "AGENT_TURN"}],
        )
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @parametrize
    async def test_method_replace_graph_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[
                {
                    "type": "AGENT_TURN",
                    "content": "content",
                    "merge_into_node_ids": ["x"],
                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ref": "x",
                    "steps": [],
                }
            ],
            allow_unmerge=True,
        )
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @parametrize
    async def test_raw_response_replace_graph(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[{"type": "AGENT_TURN"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @parametrize
    async def test_streaming_response_replace_graph(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[{"type": "AGENT_TURN"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace_graph(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.customer_flow.with_raw_response.replace_graph(
                flow_id="",
                graph=[{"type": "AGENT_TURN"}],
            )

    @parametrize
    async def test_method_update_happy_path(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @parametrize
    async def test_method_update_happy_path_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            persona_override_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
            title="x",
        )
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @parametrize
    async def test_raw_response_update_happy_path(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @parametrize
    async def test_streaming_response_update_happy_path(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_happy_path(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.customer_flow.with_raw_response.update_happy_path(
                flow_id="",
            )
