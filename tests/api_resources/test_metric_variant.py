# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    MetricVariantListResponse,
    MetricVariantCreateResponse,
    MetricVariantDeleteResponse,
    MetricVariantUpdateResponse,
    MetricVariantGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetricVariant:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        metric_variant = client.metric_variant.create(
            id_or_slug="idOrSlug",
            name="Strict",
        )
        assert_matches_type(MetricVariantCreateResponse, metric_variant, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.metric_variant.with_raw_response.create(
            id_or_slug="idOrSlug",
            name="Strict",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = response.parse()
        assert_matches_type(MetricVariantCreateResponse, metric_variant, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.metric_variant.with_streaming_response.create(
            id_or_slug="idOrSlug",
            name="Strict",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = response.parse()
            assert_matches_type(MetricVariantCreateResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            client.metric_variant.with_raw_response.create(
                id_or_slug="",
                name="Strict",
            )

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        metric_variant = client.metric_variant.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )
        assert_matches_type(MetricVariantUpdateResponse, metric_variant, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        metric_variant = client.metric_variant.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
            boolean_false_label="booleanFalseLabel",
            boolean_true_label="booleanTrueLabel",
            change_reason="changeReason",
            llm_prompt="llmPrompt",
            max_classifications=1,
            name="x",
            scale_max=0,
            scale_min=0,
        )
        assert_matches_type(MetricVariantUpdateResponse, metric_variant, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.metric_variant.with_raw_response.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = response.parse()
        assert_matches_type(MetricVariantUpdateResponse, metric_variant, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.metric_variant.with_streaming_response.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = response.parse()
            assert_matches_type(MetricVariantUpdateResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.metric_variant.with_raw_response.update(
                variant_id="",
                id_or_slug="idOrSlug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            client.metric_variant.with_raw_response.update(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id_or_slug="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        metric_variant = client.metric_variant.list(
            "idOrSlug",
        )
        assert_matches_type(MetricVariantListResponse, metric_variant, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.metric_variant.with_raw_response.list(
            "idOrSlug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = response.parse()
        assert_matches_type(MetricVariantListResponse, metric_variant, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.metric_variant.with_streaming_response.list(
            "idOrSlug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = response.parse()
            assert_matches_type(MetricVariantListResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            client.metric_variant.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        metric_variant = client.metric_variant.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )
        assert_matches_type(MetricVariantDeleteResponse, metric_variant, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.metric_variant.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = response.parse()
        assert_matches_type(MetricVariantDeleteResponse, metric_variant, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.metric_variant.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = response.parse()
            assert_matches_type(MetricVariantDeleteResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.metric_variant.with_raw_response.delete(
                "",
                id_or_slug="idOrSlug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            client.metric_variant.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id_or_slug="",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        metric_variant = client.metric_variant.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )
        assert_matches_type(MetricVariantGetByIDResponse, metric_variant, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.metric_variant.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = response.parse()
        assert_matches_type(MetricVariantGetByIDResponse, metric_variant, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.metric_variant.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = response.parse()
            assert_matches_type(MetricVariantGetByIDResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.metric_variant.with_raw_response.get_by_id(
                "",
                id_or_slug="idOrSlug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            client.metric_variant.with_raw_response.get_by_id(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id_or_slug="",
            )


class TestAsyncMetricVariant:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        metric_variant = await async_client.metric_variant.create(
            id_or_slug="idOrSlug",
            name="Strict",
        )
        assert_matches_type(MetricVariantCreateResponse, metric_variant, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_variant.with_raw_response.create(
            id_or_slug="idOrSlug",
            name="Strict",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = await response.parse()
        assert_matches_type(MetricVariantCreateResponse, metric_variant, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_variant.with_streaming_response.create(
            id_or_slug="idOrSlug",
            name="Strict",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = await response.parse()
            assert_matches_type(MetricVariantCreateResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            await async_client.metric_variant.with_raw_response.create(
                id_or_slug="",
                name="Strict",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        metric_variant = await async_client.metric_variant.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )
        assert_matches_type(MetricVariantUpdateResponse, metric_variant, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        metric_variant = await async_client.metric_variant.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
            boolean_false_label="booleanFalseLabel",
            boolean_true_label="booleanTrueLabel",
            change_reason="changeReason",
            llm_prompt="llmPrompt",
            max_classifications=1,
            name="x",
            scale_max=0,
            scale_min=0,
        )
        assert_matches_type(MetricVariantUpdateResponse, metric_variant, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_variant.with_raw_response.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = await response.parse()
        assert_matches_type(MetricVariantUpdateResponse, metric_variant, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_variant.with_streaming_response.update(
            variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = await response.parse()
            assert_matches_type(MetricVariantUpdateResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.metric_variant.with_raw_response.update(
                variant_id="",
                id_or_slug="idOrSlug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            await async_client.metric_variant.with_raw_response.update(
                variant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id_or_slug="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        metric_variant = await async_client.metric_variant.list(
            "idOrSlug",
        )
        assert_matches_type(MetricVariantListResponse, metric_variant, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_variant.with_raw_response.list(
            "idOrSlug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = await response.parse()
        assert_matches_type(MetricVariantListResponse, metric_variant, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_variant.with_streaming_response.list(
            "idOrSlug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = await response.parse()
            assert_matches_type(MetricVariantListResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            await async_client.metric_variant.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        metric_variant = await async_client.metric_variant.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )
        assert_matches_type(MetricVariantDeleteResponse, metric_variant, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_variant.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = await response.parse()
        assert_matches_type(MetricVariantDeleteResponse, metric_variant, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_variant.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = await response.parse()
            assert_matches_type(MetricVariantDeleteResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.metric_variant.with_raw_response.delete(
                "",
                id_or_slug="idOrSlug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            await async_client.metric_variant.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id_or_slug="",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        metric_variant = await async_client.metric_variant.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )
        assert_matches_type(MetricVariantGetByIDResponse, metric_variant, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_variant.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_variant = await response.parse()
        assert_matches_type(MetricVariantGetByIDResponse, metric_variant, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_variant.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id_or_slug="idOrSlug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_variant = await response.parse()
            assert_matches_type(MetricVariantGetByIDResponse, metric_variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.metric_variant.with_raw_response.get_by_id(
                "",
                id_or_slug="idOrSlug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_slug` but received ''"):
            await async_client.metric_variant.with_raw_response.get_by_id(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id_or_slug="",
            )
