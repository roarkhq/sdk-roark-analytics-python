# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import metric_create_definition_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.metric_list_definitions_response import MetricListDefinitionsResponse
from ..types.metric_create_definition_response import MetricCreateDefinitionResponse

__all__ = ["MetricResource", "AsyncMetricResource"]


class MetricResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return MetricResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return MetricResourceWithStreamingResponse(self)

    def create_definition(
        self,
        *,
        analysis_package_id: str,
        name: str,
        output_type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"],
        boolean_false_label: str | Omit = omit,
        boolean_true_label: str | Omit = omit,
        classification_options: Iterable[metric_create_definition_params.ClassificationOption] | Omit = omit,
        llm_prompt: str | Omit = omit,
        max_classifications: int | Omit = omit,
        metric_id: str | Omit = omit,
        participant_role: Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"] | Omit = omit,
        scale_labels: Iterable[metric_create_definition_params.ScaleLabel] | Omit = omit,
        scale_max: int | Omit = omit,
        scale_min: int | Omit = omit,
        scope: Literal["GLOBAL", "PER_PARTICIPANT"] | Omit = omit,
        supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        """Create a new custom metric definition.

        The metric will be added to the specified
        analysis package and can be used for evaluating calls.

        Args:
          analysis_package_id: ID of the analysis package to add this metric to

          name: Name of the metric

          output_type: Type of value this metric produces

          boolean_false_label: Label for the false/negative case (only for BOOLEAN type)

          boolean_true_label: Label for the true/positive case (only for BOOLEAN type)

          classification_options: Options for classification. Required for CLASSIFICATION type.

          llm_prompt: LLM prompt/criteria for evaluating this metric. Used to instruct the model on
              how to score. Required for BOOLEAN, NUMERIC, TEXT, and SCALE types.

          max_classifications: Maximum number of classifications that can be selected (only for CLASSIFICATION
              type)

          metric_id: Unique identifier for the metric (e.g. "customer_satisfaction"). Auto-generated
              from name if not provided.

          participant_role: Participant role to evaluate. Required when scope is PER_PARTICIPANT.

          scale_labels: Labels for scale ranges (only for SCALE type)

          scale_max: Maximum value for scale. Required for SCALE type.

          scale_min: Minimum value for scale. Required for SCALE type.

          scope: Whether metric is global or per-participant (default: GLOBAL)

          supported_contexts: Which levels this metric can produce values at (default: ["CALL"])

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/metric/definitions",
            body=maybe_transform(
                {
                    "analysis_package_id": analysis_package_id,
                    "name": name,
                    "output_type": output_type,
                    "boolean_false_label": boolean_false_label,
                    "boolean_true_label": boolean_true_label,
                    "classification_options": classification_options,
                    "llm_prompt": llm_prompt,
                    "max_classifications": max_classifications,
                    "metric_id": metric_id,
                    "participant_role": participant_role,
                    "scale_labels": scale_labels,
                    "scale_max": scale_max,
                    "scale_min": scale_min,
                    "scope": scope,
                    "supported_contexts": supported_contexts,
                },
                metric_create_definition_params.MetricCreateDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricCreateDefinitionResponse,
        )

    def list_definitions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricListDefinitionsResponse:
        """
        Fetch all metric definitions available in the project, including both
        system-generated and custom metrics. Only returns metrics from enabled analysis
        packages.
        """
        return self._get(
            "/v1/metric/definitions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricListDefinitionsResponse,
        )


class AsyncMetricResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncMetricResourceWithStreamingResponse(self)

    async def create_definition(
        self,
        *,
        analysis_package_id: str,
        name: str,
        output_type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"],
        boolean_false_label: str | Omit = omit,
        boolean_true_label: str | Omit = omit,
        classification_options: Iterable[metric_create_definition_params.ClassificationOption] | Omit = omit,
        llm_prompt: str | Omit = omit,
        max_classifications: int | Omit = omit,
        metric_id: str | Omit = omit,
        participant_role: Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"] | Omit = omit,
        scale_labels: Iterable[metric_create_definition_params.ScaleLabel] | Omit = omit,
        scale_max: int | Omit = omit,
        scale_min: int | Omit = omit,
        scope: Literal["GLOBAL", "PER_PARTICIPANT"] | Omit = omit,
        supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        """Create a new custom metric definition.

        The metric will be added to the specified
        analysis package and can be used for evaluating calls.

        Args:
          analysis_package_id: ID of the analysis package to add this metric to

          name: Name of the metric

          output_type: Type of value this metric produces

          boolean_false_label: Label for the false/negative case (only for BOOLEAN type)

          boolean_true_label: Label for the true/positive case (only for BOOLEAN type)

          classification_options: Options for classification. Required for CLASSIFICATION type.

          llm_prompt: LLM prompt/criteria for evaluating this metric. Used to instruct the model on
              how to score. Required for BOOLEAN, NUMERIC, TEXT, and SCALE types.

          max_classifications: Maximum number of classifications that can be selected (only for CLASSIFICATION
              type)

          metric_id: Unique identifier for the metric (e.g. "customer_satisfaction"). Auto-generated
              from name if not provided.

          participant_role: Participant role to evaluate. Required when scope is PER_PARTICIPANT.

          scale_labels: Labels for scale ranges (only for SCALE type)

          scale_max: Maximum value for scale. Required for SCALE type.

          scale_min: Minimum value for scale. Required for SCALE type.

          scope: Whether metric is global or per-participant (default: GLOBAL)

          supported_contexts: Which levels this metric can produce values at (default: ["CALL"])

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/metric/definitions",
            body=await async_maybe_transform(
                {
                    "analysis_package_id": analysis_package_id,
                    "name": name,
                    "output_type": output_type,
                    "boolean_false_label": boolean_false_label,
                    "boolean_true_label": boolean_true_label,
                    "classification_options": classification_options,
                    "llm_prompt": llm_prompt,
                    "max_classifications": max_classifications,
                    "metric_id": metric_id,
                    "participant_role": participant_role,
                    "scale_labels": scale_labels,
                    "scale_max": scale_max,
                    "scale_min": scale_min,
                    "scope": scope,
                    "supported_contexts": supported_contexts,
                },
                metric_create_definition_params.MetricCreateDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricCreateDefinitionResponse,
        )

    async def list_definitions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricListDefinitionsResponse:
        """
        Fetch all metric definitions available in the project, including both
        system-generated and custom metrics. Only returns metrics from enabled analysis
        packages.
        """
        return await self._get(
            "/v1/metric/definitions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricListDefinitionsResponse,
        )


class MetricResourceWithRawResponse:
    def __init__(self, metric: MetricResource) -> None:
        self._metric = metric

        self.create_definition = to_raw_response_wrapper(
            metric.create_definition,
        )
        self.list_definitions = to_raw_response_wrapper(
            metric.list_definitions,
        )


class AsyncMetricResourceWithRawResponse:
    def __init__(self, metric: AsyncMetricResource) -> None:
        self._metric = metric

        self.create_definition = async_to_raw_response_wrapper(
            metric.create_definition,
        )
        self.list_definitions = async_to_raw_response_wrapper(
            metric.list_definitions,
        )


class MetricResourceWithStreamingResponse:
    def __init__(self, metric: MetricResource) -> None:
        self._metric = metric

        self.create_definition = to_streamed_response_wrapper(
            metric.create_definition,
        )
        self.list_definitions = to_streamed_response_wrapper(
            metric.list_definitions,
        )


class AsyncMetricResourceWithStreamingResponse:
    def __init__(self, metric: AsyncMetricResource) -> None:
        self._metric = metric

        self.create_definition = async_to_streamed_response_wrapper(
            metric.create_definition,
        )
        self.list_definitions = async_to_streamed_response_wrapper(
            metric.list_definitions,
        )
