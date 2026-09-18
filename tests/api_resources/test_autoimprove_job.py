# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    AutoimproveJobListResponse,
    AutoimproveJobCancelResponse,
    AutoimproveJobCreateResponse,
    AutoimproveJobDismissResponse,
    AutoimproveJobGetByIDResponse,
    AutoimproveJobPromoteResponse,
    AutoimproveJobSendGuidanceResponse,
    AutoimproveJobAnswerQuestionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutoimproveJob:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        autoimprove_job = client.autoimprove_job.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        )
        assert_matches_type(AutoimproveJobCreateResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        autoimprove_job = client.autoimprove_job.create(
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
        assert_matches_type(AutoimproveJobCreateResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.autoimprove_job.with_raw_response.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = response.parse()
        assert_matches_type(AutoimproveJobCreateResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.autoimprove_job.with_streaming_response.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = response.parse()
            assert_matches_type(AutoimproveJobCreateResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        autoimprove_job = client.autoimprove_job.list()
        assert_matches_type(AutoimproveJobListResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.autoimprove_job.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = response.parse()
        assert_matches_type(AutoimproveJobListResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.autoimprove_job.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = response.parse()
            assert_matches_type(AutoimproveJobListResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_answer_question(self, client: Roark) -> None:
        autoimprove_job = client.autoimprove_job.answer_question(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )
        assert_matches_type(AutoimproveJobAnswerQuestionResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_raw_response_answer_question(self, client: Roark) -> None:
        response = client.autoimprove_job.with_raw_response.answer_question(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = response.parse()
        assert_matches_type(AutoimproveJobAnswerQuestionResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_streaming_response_answer_question(self, client: Roark) -> None:
        with client.autoimprove_job.with_streaming_response.answer_question(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = response.parse()
            assert_matches_type(AutoimproveJobAnswerQuestionResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_answer_question(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.autoimprove_job.with_raw_response.answer_question(
                job_id="",
                text="Keep the current voice; focus on the closing confirmation.",
            )

    @parametrize
    def test_method_cancel(self, client: Roark) -> None:
        autoimprove_job = client.autoimprove_job.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveJobCancelResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Roark) -> None:
        response = client.autoimprove_job.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = response.parse()
        assert_matches_type(AutoimproveJobCancelResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Roark) -> None:
        with client.autoimprove_job.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = response.parse()
            assert_matches_type(AutoimproveJobCancelResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.autoimprove_job.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_dismiss(self, client: Roark) -> None:
        autoimprove_job = client.autoimprove_job.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveJobDismissResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_raw_response_dismiss(self, client: Roark) -> None:
        response = client.autoimprove_job.with_raw_response.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = response.parse()
        assert_matches_type(AutoimproveJobDismissResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_streaming_response_dismiss(self, client: Roark) -> None:
        with client.autoimprove_job.with_streaming_response.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = response.parse()
            assert_matches_type(AutoimproveJobDismissResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_dismiss(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.autoimprove_job.with_raw_response.dismiss(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        autoimprove_job = client.autoimprove_job.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveJobGetByIDResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.autoimprove_job.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = response.parse()
        assert_matches_type(AutoimproveJobGetByIDResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.autoimprove_job.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = response.parse()
            assert_matches_type(AutoimproveJobGetByIDResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.autoimprove_job.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_promote(self, client: Roark) -> None:
        autoimprove_job = client.autoimprove_job.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveJobPromoteResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_raw_response_promote(self, client: Roark) -> None:
        response = client.autoimprove_job.with_raw_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = response.parse()
        assert_matches_type(AutoimproveJobPromoteResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_streaming_response_promote(self, client: Roark) -> None:
        with client.autoimprove_job.with_streaming_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = response.parse()
            assert_matches_type(AutoimproveJobPromoteResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_promote(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.autoimprove_job.with_raw_response.promote(
                "",
            )

    @parametrize
    def test_method_send_guidance(self, client: Roark) -> None:
        autoimprove_job = client.autoimprove_job.send_guidance(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )
        assert_matches_type(AutoimproveJobSendGuidanceResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_raw_response_send_guidance(self, client: Roark) -> None:
        response = client.autoimprove_job.with_raw_response.send_guidance(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = response.parse()
        assert_matches_type(AutoimproveJobSendGuidanceResponse, autoimprove_job, path=["response"])

    @parametrize
    def test_streaming_response_send_guidance(self, client: Roark) -> None:
        with client.autoimprove_job.with_streaming_response.send_guidance(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = response.parse()
            assert_matches_type(AutoimproveJobSendGuidanceResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send_guidance(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.autoimprove_job.with_raw_response.send_guidance(
                job_id="",
                text="Keep the current voice; focus on the closing confirmation.",
            )


class TestAsyncAutoimproveJob:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        autoimprove_job = await async_client.autoimprove_job.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        )
        assert_matches_type(AutoimproveJobCreateResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        autoimprove_job = await async_client.autoimprove_job.create(
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
        assert_matches_type(AutoimproveJobCreateResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_job.with_raw_response.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = await response.parse()
        assert_matches_type(AutoimproveJobCreateResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_job.with_streaming_response.create(
            agent_id="b3b0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
            objective_label="Consent collection should pass",
            objective_metric_definition_id="f2f0c8e2-4c1d-4f6a-9e2b-1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = await response.parse()
            assert_matches_type(AutoimproveJobCreateResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        autoimprove_job = await async_client.autoimprove_job.list()
        assert_matches_type(AutoimproveJobListResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_job.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = await response.parse()
        assert_matches_type(AutoimproveJobListResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_job.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = await response.parse()
            assert_matches_type(AutoimproveJobListResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_answer_question(self, async_client: AsyncRoark) -> None:
        autoimprove_job = await async_client.autoimprove_job.answer_question(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )
        assert_matches_type(AutoimproveJobAnswerQuestionResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_raw_response_answer_question(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_job.with_raw_response.answer_question(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = await response.parse()
        assert_matches_type(AutoimproveJobAnswerQuestionResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_streaming_response_answer_question(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_job.with_streaming_response.answer_question(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = await response.parse()
            assert_matches_type(AutoimproveJobAnswerQuestionResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_answer_question(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.autoimprove_job.with_raw_response.answer_question(
                job_id="",
                text="Keep the current voice; focus on the closing confirmation.",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncRoark) -> None:
        autoimprove_job = await async_client.autoimprove_job.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveJobCancelResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_job.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = await response.parse()
        assert_matches_type(AutoimproveJobCancelResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_job.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = await response.parse()
            assert_matches_type(AutoimproveJobCancelResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.autoimprove_job.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_dismiss(self, async_client: AsyncRoark) -> None:
        autoimprove_job = await async_client.autoimprove_job.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveJobDismissResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_raw_response_dismiss(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_job.with_raw_response.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = await response.parse()
        assert_matches_type(AutoimproveJobDismissResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_streaming_response_dismiss(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_job.with_streaming_response.dismiss(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = await response.parse()
            assert_matches_type(AutoimproveJobDismissResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_dismiss(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.autoimprove_job.with_raw_response.dismiss(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        autoimprove_job = await async_client.autoimprove_job.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveJobGetByIDResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_job.with_raw_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = await response.parse()
        assert_matches_type(AutoimproveJobGetByIDResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_job.with_streaming_response.get_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = await response.parse()
            assert_matches_type(AutoimproveJobGetByIDResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.autoimprove_job.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_promote(self, async_client: AsyncRoark) -> None:
        autoimprove_job = await async_client.autoimprove_job.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoimproveJobPromoteResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_raw_response_promote(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_job.with_raw_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = await response.parse()
        assert_matches_type(AutoimproveJobPromoteResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_streaming_response_promote(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_job.with_streaming_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = await response.parse()
            assert_matches_type(AutoimproveJobPromoteResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_promote(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.autoimprove_job.with_raw_response.promote(
                "",
            )

    @parametrize
    async def test_method_send_guidance(self, async_client: AsyncRoark) -> None:
        autoimprove_job = await async_client.autoimprove_job.send_guidance(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )
        assert_matches_type(AutoimproveJobSendGuidanceResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_raw_response_send_guidance(self, async_client: AsyncRoark) -> None:
        response = await async_client.autoimprove_job.with_raw_response.send_guidance(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoimprove_job = await response.parse()
        assert_matches_type(AutoimproveJobSendGuidanceResponse, autoimprove_job, path=["response"])

    @parametrize
    async def test_streaming_response_send_guidance(self, async_client: AsyncRoark) -> None:
        async with async_client.autoimprove_job.with_streaming_response.send_guidance(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="Keep the current voice; focus on the closing confirmation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoimprove_job = await response.parse()
            assert_matches_type(AutoimproveJobSendGuidanceResponse, autoimprove_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send_guidance(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.autoimprove_job.with_raw_response.send_guidance(
                job_id="",
                text="Keep the current voice; focus on the closing confirmation.",
            )
