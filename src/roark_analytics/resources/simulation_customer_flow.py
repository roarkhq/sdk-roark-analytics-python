# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..types import (
    simulation_customer_flow_list_params,
    simulation_customer_flow_create_params,
    simulation_customer_flow_update_params,
    simulation_customer_flow_replace_graph_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.flow_step_param import FlowStepParam
from ..types.simulation_customer_flow_list_response import SimulationCustomerFlowListResponse
from ..types.simulation_customer_flow_create_response import SimulationCustomerFlowCreateResponse
from ..types.simulation_customer_flow_delete_response import SimulationCustomerFlowDeleteResponse
from ..types.simulation_customer_flow_update_response import SimulationCustomerFlowUpdateResponse
from ..types.simulation_customer_flow_get_by_id_response import SimulationCustomerFlowGetByIDResponse
from ..types.simulation_customer_flow_replace_graph_response import SimulationCustomerFlowReplaceGraphResponse

__all__ = ["SimulationCustomerFlowResource", "AsyncSimulationCustomerFlowResource"]


class SimulationCustomerFlowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationCustomerFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationCustomerFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationCustomerFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationCustomerFlowResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        graph: Iterable[FlowStepParam],
        title: str,
        type: Literal["SCRIPTED"],
        agent_expectations: Iterable[
            simulation_customer_flow_create_params.CreateScriptedCustomerFlowInputAgentExpectation
        ]
        | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowCreateResponse:
        """Creates a customer flow.

        A SCRIPTED flow carries a step graph and gets one
        variant per path through it; an IMPROV flow carries briefs and gets the variants
        you send.

        Args:
          agent_ids: Agents this flow exercises. At least one is required.

          graph: The conversation, as a graph of steps. At most 100 steps across at most 25
              paths. The variants come from the graph: one per path, so they are not sent
              here.

          branching_mode: DETERMINISTIC (the default) runs one variant per path through the graph;
              ADAPTIVE collapses the paths into one call the simulated customer adapts across.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        title: str,
        type: Literal["IMPROV"],
        variants: Iterable[simulation_customer_flow_create_params.CreateImprovCustomerFlowInputVariant],
        agent_expectations: Iterable[
            simulation_customer_flow_create_params.CreateImprovCustomerFlowInputAgentExpectation
        ]
        | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowCreateResponse:
        """Creates a customer flow.

        A SCRIPTED flow carries a step graph and gets one
        variant per path through it; an IMPROV flow carries briefs and gets the variants
        you send.

        Args:
          agent_ids: Agents this flow exercises. At least one is required.

          variants: The briefs to run. At least one, and one of them is the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_ids", "graph", "title", "type"], ["agent_ids", "title", "type", "variants"])
    def create(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        graph: Iterable[FlowStepParam] | Omit = omit,
        title: str,
        type: Literal["SCRIPTED"] | Literal["IMPROV"],
        agent_expectations: Iterable[
            simulation_customer_flow_create_params.CreateScriptedCustomerFlowInputAgentExpectation
        ]
        | Iterable[simulation_customer_flow_create_params.CreateImprovCustomerFlowInputAgentExpectation]
        | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        variants: Iterable[simulation_customer_flow_create_params.CreateImprovCustomerFlowInputVariant] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowCreateResponse:
        return self._post(
            "/v1/simulation/customer-flow",
            body=maybe_transform(
                {
                    "agent_ids": agent_ids,
                    "graph": graph,
                    "title": title,
                    "type": type,
                    "agent_expectations": agent_expectations,
                    "branching_mode": branching_mode,
                    "description": description,
                    "variants": variants,
                },
                simulation_customer_flow_create_params.SimulationCustomerFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowCreateResponse,
        )

    def update(
        self,
        flow_id: str,
        *,
        agent_expectations: Iterable[simulation_customer_flow_update_params.AgentExpectation] | Omit = omit,
        agent_ids: SequenceNotStr[str] | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowUpdateResponse:
        """
        Updates a flow's title, description, branching mode, linked agents or flow-level
        expectations. The step graph is replaced through PUT /graph.

        Args:
          agent_expectations: Replaces the flow-level expectations. Omit to leave them unchanged.

          agent_ids: Replaces the linked agents. Omit to leave them unchanged.

          branching_mode: Scripted flows only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._put(
            path_template("/v1/simulation/customer-flow/{flow_id}", flow_id=flow_id),
            body=maybe_transform(
                {
                    "agent_expectations": agent_expectations,
                    "agent_ids": agent_ids,
                    "branching_mode": branching_mode,
                    "description": description,
                    "title": title,
                },
                simulation_customer_flow_update_params.SimulationCustomerFlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        include_system: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        type: Literal["SCRIPTED", "IMPROV", "VOICEMAIL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowListResponse:
        """
        Returns a paginated list of customer flows with their agents, expectations and
        variants. The step graph is the one field omitted: reading it walks the
        project's whole step graph, so it comes back from the single-flow endpoint
        instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/simulation/customer-flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "include_system": include_system,
                        "limit": limit,
                        "search_text": search_text,
                        "type": type,
                    },
                    simulation_customer_flow_list_params.SimulationCustomerFlowListParams,
                ),
            ),
            cast_to=SimulationCustomerFlowListResponse,
        )

    def delete(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowDeleteResponse:
        """
        Soft-deletes a customer flow along with its variants, expectations and (for
        scripted flows) its step graph. Run plans that linked it drop it from their test
        cases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._delete(
            path_template("/v1/simulation/customer-flow/{flow_id}", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowDeleteResponse,
        )

    def get_by_id(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowGetByIDResponse:
        """
        Returns a customer flow with its variants, expectations and linked agents.
        Scripted flows also carry their step graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._get(
            path_template("/v1/simulation/customer-flow/{flow_id}", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowGetByIDResponse,
        )

    def replace_graph(
        self,
        flow_id: str,
        *,
        graph: Iterable[FlowStepParam],
        allow_unmerge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowReplaceGraphResponse:
        """Replaces a scripted flow's conversation graph with the tree you send.

        This is a
        full replace, not a merge: a step you omit is removed.

        Include `nodeId` on a step to update the existing one, omit it to create a new
        step. Where two branches rejoin, keep the `mergeIntoNodeIds` references a read
        gave you. Dropping them un-merges those branches and is refused unless
        `allowUnmerge` is set.

        A change to the set of paths re-seeds the flow's variants, which the response
        reports as `variantsReshaped` along with the resulting variants.

        Args:
          graph: The complete graph. This replaces the flow's existing steps rather than merging
              into them.

          allow_unmerge: Confirms a write that drops branches which currently rejoin. Only needed when
              the request omits mergeIntoNodeIds references the flow already had; a faithful
              round trip never needs it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._put(
            path_template("/v1/simulation/customer-flow/{flow_id}/graph", flow_id=flow_id),
            body=maybe_transform(
                {
                    "graph": graph,
                    "allow_unmerge": allow_unmerge,
                },
                simulation_customer_flow_replace_graph_params.SimulationCustomerFlowReplaceGraphParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowReplaceGraphResponse,
        )


class AsyncSimulationCustomerFlowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationCustomerFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationCustomerFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationCustomerFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationCustomerFlowResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        graph: Iterable[FlowStepParam],
        title: str,
        type: Literal["SCRIPTED"],
        agent_expectations: Iterable[
            simulation_customer_flow_create_params.CreateScriptedCustomerFlowInputAgentExpectation
        ]
        | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowCreateResponse:
        """Creates a customer flow.

        A SCRIPTED flow carries a step graph and gets one
        variant per path through it; an IMPROV flow carries briefs and gets the variants
        you send.

        Args:
          agent_ids: Agents this flow exercises. At least one is required.

          graph: The conversation, as a graph of steps. At most 100 steps across at most 25
              paths. The variants come from the graph: one per path, so they are not sent
              here.

          branching_mode: DETERMINISTIC (the default) runs one variant per path through the graph;
              ADAPTIVE collapses the paths into one call the simulated customer adapts across.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        title: str,
        type: Literal["IMPROV"],
        variants: Iterable[simulation_customer_flow_create_params.CreateImprovCustomerFlowInputVariant],
        agent_expectations: Iterable[
            simulation_customer_flow_create_params.CreateImprovCustomerFlowInputAgentExpectation
        ]
        | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowCreateResponse:
        """Creates a customer flow.

        A SCRIPTED flow carries a step graph and gets one
        variant per path through it; an IMPROV flow carries briefs and gets the variants
        you send.

        Args:
          agent_ids: Agents this flow exercises. At least one is required.

          variants: The briefs to run. At least one, and one of them is the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_ids", "graph", "title", "type"], ["agent_ids", "title", "type", "variants"])
    async def create(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        graph: Iterable[FlowStepParam] | Omit = omit,
        title: str,
        type: Literal["SCRIPTED"] | Literal["IMPROV"],
        agent_expectations: Iterable[
            simulation_customer_flow_create_params.CreateScriptedCustomerFlowInputAgentExpectation
        ]
        | Iterable[simulation_customer_flow_create_params.CreateImprovCustomerFlowInputAgentExpectation]
        | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        variants: Iterable[simulation_customer_flow_create_params.CreateImprovCustomerFlowInputVariant] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowCreateResponse:
        return await self._post(
            "/v1/simulation/customer-flow",
            body=await async_maybe_transform(
                {
                    "agent_ids": agent_ids,
                    "graph": graph,
                    "title": title,
                    "type": type,
                    "agent_expectations": agent_expectations,
                    "branching_mode": branching_mode,
                    "description": description,
                    "variants": variants,
                },
                simulation_customer_flow_create_params.SimulationCustomerFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowCreateResponse,
        )

    async def update(
        self,
        flow_id: str,
        *,
        agent_expectations: Iterable[simulation_customer_flow_update_params.AgentExpectation] | Omit = omit,
        agent_ids: SequenceNotStr[str] | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowUpdateResponse:
        """
        Updates a flow's title, description, branching mode, linked agents or flow-level
        expectations. The step graph is replaced through PUT /graph.

        Args:
          agent_expectations: Replaces the flow-level expectations. Omit to leave them unchanged.

          agent_ids: Replaces the linked agents. Omit to leave them unchanged.

          branching_mode: Scripted flows only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._put(
            path_template("/v1/simulation/customer-flow/{flow_id}", flow_id=flow_id),
            body=await async_maybe_transform(
                {
                    "agent_expectations": agent_expectations,
                    "agent_ids": agent_ids,
                    "branching_mode": branching_mode,
                    "description": description,
                    "title": title,
                },
                simulation_customer_flow_update_params.SimulationCustomerFlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        include_system: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        type: Literal["SCRIPTED", "IMPROV", "VOICEMAIL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowListResponse:
        """
        Returns a paginated list of customer flows with their agents, expectations and
        variants. The step graph is the one field omitted: reading it walks the
        project's whole step graph, so it comes back from the single-flow endpoint
        instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/simulation/customer-flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "include_system": include_system,
                        "limit": limit,
                        "search_text": search_text,
                        "type": type,
                    },
                    simulation_customer_flow_list_params.SimulationCustomerFlowListParams,
                ),
            ),
            cast_to=SimulationCustomerFlowListResponse,
        )

    async def delete(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowDeleteResponse:
        """
        Soft-deletes a customer flow along with its variants, expectations and (for
        scripted flows) its step graph. Run plans that linked it drop it from their test
        cases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._delete(
            path_template("/v1/simulation/customer-flow/{flow_id}", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowDeleteResponse,
        )

    async def get_by_id(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowGetByIDResponse:
        """
        Returns a customer flow with its variants, expectations and linked agents.
        Scripted flows also carry their step graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._get(
            path_template("/v1/simulation/customer-flow/{flow_id}", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowGetByIDResponse,
        )

    async def replace_graph(
        self,
        flow_id: str,
        *,
        graph: Iterable[FlowStepParam],
        allow_unmerge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationCustomerFlowReplaceGraphResponse:
        """Replaces a scripted flow's conversation graph with the tree you send.

        This is a
        full replace, not a merge: a step you omit is removed.

        Include `nodeId` on a step to update the existing one, omit it to create a new
        step. Where two branches rejoin, keep the `mergeIntoNodeIds` references a read
        gave you. Dropping them un-merges those branches and is refused unless
        `allowUnmerge` is set.

        A change to the set of paths re-seeds the flow's variants, which the response
        reports as `variantsReshaped` along with the resulting variants.

        Args:
          graph: The complete graph. This replaces the flow's existing steps rather than merging
              into them.

          allow_unmerge: Confirms a write that drops branches which currently rejoin. Only needed when
              the request omits mergeIntoNodeIds references the flow already had; a faithful
              round trip never needs it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._put(
            path_template("/v1/simulation/customer-flow/{flow_id}/graph", flow_id=flow_id),
            body=await async_maybe_transform(
                {
                    "graph": graph,
                    "allow_unmerge": allow_unmerge,
                },
                simulation_customer_flow_replace_graph_params.SimulationCustomerFlowReplaceGraphParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationCustomerFlowReplaceGraphResponse,
        )


class SimulationCustomerFlowResourceWithRawResponse:
    def __init__(self, simulation_customer_flow: SimulationCustomerFlowResource) -> None:
        self._simulation_customer_flow = simulation_customer_flow

        self.create = to_raw_response_wrapper(
            simulation_customer_flow.create,
        )
        self.update = to_raw_response_wrapper(
            simulation_customer_flow.update,
        )
        self.list = to_raw_response_wrapper(
            simulation_customer_flow.list,
        )
        self.delete = to_raw_response_wrapper(
            simulation_customer_flow.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_customer_flow.get_by_id,
        )
        self.replace_graph = to_raw_response_wrapper(
            simulation_customer_flow.replace_graph,
        )


class AsyncSimulationCustomerFlowResourceWithRawResponse:
    def __init__(self, simulation_customer_flow: AsyncSimulationCustomerFlowResource) -> None:
        self._simulation_customer_flow = simulation_customer_flow

        self.create = async_to_raw_response_wrapper(
            simulation_customer_flow.create,
        )
        self.update = async_to_raw_response_wrapper(
            simulation_customer_flow.update,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_customer_flow.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simulation_customer_flow.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_customer_flow.get_by_id,
        )
        self.replace_graph = async_to_raw_response_wrapper(
            simulation_customer_flow.replace_graph,
        )


class SimulationCustomerFlowResourceWithStreamingResponse:
    def __init__(self, simulation_customer_flow: SimulationCustomerFlowResource) -> None:
        self._simulation_customer_flow = simulation_customer_flow

        self.create = to_streamed_response_wrapper(
            simulation_customer_flow.create,
        )
        self.update = to_streamed_response_wrapper(
            simulation_customer_flow.update,
        )
        self.list = to_streamed_response_wrapper(
            simulation_customer_flow.list,
        )
        self.delete = to_streamed_response_wrapper(
            simulation_customer_flow.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_customer_flow.get_by_id,
        )
        self.replace_graph = to_streamed_response_wrapper(
            simulation_customer_flow.replace_graph,
        )


class AsyncSimulationCustomerFlowResourceWithStreamingResponse:
    def __init__(self, simulation_customer_flow: AsyncSimulationCustomerFlowResource) -> None:
        self._simulation_customer_flow = simulation_customer_flow

        self.create = async_to_streamed_response_wrapper(
            simulation_customer_flow.create,
        )
        self.update = async_to_streamed_response_wrapper(
            simulation_customer_flow.update,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_customer_flow.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simulation_customer_flow.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_customer_flow.get_by_id,
        )
        self.replace_graph = async_to_streamed_response_wrapper(
            simulation_customer_flow.replace_graph,
        )
