# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from roark_analytics import Roark, AsyncRoark
from roark_analytics.types import (
    LiveReportRunResponse,
    LiveReportListResponse,
    LiveReportCreateResponse,
    LiveReportDeleteResponse,
    LiveReportUpdateResponse,
    LiveReportGetByIDResponse,
    LiveReportGetDocumentResponse,
    LiveReportListDocumentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLiveReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Roark) -> None:
        live_report = client.live_report.create(
            name="x",
        )
        assert_matches_type(LiveReportCreateResponse, live_report, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Roark) -> None:
        live_report = client.live_report.create(
            name="x",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cadence="DAILY",
            dashboard_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            delivery_hour=0,
            description="description",
            filters=[{"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}],
            generate_now=True,
            include_transcript_excerpts=True,
            notifications={
                "email": {"enabled": True, "recipients": ["dev@stainless.com"]},
                "slack": [{"channel_id": "x", "channel_name": "x"}],
            },
            status="ACTIVE",
            targets=[
                {
                    "metric": "x",
                    "value": 0,
                    "aggregation": "PASS_RATE",
                    "comparator": "AT_LEAST",
                    "label": "x",
                    "pass_operator": "EQUALS",
                    "pass_value": "string",
                    "percentile": 1,
                }
            ],
            timezone="x",
        )
        assert_matches_type(LiveReportCreateResponse, live_report, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Roark) -> None:
        response = client.live_report.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = response.parse()
        assert_matches_type(LiveReportCreateResponse, live_report, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Roark) -> None:
        with client.live_report.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = response.parse()
            assert_matches_type(LiveReportCreateResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Roark) -> None:
        live_report = client.live_report.update(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportUpdateResponse, live_report, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Roark) -> None:
        live_report = client.live_report.update(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cadence="DAILY",
            dashboard_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            delivery_hour=0,
            description="description",
            filters=[{"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}],
            include_transcript_excerpts=True,
            name="x",
            notifications={
                "email": {"enabled": True, "recipients": ["dev@stainless.com"]},
                "slack": [{"channel_id": "x", "channel_name": "x"}],
            },
            status="ACTIVE",
            targets=[
                {
                    "metric": "x",
                    "value": 0,
                    "aggregation": "PASS_RATE",
                    "comparator": "AT_LEAST",
                    "label": "x",
                    "pass_operator": "EQUALS",
                    "pass_value": "string",
                    "percentile": 1,
                }
            ],
            timezone="x",
        )
        assert_matches_type(LiveReportUpdateResponse, live_report, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Roark) -> None:
        response = client.live_report.with_raw_response.update(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = response.parse()
        assert_matches_type(LiveReportUpdateResponse, live_report, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Roark) -> None:
        with client.live_report.with_streaming_response.update(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = response.parse()
            assert_matches_type(LiveReportUpdateResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.live_report.with_raw_response.update(
                report_id="",
            )

    @parametrize
    def test_method_list(self, client: Roark) -> None:
        live_report = client.live_report.list()
        assert_matches_type(LiveReportListResponse, live_report, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Roark) -> None:
        live_report = client.live_report.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(LiveReportListResponse, live_report, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Roark) -> None:
        response = client.live_report.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = response.parse()
        assert_matches_type(LiveReportListResponse, live_report, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Roark) -> None:
        with client.live_report.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = response.parse()
            assert_matches_type(LiveReportListResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Roark) -> None:
        live_report = client.live_report.delete(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportDeleteResponse, live_report, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Roark) -> None:
        response = client.live_report.with_raw_response.delete(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = response.parse()
        assert_matches_type(LiveReportDeleteResponse, live_report, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Roark) -> None:
        with client.live_report.with_streaming_response.delete(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = response.parse()
            assert_matches_type(LiveReportDeleteResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.live_report.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Roark) -> None:
        live_report = client.live_report.get_by_id(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportGetByIDResponse, live_report, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Roark) -> None:
        response = client.live_report.with_raw_response.get_by_id(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = response.parse()
        assert_matches_type(LiveReportGetByIDResponse, live_report, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Roark) -> None:
        with client.live_report.with_streaming_response.get_by_id(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = response.parse()
            assert_matches_type(LiveReportGetByIDResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.live_report.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_get_document(self, client: Roark) -> None:
        live_report = client.live_report.get_document(
            "9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportGetDocumentResponse, live_report, path=["response"])

    @parametrize
    def test_raw_response_get_document(self, client: Roark) -> None:
        response = client.live_report.with_raw_response.get_document(
            "9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = response.parse()
        assert_matches_type(LiveReportGetDocumentResponse, live_report, path=["response"])

    @parametrize
    def test_streaming_response_get_document(self, client: Roark) -> None:
        with client.live_report.with_streaming_response.get_document(
            "9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = response.parse()
            assert_matches_type(LiveReportGetDocumentResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_document(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.live_report.with_raw_response.get_document(
                "",
                report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.live_report.with_raw_response.get_document(
                "9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
                report_id="",
            )

    @parametrize
    def test_method_list_documents(self, client: Roark) -> None:
        live_report = client.live_report.list_documents(
            report_id="reportId",
        )
        assert_matches_type(LiveReportListDocumentsResponse, live_report, path=["response"])

    @parametrize
    def test_method_list_documents_with_all_params(self, client: Roark) -> None:
        live_report = client.live_report.list_documents(
            report_id="reportId",
            limit=1,
            offset=0,
        )
        assert_matches_type(LiveReportListDocumentsResponse, live_report, path=["response"])

    @parametrize
    def test_raw_response_list_documents(self, client: Roark) -> None:
        response = client.live_report.with_raw_response.list_documents(
            report_id="reportId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = response.parse()
        assert_matches_type(LiveReportListDocumentsResponse, live_report, path=["response"])

    @parametrize
    def test_streaming_response_list_documents(self, client: Roark) -> None:
        with client.live_report.with_streaming_response.list_documents(
            report_id="reportId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = response.parse()
            assert_matches_type(LiveReportListDocumentsResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_documents(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.live_report.with_raw_response.list_documents(
                report_id="",
            )

    @parametrize
    def test_method_run(self, client: Roark) -> None:
        live_report = client.live_report.run(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportRunResponse, live_report, path=["response"])

    @parametrize
    def test_method_run_with_all_params(self, client: Roark) -> None:
        live_report = client.live_report.run(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
            period_end="2019-12-27T18:11:19.117Z",
            period_start="2019-12-27T18:11:19.117Z",
        )
        assert_matches_type(LiveReportRunResponse, live_report, path=["response"])

    @parametrize
    def test_raw_response_run(self, client: Roark) -> None:
        response = client.live_report.with_raw_response.run(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = response.parse()
        assert_matches_type(LiveReportRunResponse, live_report, path=["response"])

    @parametrize
    def test_streaming_response_run(self, client: Roark) -> None:
        with client.live_report.with_streaming_response.run(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = response.parse()
            assert_matches_type(LiveReportRunResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run(self, client: Roark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.live_report.with_raw_response.run(
                report_id="",
            )


class TestAsyncLiveReport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.create(
            name="x",
        )
        assert_matches_type(LiveReportCreateResponse, live_report, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.create(
            name="x",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cadence="DAILY",
            dashboard_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            delivery_hour=0,
            description="description",
            filters=[{"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}],
            generate_now=True,
            include_transcript_excerpts=True,
            notifications={
                "email": {"enabled": True, "recipients": ["dev@stainless.com"]},
                "slack": [{"channel_id": "x", "channel_name": "x"}],
            },
            status="ACTIVE",
            targets=[
                {
                    "metric": "x",
                    "value": 0,
                    "aggregation": "PASS_RATE",
                    "comparator": "AT_LEAST",
                    "label": "x",
                    "pass_operator": "EQUALS",
                    "pass_value": "string",
                    "percentile": 1,
                }
            ],
            timezone="x",
        )
        assert_matches_type(LiveReportCreateResponse, live_report, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRoark) -> None:
        response = await async_client.live_report.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = await response.parse()
        assert_matches_type(LiveReportCreateResponse, live_report, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRoark) -> None:
        async with async_client.live_report.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = await response.parse()
            assert_matches_type(LiveReportCreateResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.update(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportUpdateResponse, live_report, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.update(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cadence="DAILY",
            dashboard_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            delivery_hour=0,
            description="description",
            filters=[{"type": "METRIC_PROPERTY", "operator": "EQUALS", "property": "property", "value": "string"}],
            include_transcript_excerpts=True,
            name="x",
            notifications={
                "email": {"enabled": True, "recipients": ["dev@stainless.com"]},
                "slack": [{"channel_id": "x", "channel_name": "x"}],
            },
            status="ACTIVE",
            targets=[
                {
                    "metric": "x",
                    "value": 0,
                    "aggregation": "PASS_RATE",
                    "comparator": "AT_LEAST",
                    "label": "x",
                    "pass_operator": "EQUALS",
                    "pass_value": "string",
                    "percentile": 1,
                }
            ],
            timezone="x",
        )
        assert_matches_type(LiveReportUpdateResponse, live_report, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRoark) -> None:
        response = await async_client.live_report.with_raw_response.update(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = await response.parse()
        assert_matches_type(LiveReportUpdateResponse, live_report, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRoark) -> None:
        async with async_client.live_report.with_streaming_response.update(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = await response.parse()
            assert_matches_type(LiveReportUpdateResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.live_report.with_raw_response.update(
                report_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.list()
        assert_matches_type(LiveReportListResponse, live_report, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(LiveReportListResponse, live_report, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRoark) -> None:
        response = await async_client.live_report.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = await response.parse()
        assert_matches_type(LiveReportListResponse, live_report, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRoark) -> None:
        async with async_client.live_report.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = await response.parse()
            assert_matches_type(LiveReportListResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.delete(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportDeleteResponse, live_report, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRoark) -> None:
        response = await async_client.live_report.with_raw_response.delete(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = await response.parse()
        assert_matches_type(LiveReportDeleteResponse, live_report, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRoark) -> None:
        async with async_client.live_report.with_streaming_response.delete(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = await response.parse()
            assert_matches_type(LiveReportDeleteResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.live_report.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.get_by_id(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportGetByIDResponse, live_report, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncRoark) -> None:
        response = await async_client.live_report.with_raw_response.get_by_id(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = await response.parse()
        assert_matches_type(LiveReportGetByIDResponse, live_report, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncRoark) -> None:
        async with async_client.live_report.with_streaming_response.get_by_id(
            "5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = await response.parse()
            assert_matches_type(LiveReportGetByIDResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.live_report.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_get_document(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.get_document(
            "9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportGetDocumentResponse, live_report, path=["response"])

    @parametrize
    async def test_raw_response_get_document(self, async_client: AsyncRoark) -> None:
        response = await async_client.live_report.with_raw_response.get_document(
            "9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = await response.parse()
        assert_matches_type(LiveReportGetDocumentResponse, live_report, path=["response"])

    @parametrize
    async def test_streaming_response_get_document(self, async_client: AsyncRoark) -> None:
        async with async_client.live_report.with_streaming_response.get_document(
            "9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = await response.parse()
            assert_matches_type(LiveReportGetDocumentResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_document(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.live_report.with_raw_response.get_document(
                "",
                report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.live_report.with_raw_response.get_document(
                "9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
                report_id="",
            )

    @parametrize
    async def test_method_list_documents(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.list_documents(
            report_id="reportId",
        )
        assert_matches_type(LiveReportListDocumentsResponse, live_report, path=["response"])

    @parametrize
    async def test_method_list_documents_with_all_params(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.list_documents(
            report_id="reportId",
            limit=1,
            offset=0,
        )
        assert_matches_type(LiveReportListDocumentsResponse, live_report, path=["response"])

    @parametrize
    async def test_raw_response_list_documents(self, async_client: AsyncRoark) -> None:
        response = await async_client.live_report.with_raw_response.list_documents(
            report_id="reportId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = await response.parse()
        assert_matches_type(LiveReportListDocumentsResponse, live_report, path=["response"])

    @parametrize
    async def test_streaming_response_list_documents(self, async_client: AsyncRoark) -> None:
        async with async_client.live_report.with_streaming_response.list_documents(
            report_id="reportId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = await response.parse()
            assert_matches_type(LiveReportListDocumentsResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_documents(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.live_report.with_raw_response.list_documents(
                report_id="",
            )

    @parametrize
    async def test_method_run(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.run(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )
        assert_matches_type(LiveReportRunResponse, live_report, path=["response"])

    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncRoark) -> None:
        live_report = await async_client.live_report.run(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
            period_end="2019-12-27T18:11:19.117Z",
            period_start="2019-12-27T18:11:19.117Z",
        )
        assert_matches_type(LiveReportRunResponse, live_report, path=["response"])

    @parametrize
    async def test_raw_response_run(self, async_client: AsyncRoark) -> None:
        response = await async_client.live_report.with_raw_response.run(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_report = await response.parse()
        assert_matches_type(LiveReportRunResponse, live_report, path=["response"])

    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncRoark) -> None:
        async with async_client.live_report.with_streaming_response.run(
            report_id="5c6d7e8f-9a0b-4c1d-8e2f-3a4b5c6d7e8f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_report = await response.parse()
            assert_matches_type(LiveReportRunResponse, live_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run(self, async_client: AsyncRoark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.live_report.with_raw_response.run(
                report_id="",
            )
