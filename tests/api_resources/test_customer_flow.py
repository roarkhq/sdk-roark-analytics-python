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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_create_overload_1(self, client: Roark) -> None:
        customer_flow = client.customer_flow.create(
            graph=[{"type": "AGENT_TURN"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Roark) -> None:
        customer_flow = client.customer_flow.create(
            graph=[
                {
                    "type": "AGENT_TURN",
                    "content": "content",
                    "merge_into_node_ids": ["x"],
                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ref": "x",
                    "steps": [
                        {
                            "type": "AGENT_TURN",
                            "content": "content",
                            "merge_into_node_ids": ["x"],
                            "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "ref": "x",
                            "steps": [
                                {
                                    "type": "AGENT_TURN",
                                    "content": "content",
                                    "merge_into_node_ids": ["x"],
                                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                    "ref": "x",
                                    "steps": [
                                        {
                                            "type": "AGENT_TURN",
                                            "content": "content",
                                            "merge_into_node_ids": [],
                                            "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                            "ref": "x",
                                            "steps": [],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
            title="Reschedule an appointment",
            type="SCRIPTED",
            agent_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            branching_mode="DETERMINISTIC",
            description="description",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.create(
            graph=[{"type": "AGENT_TURN"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.create(
            graph=[{"type": "AGENT_TURN"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_create_overload_2(self, client: Roark) -> None:
        customer_flow = client.customer_flow.create(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            happy_path={
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "title": "x",
            },
            title="Reschedule an appointment",
            type="IMPROV",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Roark) -> None:
        customer_flow = client.customer_flow.create(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            happy_path={
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "title": "x",
                "preceded_by_customer_flow_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "preceded_by_customer_flow_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "prompt": "prompt",
            },
            title="Reschedule an appointment",
            type="IMPROV",
            agent_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            description="description",
            edge_cases=[
                {
                    "title": "x",
                    "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preceded_by_customer_flow_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preceded_by_customer_flow_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "prompt": "prompt",
                }
            ],
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.create(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            happy_path={
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "title": "x",
            },
            title="Reschedule an appointment",
            type="IMPROV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Roark) -> None:
        with client.customer_flow.with_streaming_response.create(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            happy_path={
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "title": "x",
            },
            title="Reschedule an appointment",
            type="IMPROV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = response.parse()
            assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_update(self, client: Roark) -> None:
        customer_flow = client.customer_flow.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_list(self, client: Roark) -> None:
        customer_flow = client.customer_flow.list()
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        customer_flow = client.customer_flow.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_replace_graph(self, client: Roark) -> None:
        customer_flow = client.customer_flow.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[{"type": "AGENT_TURN"}],
        )
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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
                    "steps": [
                        {
                            "type": "AGENT_TURN",
                            "content": "content",
                            "merge_into_node_ids": ["x"],
                            "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "ref": "x",
                            "steps": [
                                {
                                    "type": "AGENT_TURN",
                                    "content": "content",
                                    "merge_into_node_ids": ["x"],
                                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                    "ref": "x",
                                    "steps": [
                                        {
                                            "type": "AGENT_TURN",
                                            "content": "content",
                                            "merge_into_node_ids": [],
                                            "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                            "ref": "x",
                                            "steps": [],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
            allow_unmerge=True,
        )
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_update_happy_path(self, client: Roark) -> None:
        customer_flow = client.customer_flow.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_raw_response_update_happy_path(self, client: Roark) -> None:
        response = client.customer_flow.with_raw_response.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = response.parse()
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.create(
            graph=[{"type": "AGENT_TURN"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.create(
            graph=[
                {
                    "type": "AGENT_TURN",
                    "content": "content",
                    "merge_into_node_ids": ["x"],
                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ref": "x",
                    "steps": [
                        {
                            "type": "AGENT_TURN",
                            "content": "content",
                            "merge_into_node_ids": ["x"],
                            "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "ref": "x",
                            "steps": [
                                {
                                    "type": "AGENT_TURN",
                                    "content": "content",
                                    "merge_into_node_ids": ["x"],
                                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                    "ref": "x",
                                    "steps": [
                                        {
                                            "type": "AGENT_TURN",
                                            "content": "content",
                                            "merge_into_node_ids": [],
                                            "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                            "ref": "x",
                                            "steps": [],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
            title="Reschedule an appointment",
            type="SCRIPTED",
            agent_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            branching_mode="DETERMINISTIC",
            description="description",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.create(
            graph=[{"type": "AGENT_TURN"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.create(
            graph=[{"type": "AGENT_TURN"}],
            title="Reschedule an appointment",
            type="SCRIPTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.create(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            happy_path={
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "title": "x",
            },
            title="Reschedule an appointment",
            type="IMPROV",
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.create(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            happy_path={
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "title": "x",
                "preceded_by_customer_flow_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "preceded_by_customer_flow_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "prompt": "prompt",
            },
            title="Reschedule an appointment",
            type="IMPROV",
            agent_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            description="description",
            edge_cases=[
                {
                    "title": "x",
                    "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preceded_by_customer_flow_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preceded_by_customer_flow_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "prompt": "prompt",
                }
            ],
        )
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.create(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            happy_path={
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "title": "x",
            },
            title="Reschedule an appointment",
            type="IMPROV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow.with_streaming_response.create(
            agent_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            happy_path={
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "persona_override_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "title": "x",
            },
            title="Reschedule an appointment",
            type="IMPROV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow = await response.parse()
            assert_matches_type(CustomerFlowCreateResponse, customer_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowUpdateResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.list()
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowListResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowGetByIDResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_replace_graph(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.replace_graph(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            graph=[{"type": "AGENT_TURN"}],
        )
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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
                    "steps": [
                        {
                            "type": "AGENT_TURN",
                            "content": "content",
                            "merge_into_node_ids": ["x"],
                            "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "ref": "x",
                            "steps": [
                                {
                                    "type": "AGENT_TURN",
                                    "content": "content",
                                    "merge_into_node_ids": ["x"],
                                    "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                    "ref": "x",
                                    "steps": [
                                        {
                                            "type": "AGENT_TURN",
                                            "content": "content",
                                            "merge_into_node_ids": [],
                                            "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                            "ref": "x",
                                            "steps": [],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
            allow_unmerge=True,
        )
        assert_matches_type(CustomerFlowReplaceGraphResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_update_happy_path(self, async_client: AsyncRoark) -> None:
        customer_flow = await async_client.customer_flow.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_raw_response_update_happy_path(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow.with_raw_response.update_happy_path(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow = await response.parse()
        assert_matches_type(CustomerFlowUpdateHappyPathResponse, customer_flow, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
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
