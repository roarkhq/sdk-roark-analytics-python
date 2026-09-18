# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    AutoimproveFixListResponse,
    AutoimproveFixCancelResponse,
    AutoimproveFixCreateResponse,
    AutoimproveFixDismissResponse,
    AutoimproveFixGetByIDResponse,
    AutoimproveFixPromoteResponse,
    AutoimproveFixSendGuidanceResponse,
    AutoimproveFixAnswerQuestionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutoimproveFix:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        autoimprove_fix = client.autoimprove_fix.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        )
        assert_matches_type(AutoimproveFixCreateResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        autoimprove_fix = client.autoimprove_fix.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            customer_integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_iterations=1,
            max_sim_calls=1,
            staging_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_value=90,
            validation_run_plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixCreateResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.autoimprove_fix.with_raw_response.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = response.parse()
        assert_matches_type(AutoimproveFixCreateResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.autoimprove_fix.with_streaming_response.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = response.parse()
            assert_matches_type(AutoimproveFixCreateResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        autoimprove_fix = client.autoimprove_fix.list()
        assert_matches_type(AutoimproveFixListResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.autoimprove_fix.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = response.parse()
        assert_matches_type(AutoimproveFixListResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.autoimprove_fix.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = response.parse()
            assert_matches_type(AutoimproveFixListResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_answer_question(self, client: Roark) -> None:
        autoimprove_fix = client.autoimprove_fix.answer_question(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )
        assert_matches_type(AutoimproveFixAnswerQuestionResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_raw_response_answer_question(self, client: Roark) -> None:
        response = client.autoimprove_fix.with_raw_response.answer_question(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = response.parse()
        assert_matches_type(AutoimproveFixAnswerQuestionResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_streaming_response_answer_question(self, client: Roark) -> None:
        with client.autoimprove_fix.with_streaming_response.answer_question(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = response.parse()
            assert_matches_type(AutoimproveFixAnswerQuestionResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_answer_question(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            client.autoimprove_fix.with_raw_response.answer_question(
                fix_id="",
                text="Keep the current voice; focus on the closing confirmation.",
            )

    @parametrize
    def test_method_cancel(self, client: Roark) -> None:
        autoimprove_fix = client.autoimprove_fix.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixCancelResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Roark) -> None:
        response = client.autoimprove_fix.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = response.parse()
        assert_matches_type(AutoimproveFixCancelResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Roark) -> None:
        with client.autoimprove_fix.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = response.parse()
            assert_matches_type(AutoimproveFixCancelResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            client.autoimprove_fix.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_dismiss(self, client: Roark) -> None:
        autoimprove_fix = client.autoimprove_fix.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixDismissResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_raw_response_dismiss(self, client: Roark) -> None:
        response = client.autoimprove_fix.with_raw_response.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = response.parse()
        assert_matches_type(AutoimproveFixDismissResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_streaming_response_dismiss(self, client: Roark) -> None:
        with client.autoimprove_fix.with_streaming_response.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = response.parse()
            assert_matches_type(AutoimproveFixDismissResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_dismiss(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            client.autoimprove_fix.with_raw_response.dismiss(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        autoimprove_fix = client.autoimprove_fix.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixGetByIDResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.autoimprove_fix.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = response.parse()
        assert_matches_type(AutoimproveFixGetByIDResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.autoimprove_fix.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = response.parse()
            assert_matches_type(AutoimproveFixGetByIDResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            client.autoimprove_fix.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_promote(self, client: Roark) -> None:
        autoimprove_fix = client.autoimprove_fix.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixPromoteResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_raw_response_promote(self, client: Roark) -> None:
        response = client.autoimprove_fix.with_raw_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = response.parse()
        assert_matches_type(AutoimproveFixPromoteResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_streaming_response_promote(self, client: Roark) -> None:
        with client.autoimprove_fix.with_streaming_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = response.parse()
            assert_matches_type(AutoimproveFixPromoteResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_promote(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            client.autoimprove_fix.with_raw_response.promote(
                "",
            )

    @parametrize
    def test_method_send_guidance(self, client: Roark) -> None:
        autoimprove_fix = client.autoimprove_fix.send_guidance(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )
        assert_matches_type(AutoimproveFixSendGuidanceResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_raw_response_send_guidance(self, client: Roark) -> None:
        response = client.autoimprove_fix.with_raw_response.send_guidance(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = response.parse()
        assert_matches_type(AutoimproveFixSendGuidanceResponse, autoimprove_fix, path=["response"])

    @parametrize
    def test_streaming_response_send_guidance(self, client: Roark) -> None:
        with client.autoimprove_fix.with_streaming_response.send_guidance(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = response.parse()
            assert_matches_type(AutoimproveFixSendGuidanceResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send_guidance(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            client.autoimprove_fix.with_raw_response.send_guidance(
                fix_id="",
                text="Keep the current voice; focus on the closing confirmation.",
            )


class TestAsyncAutoimproveFix:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        autoimprove_fix = await async_client.autoimprove_fix.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        )
        assert_matches_type(AutoimproveFixCreateResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        autoimprove_fix = await async_client.autoimprove_fix.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            customer_integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_iterations=1,
            max_sim_calls=1,
            staging_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_value=90,
            validation_run_plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixCreateResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_fix.with_raw_response.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = await response.parse()
        assert_matches_type(AutoimproveFixCreateResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_fix.with_streaming_response.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = await response.parse()
            assert_matches_type(AutoimproveFixCreateResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        autoimprove_fix = await async_client.autoimprove_fix.list()
        assert_matches_type(AutoimproveFixListResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_fix.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = await response.parse()
        assert_matches_type(AutoimproveFixListResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_fix.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = await response.parse()
            assert_matches_type(AutoimproveFixListResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_answer_question(self, async_client: AsyncRoark) -> None:
        autoimprove_fix = await async_client.autoimprove_fix.answer_question(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )
        assert_matches_type(AutoimproveFixAnswerQuestionResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_raw_response_answer_question(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_fix.with_raw_response.answer_question(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = await response.parse()
        assert_matches_type(AutoimproveFixAnswerQuestionResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_streaming_response_answer_question(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_fix.with_streaming_response.answer_question(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = await response.parse()
            assert_matches_type(AutoimproveFixAnswerQuestionResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_answer_question(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            await async_client.autoimprove_fix.with_raw_response.answer_question(
                fix_id="",
                text="Keep the current voice; focus on the closing confirmation.",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncRoark) -> None:
        autoimprove_fix = await async_client.autoimprove_fix.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixCancelResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_fix.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = await response.parse()
        assert_matches_type(AutoimproveFixCancelResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_fix.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = await response.parse()
            assert_matches_type(AutoimproveFixCancelResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            await async_client.autoimprove_fix.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_dismiss(self, async_client: AsyncRoark) -> None:
        autoimprove_fix = await async_client.autoimprove_fix.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixDismissResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_raw_response_dismiss(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_fix.with_raw_response.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = await response.parse()
        assert_matches_type(AutoimproveFixDismissResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_streaming_response_dismiss(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_fix.with_streaming_response.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = await response.parse()
            assert_matches_type(AutoimproveFixDismissResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_dismiss(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            await async_client.autoimprove_fix.with_raw_response.dismiss(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        autoimprove_fix = await async_client.autoimprove_fix.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixGetByIDResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_fix.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = await response.parse()
        assert_matches_type(AutoimproveFixGetByIDResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_fix.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = await response.parse()
            assert_matches_type(AutoimproveFixGetByIDResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            await async_client.autoimprove_fix.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_promote(self, async_client: AsyncRoark) -> None:
        autoimprove_fix = await async_client.autoimprove_fix.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveFixPromoteResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_raw_response_promote(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_fix.with_raw_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = await response.parse()
        assert_matches_type(AutoimproveFixPromoteResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_streaming_response_promote(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_fix.with_streaming_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = await response.parse()
            assert_matches_type(AutoimproveFixPromoteResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_promote(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            await async_client.autoimprove_fix.with_raw_response.promote(
                "",
            )

    @parametrize
    async def test_method_send_guidance(self, async_client: AsyncRoark) -> None:
        autoimprove_fix = await async_client.autoimprove_fix.send_guidance(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )
        assert_matches_type(AutoimproveFixSendGuidanceResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_raw_response_send_guidance(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_fix.with_raw_response.send_guidance(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_fix = await response.parse()
        assert_matches_type(AutoimproveFixSendGuidanceResponse, autoimprove_fix, path=["response"])

    @parametrize
    async def test_streaming_response_send_guidance(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_fix.with_streaming_response.send_guidance(
            fix_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_fix = await response.parse()
            assert_matches_type(AutoimproveFixSendGuidanceResponse, autoimprove_fix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send_guidance(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fix_id` but received ''"):
            await async_client.autoimprove_fix.with_raw_response.send_guidance(
                fix_id="",
                text="Keep the current voice; focus on the closing confirmation.",
            )
