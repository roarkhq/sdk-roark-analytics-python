# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import metric_variant_create_params, metric_variant_update_params
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
from ..types.metric_variant_list_response import MetricVariantListResponse
from ..types.metric_variant_create_response import MetricVariantCreateResponse
from ..types.metric_variant_delete_response import MetricVariantDeleteResponse
from ..types.metric_variant_update_response import MetricVariantUpdateResponse
from ..types.metric_variant_get_by_id_response import MetricVariantGetByIDResponse

__all__ = ["MetricVariantResource", "AsyncMetricVariantResource"]


class MetricVariantResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricVariantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return MetricVariantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricVariantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return MetricVariantResourceWithStreamingResponse(self)

    def create(
        self,
        id_or_slug: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantCreateResponse:
        """
        Add a configuration of this metric for your organization, seeded from its
        Default. Edit it with PUT to change what it measures, then pin it where you want
        it used. Threshold metrics have no variants: their configuration comes from the
        metric they derive from. Metrics in a package that manages its own variants
        reject this too.

        Args:
          name: Name for the new variant. Must be unique for this metric within your
              organization and cannot be `Default`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return self._post(
            f"/v1/metric/definitions/{id_or_slug}/variants",
            body=maybe_transform({"name": name}, metric_variant_create_params.MetricVariantCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantCreateResponse,
        )

    def update(
        self,
        variant_id: str,
        *,
        id_or_slug: str,
        boolean_false_label: str | Omit = omit,
        boolean_true_label: str | Omit = omit,
        change_reason: str | Omit = omit,
        llm_prompt: str | Omit = omit,
        max_classifications: int | Omit = omit,
        name: str | Omit = omit,
        scale_max: int | Omit = omit,
        scale_min: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantUpdateResponse:
        """Rename a variant, change its configuration, or both.

        Every configuration change
        creates a new immutable version and advances `versionId`; the response carries
        the advanced value. **Editing one of Roark’s own variants forks it for your
        organization.** The response carries the new variant’s `id`, which will differ
        from the one in the path, and `isSystem` becomes false. Roark’s variant is
        untouched and other organizations keep it. DELETE your fork to go back to it.
        Which fields are editable depends on the metric: some Roark metrics lock their
        prompt or output configuration, and a locked field is rejected rather than
        ignored.

        Args:
          id_or_slug: Metric definition UUID or its stable slug.

          boolean_false_label: What a `false` value means. Given to the judge as its polarity rule, so keep it
              accurate.

          boolean_true_label: What a `true` value means. Given to the judge as its polarity rule, so keep it
              accurate.

          change_reason: Free-text audit note recorded on the new version.

          llm_prompt: The rubric this variant applies. LLM judge metrics only.

          max_classifications: Maximum classifications returned. CLASSIFICATION output only.

          name: Rename the variant. Does not change its configuration, so `versionId` is
              unaffected. `Default` is reserved.

          scale_max: Scale maximum. SCALE output only.

          scale_min: Scale minimum. SCALE output only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return self._put(
            f"/v1/metric/definitions/{id_or_slug}/variants/{variant_id}",
            body=maybe_transform(
                {
                    "id_or_slug": id_or_slug,
                    "boolean_false_label": boolean_false_label,
                    "boolean_true_label": boolean_true_label,
                    "change_reason": change_reason,
                    "llm_prompt": llm_prompt,
                    "max_classifications": max_classifications,
                    "name": name,
                    "scale_max": scale_max,
                    "scale_min": scale_min,
                },
                metric_variant_update_params.MetricVariantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantUpdateResponse,
        )

    def list(
        self,
        id_or_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantListResponse:
        """
        Every configuration of this metric your organization can use: Roark’s own
        variants and any your organization has added or forked. `isDefault` marks the
        one the metric is scored with when nothing pins another; pass any variant’s `id`
        as `sourceVariantId` to pin it on a derived metric. Auto-managed variants (the
        ones a package materializes for you) are not listed: they are engine state, not
        configuration you author.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return self._get(
            f"/v1/metric/definitions/{id_or_slug}/variants",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantListResponse,
        )

    def delete(
        self,
        variant_id: str,
        *,
        id_or_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantDeleteResponse:
        """Remove one of your organization’s variants.

        Anything pinned to it falls back to
        the Default, so deleting a fork of a Roark variant returns you to Roark’s
        configuration. Roark’s own variants cannot be deleted, and neither can a
        Default. Values already collected under the deleted variant are retained.

        Args:
          id_or_slug: Metric definition UUID or its stable slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return self._delete(
            f"/v1/metric/definitions/{id_or_slug}/variants/{variant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantDeleteResponse,
        )

    def get_by_id(
        self,
        variant_id: str,
        *,
        id_or_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantGetByIDResponse:
        """
        One configuration of this metric, by id.

        Args:
          id_or_slug: Metric definition UUID or its stable slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return self._get(
            f"/v1/metric/definitions/{id_or_slug}/variants/{variant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantGetByIDResponse,
        )


class AsyncMetricVariantResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricVariantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricVariantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricVariantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncMetricVariantResourceWithStreamingResponse(self)

    async def create(
        self,
        id_or_slug: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantCreateResponse:
        """
        Add a configuration of this metric for your organization, seeded from its
        Default. Edit it with PUT to change what it measures, then pin it where you want
        it used. Threshold metrics have no variants: their configuration comes from the
        metric they derive from. Metrics in a package that manages its own variants
        reject this too.

        Args:
          name: Name for the new variant. Must be unique for this metric within your
              organization and cannot be `Default`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return await self._post(
            f"/v1/metric/definitions/{id_or_slug}/variants",
            body=await async_maybe_transform({"name": name}, metric_variant_create_params.MetricVariantCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantCreateResponse,
        )

    async def update(
        self,
        variant_id: str,
        *,
        id_or_slug: str,
        boolean_false_label: str | Omit = omit,
        boolean_true_label: str | Omit = omit,
        change_reason: str | Omit = omit,
        llm_prompt: str | Omit = omit,
        max_classifications: int | Omit = omit,
        name: str | Omit = omit,
        scale_max: int | Omit = omit,
        scale_min: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantUpdateResponse:
        """Rename a variant, change its configuration, or both.

        Every configuration change
        creates a new immutable version and advances `versionId`; the response carries
        the advanced value. **Editing one of Roark’s own variants forks it for your
        organization.** The response carries the new variant’s `id`, which will differ
        from the one in the path, and `isSystem` becomes false. Roark’s variant is
        untouched and other organizations keep it. DELETE your fork to go back to it.
        Which fields are editable depends on the metric: some Roark metrics lock their
        prompt or output configuration, and a locked field is rejected rather than
        ignored.

        Args:
          id_or_slug: Metric definition UUID or its stable slug.

          boolean_false_label: What a `false` value means. Given to the judge as its polarity rule, so keep it
              accurate.

          boolean_true_label: What a `true` value means. Given to the judge as its polarity rule, so keep it
              accurate.

          change_reason: Free-text audit note recorded on the new version.

          llm_prompt: The rubric this variant applies. LLM judge metrics only.

          max_classifications: Maximum classifications returned. CLASSIFICATION output only.

          name: Rename the variant. Does not change its configuration, so `versionId` is
              unaffected. `Default` is reserved.

          scale_max: Scale maximum. SCALE output only.

          scale_min: Scale minimum. SCALE output only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return await self._put(
            f"/v1/metric/definitions/{id_or_slug}/variants/{variant_id}",
            body=await async_maybe_transform(
                {
                    "id_or_slug": id_or_slug,
                    "boolean_false_label": boolean_false_label,
                    "boolean_true_label": boolean_true_label,
                    "change_reason": change_reason,
                    "llm_prompt": llm_prompt,
                    "max_classifications": max_classifications,
                    "name": name,
                    "scale_max": scale_max,
                    "scale_min": scale_min,
                },
                metric_variant_update_params.MetricVariantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantUpdateResponse,
        )

    async def list(
        self,
        id_or_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantListResponse:
        """
        Every configuration of this metric your organization can use: Roark’s own
        variants and any your organization has added or forked. `isDefault` marks the
        one the metric is scored with when nothing pins another; pass any variant’s `id`
        as `sourceVariantId` to pin it on a derived metric. Auto-managed variants (the
        ones a package materializes for you) are not listed: they are engine state, not
        configuration you author.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return await self._get(
            f"/v1/metric/definitions/{id_or_slug}/variants",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantListResponse,
        )

    async def delete(
        self,
        variant_id: str,
        *,
        id_or_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantDeleteResponse:
        """Remove one of your organization’s variants.

        Anything pinned to it falls back to
        the Default, so deleting a fork of a Roark variant returns you to Roark’s
        configuration. Roark’s own variants cannot be deleted, and neither can a
        Default. Values already collected under the deleted variant are retained.

        Args:
          id_or_slug: Metric definition UUID or its stable slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return await self._delete(
            f"/v1/metric/definitions/{id_or_slug}/variants/{variant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantDeleteResponse,
        )

    async def get_by_id(
        self,
        variant_id: str,
        *,
        id_or_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricVariantGetByIDResponse:
        """
        One configuration of this metric, by id.

        Args:
          id_or_slug: Metric definition UUID or its stable slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        if not id_or_slug:
            raise ValueError(f"Expected a non-empty value for `id_or_slug` but received {id_or_slug!r}")
        return await self._get(
            f"/v1/metric/definitions/{id_or_slug}/variants/{variant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricVariantGetByIDResponse,
        )


class MetricVariantResourceWithRawResponse:
    def __init__(self, metric_variant: MetricVariantResource) -> None:
        self._metric_variant = metric_variant

        self.create = to_raw_response_wrapper(
            metric_variant.create,
        )
        self.update = to_raw_response_wrapper(
            metric_variant.update,
        )
        self.list = to_raw_response_wrapper(
            metric_variant.list,
        )
        self.delete = to_raw_response_wrapper(
            metric_variant.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            metric_variant.get_by_id,
        )


class AsyncMetricVariantResourceWithRawResponse:
    def __init__(self, metric_variant: AsyncMetricVariantResource) -> None:
        self._metric_variant = metric_variant

        self.create = async_to_raw_response_wrapper(
            metric_variant.create,
        )
        self.update = async_to_raw_response_wrapper(
            metric_variant.update,
        )
        self.list = async_to_raw_response_wrapper(
            metric_variant.list,
        )
        self.delete = async_to_raw_response_wrapper(
            metric_variant.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            metric_variant.get_by_id,
        )


class MetricVariantResourceWithStreamingResponse:
    def __init__(self, metric_variant: MetricVariantResource) -> None:
        self._metric_variant = metric_variant

        self.create = to_streamed_response_wrapper(
            metric_variant.create,
        )
        self.update = to_streamed_response_wrapper(
            metric_variant.update,
        )
        self.list = to_streamed_response_wrapper(
            metric_variant.list,
        )
        self.delete = to_streamed_response_wrapper(
            metric_variant.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            metric_variant.get_by_id,
        )


class AsyncMetricVariantResourceWithStreamingResponse:
    def __init__(self, metric_variant: AsyncMetricVariantResource) -> None:
        self._metric_variant = metric_variant

        self.create = async_to_streamed_response_wrapper(
            metric_variant.create,
        )
        self.update = async_to_streamed_response_wrapper(
            metric_variant.update,
        )
        self.list = async_to_streamed_response_wrapper(
            metric_variant.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            metric_variant.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            metric_variant.get_by_id,
        )
