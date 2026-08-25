# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    CustomerFlowEdgeCaseAddResponse,
    CustomerFlowEdgeCaseRemoveResponse,
    CustomerFlowEdgeCaseUpdateResponse,
    CustomerFlowEdgeCasePromoteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomerFlowEdgeCase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_update(self, client: Roark) -> None:
        customer_flow_edge_case = client.customer_flow_edge_case.update(
            edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowEdgeCaseUpdateResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        customer_flow_edge_case = client.customer_flow_edge_case.update(
            edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            persona_override_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
            title="x",
        )
        assert_matches_type(CustomerFlowEdgeCaseUpdateResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.customer_flow_edge_case.with_raw_response.update(
            edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_edge_case = response.parse()
        assert_matches_type(CustomerFlowEdgeCaseUpdateResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.customer_flow_edge_case.with_streaming_response.update(
            edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_edge_case = response.parse()
            assert_matches_type(CustomerFlowEdgeCaseUpdateResponse, customer_flow_edge_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `edge_case_id` but received ''"):
            client.customer_flow_edge_case.with_raw_response.update(
                edge_case_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.customer_flow_edge_case.with_raw_response.update(
                edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_add(self, client: Roark) -> None:
        customer_flow_edge_case = client.customer_flow_edge_case.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        )
        assert_matches_type(CustomerFlowEdgeCaseAddResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_add_with_all_params(self, client: Roark) -> None:
        customer_flow_edge_case = client.customer_flow_edge_case.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            persona_override_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )
        assert_matches_type(CustomerFlowEdgeCaseAddResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_raw_response_add(self, client: Roark) -> None:
        response = client.customer_flow_edge_case.with_raw_response.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_edge_case = response.parse()
        assert_matches_type(CustomerFlowEdgeCaseAddResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_streaming_response_add(self, client: Roark) -> None:
        with client.customer_flow_edge_case.with_streaming_response.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_edge_case = response.parse()
            assert_matches_type(CustomerFlowEdgeCaseAddResponse, customer_flow_edge_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.customer_flow_edge_case.with_raw_response.add(
                flow_id="",
                title="x",
            )

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_method_promote(self, client: Roark) -> None:
        customer_flow_edge_case = client.customer_flow_edge_case.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowEdgeCasePromoteResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_raw_response_promote(self, client: Roark) -> None:
        response = client.customer_flow_edge_case.with_raw_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_edge_case = response.parse()
        assert_matches_type(CustomerFlowEdgeCasePromoteResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    def test_streaming_response_promote(self, client: Roark) -> None:
        with client.customer_flow_edge_case.with_streaming_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_edge_case = response.parse()
            assert_matches_type(CustomerFlowEdgeCasePromoteResponse, customer_flow_edge_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_promote(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `edge_case_id` but received ''"):
            client.customer_flow_edge_case.with_raw_response.promote(
                "",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.customer_flow_edge_case.with_raw_response.promote(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

    @parametrize
    def test_method_remove(self, client: Roark) -> None:
        customer_flow_edge_case = client.customer_flow_edge_case.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowEdgeCaseRemoveResponse, customer_flow_edge_case, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Roark) -> None:
        response = client.customer_flow_edge_case.with_raw_response.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_edge_case = response.parse()
        assert_matches_type(CustomerFlowEdgeCaseRemoveResponse, customer_flow_edge_case, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Roark) -> None:
        with client.customer_flow_edge_case.with_streaming_response.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_edge_case = response.parse()
            assert_matches_type(CustomerFlowEdgeCaseRemoveResponse, customer_flow_edge_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `edge_case_id` but received ''"):
            client.customer_flow_edge_case.with_raw_response.remove(
                "",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.customer_flow_edge_case.with_raw_response.remove(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )


class TestAsyncCustomerFlowEdgeCase:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        customer_flow_edge_case = await async_client.customer_flow_edge_case.update(
            edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowEdgeCaseUpdateResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_flow_edge_case = await async_client.customer_flow_edge_case.update(
            edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_expectations=[{"prompt": "The agent confirmed the new appointment time back to the customer"}],
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            persona_override_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
            title="x",
        )
        assert_matches_type(CustomerFlowEdgeCaseUpdateResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow_edge_case.with_raw_response.update(
            edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_edge_case = await response.parse()
        assert_matches_type(CustomerFlowEdgeCaseUpdateResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow_edge_case.with_streaming_response.update(
            edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_edge_case = await response.parse()
            assert_matches_type(CustomerFlowEdgeCaseUpdateResponse, customer_flow_edge_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `edge_case_id` but received ''"):
            await async_client.customer_flow_edge_case.with_raw_response.update(
                edge_case_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.customer_flow_edge_case.with_raw_response.update(
                edge_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_add(self, async_client: AsyncRoark) -> None:
        customer_flow_edge_case = await async_client.customer_flow_edge_case.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        )
        assert_matches_type(CustomerFlowEdgeCaseAddResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncRoark) -> None:
        customer_flow_edge_case = await async_client.customer_flow_edge_case.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            persona_override_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )
        assert_matches_type(CustomerFlowEdgeCaseAddResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow_edge_case.with_raw_response.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_edge_case = await response.parse()
        assert_matches_type(CustomerFlowEdgeCaseAddResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow_edge_case.with_streaming_response.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_edge_case = await response.parse()
            assert_matches_type(CustomerFlowEdgeCaseAddResponse, customer_flow_edge_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.customer_flow_edge_case.with_raw_response.add(
                flow_id="",
                title="x",
            )

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_method_promote(self, async_client: AsyncRoark) -> None:
        customer_flow_edge_case = await async_client.customer_flow_edge_case.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowEdgeCasePromoteResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_raw_response_promote(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow_edge_case.with_raw_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_edge_case = await response.parse()
        assert_matches_type(CustomerFlowEdgeCasePromoteResponse, customer_flow_edge_case, path=["response"])

    @pytest.mark.skip(reason="prism cannot mock a recursive response schema")
    @parametrize
    async def test_streaming_response_promote(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow_edge_case.with_streaming_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_edge_case = await response.parse()
            assert_matches_type(CustomerFlowEdgeCasePromoteResponse, customer_flow_edge_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_promote(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `edge_case_id` but received ''"):
            await async_client.customer_flow_edge_case.with_raw_response.promote(
                "",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.customer_flow_edge_case.with_raw_response.promote(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncRoark) -> None:
        customer_flow_edge_case = await async_client.customer_flow_edge_case.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerFlowEdgeCaseRemoveResponse, customer_flow_edge_case, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncRoark) -> None:
        response = await async_client.customer_flow_edge_case.with_raw_response.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_flow_edge_case = await response.parse()
        assert_matches_type(CustomerFlowEdgeCaseRemoveResponse, customer_flow_edge_case, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncRoark) -> None:
        async with async_client.customer_flow_edge_case.with_streaming_response.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_flow_edge_case = await response.parse()
            assert_matches_type(CustomerFlowEdgeCaseRemoveResponse, customer_flow_edge_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `edge_case_id` but received ''"):
            await async_client.customer_flow_edge_case.with_raw_response.remove(
                "",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.customer_flow_edge_case.with_raw_response.remove(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )
