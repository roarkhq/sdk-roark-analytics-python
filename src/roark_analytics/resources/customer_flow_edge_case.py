# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import customer_flow_edge_case_add_params, customer_flow_edge_case_update_params
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
from ..types.customer_flow_edge_case_add_response import CustomerFlowEdgeCaseAddResponse
from ..types.customer_flow_edge_case_remove_response import CustomerFlowEdgeCaseRemoveResponse
from ..types.customer_flow_edge_case_update_response import CustomerFlowEdgeCaseUpdateResponse
from ..types.customer_flow_edge_case_promote_response import CustomerFlowEdgeCasePromoteResponse

__all__ = ["CustomerFlowEdgeCaseResource", "AsyncCustomerFlowEdgeCaseResource"]


class CustomerFlowEdgeCaseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomerFlowEdgeCaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return CustomerFlowEdgeCaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerFlowEdgeCaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return CustomerFlowEdgeCaseResourceWithStreamingResponse(self)

    def update(
        self,
        edge_case_id: str,
        *,
        flow_id: str,
        additional_expectations: Iterable[customer_flow_edge_case_update_params.AdditionalExpectation] | Omit = omit,
        environment_id: Optional[str] | Omit = omit,
        persona_override_id: Optional[str] | Omit = omit,
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
    ) -> CustomerFlowEdgeCaseUpdateResponse:
        """
        Updates an edge case's title, persona, environment, brief, preceded-by link or
        expectations. Omitted fields are left alone; `additionalExpectations` replaces
        the set wholesale rather than appending. Promoting it to the happy path is a
        separate call, since that also demotes the incumbent.

        Args:
          additional_expectations: Replaces the expectations that apply to this variant on top of the flow's. Omit
              to leave them alone, send [] to clear. Improv flows only: a scripted variant's
              expectations come from the agent turns on its path and are rewritten on the next
              graph edit.

          persona_override_id: The persona this runs as. Null on an edge case inherits the happy path's.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not edge_case_id:
            raise ValueError(f"Expected a non-empty value for `edge_case_id` but received {edge_case_id!r}")
        return self._put(
            path_template(
                "/v1/customer-flow/{flow_id}/edge-case/{edge_case_id}", flow_id=flow_id, edge_case_id=edge_case_id
            ),
            body=maybe_transform(
                {
                    "additional_expectations": additional_expectations,
                    "environment_id": environment_id,
                    "persona_override_id": persona_override_id,
                    "preceded_by_customer_flow_id": preceded_by_customer_flow_id,
                    "preceded_by_customer_flow_variant_id": preceded_by_customer_flow_variant_id,
                    "prompt": prompt,
                    "title": title,
                },
                customer_flow_edge_case_update_params.CustomerFlowEdgeCaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowEdgeCaseUpdateResponse,
        )

    def add(
        self,
        flow_id: str,
        *,
        title: str,
        environment_id: Optional[str] | Omit = omit,
        persona_override_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_variant_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowEdgeCaseAddResponse:
        """
        Adds a variant to an IMPROV flow.

        A scripted flow's variants are owned by the path engine, one per path through
        the graph, so they are created by editing the graph through PUT
        /v1/customer-flow/{flowId}/graph rather than here.

        Leave personaOverrideId or environmentId unset to inherit the happy path's.

        Args:
          persona_override_id: The persona this runs as. Omit to inherit the happy path's.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._post(
            path_template("/v1/customer-flow/{flow_id}/edge-case", flow_id=flow_id),
            body=maybe_transform(
                {
                    "title": title,
                    "environment_id": environment_id,
                    "persona_override_id": persona_override_id,
                    "preceded_by_customer_flow_id": preceded_by_customer_flow_id,
                    "preceded_by_customer_flow_variant_id": preceded_by_customer_flow_variant_id,
                    "prompt": prompt,
                },
                customer_flow_edge_case_add_params.CustomerFlowEdgeCaseAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowEdgeCaseAddResponse,
        )

    def promote(
        self,
        edge_case_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowEdgeCasePromoteResponse:
        """
        Makes this edge case the flow's happy path, and the outgoing happy path an edge
        case. Its persona and environment are baked into it first, so edge cases that
        were inheriting keep the configuration they had.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not edge_case_id:
            raise ValueError(f"Expected a non-empty value for `edge_case_id` but received {edge_case_id!r}")
        return self._post(
            path_template(
                "/v1/customer-flow/{flow_id}/edge-case/{edge_case_id}/promote",
                flow_id=flow_id,
                edge_case_id=edge_case_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowEdgeCasePromoteResponse,
        )

    def remove(
        self,
        edge_case_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowEdgeCaseRemoveResponse:
        """Soft-deletes a variant.

        On a scripted flow the path engine re-creates a variant
        for any path still in the graph, so remove the path through PUT /graph instead
        if that is what you meant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not edge_case_id:
            raise ValueError(f"Expected a non-empty value for `edge_case_id` but received {edge_case_id!r}")
        return self._delete(
            path_template(
                "/v1/customer-flow/{flow_id}/edge-case/{edge_case_id}", flow_id=flow_id, edge_case_id=edge_case_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowEdgeCaseRemoveResponse,
        )


class AsyncCustomerFlowEdgeCaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomerFlowEdgeCaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerFlowEdgeCaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerFlowEdgeCaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncCustomerFlowEdgeCaseResourceWithStreamingResponse(self)

    async def update(
        self,
        edge_case_id: str,
        *,
        flow_id: str,
        additional_expectations: Iterable[customer_flow_edge_case_update_params.AdditionalExpectation] | Omit = omit,
        environment_id: Optional[str] | Omit = omit,
        persona_override_id: Optional[str] | Omit = omit,
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
    ) -> CustomerFlowEdgeCaseUpdateResponse:
        """
        Updates an edge case's title, persona, environment, brief, preceded-by link or
        expectations. Omitted fields are left alone; `additionalExpectations` replaces
        the set wholesale rather than appending. Promoting it to the happy path is a
        separate call, since that also demotes the incumbent.

        Args:
          additional_expectations: Replaces the expectations that apply to this variant on top of the flow's. Omit
              to leave them alone, send [] to clear. Improv flows only: a scripted variant's
              expectations come from the agent turns on its path and are rewritten on the next
              graph edit.

          persona_override_id: The persona this runs as. Null on an edge case inherits the happy path's.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not edge_case_id:
            raise ValueError(f"Expected a non-empty value for `edge_case_id` but received {edge_case_id!r}")
        return await self._put(
            path_template(
                "/v1/customer-flow/{flow_id}/edge-case/{edge_case_id}", flow_id=flow_id, edge_case_id=edge_case_id
            ),
            body=await async_maybe_transform(
                {
                    "additional_expectations": additional_expectations,
                    "environment_id": environment_id,
                    "persona_override_id": persona_override_id,
                    "preceded_by_customer_flow_id": preceded_by_customer_flow_id,
                    "preceded_by_customer_flow_variant_id": preceded_by_customer_flow_variant_id,
                    "prompt": prompt,
                    "title": title,
                },
                customer_flow_edge_case_update_params.CustomerFlowEdgeCaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowEdgeCaseUpdateResponse,
        )

    async def add(
        self,
        flow_id: str,
        *,
        title: str,
        environment_id: Optional[str] | Omit = omit,
        persona_override_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_id: Optional[str] | Omit = omit,
        preceded_by_customer_flow_variant_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowEdgeCaseAddResponse:
        """
        Adds a variant to an IMPROV flow.

        A scripted flow's variants are owned by the path engine, one per path through
        the graph, so they are created by editing the graph through PUT
        /v1/customer-flow/{flowId}/graph rather than here.

        Leave personaOverrideId or environmentId unset to inherit the happy path's.

        Args:
          persona_override_id: The persona this runs as. Omit to inherit the happy path's.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._post(
            path_template("/v1/customer-flow/{flow_id}/edge-case", flow_id=flow_id),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "environment_id": environment_id,
                    "persona_override_id": persona_override_id,
                    "preceded_by_customer_flow_id": preceded_by_customer_flow_id,
                    "preceded_by_customer_flow_variant_id": preceded_by_customer_flow_variant_id,
                    "prompt": prompt,
                },
                customer_flow_edge_case_add_params.CustomerFlowEdgeCaseAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowEdgeCaseAddResponse,
        )

    async def promote(
        self,
        edge_case_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowEdgeCasePromoteResponse:
        """
        Makes this edge case the flow's happy path, and the outgoing happy path an edge
        case. Its persona and environment are baked into it first, so edge cases that
        were inheriting keep the configuration they had.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not edge_case_id:
            raise ValueError(f"Expected a non-empty value for `edge_case_id` but received {edge_case_id!r}")
        return await self._post(
            path_template(
                "/v1/customer-flow/{flow_id}/edge-case/{edge_case_id}/promote",
                flow_id=flow_id,
                edge_case_id=edge_case_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowEdgeCasePromoteResponse,
        )

    async def remove(
        self,
        edge_case_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowEdgeCaseRemoveResponse:
        """Soft-deletes a variant.

        On a scripted flow the path engine re-creates a variant
        for any path still in the graph, so remove the path through PUT /graph instead
        if that is what you meant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not edge_case_id:
            raise ValueError(f"Expected a non-empty value for `edge_case_id` but received {edge_case_id!r}")
        return await self._delete(
            path_template(
                "/v1/customer-flow/{flow_id}/edge-case/{edge_case_id}", flow_id=flow_id, edge_case_id=edge_case_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowEdgeCaseRemoveResponse,
        )


class CustomerFlowEdgeCaseResourceWithRawResponse:
    def __init__(self, customer_flow_edge_case: CustomerFlowEdgeCaseResource) -> None:
        self._customer_flow_edge_case = customer_flow_edge_case

        self.update = to_raw_response_wrapper(
            customer_flow_edge_case.update,
        )
        self.add = to_raw_response_wrapper(
            customer_flow_edge_case.add,
        )
        self.promote = to_raw_response_wrapper(
            customer_flow_edge_case.promote,
        )
        self.remove = to_raw_response_wrapper(
            customer_flow_edge_case.remove,
        )


class AsyncCustomerFlowEdgeCaseResourceWithRawResponse:
    def __init__(self, customer_flow_edge_case: AsyncCustomerFlowEdgeCaseResource) -> None:
        self._customer_flow_edge_case = customer_flow_edge_case

        self.update = async_to_raw_response_wrapper(
            customer_flow_edge_case.update,
        )
        self.add = async_to_raw_response_wrapper(
            customer_flow_edge_case.add,
        )
        self.promote = async_to_raw_response_wrapper(
            customer_flow_edge_case.promote,
        )
        self.remove = async_to_raw_response_wrapper(
            customer_flow_edge_case.remove,
        )


class CustomerFlowEdgeCaseResourceWithStreamingResponse:
    def __init__(self, customer_flow_edge_case: CustomerFlowEdgeCaseResource) -> None:
        self._customer_flow_edge_case = customer_flow_edge_case

        self.update = to_streamed_response_wrapper(
            customer_flow_edge_case.update,
        )
        self.add = to_streamed_response_wrapper(
            customer_flow_edge_case.add,
        )
        self.promote = to_streamed_response_wrapper(
            customer_flow_edge_case.promote,
        )
        self.remove = to_streamed_response_wrapper(
            customer_flow_edge_case.remove,
        )


class AsyncCustomerFlowEdgeCaseResourceWithStreamingResponse:
    def __init__(self, customer_flow_edge_case: AsyncCustomerFlowEdgeCaseResource) -> None:
        self._customer_flow_edge_case = customer_flow_edge_case

        self.update = async_to_streamed_response_wrapper(
            customer_flow_edge_case.update,
        )
        self.add = async_to_streamed_response_wrapper(
            customer_flow_edge_case.add,
        )
        self.promote = async_to_streamed_response_wrapper(
            customer_flow_edge_case.promote,
        )
        self.remove = async_to_streamed_response_wrapper(
            customer_flow_edge_case.remove,
        )
