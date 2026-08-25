# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    MetricListDefinitionsResponse,
    MetricCreateDefinitionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetric:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_definition_overload_1(self, client: Roark) -> None:
        metric = client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="LLM_JUDGE",
            name="Customer Satisfaction",
            output_type="BOOLEAN",
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    def test_method_create_definition_with_all_params_overload_1(self, client: Roark) -> None:
        metric = client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="LLM_JUDGE",
            name="Customer Satisfaction",
            output_type="BOOLEAN",
            boolean_false_label="booleanFalseLabel",
            boolean_true_label="booleanTrueLabel",
            classification_options=[{"description": "description", "display_order": 0, "label": "label"}],
            llm_prompt="Evaluate whether the customer expressed satisfaction with the service provided.",
            max_classifications=1,
            metric_id="customer_satisfaction",
            participant_role="AGENT",
            scale_labels=[
                {
                    "display_order": 0,
                    "label": "label",
                    "range_max": 0,
                    "range_min": 0,
                    "color_hex": "colorHex",
                    "description": "description",
                }
            ],
            scale_max=0,
            scale_min=0,
            scope="GLOBAL",
            slug="customer_satisfaction",
            supported_contexts=["CALL"],
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_create_definition_overload_1(self, client: Roark) -> None:
        response = client.metric.with_raw_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="LLM_JUDGE",
            name="Customer Satisfaction",
            output_type="BOOLEAN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_create_definition_overload_1(self, client: Roark) -> None:
        with client.metric.with_streaming_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="LLM_JUDGE",
            name="Customer Satisfaction",
            output_type="BOOLEAN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_definition_overload_2(self, client: Roark) -> None:
        metric = client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="FORMULA",
            formula="{{id:00000000-0000-0000-0000-000000000001}} / {{id:00000000-0000-0000-0000-000000000002}}",
            name="Customer Satisfaction",
            output_type="NUMERIC",
            sources=[{"source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    def test_method_create_definition_with_all_params_overload_2(self, client: Roark) -> None:
        metric = client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="FORMULA",
            formula="{{id:00000000-0000-0000-0000-000000000001}} / {{id:00000000-0000-0000-0000-000000000002}}",
            name="Customer Satisfaction",
            output_type="NUMERIC",
            sources=[
                {
                    "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "source_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            metric_id="customer_satisfaction",
            slug="customer_satisfaction",
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_create_definition_overload_2(self, client: Roark) -> None:
        response = client.metric.with_raw_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="FORMULA",
            formula="{{id:00000000-0000-0000-0000-000000000001}} / {{id:00000000-0000-0000-0000-000000000002}}",
            name="Customer Satisfaction",
            output_type="NUMERIC",
            sources=[{"source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_create_definition_overload_2(self, client: Roark) -> None:
        with client.metric.with_streaming_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="FORMULA",
            formula="{{id:00000000-0000-0000-0000-000000000001}} / {{id:00000000-0000-0000-0000-000000000002}}",
            name="Customer Satisfaction",
            output_type="NUMERIC",
            sources=[{"source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_definition_overload_3(self, client: Roark) -> None:
        metric = client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="PATTERN",
            name="Customer Satisfaction",
            operation="PATTERN_EXISTS",
            outcome={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "window_after": 0,
            },
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    def test_method_create_definition_with_all_params_overload_3(self, client: Roark) -> None:
        metric = client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="PATTERN",
            name="Customer Satisfaction",
            operation="PATTERN_EXISTS",
            outcome={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "window_after": 0,
                "source_participant_role": "AGENT",
                "source_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "window_before": 0,
            },
            metric_id="customer_satisfaction",
            slug="customer_satisfaction",
            trigger={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "source_participant_role": "AGENT",
                "source_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            trigger_combinator="AND",
            triggers=[
                {
                    "operator": "GREATER_THAN",
                    "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "threshold_value": "x",
                    "source_participant_role": "AGENT",
                    "source_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            window_mode="seconds",
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_create_definition_overload_3(self, client: Roark) -> None:
        response = client.metric.with_raw_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="PATTERN",
            name="Customer Satisfaction",
            operation="PATTERN_EXISTS",
            outcome={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "window_after": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_create_definition_overload_3(self, client: Roark) -> None:
        with client.metric.with_streaming_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="PATTERN",
            name="Customer Satisfaction",
            operation="PATTERN_EXISTS",
            outcome={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "window_after": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_definitions(self, client: Roark) -> None:
        metric = client.metric.list_definitions()
        assert_matches_type(MetricListDefinitionsResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_list_definitions(self, client: Roark) -> None:
        response = client.metric.with_raw_response.list_definitions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricListDefinitionsResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_list_definitions(self, client: Roark) -> None:
        with client.metric.with_streaming_response.list_definitions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricListDefinitionsResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetric:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_definition_overload_1(self, async_client: AsyncRoark) -> None:
        metric = await async_client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="LLM_JUDGE",
            name="Customer Satisfaction",
            output_type="BOOLEAN",
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    async def test_method_create_definition_with_all_params_overload_1(self, async_client: AsyncRoark) -> None:
        metric = await async_client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="LLM_JUDGE",
            name="Customer Satisfaction",
            output_type="BOOLEAN",
            boolean_false_label="booleanFalseLabel",
            boolean_true_label="booleanTrueLabel",
            classification_options=[{"description": "description", "display_order": 0, "label": "label"}],
            llm_prompt="Evaluate whether the customer expressed satisfaction with the service provided.",
            max_classifications=1,
            metric_id="customer_satisfaction",
            participant_role="AGENT",
            scale_labels=[
                {
                    "display_order": 0,
                    "label": "label",
                    "range_max": 0,
                    "range_min": 0,
                    "color_hex": "colorHex",
                    "description": "description",
                }
            ],
            scale_max=0,
            scale_min=0,
            scope="GLOBAL",
            slug="customer_satisfaction",
            supported_contexts=["CALL"],
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_definition_overload_1(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric.with_raw_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="LLM_JUDGE",
            name="Customer Satisfaction",
            output_type="BOOLEAN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create_definition_overload_1(self, async_client: AsyncRoark) -> None:
        async with async_client.metric.with_streaming_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="LLM_JUDGE",
            name="Customer Satisfaction",
            output_type="BOOLEAN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_definition_overload_2(self, async_client: AsyncRoark) -> None:
        metric = await async_client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="FORMULA",
            formula="{{id:00000000-0000-0000-0000-000000000001}} / {{id:00000000-0000-0000-0000-000000000002}}",
            name="Customer Satisfaction",
            output_type="NUMERIC",
            sources=[{"source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    async def test_method_create_definition_with_all_params_overload_2(self, async_client: AsyncRoark) -> None:
        metric = await async_client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="FORMULA",
            formula="{{id:00000000-0000-0000-0000-000000000001}} / {{id:00000000-0000-0000-0000-000000000002}}",
            name="Customer Satisfaction",
            output_type="NUMERIC",
            sources=[
                {
                    "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "source_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            metric_id="customer_satisfaction",
            slug="customer_satisfaction",
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_definition_overload_2(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric.with_raw_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="FORMULA",
            formula="{{id:00000000-0000-0000-0000-000000000001}} / {{id:00000000-0000-0000-0000-000000000002}}",
            name="Customer Satisfaction",
            output_type="NUMERIC",
            sources=[{"source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create_definition_overload_2(self, async_client: AsyncRoark) -> None:
        async with async_client.metric.with_streaming_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="FORMULA",
            formula="{{id:00000000-0000-0000-0000-000000000001}} / {{id:00000000-0000-0000-0000-000000000002}}",
            name="Customer Satisfaction",
            output_type="NUMERIC",
            sources=[{"source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_definition_overload_3(self, async_client: AsyncRoark) -> None:
        metric = await async_client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="PATTERN",
            name="Customer Satisfaction",
            operation="PATTERN_EXISTS",
            outcome={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "window_after": 0,
            },
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    async def test_method_create_definition_with_all_params_overload_3(self, async_client: AsyncRoark) -> None:
        metric = await async_client.metric.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="PATTERN",
            name="Customer Satisfaction",
            operation="PATTERN_EXISTS",
            outcome={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "window_after": 0,
                "source_participant_role": "AGENT",
                "source_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "window_before": 0,
            },
            metric_id="customer_satisfaction",
            slug="customer_satisfaction",
            trigger={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "source_participant_role": "AGENT",
                "source_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            trigger_combinator="AND",
            triggers=[
                {
                    "operator": "GREATER_THAN",
                    "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "threshold_value": "x",
                    "source_participant_role": "AGENT",
                    "source_variant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            window_mode="seconds",
        )
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_definition_overload_3(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric.with_raw_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="PATTERN",
            name="Customer Satisfaction",
            operation="PATTERN_EXISTS",
            outcome={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "window_after": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create_definition_overload_3(self, async_client: AsyncRoark) -> None:
        async with async_client.metric.with_streaming_response.create_definition(
            analysis_package_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            calculation_type="PATTERN",
            name="Customer Satisfaction",
            operation="PATTERN_EXISTS",
            outcome={
                "operator": "GREATER_THAN",
                "source_metric_definition_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "threshold_value": "x",
                "window_after": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricCreateDefinitionResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_definitions(self, async_client: AsyncRoark) -> None:
        metric = await async_client.metric.list_definitions()
        assert_matches_type(MetricListDefinitionsResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_list_definitions(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric.with_raw_response.list_definitions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricListDefinitionsResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_list_definitions(self, async_client: AsyncRoark) -> None:
        async with async_client.metric.with_streaming_response.list_definitions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricListDefinitionsResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True
