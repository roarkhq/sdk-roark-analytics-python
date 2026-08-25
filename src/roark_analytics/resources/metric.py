# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, overload
from typing_extensions import Literal

import httpx

from ..types import metric_create_definition_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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

    @overload
    def create_definition(
        self,
        *,
        analysis_package_id: str,
        calculation_type: Literal["LLM_JUDGE"],
        name: str,
        output_type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"],
        boolean_false_label: str | Omit = omit,
        boolean_true_label: str | Omit = omit,
        classification_options: Iterable[metric_create_definition_params.PromptMetricInputClassificationOption]
        | Omit = omit,
        llm_prompt: str | Omit = omit,
        max_classifications: int | Omit = omit,
        metric_id: str | Omit = omit,
        participant_role: Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"] | Omit = omit,
        scale_labels: Iterable[metric_create_definition_params.PromptMetricInputScaleLabel] | Omit = omit,
        scale_max: int | Omit = omit,
        scale_min: int | Omit = omit,
        scope: Literal["GLOBAL", "PER_PARTICIPANT"] | Omit = omit,
        slug: str | Omit = omit,
        supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        """Create a new metric definition.

        The `calculationType` field selects the variant:
        LLM_JUDGE (LLM-evaluated), FORMULA (computed from a math expression over other
        metrics), or PATTERN (detects a trigger→outcome pattern within a window). To
        create a threshold on top of an existing metric, use `POST
        /metric/definitions/{idOrSlug}/thresholds` instead.

        Args:
          analysis_package_id: ID of the analysis package to add this metric to

          calculation_type: LLM-evaluated metric.

          name: Name of the metric

          output_type: Type of value this metric produces

          boolean_false_label: Label for the false case (only for BOOLEAN type)

          boolean_true_label: Label for the true case (only for BOOLEAN type)

          classification_options: Options for classification. Required for CLASSIFICATION type.

          llm_prompt: LLM prompt/criteria for evaluating this metric. Required for BOOLEAN, NUMERIC,
              TEXT, and SCALE types.

          max_classifications: Maximum number of classifications that can be selected (only for CLASSIFICATION
              type)

          metric_id: Alias of `slug` accepted for backwards compatibility. Use `slug` for new
              integrations.

          participant_role: Participant role to evaluate. Required when scope is PER_PARTICIPANT.

          scale_labels: Labels for scale ranges (only for SCALE type)

          scale_max: Maximum value for scale. Required for SCALE type.

          scale_min: Minimum value for scale. Required for SCALE type.

          scope: Whether metric is global or per-participant (default: GLOBAL)

          slug: Stable slug for the metric. Auto-generated from name if omitted.

          supported_contexts: Which levels this metric can produce values at (default: ["CALL"])

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_definition(
        self,
        *,
        analysis_package_id: str,
        calculation_type: Literal["FORMULA"],
        formula: str,
        name: str,
        output_type: Literal["NUMERIC", "BOOLEAN"],
        sources: Iterable[metric_create_definition_params.FormulaMetricInputSource],
        metric_id: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        """Create a new metric definition.

        The `calculationType` field selects the variant:
        LLM_JUDGE (LLM-evaluated), FORMULA (computed from a math expression over other
        metrics), or PATTERN (detects a trigger→outcome pattern within a window). To
        create a threshold on top of an existing metric, use `POST
        /metric/definitions/{idOrSlug}/thresholds` instead.

        Args:
          analysis_package_id: ID of the analysis package to add this metric to

          calculation_type: Metric computed by evaluating a mathematical expression over other metrics.

          formula: Formula expression using `{{id:<uuid>}}` references to source metrics. Operators
              depend on output type: +, -, *, / for NUMERIC; ==, !=, >=, <=, >, < for BOOLEAN.

          name: Name of the metric

          output_type: Output type of the formula. NUMERIC for arithmetic expressions, BOOLEAN for
              comparison expressions.

          sources: Source metrics referenced by the formula. Minimum 2.

          metric_id: Alias of `slug` accepted for backwards compatibility. Use `slug` for new
              integrations.

          slug: Stable slug for the metric. Auto-generated from name if omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_definition(
        self,
        *,
        analysis_package_id: str,
        calculation_type: Literal["PATTERN"],
        name: str,
        operation: Literal["PATTERN_EXISTS", "PATTERN_COUNT", "OUTCOME_AGGREGATE"],
        outcome: metric_create_definition_params.PatternMetricInputOutcome,
        metric_id: str | Omit = omit,
        slug: str | Omit = omit,
        trigger: metric_create_definition_params.PatternMetricInputTrigger | Omit = omit,
        trigger_combinator: Literal["AND", "OR"] | Omit = omit,
        triggers: Iterable[metric_create_definition_params.PatternMetricInputTrigger] | Omit = omit,
        window_mode: Literal["seconds", "segments"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        """Create a new metric definition.

        The `calculationType` field selects the variant:
        LLM_JUDGE (LLM-evaluated), FORMULA (computed from a math expression over other
        metrics), or PATTERN (detects a trigger→outcome pattern within a window). To
        create a threshold on top of an existing metric, use `POST
        /metric/definitions/{idOrSlug}/thresholds` instead.

        Args:
          analysis_package_id: ID of the analysis package to add this metric to

          calculation_type: Metric detecting temporal patterns: a trigger condition followed by an outcome
              within a window.

          name: Name of the metric

          operation: Pattern operation. PATTERN_EXISTS produces a BOOLEAN; PATTERN_COUNT produces a
              NUMERIC count; OUTCOME_AGGREGATE aggregates a numeric outcome.

          outcome: Outcome condition evaluated within the window relative to the trigger.

          metric_id: Alias of `slug` accepted for backwards compatibility. Use `slug` for new
              integrations.

          slug: Stable slug for the metric. Auto-generated from name if omitted.

          trigger: Single trigger condition. Use either trigger or triggers + triggerCombinator.

          trigger_combinator: How to combine multiple triggers. Required when triggers has more than 1 entry.

          triggers: Multiple trigger conditions. Use with triggerCombinator.

          window_mode: Unit for trigger/outcome window values (default: seconds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["analysis_package_id", "calculation_type", "name", "output_type"],
        ["analysis_package_id", "calculation_type", "formula", "name", "output_type", "sources"],
        ["analysis_package_id", "calculation_type", "name", "operation", "outcome"],
    )
    def create_definition(
        self,
        *,
        analysis_package_id: str,
        calculation_type: Literal["LLM_JUDGE", "FORMULA", "PATTERN"],
        name: str,
        output_type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"] | Omit = omit,
        boolean_false_label: str | Omit = omit,
        boolean_true_label: str | Omit = omit,
        classification_options: Iterable[metric_create_definition_params.PromptMetricInputClassificationOption]
        | Omit = omit,
        llm_prompt: str | Omit = omit,
        max_classifications: int | Omit = omit,
        metric_id: str | Omit = omit,
        participant_role: Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"] | Omit = omit,
        scale_labels: Iterable[metric_create_definition_params.PromptMetricInputScaleLabel] | Omit = omit,
        scale_max: int | Omit = omit,
        scale_min: int | Omit = omit,
        scope: Literal["GLOBAL", "PER_PARTICIPANT"] | Omit = omit,
        slug: str | Omit = omit,
        supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] | Omit = omit,
        formula: str | Omit = omit,
        sources: Iterable[metric_create_definition_params.FormulaMetricInputSource] | Omit = omit,
        operation: Literal["PATTERN_EXISTS", "PATTERN_COUNT", "OUTCOME_AGGREGATE"] | Omit = omit,
        outcome: metric_create_definition_params.PatternMetricInputOutcome | Omit = omit,
        trigger: metric_create_definition_params.PatternMetricInputTrigger | Omit = omit,
        trigger_combinator: Literal["AND", "OR"] | Omit = omit,
        triggers: Iterable[metric_create_definition_params.PatternMetricInputTrigger] | Omit = omit,
        window_mode: Literal["seconds", "segments"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        return self._post(
            "/v1/metric/definitions",
            body=maybe_transform(
                {
                    "analysis_package_id": analysis_package_id,
                    "calculation_type": calculation_type,
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
                    "slug": slug,
                    "supported_contexts": supported_contexts,
                    "formula": formula,
                    "sources": sources,
                    "operation": operation,
                    "outcome": outcome,
                    "trigger": trigger,
                    "trigger_combinator": trigger_combinator,
                    "triggers": triggers,
                    "window_mode": window_mode,
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
        system-generated and custom metrics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

    @overload
    async def create_definition(
        self,
        *,
        analysis_package_id: str,
        calculation_type: Literal["LLM_JUDGE"],
        name: str,
        output_type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"],
        boolean_false_label: str | Omit = omit,
        boolean_true_label: str | Omit = omit,
        classification_options: Iterable[metric_create_definition_params.PromptMetricInputClassificationOption]
        | Omit = omit,
        llm_prompt: str | Omit = omit,
        max_classifications: int | Omit = omit,
        metric_id: str | Omit = omit,
        participant_role: Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"] | Omit = omit,
        scale_labels: Iterable[metric_create_definition_params.PromptMetricInputScaleLabel] | Omit = omit,
        scale_max: int | Omit = omit,
        scale_min: int | Omit = omit,
        scope: Literal["GLOBAL", "PER_PARTICIPANT"] | Omit = omit,
        slug: str | Omit = omit,
        supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        """Create a new metric definition.

        The `calculationType` field selects the variant:
        LLM_JUDGE (LLM-evaluated), FORMULA (computed from a math expression over other
        metrics), or PATTERN (detects a trigger→outcome pattern within a window). To
        create a threshold on top of an existing metric, use `POST
        /metric/definitions/{idOrSlug}/thresholds` instead.

        Args:
          analysis_package_id: ID of the analysis package to add this metric to

          calculation_type: LLM-evaluated metric.

          name: Name of the metric

          output_type: Type of value this metric produces

          boolean_false_label: Label for the false case (only for BOOLEAN type)

          boolean_true_label: Label for the true case (only for BOOLEAN type)

          classification_options: Options for classification. Required for CLASSIFICATION type.

          llm_prompt: LLM prompt/criteria for evaluating this metric. Required for BOOLEAN, NUMERIC,
              TEXT, and SCALE types.

          max_classifications: Maximum number of classifications that can be selected (only for CLASSIFICATION
              type)

          metric_id: Alias of `slug` accepted for backwards compatibility. Use `slug` for new
              integrations.

          participant_role: Participant role to evaluate. Required when scope is PER_PARTICIPANT.

          scale_labels: Labels for scale ranges (only for SCALE type)

          scale_max: Maximum value for scale. Required for SCALE type.

          scale_min: Minimum value for scale. Required for SCALE type.

          scope: Whether metric is global or per-participant (default: GLOBAL)

          slug: Stable slug for the metric. Auto-generated from name if omitted.

          supported_contexts: Which levels this metric can produce values at (default: ["CALL"])

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_definition(
        self,
        *,
        analysis_package_id: str,
        calculation_type: Literal["FORMULA"],
        formula: str,
        name: str,
        output_type: Literal["NUMERIC", "BOOLEAN"],
        sources: Iterable[metric_create_definition_params.FormulaMetricInputSource],
        metric_id: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        """Create a new metric definition.

        The `calculationType` field selects the variant:
        LLM_JUDGE (LLM-evaluated), FORMULA (computed from a math expression over other
        metrics), or PATTERN (detects a trigger→outcome pattern within a window). To
        create a threshold on top of an existing metric, use `POST
        /metric/definitions/{idOrSlug}/thresholds` instead.

        Args:
          analysis_package_id: ID of the analysis package to add this metric to

          calculation_type: Metric computed by evaluating a mathematical expression over other metrics.

          formula: Formula expression using `{{id:<uuid>}}` references to source metrics. Operators
              depend on output type: +, -, *, / for NUMERIC; ==, !=, >=, <=, >, < for BOOLEAN.

          name: Name of the metric

          output_type: Output type of the formula. NUMERIC for arithmetic expressions, BOOLEAN for
              comparison expressions.

          sources: Source metrics referenced by the formula. Minimum 2.

          metric_id: Alias of `slug` accepted for backwards compatibility. Use `slug` for new
              integrations.

          slug: Stable slug for the metric. Auto-generated from name if omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_definition(
        self,
        *,
        analysis_package_id: str,
        calculation_type: Literal["PATTERN"],
        name: str,
        operation: Literal["PATTERN_EXISTS", "PATTERN_COUNT", "OUTCOME_AGGREGATE"],
        outcome: metric_create_definition_params.PatternMetricInputOutcome,
        metric_id: str | Omit = omit,
        slug: str | Omit = omit,
        trigger: metric_create_definition_params.PatternMetricInputTrigger | Omit = omit,
        trigger_combinator: Literal["AND", "OR"] | Omit = omit,
        triggers: Iterable[metric_create_definition_params.PatternMetricInputTrigger] | Omit = omit,
        window_mode: Literal["seconds", "segments"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        """Create a new metric definition.

        The `calculationType` field selects the variant:
        LLM_JUDGE (LLM-evaluated), FORMULA (computed from a math expression over other
        metrics), or PATTERN (detects a trigger→outcome pattern within a window). To
        create a threshold on top of an existing metric, use `POST
        /metric/definitions/{idOrSlug}/thresholds` instead.

        Args:
          analysis_package_id: ID of the analysis package to add this metric to

          calculation_type: Metric detecting temporal patterns: a trigger condition followed by an outcome
              within a window.

          name: Name of the metric

          operation: Pattern operation. PATTERN_EXISTS produces a BOOLEAN; PATTERN_COUNT produces a
              NUMERIC count; OUTCOME_AGGREGATE aggregates a numeric outcome.

          outcome: Outcome condition evaluated within the window relative to the trigger.

          metric_id: Alias of `slug` accepted for backwards compatibility. Use `slug` for new
              integrations.

          slug: Stable slug for the metric. Auto-generated from name if omitted.

          trigger: Single trigger condition. Use either trigger or triggers + triggerCombinator.

          trigger_combinator: How to combine multiple triggers. Required when triggers has more than 1 entry.

          triggers: Multiple trigger conditions. Use with triggerCombinator.

          window_mode: Unit for trigger/outcome window values (default: seconds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["analysis_package_id", "calculation_type", "name", "output_type"],
        ["analysis_package_id", "calculation_type", "formula", "name", "output_type", "sources"],
        ["analysis_package_id", "calculation_type", "name", "operation", "outcome"],
    )
    async def create_definition(
        self,
        *,
        analysis_package_id: str,
        calculation_type: Literal["LLM_JUDGE", "FORMULA", "PATTERN"],
        name: str,
        output_type: Literal["COUNT", "NUMERIC", "BOOLEAN", "SCALE", "TEXT", "CLASSIFICATION", "OFFSET"] | Omit = omit,
        boolean_false_label: str | Omit = omit,
        boolean_true_label: str | Omit = omit,
        classification_options: Iterable[metric_create_definition_params.PromptMetricInputClassificationOption]
        | Omit = omit,
        llm_prompt: str | Omit = omit,
        max_classifications: int | Omit = omit,
        metric_id: str | Omit = omit,
        participant_role: Literal["AGENT", "CUSTOMER", "SIMULATED_CUSTOMER", "BACKGROUND_SPEAKER"] | Omit = omit,
        scale_labels: Iterable[metric_create_definition_params.PromptMetricInputScaleLabel] | Omit = omit,
        scale_max: int | Omit = omit,
        scale_min: int | Omit = omit,
        scope: Literal["GLOBAL", "PER_PARTICIPANT"] | Omit = omit,
        slug: str | Omit = omit,
        supported_contexts: List[Literal["CALL", "SEGMENT", "TURN"]] | Omit = omit,
        formula: str | Omit = omit,
        sources: Iterable[metric_create_definition_params.FormulaMetricInputSource] | Omit = omit,
        operation: Literal["PATTERN_EXISTS", "PATTERN_COUNT", "OUTCOME_AGGREGATE"] | Omit = omit,
        outcome: metric_create_definition_params.PatternMetricInputOutcome | Omit = omit,
        trigger: metric_create_definition_params.PatternMetricInputTrigger | Omit = omit,
        trigger_combinator: Literal["AND", "OR"] | Omit = omit,
        triggers: Iterable[metric_create_definition_params.PatternMetricInputTrigger] | Omit = omit,
        window_mode: Literal["seconds", "segments"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricCreateDefinitionResponse:
        return await self._post(
            "/v1/metric/definitions",
            body=await async_maybe_transform(
                {
                    "analysis_package_id": analysis_package_id,
                    "calculation_type": calculation_type,
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
                    "slug": slug,
                    "supported_contexts": supported_contexts,
                    "formula": formula,
                    "sources": sources,
                    "operation": operation,
                    "outcome": outcome,
                    "trigger": trigger,
                    "trigger_combinator": trigger_combinator,
                    "triggers": triggers,
                    "window_mode": window_mode,
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
        system-generated and custom metrics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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
