# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import simulation_customer_flow_variant_create_params, simulation_customer_flow_variant_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.simulation_customer_flow_variant_list_response import SimulationCustomerFlowVariantListResponse
from ..types.simulation_customer_flow_variant_create_response import SimulationCustomerFlowVariantCreateResponse
from ..types.simulation_customer_flow_variant_delete_response import SimulationCustomerFlowVariantDeleteResponse
from ..types.simulation_customer_flow_variant_update_response import SimulationCustomerFlowVariantUpdateResponse
from ..types.simulation_customer_flow_variant_get_by_id_response import SimulationCustomerFlowVariantGetByIDResponse
from ..types.simulation_customer_flow_variant_set_default_response import (
    SimulationCustomerFlowVariantSetDefaultResponse,
)

__all__ = ["SimulationCustomerFlowVariantResource", "AsyncSimulationCustomerFlowVariantResource"]


class SimulationCustomerFlowVariantResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationCustomerFlowVariantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationCustomerFlowVariantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationCustomerFlowVariantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationCustomerFlowVariantResourceWithStreamingResponse(self)

    def create(
        self,
        flow_id: str,
        *,
        title: str,
        environment_id: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        persona_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_variant_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantCreateResponse:
        """
        Adds a variant to an UNSCRIPTED flow.

        A scripted flow's variants are owned by the path engine, one per path through
        the graph, so they are created by editing the graph through PUT
        /v1/simulation/customer-flow/{flowId}/steps rather than here.

        Leave personaId or environmentId unset to inherit the default variant's.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._post(
            path_template("/v1/simulation/customer-flow/{flow_id}/variant", flow_id=flow_id),
            body=maybe_transform(
                {
                    "title": title,
                    "environment_id": environment_id,
                    "is_default": is_default,
                    "persona_id": persona_id,
                    "preceded_by_customer_flow_id": preceded_by_customer_flow_id,
                    "preceded_by_customer_flow_variant_id": preceded_by_customer_flow_variant_id,
                    "prompt": prompt,
                },
                simulation_customer_flow_variant_create_params.SimulationCustomerFlowVariantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantCreateResponse,
        )

    def update(
        self,
        variant_id: str,
        *,
        flow_id: str,
        additional_expectations: Iterable[simulation_customer_flow_variant_update_params.AdditionalExpectation]
        | Omit = omit,
        environment_id: Optional[str] | Omit = omit,
        persona_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_variant_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantUpdateResponse:
        """
        Updates a variant's title, persona, environment, brief, preceded-by link or
        expectations. Omitted fields are left alone; `additionalExpectations` replaces
        the set wholesale rather than appending. Making it the flow's default is a
        separate call, since that also demotes the current default.

        Args:
          additional_expectations: Replaces the expectations that apply to this variant on top of the flow's. Omit
              to leave them alone, send [] to clear. Unscripted flows only: a scripted
              variant's expectations come from the agent turns on its path and are rewritten
              on the next step edit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return self._put(
            path_template(
                "/v1/simulation/customer-flow/{flow_id}/variant/{variant_id}", flow_id=flow_id, variant_id=variant_id
            ),
            body=maybe_transform(
                {
                    "additional_expectations": additional_expectations,
                    "environment_id": environment_id,
                    "persona_id": persona_id,
                    "preceded_by_customer_flow_id": preceded_by_customer_flow_id,
                    "preceded_by_customer_flow_variant_id": preceded_by_customer_flow_variant_id,
                    "prompt": prompt,
                    "title": title,
                },
                simulation_customer_flow_variant_update_params.SimulationCustomerFlowVariantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantUpdateResponse,
        )

    def list(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantListResponse:
        """Returns every variant of a customer flow with its additional expectations.

        Not
        paginated: a flow's variants are bounded by its paths.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._get(
            path_template("/v1/simulation/customer-flow/{flow_id}/variant", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantListResponse,
        )

    def delete(
        self,
        variant_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantDeleteResponse:
        """Soft-deletes a variant.

        On a scripted flow the path engine re-creates a variant
        for any path still in the graph, so remove the path through PUT /steps instead
        if that is what you meant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return self._delete(
            path_template(
                "/v1/simulation/customer-flow/{flow_id}/variant/{variant_id}", flow_id=flow_id, variant_id=variant_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantDeleteResponse,
        )

    def get_by_id(
        self,
        variant_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantGetByIDResponse:
        """
        Get a flow variant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return self._get(
            path_template(
                "/v1/simulation/customer-flow/{flow_id}/variant/{variant_id}", flow_id=flow_id, variant_id=variant_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantGetByIDResponse,
        )

    def set_default(
        self,
        variant_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantSetDefaultResponse:
        """Promotes a variant to the flow's default, demoting the current one.

        The outgoing
        default's persona and environment are baked into it first, so variants that were
        inheriting keep the configuration they had.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return self._post(
            path_template(
                "/v1/simulation/customer-flow/{flow_id}/variant/{variant_id}/default",
                flow_id=flow_id,
                variant_id=variant_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantSetDefaultResponse,
        )


class AsyncSimulationCustomerFlowVariantResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationCustomerFlowVariantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationCustomerFlowVariantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationCustomerFlowVariantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationCustomerFlowVariantResourceWithStreamingResponse(self)

    async def create(
        self,
        flow_id: str,
        *,
        title: str,
        environment_id: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        persona_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_variant_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantCreateResponse:
        """
        Adds a variant to an UNSCRIPTED flow.

        A scripted flow's variants are owned by the path engine, one per path through
        the graph, so they are created by editing the graph through PUT
        /v1/simulation/customer-flow/{flowId}/steps rather than here.

        Leave personaId or environmentId unset to inherit the default variant's.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._post(
            path_template("/v1/simulation/customer-flow/{flow_id}/variant", flow_id=flow_id),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "environment_id": environment_id,
                    "is_default": is_default,
                    "persona_id": persona_id,
                    "preceded_by_customer_flow_id": preceded_by_customer_flow_id,
                    "preceded_by_customer_flow_variant_id": preceded_by_customer_flow_variant_id,
                    "prompt": prompt,
                },
                simulation_customer_flow_variant_create_params.SimulationCustomerFlowVariantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantCreateResponse,
        )

    async def update(
        self,
        variant_id: str,
        *,
        flow_id: str,
        additional_expectations: Iterable[simulation_customer_flow_variant_update_params.AdditionalExpectation]
        | Omit = omit,
        environment_id: Optional[str] | Omit = omit,
        persona_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_variant_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantUpdateResponse:
        """
        Updates a variant's title, persona, environment, brief, preceded-by link or
        expectations. Omitted fields are left alone; `additionalExpectations` replaces
        the set wholesale rather than appending. Making it the flow's default is a
        separate call, since that also demotes the current default.

        Args:
          additional_expectations: Replaces the expectations that apply to this variant on top of the flow's. Omit
              to leave them alone, send [] to clear. Unscripted flows only: a scripted
              variant's expectations come from the agent turns on its path and are rewritten
              on the next step edit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return await self._put(
            path_template(
                "/v1/simulation/customer-flow/{flow_id}/variant/{variant_id}", flow_id=flow_id, variant_id=variant_id
            ),
            body=await async_maybe_transform(
                {
                    "additional_expectations": additional_expectations,
                    "environment_id": environment_id,
                    "persona_id": persona_id,
                    "preceded_by_customer_flow_id": preceded_by_customer_flow_id,
                    "preceded_by_customer_flow_variant_id": preceded_by_customer_flow_variant_id,
                    "prompt": prompt,
                    "title": title,
                },
                simulation_customer_flow_variant_update_params.SimulationCustomerFlowVariantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantUpdateResponse,
        )

    async def list(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantListResponse:
        """Returns every variant of a customer flow with its additional expectations.

        Not
        paginated: a flow's variants are bounded by its paths.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._get(
            path_template("/v1/simulation/customer-flow/{flow_id}/variant", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantListResponse,
        )

    async def delete(
        self,
        variant_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantDeleteResponse:
        """Soft-deletes a variant.

        On a scripted flow the path engine re-creates a variant
        for any path still in the graph, so remove the path through PUT /steps instead
        if that is what you meant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return await self._delete(
            path_template(
                "/v1/simulation/customer-flow/{flow_id}/variant/{variant_id}", flow_id=flow_id, variant_id=variant_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantDeleteResponse,
        )

    async def get_by_id(
        self,
        variant_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantGetByIDResponse:
        """
        Get a flow variant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return await self._get(
            path_template(
                "/v1/simulation/customer-flow/{flow_id}/variant/{variant_id}", flow_id=flow_id, variant_id=variant_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantGetByIDResponse,
        )

    async def set_default(
        self,
        variant_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowVariantSetDefaultResponse:
        """Promotes a variant to the flow's default, demoting the current one.

        The outgoing
        default's persona and environment are baked into it first, so variants that were
        inheriting keep the configuration they had.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return await self._post(
            path_template(
                "/v1/simulation/customer-flow/{flow_id}/variant/{variant_id}/default",
                flow_id=flow_id,
                variant_id=variant_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowVariantSetDefaultResponse,
        )


class SimulationCustomerFlowVariantResourceWithRawResponse:
    def __init__(self, simulation_customer_flow_variant: SimulationCustomerFlowVariantResource) -> None:
        self._simulation_customer_flow_variant = simulation_customer_flow_variant

        self.create = to_raw_response_wrapper(
            simulation_customer_flow_variant.create,
        )
        self.update = to_raw_response_wrapper(
            simulation_customer_flow_variant.update,
        )
        self.list = to_raw_response_wrapper(
            simulation_customer_flow_variant.list,
        )
        self.delete = to_raw_response_wrapper(
            simulation_customer_flow_variant.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_customer_flow_variant.get_by_id,
        )
        self.set_default = to_raw_response_wrapper(
            simulation_customer_flow_variant.set_default,
        )


class AsyncSimulationCustomerFlowVariantResourceWithRawResponse:
    def __init__(self, simulation_customer_flow_variant: AsyncSimulationCustomerFlowVariantResource) -> None:
        self._simulation_customer_flow_variant = simulation_customer_flow_variant

        self.create = async_to_raw_response_wrapper(
            simulation_customer_flow_variant.create,
        )
        self.update = async_to_raw_response_wrapper(
            simulation_customer_flow_variant.update,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_customer_flow_variant.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simulation_customer_flow_variant.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_customer_flow_variant.get_by_id,
        )
        self.set_default = async_to_raw_response_wrapper(
            simulation_customer_flow_variant.set_default,
        )


class SimulationCustomerFlowVariantResourceWithStreamingResponse:
    def __init__(self, simulation_customer_flow_variant: SimulationCustomerFlowVariantResource) -> None:
        self._simulation_customer_flow_variant = simulation_customer_flow_variant

        self.create = to_streamed_response_wrapper(
            simulation_customer_flow_variant.create,
        )
        self.update = to_streamed_response_wrapper(
            simulation_customer_flow_variant.update,
        )
        self.list = to_streamed_response_wrapper(
            simulation_customer_flow_variant.list,
        )
        self.delete = to_streamed_response_wrapper(
            simulation_customer_flow_variant.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_customer_flow_variant.get_by_id,
        )
        self.set_default = to_streamed_response_wrapper(
            simulation_customer_flow_variant.set_default,
        )


class AsyncSimulationCustomerFlowVariantResourceWithStreamingResponse:
    def __init__(self, simulation_customer_flow_variant: AsyncSimulationCustomerFlowVariantResource) -> None:
        self._simulation_customer_flow_variant = simulation_customer_flow_variant

        self.create = async_to_streamed_response_wrapper(
            simulation_customer_flow_variant.create,
        )
        self.update = async_to_streamed_response_wrapper(
            simulation_customer_flow_variant.update,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_customer_flow_variant.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simulation_customer_flow_variant.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_customer_flow_variant.get_by_id,
        )
        self.set_default = async_to_streamed_response_wrapper(
            simulation_customer_flow_variant.set_default,
        )
