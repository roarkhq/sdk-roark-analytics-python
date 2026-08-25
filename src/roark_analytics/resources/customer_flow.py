# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional, overload
from typing_extensions import Literal

import httpx

from ..types import (
    customer_flow_list_params,
    customer_flow_create_params,
    customer_flow_update_params,
    customer_flow_replace_graph_params,
    customer_flow_update_happy_path_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.flow_step import FlowStep
from ..types.customer_flow_list_response import CustomerFlowListResponse
from ..types.customer_flow_create_response import CustomerFlowCreateResponse
from ..types.customer_flow_delete_response import CustomerFlowDeleteResponse
from ..types.customer_flow_update_response import CustomerFlowUpdateResponse
from ..types.customer_flow_get_by_id_response import CustomerFlowGetByIDResponse
from ..types.customer_flow_replace_graph_response import CustomerFlowReplaceGraphResponse
from ..types.customer_flow_update_happy_path_response import CustomerFlowUpdateHappyPathResponse

__all__ = ["CustomerFlowResource", "AsyncCustomerFlowResource"]


class CustomerFlowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomerFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return CustomerFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return CustomerFlowResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        graph: List[FlowStep],
        title: str,
        type: Literal["SCRIPTED"],
        agent_expectations: Iterable[customer_flow_create_params.CreateScriptedCustomerFlowInputAgentExpectation]
        | Omit = omit,
        agent_ids: SequenceNotStr[str] | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowCreateResponse:
        """Creates a customer flow.

        A SCRIPTED flow carries a step graph and gets one way
        of running it per path through the graph; an IMPROV flow carries the briefs you
        send. Customer flows replace the older simulation scenarios, so build a flow for
        anything new.

        Args:
          graph: The conversation, as a graph of steps. At most 100 steps across at most 25
              paths. The variants come from the graph: one per path, so they are not sent
              here.

          agent_ids: Agents this flow exercises. Optional for scripted flows.

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
        happy_path: customer_flow_create_params.CreateImprovCustomerFlowInputHappyPath,
        title: str,
        type: Literal["IMPROV"],
        agent_expectations: Iterable[customer_flow_create_params.CreateImprovCustomerFlowInputAgentExpectation]
        | Omit = omit,
        description: Optional[str] | Omit = omit,
        edge_cases: Iterable[customer_flow_create_params.CreateImprovCustomerFlowInputEdgeCase] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowCreateResponse:
        """Creates a customer flow.

        A SCRIPTED flow carries a step graph and gets one way
        of running it per path through the graph; an IMPROV flow carries the briefs you
        send. Customer flows replace the older simulation scenarios, so build a flow for
        anything new.

        Args:
          agent_ids: Agents this flow exercises. At least one is required for improv flows.

          happy_path: The way this flow is meant to go.

          edge_cases: Other ways of running it, each inheriting from the happy path what it does not
              name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["graph", "title", "type"], ["agent_ids", "happy_path", "title", "type"])
    def create(
        self,
        *,
        title: str,
        type: Literal["SCRIPTED", "IMPROV"],
        graph: List[FlowStep] | Omit = omit,
        agent_expectations: Union[
            Iterable[customer_flow_create_params.CreateScriptedCustomerFlowInputAgentExpectation],
            Iterable[customer_flow_create_params.CreateImprovCustomerFlowInputAgentExpectation],
        ]
        | Omit = omit,
        agent_ids: SequenceNotStr[str] | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        happy_path: customer_flow_create_params.CreateImprovCustomerFlowInputHappyPath | Omit = omit,
        edge_cases: Iterable[customer_flow_create_params.CreateImprovCustomerFlowInputEdgeCase] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowCreateResponse:
        return self._post(
            "/v1/customer-flow",
            body=maybe_transform(
                {
                    "title": title,
                    "type": type,
                    "graph": graph,
                    "agent_expectations": agent_expectations,
                    "agent_ids": agent_ids,
                    "branching_mode": branching_mode,
                    "description": description,
                    "happy_path": happy_path,
                    "edge_cases": edge_cases,
                },
                customer_flow_create_params.CustomerFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowCreateResponse,
        )

    def update(
        self,
        flow_id: str,
        *,
        agent_expectations: Iterable[customer_flow_update_params.AgentExpectation] | Omit = omit,
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
    ) -> CustomerFlowUpdateResponse:
        """
        Updates a flow's title, description, branching mode, linked agents or flow-level
        expectations. The step graph is replaced through PUT /graph.

        Args:
          agent_expectations: Replaces the flow-level expectations. Omit to leave them unchanged.

          agent_ids: Replaces the linked agents. Omit to leave them unchanged. An improv flow must
              keep at least one; a scripted flow can be left with none.

          branching_mode: Scripted flows only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._put(
            f"/v1/customer-flow/{flow_id}",
            body=maybe_transform(
                {
                    "agent_expectations": agent_expectations,
                    "agent_ids": agent_ids,
                    "branching_mode": branching_mode,
                    "description": description,
                    "title": title,
                },
                customer_flow_update_params.CustomerFlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowUpdateResponse,
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
    ) -> CustomerFlowListResponse:
        """
        Returns a paginated list of customer flows with their agents, expectations,
        happy path and edge cases. The step graph is the one field omitted: reading it
        walks the project's whole step graph, so it comes back from the single-flow
        endpoint instead. Customer flows are how a project describes what to test; they
        replace the older simulation scenarios.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/customer-flow",
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
                    customer_flow_list_params.CustomerFlowListParams,
                ),
            ),
            cast_to=CustomerFlowListResponse,
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
    ) -> CustomerFlowDeleteResponse:
        """
        Soft-deletes a customer flow along with its edge cases, expectations and (for
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
            f"/v1/customer-flow/{flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowDeleteResponse,
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
    ) -> CustomerFlowGetByIDResponse:
        """
        Returns a customer flow with its happy path, edge cases, expectations and linked
        agents. Scripted flows also carry their step graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._get(
            f"/v1/customer-flow/{flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowGetByIDResponse,
        )

    def replace_graph(
        self,
        flow_id: str,
        *,
        graph: List[FlowStep],
        allow_unmerge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowReplaceGraphResponse:
        """Replaces a scripted flow's conversation graph with the tree you send.

        This is a
        full replace, not a merge: a step you omit is removed. Include `nodeId` on a
        step to update the existing one, omit it to create a new step. Where two
        branches rejoin, keep the `mergeIntoNodeIds` references a read gave you.
        Dropping them un-merges those branches and is refused unless `allowUnmerge` is
        set. A change to the set of paths re-seeds how the flow runs, which the response
        reports as `variantsReshaped` along with the resulting happy path and edge
        cases.

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
            f"/v1/customer-flow/{flow_id}/graph",
            body=maybe_transform(
                {
                    "graph": graph,
                    "allow_unmerge": allow_unmerge,
                },
                customer_flow_replace_graph_params.CustomerFlowReplaceGraphParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowReplaceGraphResponse,
        )

    def update_happy_path(
        self,
        flow_id: str,
        *,
        additional_expectations: Iterable[customer_flow_update_happy_path_params.AdditionalExpectation] | Omit = omit,
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
    ) -> CustomerFlowUpdateHappyPathResponse:
        """
        Updates the happy path's title, persona, environment, brief or expectations.
        Omitted fields are left alone; `additionalExpectations` replaces the set
        wholesale rather than appending. Its persona and environment are what the edge
        cases inherit, so changing them here changes every edge case that does not name
        its own.

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
        return self._put(
            f"/v1/customer-flow/{flow_id}/happy-path",
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
                customer_flow_update_happy_path_params.CustomerFlowUpdateHappyPathParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowUpdateHappyPathResponse,
        )


class AsyncCustomerFlowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomerFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncCustomerFlowResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        graph: List[FlowStep],
        title: str,
        type: Literal["SCRIPTED"],
        agent_expectations: Iterable[customer_flow_create_params.CreateScriptedCustomerFlowInputAgentExpectation]
        | Omit = omit,
        agent_ids: SequenceNotStr[str] | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowCreateResponse:
        """Creates a customer flow.

        A SCRIPTED flow carries a step graph and gets one way
        of running it per path through the graph; an IMPROV flow carries the briefs you
        send. Customer flows replace the older simulation scenarios, so build a flow for
        anything new.

        Args:
          graph: The conversation, as a graph of steps. At most 100 steps across at most 25
              paths. The variants come from the graph: one per path, so they are not sent
              here.

          agent_ids: Agents this flow exercises. Optional for scripted flows.

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
        happy_path: customer_flow_create_params.CreateImprovCustomerFlowInputHappyPath,
        title: str,
        type: Literal["IMPROV"],
        agent_expectations: Iterable[customer_flow_create_params.CreateImprovCustomerFlowInputAgentExpectation]
        | Omit = omit,
        description: Optional[str] | Omit = omit,
        edge_cases: Iterable[customer_flow_create_params.CreateImprovCustomerFlowInputEdgeCase] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowCreateResponse:
        """Creates a customer flow.

        A SCRIPTED flow carries a step graph and gets one way
        of running it per path through the graph; an IMPROV flow carries the briefs you
        send. Customer flows replace the older simulation scenarios, so build a flow for
        anything new.

        Args:
          agent_ids: Agents this flow exercises. At least one is required for improv flows.

          happy_path: The way this flow is meant to go.

          edge_cases: Other ways of running it, each inheriting from the happy path what it does not
              name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["graph", "title", "type"], ["agent_ids", "happy_path", "title", "type"])
    async def create(
        self,
        *,
        title: str,
        type: Literal["SCRIPTED", "IMPROV"],
        graph: List[FlowStep] | Omit = omit,
        agent_expectations: Union[
            Iterable[customer_flow_create_params.CreateScriptedCustomerFlowInputAgentExpectation],
            Iterable[customer_flow_create_params.CreateImprovCustomerFlowInputAgentExpectation],
        ]
        | Omit = omit,
        agent_ids: SequenceNotStr[str] | Omit = omit,
        branching_mode: Literal["DETERMINISTIC", "ADAPTIVE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        happy_path: customer_flow_create_params.CreateImprovCustomerFlowInputHappyPath | Omit = omit,
        edge_cases: Iterable[customer_flow_create_params.CreateImprovCustomerFlowInputEdgeCase] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowCreateResponse:
        return await self._post(
            "/v1/customer-flow",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "type": type,
                    "graph": graph,
                    "agent_expectations": agent_expectations,
                    "agent_ids": agent_ids,
                    "branching_mode": branching_mode,
                    "description": description,
                    "happy_path": happy_path,
                    "edge_cases": edge_cases,
                },
                customer_flow_create_params.CustomerFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowCreateResponse,
        )

    async def update(
        self,
        flow_id: str,
        *,
        agent_expectations: Iterable[customer_flow_update_params.AgentExpectation] | Omit = omit,
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
    ) -> CustomerFlowUpdateResponse:
        """
        Updates a flow's title, description, branching mode, linked agents or flow-level
        expectations. The step graph is replaced through PUT /graph.

        Args:
          agent_expectations: Replaces the flow-level expectations. Omit to leave them unchanged.

          agent_ids: Replaces the linked agents. Omit to leave them unchanged. An improv flow must
              keep at least one; a scripted flow can be left with none.

          branching_mode: Scripted flows only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._put(
            f"/v1/customer-flow/{flow_id}",
            body=await async_maybe_transform(
                {
                    "agent_expectations": agent_expectations,
                    "agent_ids": agent_ids,
                    "branching_mode": branching_mode,
                    "description": description,
                    "title": title,
                },
                customer_flow_update_params.CustomerFlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowUpdateResponse,
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
    ) -> CustomerFlowListResponse:
        """
        Returns a paginated list of customer flows with their agents, expectations,
        happy path and edge cases. The step graph is the one field omitted: reading it
        walks the project's whole step graph, so it comes back from the single-flow
        endpoint instead. Customer flows are how a project describes what to test; they
        replace the older simulation scenarios.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/customer-flow",
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
                    customer_flow_list_params.CustomerFlowListParams,
                ),
            ),
            cast_to=CustomerFlowListResponse,
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
    ) -> CustomerFlowDeleteResponse:
        """
        Soft-deletes a customer flow along with its edge cases, expectations and (for
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
            f"/v1/customer-flow/{flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowDeleteResponse,
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
    ) -> CustomerFlowGetByIDResponse:
        """
        Returns a customer flow with its happy path, edge cases, expectations and linked
        agents. Scripted flows also carry their step graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._get(
            f"/v1/customer-flow/{flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowGetByIDResponse,
        )

    async def replace_graph(
        self,
        flow_id: str,
        *,
        graph: List[FlowStep],
        allow_unmerge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowReplaceGraphResponse:
        """Replaces a scripted flow's conversation graph with the tree you send.

        This is a
        full replace, not a merge: a step you omit is removed. Include `nodeId` on a
        step to update the existing one, omit it to create a new step. Where two
        branches rejoin, keep the `mergeIntoNodeIds` references a read gave you.
        Dropping them un-merges those branches and is refused unless `allowUnmerge` is
        set. A change to the set of paths re-seeds how the flow runs, which the response
        reports as `variantsReshaped` along with the resulting happy path and edge
        cases.

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
            f"/v1/customer-flow/{flow_id}/graph",
            body=await async_maybe_transform(
                {
                    "graph": graph,
                    "allow_unmerge": allow_unmerge,
                },
                customer_flow_replace_graph_params.CustomerFlowReplaceGraphParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowReplaceGraphResponse,
        )

    async def update_happy_path(
        self,
        flow_id: str,
        *,
        additional_expectations: Iterable[customer_flow_update_happy_path_params.AdditionalExpectation] | Omit = omit,
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
    ) -> CustomerFlowUpdateHappyPathResponse:
        """
        Updates the happy path's title, persona, environment, brief or expectations.
        Omitted fields are left alone; `additionalExpectations` replaces the set
        wholesale rather than appending. Its persona and environment are what the edge
        cases inherit, so changing them here changes every edge case that does not name
        its own.

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
        return await self._put(
            f"/v1/customer-flow/{flow_id}/happy-path",
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
                customer_flow_update_happy_path_params.CustomerFlowUpdateHappyPathParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowUpdateHappyPathResponse,
        )


class CustomerFlowResourceWithRawResponse:
    def __init__(self, customer_flow: CustomerFlowResource) -> None:
        self._customer_flow = customer_flow

        self.create = to_raw_response_wrapper(
            customer_flow.create,
        )
        self.update = to_raw_response_wrapper(
            customer_flow.update,
        )
        self.list = to_raw_response_wrapper(
            customer_flow.list,
        )
        self.delete = to_raw_response_wrapper(
            customer_flow.delete,
        )
        self.get_by_id = to_raw_response_wrapper(
            customer_flow.get_by_id,
        )
        self.replace_graph = to_raw_response_wrapper(
            customer_flow.replace_graph,
        )
        self.update_happy_path = to_raw_response_wrapper(
            customer_flow.update_happy_path,
        )


class AsyncCustomerFlowResourceWithRawResponse:
    def __init__(self, customer_flow: AsyncCustomerFlowResource) -> None:
        self._customer_flow = customer_flow

        self.create = async_to_raw_response_wrapper(
            customer_flow.create,
        )
        self.update = async_to_raw_response_wrapper(
            customer_flow.update,
        )
        self.list = async_to_raw_response_wrapper(
            customer_flow.list,
        )
        self.delete = async_to_raw_response_wrapper(
            customer_flow.delete,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            customer_flow.get_by_id,
        )
        self.replace_graph = async_to_raw_response_wrapper(
            customer_flow.replace_graph,
        )
        self.update_happy_path = async_to_raw_response_wrapper(
            customer_flow.update_happy_path,
        )


class CustomerFlowResourceWithStreamingResponse:
    def __init__(self, customer_flow: CustomerFlowResource) -> None:
        self._customer_flow = customer_flow

        self.create = to_streamed_response_wrapper(
            customer_flow.create,
        )
        self.update = to_streamed_response_wrapper(
            customer_flow.update,
        )
        self.list = to_streamed_response_wrapper(
            customer_flow.list,
        )
        self.delete = to_streamed_response_wrapper(
            customer_flow.delete,
        )
        self.get_by_id = to_streamed_response_wrapper(
            customer_flow.get_by_id,
        )
        self.replace_graph = to_streamed_response_wrapper(
            customer_flow.replace_graph,
        )
        self.update_happy_path = to_streamed_response_wrapper(
            customer_flow.update_happy_path,
        )


class AsyncCustomerFlowResourceWithStreamingResponse:
    def __init__(self, customer_flow: AsyncCustomerFlowResource) -> None:
        self._customer_flow = customer_flow

        self.create = async_to_streamed_response_wrapper(
            customer_flow.create,
        )
        self.update = async_to_streamed_response_wrapper(
            customer_flow.update,
        )
        self.list = async_to_streamed_response_wrapper(
            customer_flow.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            customer_flow.delete,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            customer_flow.get_by_id,
        )
        self.replace_graph = async_to_streamed_response_wrapper(
            customer_flow.replace_graph,
        )
        self.update_happy_path = async_to_streamed_response_wrapper(
            customer_flow.update_happy_path,
        )
