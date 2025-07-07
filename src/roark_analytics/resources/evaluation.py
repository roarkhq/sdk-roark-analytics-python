# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ..types import evaluation_create_job_params, evaluation_get_job_runs_params, evaluation_get_evaluators_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.evaluation_get_job_response import EvaluationGetJobResponse
from ..types.evaluation_create_job_response import EvaluationCreateJobResponse
from ..types.evaluation_get_job_runs_response import EvaluationGetJobRunsResponse

__all__ = ["EvaluationResource", "AsyncEvaluationResource"]


class EvaluationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return EvaluationResourceWithStreamingResponse(self)

    def create_job(
        self,
        *,
        evaluators: Union[List[str], Literal["all"]],
        call: evaluation_create_job_params.Call | NotGiven = NOT_GIVEN,
        dataset: evaluation_create_job_params.Dataset | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationCreateJobResponse:
        """
        Create a evaluation job for a single call or dataset of calls

        Args:
          evaluators: List of evaluators slugs to evaluate the calls or "all" to evaluate all
              evaluators

          call: Call input to evaluate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/evaluation/job",
            body=maybe_transform(
                {
                    "evaluators": evaluators,
                    "call": call,
                    "dataset": dataset,
                },
                evaluation_create_job_params.EvaluationCreateJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationCreateJobResponse,
        )

    def get_evaluator_by_id(
        self,
        evaluator_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Returns a specific evaluator with its blocks and configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluator_id:
            raise ValueError(f"Expected a non-empty value for `evaluator_id` but received {evaluator_id!r}")
        return self._get(
            f"/v1/evaluation/evaluators/{evaluator_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_evaluators(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Returns a list of evaluators with their blocks and configuration for the
        authenticated project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/evaluation/evaluators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    evaluation_get_evaluators_params.EvaluationGetEvaluatorsParams,
                ),
            ),
            cast_to=object,
        )

    def get_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationGetJobResponse:
        """
        Retrieve details of a specific evaluation job

        Args:
          job_id: ID of the evaluation job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/evaluation/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationGetJobResponse,
        )

    def get_job_runs(
        self,
        job_id: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        next_cursor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationGetJobRunsResponse:
        """
        Retrieve paginated details of a specific evaluation job runs

        Args:
          limit: Number of items to return per page

          next_cursor: Cursor for the next page of items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/evaluation/job/{job_id}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_cursor": next_cursor,
                    },
                    evaluation_get_job_runs_params.EvaluationGetJobRunsParams,
                ),
            ),
            cast_to=EvaluationGetJobRunsResponse,
        )


class AsyncEvaluationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncEvaluationResourceWithStreamingResponse(self)

    async def create_job(
        self,
        *,
        evaluators: Union[List[str], Literal["all"]],
        call: evaluation_create_job_params.Call | NotGiven = NOT_GIVEN,
        dataset: evaluation_create_job_params.Dataset | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationCreateJobResponse:
        """
        Create a evaluation job for a single call or dataset of calls

        Args:
          evaluators: List of evaluators slugs to evaluate the calls or "all" to evaluate all
              evaluators

          call: Call input to evaluate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/evaluation/job",
            body=await async_maybe_transform(
                {
                    "evaluators": evaluators,
                    "call": call,
                    "dataset": dataset,
                },
                evaluation_create_job_params.EvaluationCreateJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationCreateJobResponse,
        )

    async def get_evaluator_by_id(
        self,
        evaluator_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Returns a specific evaluator with its blocks and configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluator_id:
            raise ValueError(f"Expected a non-empty value for `evaluator_id` but received {evaluator_id!r}")
        return await self._get(
            f"/v1/evaluation/evaluators/{evaluator_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_evaluators(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Returns a list of evaluators with their blocks and configuration for the
        authenticated project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/evaluation/evaluators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    evaluation_get_evaluators_params.EvaluationGetEvaluatorsParams,
                ),
            ),
            cast_to=object,
        )

    async def get_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationGetJobResponse:
        """
        Retrieve details of a specific evaluation job

        Args:
          job_id: ID of the evaluation job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/evaluation/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationGetJobResponse,
        )

    async def get_job_runs(
        self,
        job_id: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        next_cursor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationGetJobRunsResponse:
        """
        Retrieve paginated details of a specific evaluation job runs

        Args:
          limit: Number of items to return per page

          next_cursor: Cursor for the next page of items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/evaluation/job/{job_id}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "next_cursor": next_cursor,
                    },
                    evaluation_get_job_runs_params.EvaluationGetJobRunsParams,
                ),
            ),
            cast_to=EvaluationGetJobRunsResponse,
        )


class EvaluationResourceWithRawResponse:
    def __init__(self, evaluation: EvaluationResource) -> None:
        self._evaluation = evaluation

        self.create_job = to_raw_response_wrapper(
            evaluation.create_job,
        )
        self.get_evaluator_by_id = to_raw_response_wrapper(
            evaluation.get_evaluator_by_id,
        )
        self.get_evaluators = to_raw_response_wrapper(
            evaluation.get_evaluators,
        )
        self.get_job = to_raw_response_wrapper(
            evaluation.get_job,
        )
        self.get_job_runs = to_raw_response_wrapper(
            evaluation.get_job_runs,
        )


class AsyncEvaluationResourceWithRawResponse:
    def __init__(self, evaluation: AsyncEvaluationResource) -> None:
        self._evaluation = evaluation

        self.create_job = async_to_raw_response_wrapper(
            evaluation.create_job,
        )
        self.get_evaluator_by_id = async_to_raw_response_wrapper(
            evaluation.get_evaluator_by_id,
        )
        self.get_evaluators = async_to_raw_response_wrapper(
            evaluation.get_evaluators,
        )
        self.get_job = async_to_raw_response_wrapper(
            evaluation.get_job,
        )
        self.get_job_runs = async_to_raw_response_wrapper(
            evaluation.get_job_runs,
        )


class EvaluationResourceWithStreamingResponse:
    def __init__(self, evaluation: EvaluationResource) -> None:
        self._evaluation = evaluation

        self.create_job = to_streamed_response_wrapper(
            evaluation.create_job,
        )
        self.get_evaluator_by_id = to_streamed_response_wrapper(
            evaluation.get_evaluator_by_id,
        )
        self.get_evaluators = to_streamed_response_wrapper(
            evaluation.get_evaluators,
        )
        self.get_job = to_streamed_response_wrapper(
            evaluation.get_job,
        )
        self.get_job_runs = to_streamed_response_wrapper(
            evaluation.get_job_runs,
        )


class AsyncEvaluationResourceWithStreamingResponse:
    def __init__(self, evaluation: AsyncEvaluationResource) -> None:
        self._evaluation = evaluation

        self.create_job = async_to_streamed_response_wrapper(
            evaluation.create_job,
        )
        self.get_evaluator_by_id = async_to_streamed_response_wrapper(
            evaluation.get_evaluator_by_id,
        )
        self.get_evaluators = async_to_streamed_response_wrapper(
            evaluation.get_evaluators,
        )
        self.get_job = async_to_streamed_response_wrapper(
            evaluation.get_job,
        )
        self.get_job_runs = async_to_streamed_response_wrapper(
            evaluation.get_job_runs,
        )
