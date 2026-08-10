# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    SimulationCustomerFlowVariantListResponse,
    SimulationCustomerFlowVariantCreateResponse,
    SimulationCustomerFlowVariantDeleteResponse,
    SimulationCustomerFlowVariantUpdateResponse,
    SimulationCustomerFlowVariantGetByIDResponse,
    SimulationCustomerFlowVariantSetDefaultResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationCustomerFlowVariant:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        simulation_customer_flow_variant = client.simulation_customer_flow_variant.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantCreateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        simulation_customer_flow_variant = client.simulation_customer_flow_variant.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_default=True,
            persona_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantCreateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.simulation_customer_flow_variant.with_raw_response.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantCreateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.simulation_customer_flow_variant.with_streaming_response.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantCreateResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.create(
                flow_id="",
                title="x",
            )

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        simulation_customer_flow_variant = client.simulation_customer_flow_variant.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantUpdateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        simulation_customer_flow_variant = client.simulation_customer_flow_variant.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_expectations=[{"llm_prompt": "x"}],
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            persona_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
            title="x",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantUpdateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.simulation_customer_flow_variant.with_raw_response.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantUpdateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.simulation_customer_flow_variant.with_streaming_response.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantUpdateResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.update(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.update(
                variant_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        simulation_customer_flow_variant = client.simulation_customer_flow_variant.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantListResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.simulation_customer_flow_variant.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantListResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.simulation_customer_flow_variant.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantListResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        simulation_customer_flow_variant = client.simulation_customer_flow_variant.delete(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantDeleteResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.simulation_customer_flow_variant.with_raw_response.delete(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantDeleteResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.simulation_customer_flow_variant.with_streaming_response.delete(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantDeleteResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.delete(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.delete(
                variant_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        simulation_customer_flow_variant = client.simulation_customer_flow_variant.get_by_id(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantGetByIDResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.simulation_customer_flow_variant.with_raw_response.get_by_id(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantGetByIDResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.simulation_customer_flow_variant.with_streaming_response.get_by_id(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantGetByIDResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.get_by_id(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.get_by_id(
                variant_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_set_default(self, client: Roark) -> None:
        simulation_customer_flow_variant = client.simulation_customer_flow_variant.set_default(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantSetDefaultResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_raw_response_set_default(self, client: Roark) -> None:
        response = client.simulation_customer_flow_variant.with_raw_response.set_default(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantSetDefaultResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    def test_streaming_response_set_default(self, client: Roark) -> None:
        with client.simulation_customer_flow_variant.with_streaming_response.set_default(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantSetDefaultResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_default(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.set_default(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.simulation_customer_flow_variant.with_raw_response.set_default(
                variant_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSimulationCustomerFlowVariant:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        simulation_customer_flow_variant = await async_client.simulation_customer_flow_variant.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantCreateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_customer_flow_variant = await async_client.simulation_customer_flow_variant.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_default=True,
            persona_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantCreateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_customer_flow_variant.with_raw_response.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = await response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantCreateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_customer_flow_variant.with_streaming_response.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = await response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantCreateResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.create(
                flow_id="",
                title="x",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        simulation_customer_flow_variant = await async_client.simulation_customer_flow_variant.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantUpdateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        simulation_customer_flow_variant = await async_client.simulation_customer_flow_variant.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_expectations=[{"llm_prompt": "x"}],
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            persona_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            preceded_by_customer_flow_variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
            title="x",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantUpdateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_customer_flow_variant.with_raw_response.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = await response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantUpdateResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_customer_flow_variant.with_streaming_response.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = await response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantUpdateResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.update(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.update(
                variant_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        simulation_customer_flow_variant = await async_client.simulation_customer_flow_variant.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantListResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_customer_flow_variant.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = await response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantListResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_customer_flow_variant.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = await response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantListResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        simulation_customer_flow_variant = await async_client.simulation_customer_flow_variant.delete(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantDeleteResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_customer_flow_variant.with_raw_response.delete(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = await response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantDeleteResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_customer_flow_variant.with_streaming_response.delete(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = await response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantDeleteResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.delete(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.delete(
                variant_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        simulation_customer_flow_variant = await async_client.simulation_customer_flow_variant.get_by_id(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantGetByIDResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_customer_flow_variant.with_raw_response.get_by_id(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = await response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantGetByIDResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_customer_flow_variant.with_streaming_response.get_by_id(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = await response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantGetByIDResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.get_by_id(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.get_by_id(
                variant_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_set_default(self, async_client: AsyncRoark) -> None:
        simulation_customer_flow_variant = await async_client.simulation_customer_flow_variant.set_default(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SimulationCustomerFlowVariantSetDefaultResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_raw_response_set_default(self, async_client: AsyncRoark) -> None:
        response = await async_client.simulation_customer_flow_variant.with_raw_response.set_default(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation_customer_flow_variant = await response.parse()
        assert_matches_type(
            SimulationCustomerFlowVariantSetDefaultResponse, simulation_customer_flow_variant, path=["response"]
        )

    @parametrize
    async def test_streaming_response_set_default(self, async_client: AsyncRoark) -> None:
        async with async_client.simulation_customer_flow_variant.with_streaming_response.set_default(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation_customer_flow_variant = await response.parse()
            assert_matches_type(
                SimulationCustomerFlowVariantSetDefaultResponse, simulation_customer_flow_variant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_default(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.set_default(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.simulation_customer_flow_variant.with_raw_response.set_default(
                variant_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
