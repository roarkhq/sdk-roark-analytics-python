# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    MetricPolicyListResponse,
    MetricPolicyCreateResponse,
    MetricPolicyDeleteResponse,
    MetricPolicyUpdateResponse,
    MetricPolicyGetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetricPolicy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        metric_policy = client.metric_policy.create(
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="Evaluate all inbound calls",
        )
        assert_matches_type(MetricPolicyCreateResponse, metric_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        metric_policy = client.metric_policy.create(
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="Evaluate all inbound calls",
            conditions=[
                {
                    "conditions": [
                        {
                            "condition_key": "conditionKey",
                            "condition_type": "AGENT",
                            "condition_operator": "EQUALS",
                            "condition_value": "conditionValue",
                        }
                    ]
                }
            ],
            status="ACTIVE",
        )
        assert_matches_type(MetricPolicyCreateResponse, metric_policy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.metric_policy.with_raw_response.create(
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="Evaluate all inbound calls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = response.parse()
        assert_matches_type(MetricPolicyCreateResponse, metric_policy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.metric_policy.with_streaming_response.create(
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="Evaluate all inbound calls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = response.parse()
            assert_matches_type(MetricPolicyCreateResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        metric_policy = client.metric_policy.update(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetricPolicyUpdateResponse, metric_policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        metric_policy = client.metric_policy.update(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conditions=[
                {
                    "conditions": [
                        {
                            "condition_key": "conditionKey",
                            "condition_type": "AGENT",
                            "condition_operator": "EQUALS",
                            "condition_value": "conditionValue",
                        }
                    ]
                }
            ],
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="x",
            status="ACTIVE",
        )
        assert_matches_type(MetricPolicyUpdateResponse, metric_policy, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.metric_policy.with_raw_response.update(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = response.parse()
        assert_matches_type(MetricPolicyUpdateResponse, metric_policy, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.metric_policy.with_streaming_response.update(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = response.parse()
            assert_matches_type(MetricPolicyUpdateResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.metric_policy.with_raw_response.update(
                policy_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        metric_policy = client.metric_policy.list()
        assert_matches_type(MetricPolicyListResponse, metric_policy, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        metric_policy = client.metric_policy.list(
            after="after",
            limit=20,
            status="ACTIVE",
        )
        assert_matches_type(MetricPolicyListResponse, metric_policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.metric_policy.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = response.parse()
        assert_matches_type(MetricPolicyListResponse, metric_policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.metric_policy.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = response.parse()
            assert_matches_type(MetricPolicyListResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        metric_policy = client.metric_policy.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetricPolicyDeleteResponse, metric_policy, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.metric_policy.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = response.parse()
        assert_matches_type(MetricPolicyDeleteResponse, metric_policy, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.metric_policy.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = response.parse()
            assert_matches_type(MetricPolicyDeleteResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.metric_policy.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        metric_policy = client.metric_policy.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetricPolicyGetByIDResponse, metric_policy, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.metric_policy.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = response.parse()
        assert_matches_type(MetricPolicyGetByIDResponse, metric_policy, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.metric_policy.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = response.parse()
            assert_matches_type(MetricPolicyGetByIDResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.metric_policy.with_raw_response.get_by_id(
                "",
            )


class TestAsyncMetricPolicy:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        metric_policy = await async_client.metric_policy.create(
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="Evaluate all inbound calls",
        )
        assert_matches_type(MetricPolicyCreateResponse, metric_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        metric_policy = await async_client.metric_policy.create(
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="Evaluate all inbound calls",
            conditions=[
                {
                    "conditions": [
                        {
                            "condition_key": "conditionKey",
                            "condition_type": "AGENT",
                            "condition_operator": "EQUALS",
                            "condition_value": "conditionValue",
                        }
                    ]
                }
            ],
            status="ACTIVE",
        )
        assert_matches_type(MetricPolicyCreateResponse, metric_policy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_policy.with_raw_response.create(
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="Evaluate all inbound calls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = await response.parse()
        assert_matches_type(MetricPolicyCreateResponse, metric_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_policy.with_streaming_response.create(
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="Evaluate all inbound calls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = await response.parse()
            assert_matches_type(MetricPolicyCreateResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        metric_policy = await async_client.metric_policy.update(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetricPolicyUpdateResponse, metric_policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        metric_policy = await async_client.metric_policy.update(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conditions=[
                {
                    "conditions": [
                        {
                            "condition_key": "conditionKey",
                            "condition_type": "AGENT",
                            "condition_operator": "EQUALS",
                            "condition_value": "conditionValue",
                        }
                    ]
                }
            ],
            metrics=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            name="x",
            status="ACTIVE",
        )
        assert_matches_type(MetricPolicyUpdateResponse, metric_policy, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_policy.with_raw_response.update(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = await response.parse()
        assert_matches_type(MetricPolicyUpdateResponse, metric_policy, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_policy.with_streaming_response.update(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = await response.parse()
            assert_matches_type(MetricPolicyUpdateResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.metric_policy.with_raw_response.update(
                policy_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        metric_policy = await async_client.metric_policy.list()
        assert_matches_type(MetricPolicyListResponse, metric_policy, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        metric_policy = await async_client.metric_policy.list(
            after="after",
            limit=20,
            status="ACTIVE",
        )
        assert_matches_type(MetricPolicyListResponse, metric_policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_policy.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = await response.parse()
        assert_matches_type(MetricPolicyListResponse, metric_policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_policy.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = await response.parse()
            assert_matches_type(MetricPolicyListResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        metric_policy = await async_client.metric_policy.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetricPolicyDeleteResponse, metric_policy, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_policy.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = await response.parse()
        assert_matches_type(MetricPolicyDeleteResponse, metric_policy, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_policy.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = await response.parse()
            assert_matches_type(MetricPolicyDeleteResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.metric_policy.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        metric_policy = await async_client.metric_policy.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetricPolicyGetByIDResponse, metric_policy, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.metric_policy.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_policy = await response.parse()
        assert_matches_type(MetricPolicyGetByIDResponse, metric_policy, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.metric_policy.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_policy = await response.parse()
            assert_matches_type(MetricPolicyGetByIDResponse, metric_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.metric_policy.with_raw_response.get_by_id(
                "",
            )
