# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, overload
from typing_extensions import Literal

import httpx

from ..types import (
    agent_connection_list_params,
    agent_connection_create_params,
    agent_connection_update_params,
    agent_connection_discover_params,
    agent_connection_create_backfill_params,
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
from ..types.agent_connection_list_response import AgentConnectionListResponse
from ..types.agent_connection_create_response import AgentConnectionCreateResponse
from ..types.agent_connection_delete_response import AgentConnectionDeleteResponse
from ..types.agent_connection_update_response import AgentConnectionUpdateResponse
from ..types.agent_connection_discover_response import AgentConnectionDiscoverResponse
from ..types.agent_connection_get_by_id_response import AgentConnectionGetByIDResponse
from ..types.agent_connection_list_backfills_response import AgentConnectionListBackfillsResponse
from ..types.agent_connection_list_providers_response import AgentConnectionListProvidersResponse
from ..types.agent_connection_cancel_backfill_response import AgentConnectionCancelBackfillResponse
from ..types.agent_connection_create_backfill_response import AgentConnectionCreateBackfillResponse

__all__ = ["AgentConnectionResource", "AsyncAgentConnectionResource"]


class AgentConnectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AgentConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AgentConnectionResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        api_key: str,
        name: str,
        provider: Literal["RETELL"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        name: str,
        provider: Literal["VAPI"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        outbound_request_body_template: Optional[Dict[str, object]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          outbound_request_body_template: Assistant overrides Roark merges into the request when it asks Vapi to place an
              outbound test call.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        name: str,
        provider: Literal["ELEVEN_LABS"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        name: str,
        provider: Literal["BLAND"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        name: str,
        provider: Literal["LEAPING"],
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          agent_ids: The Leaping agent ids to import calls for. Leaping does not list agents, so name
              each one.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        api_secret: str,
        name: str,
        provider: Literal["LIVEKIT"],
        url: str,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        endpoint: agent_connection_create_params.AgentConnectionCreateLivekitEndpoint | Omit = omit,
        metadata_egress_strategy: Literal["EAGER", "DEFERRED"] | Omit = omit,
        metadata_filtering_enabled: bool | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: LiveKit API key. Stored encrypted and never returned.

          api_secret: LiveKit API secret. Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          url: Your LiveKit server URL.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          endpoint: Creates a LiveKit endpoint for each agent the connection brings in, so Roark can
              place test calls to it. Omit to create none; endpoints can be added later on the
              agent.

          metadata_egress_strategy: When the recording starts for a marked room. EAGER starts it at room creation;
              DEFERRED waits for the metadata. Needs `metadataFilteringEnabled`. Defaults to
              DEFERRED.

          metadata_filtering_enabled: Only import rooms whose metadata marks them for Roark. Defaults to false.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        name: str,
        provider: Literal["LIVEKIT_SELF_HOSTED"],
        observer_api_key_name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          name: What the connection is called in Roark. At least 3 characters.

          observer_api_key_name: Name for the Roark API key minted for your SDK to report calls with. Defaults to
              the connection name plus "SDK".

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        name: str,
        provider: Literal["PIPECAT_SELF_HOSTED_INTEGRATION"],
        append_agent_id: bool | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        base_signaling_url: str | Omit = omit,
        observer_api_key_name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          name: What the connection is called in Roark. At least 3 characters.

          append_agent_id: Append the agent's name to the signaling URL, for one server hosting several
              bots. Defaults to true.

          auth_token: Bearer token Roark sends to the signaling URL. Stored encrypted and never
              returned. Null clears it.

          base_signaling_url: Your bot's SmallWebRTC signaling URL. Set it to let Roark place test calls to
              the bot; omit for call import only.

          observer_api_key_name: Name for the Roark API key minted for your SDK to report calls with. Defaults to
              the connection name plus "SDK".

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        name: str,
        provider: Literal["PIPECAT_CLOUD_INTEGRATION"],
        observer_api_key_name: str | Omit = omit,
        pcc_public_key: str | Omit = omit,
        pcc_room_properties: Optional[Dict[str, object]] | Omit = omit,
        pcc_start_body: Optional[Dict[str, object]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          name: What the connection is called in Roark. At least 3 characters.

          observer_api_key_name: Name for the Roark API key minted for your SDK to report calls with. Defaults to
              the connection name plus "SDK".

          pcc_public_key: Pipecat Cloud public API key. Set it to let Roark place test calls through
              Pipecat Cloud; omit for call import only. Stored encrypted and never returned.

          pcc_room_properties: Daily room properties for test calls.

          pcc_start_body: Body Roark sends when starting a session.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        app_id: str,
        env_name: str,
        name: str,
        provider: Literal["KORE"],
        base_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: Kore AI API key. Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          base_url: Kore AI platform URL, when not the default.

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
        app_id: str,
        deployment_id: str,
        location: str,
        name: str,
        provider: Literal["GOOGLE_CES"],
        wif_config: agent_connection_create_params.AgentConnectionCreateGoogleCesWifConfig,
        version_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          name: What the connection is called in Roark. At least 3 characters.

          wif_config: The Workload Identity Federation credential file (`type: external_account`)
              exactly as Google generates it. Stored encrypted and never returned.

          version_id: Pin a version. Omit to use whatever version the deployment serves.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["api_key", "name", "provider"],
        ["api_key", "name", "provider"],
        ["api_key", "name", "provider"],
        ["api_key", "name", "provider"],
        ["agent_ids", "api_key", "name", "provider"],
        ["api_key", "api_secret", "name", "provider", "url"],
        ["name", "provider"],
        ["name", "provider"],
        ["name", "provider"],
        ["api_key", "app_id", "env_name", "name", "provider"],
        ["app_id", "deployment_id", "location", "name", "provider", "wif_config"],
    )
    def create(
        self,
        *,
        name: str,
        provider: Literal[
            "RETELL",
            "VAPI",
            "ELEVEN_LABS",
            "BLAND",
            "LEAPING",
            "LIVEKIT",
            "LIVEKIT_SELF_HOSTED",
            "PIPECAT_SELF_HOSTED_INTEGRATION",
            "PIPECAT_CLOUD_INTEGRATION",
            "KORE",
            "GOOGLE_CES",
        ],
        api_key: str | Omit = omit,
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        outbound_request_body_template: Optional[Dict[str, object]] | Omit = omit,
        api_secret: str | Omit = omit,
        url: str | Omit = omit,
        endpoint: agent_connection_create_params.AgentConnectionCreateLivekitEndpoint | Omit = omit,
        metadata_egress_strategy: Literal["EAGER", "DEFERRED"] | Omit = omit,
        metadata_filtering_enabled: bool | Omit = omit,
        observer_api_key_name: str | Omit = omit,
        append_agent_id: bool | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        base_signaling_url: str | Omit = omit,
        pcc_public_key: str | Omit = omit,
        pcc_room_properties: Optional[Dict[str, object]] | Omit = omit,
        pcc_start_body: Optional[Dict[str, object]] | Omit = omit,
        app_id: str | Omit = omit,
        env_name: str | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        deployment_id: str | Omit = omit,
        location: str | Omit = omit,
        wif_config: agent_connection_create_params.AgentConnectionCreateGoogleCesWifConfig | Omit = omit,
        version_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        return self._post(
            "/v1/connections/agent",
            body=maybe_transform(
                {
                    "name": name,
                    "provider": provider,
                    "api_key": api_key,
                    "agent_ids": agent_ids,
                    "agent_names": agent_names,
                    "agent_scope": agent_scope,
                    "capabilities": capabilities,
                    "sampling_rate": sampling_rate,
                    "outbound_request_body_template": outbound_request_body_template,
                    "api_secret": api_secret,
                    "url": url,
                    "endpoint": endpoint,
                    "metadata_egress_strategy": metadata_egress_strategy,
                    "metadata_filtering_enabled": metadata_filtering_enabled,
                    "observer_api_key_name": observer_api_key_name,
                    "append_agent_id": append_agent_id,
                    "auth_token": auth_token,
                    "base_signaling_url": base_signaling_url,
                    "pcc_public_key": pcc_public_key,
                    "pcc_room_properties": pcc_room_properties,
                    "pcc_start_body": pcc_start_body,
                    "app_id": app_id,
                    "env_name": env_name,
                    "base_url": base_url,
                    "deployment_id": deployment_id,
                    "location": location,
                    "wif_config": wif_config,
                    "version_id": version_id,
                },
                agent_connection_create_params.AgentConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionCreateResponse,
        )

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["RETELL"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["VAPI"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        outbound_request_body_template: Optional[Dict[str, object]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          name: What the connection is called in Roark. At least 3 characters.

          outbound_request_body_template: Assistant overrides Roark merges into the request when it asks Vapi to place an
              outbound test call.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["ELEVEN_LABS"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["BLAND"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["LEAPING"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        api_key: str | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The Leaping agent ids to import calls for. Leaping does not list agents, so name
              each one.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["LIVEKIT"],
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        api_secret: str | Omit = omit,
        metadata_egress_strategy: Literal["EAGER", "DEFERRED"] | Omit = omit,
        metadata_filtering_enabled: bool | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: LiveKit API key. Stored encrypted and never returned.

          api_secret: LiveKit API secret. Stored encrypted and never returned.

          metadata_egress_strategy: When the recording starts for a marked room. EAGER starts it at room creation;
              DEFERRED waits for the metadata. Needs `metadataFilteringEnabled`. Defaults to
              DEFERRED.

          metadata_filtering_enabled: Only import rooms whose metadata marks them for Roark. Defaults to false.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          url: Your LiveKit server URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["LIVEKIT_SELF_HOSTED"],
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["PIPECAT_SELF_HOSTED_INTEGRATION"],
        append_agent_id: bool | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        base_signaling_url: str | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          append_agent_id: Append the agent's name to the signaling URL, for one server hosting several
              bots. Defaults to true.

          auth_token: Bearer token Roark sends to the signaling URL. Stored encrypted and never
              returned. Null clears it.

          base_signaling_url: Your bot's SmallWebRTC signaling URL. Set it to let Roark place test calls to
              the bot; omit for call import only.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["PIPECAT_CLOUD_INTEGRATION"],
        name: str | Omit = omit,
        pcc_public_key: str | Omit = omit,
        pcc_room_properties: Optional[Dict[str, object]] | Omit = omit,
        pcc_start_body: Optional[Dict[str, object]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          name: What the connection is called in Roark. At least 3 characters.

          pcc_public_key: Pipecat Cloud public API key. Set it to let Roark place test calls through
              Pipecat Cloud; omit for call import only. Stored encrypted and never returned.

          pcc_room_properties: Daily room properties for test calls.

          pcc_start_body: Body Roark sends when starting a session.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["KORE"],
        api_key: str | Omit = omit,
        app_id: str | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        env_name: str | Omit = omit,
        name: str | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          api_key: Kore AI API key. Stored encrypted and never returned.

          base_url: Kore AI platform URL, when not the default.

          name: What the connection is called in Roark. At least 3 characters.

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal["GOOGLE_CES"],
        app_id: str | Omit = omit,
        deployment_id: str | Omit = omit,
        location: str | Omit = omit,
        name: str | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        version_id: Optional[str] | Omit = omit,
        wif_config: agent_connection_update_params.AgentConnectionUpdateGoogleCesWifConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          name: What the connection is called in Roark. At least 3 characters.

          status: INACTIVE pauses syncing and call import without deleting anything.

          version_id: Pin a version. Omit to use whatever version the deployment serves.

          wif_config: The Workload Identity Federation credential file (`type: external_account`)
              exactly as Google generates it. Stored encrypted and never returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
    )
    def update(
        self,
        connection_id: str,
        *,
        provider: Literal[
            "RETELL",
            "VAPI",
            "ELEVEN_LABS",
            "BLAND",
            "LEAPING",
            "LIVEKIT",
            "LIVEKIT_SELF_HOSTED",
            "PIPECAT_SELF_HOSTED_INTEGRATION",
            "PIPECAT_CLOUD_INTEGRATION",
            "KORE",
            "GOOGLE_CES",
        ],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        outbound_request_body_template: Optional[Dict[str, object]] | Omit = omit,
        api_secret: str | Omit = omit,
        metadata_egress_strategy: Literal["EAGER", "DEFERRED"] | Omit = omit,
        metadata_filtering_enabled: bool | Omit = omit,
        url: str | Omit = omit,
        append_agent_id: bool | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        base_signaling_url: str | Omit = omit,
        pcc_public_key: str | Omit = omit,
        pcc_room_properties: Optional[Dict[str, object]] | Omit = omit,
        pcc_start_body: Optional[Dict[str, object]] | Omit = omit,
        app_id: str | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        env_name: str | Omit = omit,
        deployment_id: str | Omit = omit,
        location: str | Omit = omit,
        version_id: Optional[str] | Omit = omit,
        wif_config: agent_connection_update_params.AgentConnectionUpdateGoogleCesWifConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._patch(
            f"/v1/connections/agent/{connection_id}",
            body=maybe_transform(
                {
                    "provider": provider,
                    "agent_ids": agent_ids,
                    "agent_names": agent_names,
                    "agent_scope": agent_scope,
                    "api_key": api_key,
                    "capabilities": capabilities,
                    "name": name,
                    "sampling_rate": sampling_rate,
                    "status": status,
                    "outbound_request_body_template": outbound_request_body_template,
                    "api_secret": api_secret,
                    "metadata_egress_strategy": metadata_egress_strategy,
                    "metadata_filtering_enabled": metadata_filtering_enabled,
                    "url": url,
                    "append_agent_id": append_agent_id,
                    "auth_token": auth_token,
                    "base_signaling_url": base_signaling_url,
                    "pcc_public_key": pcc_public_key,
                    "pcc_room_properties": pcc_room_properties,
                    "pcc_start_body": pcc_start_body,
                    "app_id": app_id,
                    "base_url": base_url,
                    "env_name": env_name,
                    "deployment_id": deployment_id,
                    "location": location,
                    "version_id": version_id,
                    "wif_config": wif_config,
                },
                agent_connection_update_params.AgentConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        provider: Literal[
            "RETELL",
            "VAPI",
            "ELEVEN_LABS",
            "BLAND",
            "LEAPING",
            "LIVEKIT",
            "LIVEKIT_SELF_HOSTED",
            "PIPECAT_CLOUD_INTEGRATION",
            "PIPECAT_SELF_HOSTED_INTEGRATION",
            "KORE",
            "GOOGLE_CES",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionListResponse:
        """
        The project's connections to the platforms its agents run on (Retell, Vapi,
        LiveKit, Pipecat and others), each with its settings and latest sync.
        Credentials are never returned.

        Args:
          provider: The platform the agents run on. LIVEKIT is LiveKit Cloud; LIVEKIT_SELF_HOSTED is
              the LiveKit Agents SDK reporting through the Roark plugin.
              PIPECAT_CLOUD_INTEGRATION and PIPECAT_SELF_HOSTED_INTEGRATION are Pipecat Cloud
              and a self-hosted Pipecat bot. `GET /v1/connections/agent/providers` describes
              what each one needs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/connections/agent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"provider": provider}, agent_connection_list_params.AgentConnectionListParams),
            ),
            cast_to=AgentConnectionListResponse,
        )

    def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionDeleteResponse:
        """Deletes the connection and its stored credential, and stops syncing.

        Agents and
        calls it already brought in stay in the project. Alerts that notify through it
        stop notifying.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._delete(
            f"/v1/connections/agent/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionDeleteResponse,
        )

    def cancel_backfill(
        self,
        backfill_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCancelBackfillResponse:
        """Stops a running backfill.

        Calls it already imported stay.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not backfill_id:
            raise ValueError(f"Expected a non-empty value for `backfill_id` but received {backfill_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            f"/v1/connections/agent/{connection_id}/backfills/{backfill_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionCancelBackfillResponse,
        )

    def create_backfill(
        self,
        connection_id: str,
        *,
        max_calls: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateBackfillResponse:
        """
        Starts a backfill that imports up to `maxCalls` of the most recent past calls
        from a Retell, Vapi, ElevenLabs or Leaping connection. Other platforms return
        400.

        Args:
          max_calls: How many of the most recent past calls to import, up to 1000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            f"/v1/connections/agent/{connection_id}/backfills",
            body=maybe_transform(
                {"max_calls": max_calls}, agent_connection_create_backfill_params.AgentConnectionCreateBackfillParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionCreateBackfillResponse,
        )

    def discover(
        self,
        *,
        api_key: str,
        provider: Literal["RETELL", "VAPI", "ELEVEN_LABS", "BLAND"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionDiscoverResponse:
        """
        Lists the agents a Retell, Vapi, ElevenLabs or Bland API key can see, without
        storing anything. Use it to check a key and to pick `agentIds` before
        connecting. Any failure returns 400: `invalid_credentials` when the platform
        refuses the key, `too_many_requests` when it rate limits the request, and
        `dependency_failure` when it returns an error.

        Args:
          api_key: The platform API key to list agents with. Stored nowhere.

          provider: Platforms whose agents can be listed with a key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/connections/agent/discover",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "provider": provider,
                },
                agent_connection_discover_params.AgentConnectionDiscoverParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionDiscoverResponse,
        )

    def get_by_id(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionGetByIDResponse:
        """One connection, with its settings and latest sync.

        Credentials are never
        returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/v1/connections/agent/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionGetByIDResponse,
        )

    def list_backfills(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionListBackfillsResponse:
        """
        A connection's imports of past calls, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/v1/connections/agent/{connection_id}/backfills",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionListBackfillsResponse,
        )

    def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionListProvidersResponse:
        """
        Every platform a project can connect, with the fields its create body needs, how
        its calls reach Roark, and which settings apply. Read this before connecting
        one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/connections/agent/providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionListProvidersResponse,
        )


class AsyncAgentConnectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncAgentConnectionResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        api_key: str,
        name: str,
        provider: Literal["RETELL"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        name: str,
        provider: Literal["VAPI"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        outbound_request_body_template: Optional[Dict[str, object]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          outbound_request_body_template: Assistant overrides Roark merges into the request when it asks Vapi to place an
              outbound test call.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        name: str,
        provider: Literal["ELEVEN_LABS"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        name: str,
        provider: Literal["BLAND"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        name: str,
        provider: Literal["LEAPING"],
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          agent_ids: The Leaping agent ids to import calls for. Leaping does not list agents, so name
              each one.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        api_secret: str,
        name: str,
        provider: Literal["LIVEKIT"],
        url: str,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        endpoint: agent_connection_create_params.AgentConnectionCreateLivekitEndpoint | Omit = omit,
        metadata_egress_strategy: Literal["EAGER", "DEFERRED"] | Omit = omit,
        metadata_filtering_enabled: bool | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: LiveKit API key. Stored encrypted and never returned.

          api_secret: LiveKit API secret. Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          url: Your LiveKit server URL.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          endpoint: Creates a LiveKit endpoint for each agent the connection brings in, so Roark can
              place test calls to it. Omit to create none; endpoints can be added later on the
              agent.

          metadata_egress_strategy: When the recording starts for a marked room. EAGER starts it at room creation;
              DEFERRED waits for the metadata. Needs `metadataFilteringEnabled`. Defaults to
              DEFERRED.

          metadata_filtering_enabled: Only import rooms whose metadata marks them for Roark. Defaults to false.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        name: str,
        provider: Literal["LIVEKIT_SELF_HOSTED"],
        observer_api_key_name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          name: What the connection is called in Roark. At least 3 characters.

          observer_api_key_name: Name for the Roark API key minted for your SDK to report calls with. Defaults to
              the connection name plus "SDK".

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        name: str,
        provider: Literal["PIPECAT_SELF_HOSTED_INTEGRATION"],
        append_agent_id: bool | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        base_signaling_url: str | Omit = omit,
        observer_api_key_name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          name: What the connection is called in Roark. At least 3 characters.

          append_agent_id: Append the agent's name to the signaling URL, for one server hosting several
              bots. Defaults to true.

          auth_token: Bearer token Roark sends to the signaling URL. Stored encrypted and never
              returned. Null clears it.

          base_signaling_url: Your bot's SmallWebRTC signaling URL. Set it to let Roark place test calls to
              the bot; omit for call import only.

          observer_api_key_name: Name for the Roark API key minted for your SDK to report calls with. Defaults to
              the connection name plus "SDK".

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        name: str,
        provider: Literal["PIPECAT_CLOUD_INTEGRATION"],
        observer_api_key_name: str | Omit = omit,
        pcc_public_key: str | Omit = omit,
        pcc_room_properties: Optional[Dict[str, object]] | Omit = omit,
        pcc_start_body: Optional[Dict[str, object]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          name: What the connection is called in Roark. At least 3 characters.

          observer_api_key_name: Name for the Roark API key minted for your SDK to report calls with. Defaults to
              the connection name plus "SDK".

          pcc_public_key: Pipecat Cloud public API key. Set it to let Roark place test calls through
              Pipecat Cloud; omit for call import only. Stored encrypted and never returned.

          pcc_room_properties: Daily room properties for test calls.

          pcc_start_body: Body Roark sends when starting a session.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

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
        api_key: str,
        app_id: str,
        env_name: str,
        name: str,
        provider: Literal["KORE"],
        base_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          api_key: Kore AI API key. Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          base_url: Kore AI platform URL, when not the default.

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
        app_id: str,
        deployment_id: str,
        location: str,
        name: str,
        provider: Literal["GOOGLE_CES"],
        wif_config: agent_connection_create_params.AgentConnectionCreateGoogleCesWifConfig,
        version_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        """Connects the platform a project’s agents run on.

        The body is shaped by
        `provider`; `GET /v1/connections/agent/providers` lists what each needs. Retell,
        Vapi, ElevenLabs and Bland keys are checked by listing agents first, so a
        refused key returns 400 and nothing is stored. An account with more agents than
        the project allows for `agentScope` ALL (25 unless raised for the project)
        returns 400 `too_many_agents`, including when `agentScope` is left out: send
        SELECTED with the `agentIds` to bring in, up to 1,000. Platforms that pull
        agents start syncing straight away. For LIVEKIT_SELF_HOSTED and the Pipecat
        providers, the response carries `observerApiKey`, shown once, for your SDK to
        report calls with. Most platforms connect once per project, and a second create
        returns 409; LiveKit Cloud may connect several accounts.

        Args:
          name: What the connection is called in Roark. At least 3 characters.

          wif_config: The Workload Identity Federation credential file (`type: external_account`)
              exactly as Google generates it. Stored encrypted and never returned.

          version_id: Pin a version. Omit to use whatever version the deployment serves.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["api_key", "name", "provider"],
        ["api_key", "name", "provider"],
        ["api_key", "name", "provider"],
        ["api_key", "name", "provider"],
        ["agent_ids", "api_key", "name", "provider"],
        ["api_key", "api_secret", "name", "provider", "url"],
        ["name", "provider"],
        ["name", "provider"],
        ["name", "provider"],
        ["api_key", "app_id", "env_name", "name", "provider"],
        ["app_id", "deployment_id", "location", "name", "provider", "wif_config"],
    )
    async def create(
        self,
        *,
        name: str,
        provider: Literal[
            "RETELL",
            "VAPI",
            "ELEVEN_LABS",
            "BLAND",
            "LEAPING",
            "LIVEKIT",
            "LIVEKIT_SELF_HOSTED",
            "PIPECAT_SELF_HOSTED_INTEGRATION",
            "PIPECAT_CLOUD_INTEGRATION",
            "KORE",
            "GOOGLE_CES",
        ],
        api_key: str | Omit = omit,
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        outbound_request_body_template: Optional[Dict[str, object]] | Omit = omit,
        api_secret: str | Omit = omit,
        url: str | Omit = omit,
        endpoint: agent_connection_create_params.AgentConnectionCreateLivekitEndpoint | Omit = omit,
        metadata_egress_strategy: Literal["EAGER", "DEFERRED"] | Omit = omit,
        metadata_filtering_enabled: bool | Omit = omit,
        observer_api_key_name: str | Omit = omit,
        append_agent_id: bool | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        base_signaling_url: str | Omit = omit,
        pcc_public_key: str | Omit = omit,
        pcc_room_properties: Optional[Dict[str, object]] | Omit = omit,
        pcc_start_body: Optional[Dict[str, object]] | Omit = omit,
        app_id: str | Omit = omit,
        env_name: str | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        deployment_id: str | Omit = omit,
        location: str | Omit = omit,
        wif_config: agent_connection_create_params.AgentConnectionCreateGoogleCesWifConfig | Omit = omit,
        version_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateResponse:
        return await self._post(
            "/v1/connections/agent",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "provider": provider,
                    "api_key": api_key,
                    "agent_ids": agent_ids,
                    "agent_names": agent_names,
                    "agent_scope": agent_scope,
                    "capabilities": capabilities,
                    "sampling_rate": sampling_rate,
                    "outbound_request_body_template": outbound_request_body_template,
                    "api_secret": api_secret,
                    "url": url,
                    "endpoint": endpoint,
                    "metadata_egress_strategy": metadata_egress_strategy,
                    "metadata_filtering_enabled": metadata_filtering_enabled,
                    "observer_api_key_name": observer_api_key_name,
                    "append_agent_id": append_agent_id,
                    "auth_token": auth_token,
                    "base_signaling_url": base_signaling_url,
                    "pcc_public_key": pcc_public_key,
                    "pcc_room_properties": pcc_room_properties,
                    "pcc_start_body": pcc_start_body,
                    "app_id": app_id,
                    "env_name": env_name,
                    "base_url": base_url,
                    "deployment_id": deployment_id,
                    "location": location,
                    "wif_config": wif_config,
                    "version_id": version_id,
                },
                agent_connection_create_params.AgentConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionCreateResponse,
        )

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["RETELL"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["VAPI"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        outbound_request_body_template: Optional[Dict[str, object]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          name: What the connection is called in Roark. At least 3 characters.

          outbound_request_body_template: Assistant overrides Roark merges into the request when it asks Vapi to place an
              outbound test call.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["ELEVEN_LABS"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["BLAND"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The platform's own ids of the agents to bring in when `agentScope` is SELECTED.
              `POST /v1/connections/agent/discover` lists them.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          capabilities: What the connection does. Defaults to PULL_AGENTS and PULL_CALLS, plus
              PUSH_AGENT_CONFIG on Retell, Vapi and ElevenLabs.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["LEAPING"],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        api_key: str | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_ids: The Leaping agent ids to import calls for. Leaping does not list agents, so name
              each one.

          api_key: The platform's API key. Checked against the platform before anything is stored.
              Stored encrypted and never returned.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["LIVEKIT"],
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        api_secret: str | Omit = omit,
        metadata_egress_strategy: Literal["EAGER", "DEFERRED"] | Omit = omit,
        metadata_filtering_enabled: bool | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          agent_names: Agents to create by name rather than by id, for agents the platform does not
              list. On LiveKit Cloud this is the agent name your worker dispatches as.

          agent_scope: ALL brings in every agent on the account, and is refused with `too_many_agents`
              when the account has more agents than the project allows (25 unless raised for
              the project). SELECTED brings in only `agentIds` and `agentNames`, up to 1,000.

          api_key: LiveKit API key. Stored encrypted and never returned.

          api_secret: LiveKit API secret. Stored encrypted and never returned.

          metadata_egress_strategy: When the recording starts for a marked room. EAGER starts it at room creation;
              DEFERRED waits for the metadata. Needs `metadataFilteringEnabled`. Defaults to
              DEFERRED.

          metadata_filtering_enabled: Only import rooms whose metadata marks them for Roark. Defaults to false.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          url: Your LiveKit server URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["LIVEKIT_SELF_HOSTED"],
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["PIPECAT_SELF_HOSTED_INTEGRATION"],
        append_agent_id: bool | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        base_signaling_url: str | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          append_agent_id: Append the agent's name to the signaling URL, for one server hosting several
              bots. Defaults to true.

          auth_token: Bearer token Roark sends to the signaling URL. Stored encrypted and never
              returned. Null clears it.

          base_signaling_url: Your bot's SmallWebRTC signaling URL. Set it to let Roark place test calls to
              the bot; omit for call import only.

          name: What the connection is called in Roark. At least 3 characters.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["PIPECAT_CLOUD_INTEGRATION"],
        name: str | Omit = omit,
        pcc_public_key: str | Omit = omit,
        pcc_room_properties: Optional[Dict[str, object]] | Omit = omit,
        pcc_start_body: Optional[Dict[str, object]] | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          name: What the connection is called in Roark. At least 3 characters.

          pcc_public_key: Pipecat Cloud public API key. Set it to let Roark place test calls through
              Pipecat Cloud; omit for call import only. Stored encrypted and never returned.

          pcc_room_properties: Daily room properties for test calls.

          pcc_start_body: Body Roark sends when starting a session.

          sampling_rate: Fraction of production calls to import and analyse, from 0 to 1. Defaults to 1
              (every call).

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["KORE"],
        api_key: str | Omit = omit,
        app_id: str | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        env_name: str | Omit = omit,
        name: str | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          api_key: Kore AI API key. Stored encrypted and never returned.

          base_url: Kore AI platform URL, when not the default.

          name: What the connection is called in Roark. At least 3 characters.

          status: INACTIVE pauses syncing and call import without deleting anything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal["GOOGLE_CES"],
        app_id: str | Omit = omit,
        deployment_id: str | Omit = omit,
        location: str | Omit = omit,
        name: str | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        version_id: Optional[str] | Omit = omit,
        wif_config: agent_connection_update_params.AgentConnectionUpdateGoogleCesWifConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        """Changes a connection’s settings or rotates its credential.

        Send `provider` (it
        must match the connection’s) and only the fields to change; the rest keep their
        stored values. A new Retell, Vapi, ElevenLabs or Bland key is checked by listing
        agents first. Moving to `agentScope` ALL, or giving an ALL connection a new key,
        on an account with more agents than the project allows returns 400
        `too_many_agents`, as does selecting more than 1,000. Set `status` to INACTIVE
        to pause syncing without deleting anything.

        Args:
          provider: The connection's provider. It cannot change.

          name: What the connection is called in Roark. At least 3 characters.

          status: INACTIVE pauses syncing and call import without deleting anything.

          version_id: Pin a version. Omit to use whatever version the deployment serves.

          wif_config: The Workload Identity Federation credential file (`type: external_account`)
              exactly as Google generates it. Stored encrypted and never returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
        ["provider"],
    )
    async def update(
        self,
        connection_id: str,
        *,
        provider: Literal[
            "RETELL",
            "VAPI",
            "ELEVEN_LABS",
            "BLAND",
            "LEAPING",
            "LIVEKIT",
            "LIVEKIT_SELF_HOSTED",
            "PIPECAT_SELF_HOSTED_INTEGRATION",
            "PIPECAT_CLOUD_INTEGRATION",
            "KORE",
            "GOOGLE_CES",
        ],
        agent_ids: SequenceNotStr[str] | Omit = omit,
        agent_names: SequenceNotStr[str] | Omit = omit,
        agent_scope: Literal["ALL", "SELECTED"] | Omit = omit,
        api_key: str | Omit = omit,
        capabilities: List[Literal["PULL_AGENTS", "PULL_CALLS", "PUSH_AGENT_CONFIG"]] | Omit = omit,
        name: str | Omit = omit,
        sampling_rate: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        outbound_request_body_template: Optional[Dict[str, object]] | Omit = omit,
        api_secret: str | Omit = omit,
        metadata_egress_strategy: Literal["EAGER", "DEFERRED"] | Omit = omit,
        metadata_filtering_enabled: bool | Omit = omit,
        url: str | Omit = omit,
        append_agent_id: bool | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        base_signaling_url: str | Omit = omit,
        pcc_public_key: str | Omit = omit,
        pcc_room_properties: Optional[Dict[str, object]] | Omit = omit,
        pcc_start_body: Optional[Dict[str, object]] | Omit = omit,
        app_id: str | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        env_name: str | Omit = omit,
        deployment_id: str | Omit = omit,
        location: str | Omit = omit,
        version_id: Optional[str] | Omit = omit,
        wif_config: agent_connection_update_params.AgentConnectionUpdateGoogleCesWifConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionUpdateResponse:
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._patch(
            f"/v1/connections/agent/{connection_id}",
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "agent_ids": agent_ids,
                    "agent_names": agent_names,
                    "agent_scope": agent_scope,
                    "api_key": api_key,
                    "capabilities": capabilities,
                    "name": name,
                    "sampling_rate": sampling_rate,
                    "status": status,
                    "outbound_request_body_template": outbound_request_body_template,
                    "api_secret": api_secret,
                    "metadata_egress_strategy": metadata_egress_strategy,
                    "metadata_filtering_enabled": metadata_filtering_enabled,
                    "url": url,
                    "append_agent_id": append_agent_id,
                    "auth_token": auth_token,
                    "base_signaling_url": base_signaling_url,
                    "pcc_public_key": pcc_public_key,
                    "pcc_room_properties": pcc_room_properties,
                    "pcc_start_body": pcc_start_body,
                    "app_id": app_id,
                    "base_url": base_url,
                    "env_name": env_name,
                    "deployment_id": deployment_id,
                    "location": location,
                    "version_id": version_id,
                    "wif_config": wif_config,
                },
                agent_connection_update_params.AgentConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionUpdateResponse,
        )

    async def list(
        self,
        *,
        provider: Literal[
            "RETELL",
            "VAPI",
            "ELEVEN_LABS",
            "BLAND",
            "LEAPING",
            "LIVEKIT",
            "LIVEKIT_SELF_HOSTED",
            "PIPECAT_CLOUD_INTEGRATION",
            "PIPECAT_SELF_HOSTED_INTEGRATION",
            "KORE",
            "GOOGLE_CES",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionListResponse:
        """
        The project's connections to the platforms its agents run on (Retell, Vapi,
        LiveKit, Pipecat and others), each with its settings and latest sync.
        Credentials are never returned.

        Args:
          provider: The platform the agents run on. LIVEKIT is LiveKit Cloud; LIVEKIT_SELF_HOSTED is
              the LiveKit Agents SDK reporting through the Roark plugin.
              PIPECAT_CLOUD_INTEGRATION and PIPECAT_SELF_HOSTED_INTEGRATION are Pipecat Cloud
              and a self-hosted Pipecat bot. `GET /v1/connections/agent/providers` describes
              what each one needs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/connections/agent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"provider": provider}, agent_connection_list_params.AgentConnectionListParams
                ),
            ),
            cast_to=AgentConnectionListResponse,
        )

    async def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionDeleteResponse:
        """Deletes the connection and its stored credential, and stops syncing.

        Agents and
        calls it already brought in stay in the project. Alerts that notify through it
        stop notifying.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._delete(
            f"/v1/connections/agent/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionDeleteResponse,
        )

    async def cancel_backfill(
        self,
        backfill_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCancelBackfillResponse:
        """Stops a running backfill.

        Calls it already imported stay.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not backfill_id:
            raise ValueError(f"Expected a non-empty value for `backfill_id` but received {backfill_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            f"/v1/connections/agent/{connection_id}/backfills/{backfill_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionCancelBackfillResponse,
        )

    async def create_backfill(
        self,
        connection_id: str,
        *,
        max_calls: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionCreateBackfillResponse:
        """
        Starts a backfill that imports up to `maxCalls` of the most recent past calls
        from a Retell, Vapi, ElevenLabs or Leaping connection. Other platforms return
        400.

        Args:
          max_calls: How many of the most recent past calls to import, up to 1000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            f"/v1/connections/agent/{connection_id}/backfills",
            body=await async_maybe_transform(
                {"max_calls": max_calls}, agent_connection_create_backfill_params.AgentConnectionCreateBackfillParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionCreateBackfillResponse,
        )

    async def discover(
        self,
        *,
        api_key: str,
        provider: Literal["RETELL", "VAPI", "ELEVEN_LABS", "BLAND"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionDiscoverResponse:
        """
        Lists the agents a Retell, Vapi, ElevenLabs or Bland API key can see, without
        storing anything. Use it to check a key and to pick `agentIds` before
        connecting. Any failure returns 400: `invalid_credentials` when the platform
        refuses the key, `too_many_requests` when it rate limits the request, and
        `dependency_failure` when it returns an error.

        Args:
          api_key: The platform API key to list agents with. Stored nowhere.

          provider: Platforms whose agents can be listed with a key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/connections/agent/discover",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "provider": provider,
                },
                agent_connection_discover_params.AgentConnectionDiscoverParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionDiscoverResponse,
        )

    async def get_by_id(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionGetByIDResponse:
        """One connection, with its settings and latest sync.

        Credentials are never
        returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/v1/connections/agent/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionGetByIDResponse,
        )

    async def list_backfills(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionListBackfillsResponse:
        """
        A connection's imports of past calls, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/v1/connections/agent/{connection_id}/backfills",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionListBackfillsResponse,
        )

    async def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentConnectionListProvidersResponse:
        """
        Every platform a project can connect, with the fields its create body needs, how
        its calls reach Roark, and which settings apply. Read this before connecting
        one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/connections/agent/providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentConnectionListProvidersResponse,
        )


class AgentConnectionResourceWithRawResponse:
    def __init__(self, agent_connection: AgentConnectionResource) -> None:
        self._agent_connection = agent_connection

        self.create = to_raw_response_wrapper(
            agent_connection.create,
        )
        self.update = to_raw_response_wrapper(
            agent_connection.update,
        )
        self.list = to_raw_response_wrapper(
            agent_connection.list,
        )
        self.delete = to_raw_response_wrapper(
            agent_connection.delete,
        )
        self.cancel_backfill = to_raw_response_wrapper(
            agent_connection.cancel_backfill,
        )
        self.create_backfill = to_raw_response_wrapper(
            agent_connection.create_backfill,
        )
        self.discover = to_raw_response_wrapper(
            agent_connection.discover,
        )
        self.get_by_id = to_raw_response_wrapper(
            agent_connection.get_by_id,
        )
        self.list_backfills = to_raw_response_wrapper(
            agent_connection.list_backfills,
        )
        self.list_providers = to_raw_response_wrapper(
            agent_connection.list_providers,
        )


class AsyncAgentConnectionResourceWithRawResponse:
    def __init__(self, agent_connection: AsyncAgentConnectionResource) -> None:
        self._agent_connection = agent_connection

        self.create = async_to_raw_response_wrapper(
            agent_connection.create,
        )
        self.update = async_to_raw_response_wrapper(
            agent_connection.update,
        )
        self.list = async_to_raw_response_wrapper(
            agent_connection.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agent_connection.delete,
        )
        self.cancel_backfill = async_to_raw_response_wrapper(
            agent_connection.cancel_backfill,
        )
        self.create_backfill = async_to_raw_response_wrapper(
            agent_connection.create_backfill,
        )
        self.discover = async_to_raw_response_wrapper(
            agent_connection.discover,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            agent_connection.get_by_id,
        )
        self.list_backfills = async_to_raw_response_wrapper(
            agent_connection.list_backfills,
        )
        self.list_providers = async_to_raw_response_wrapper(
            agent_connection.list_providers,
        )


class AgentConnectionResourceWithStreamingResponse:
    def __init__(self, agent_connection: AgentConnectionResource) -> None:
        self._agent_connection = agent_connection

        self.create = to_streamed_response_wrapper(
            agent_connection.create,
        )
        self.update = to_streamed_response_wrapper(
            agent_connection.update,
        )
        self.list = to_streamed_response_wrapper(
            agent_connection.list,
        )
        self.delete = to_streamed_response_wrapper(
            agent_connection.delete,
        )
        self.cancel_backfill = to_streamed_response_wrapper(
            agent_connection.cancel_backfill,
        )
        self.create_backfill = to_streamed_response_wrapper(
            agent_connection.create_backfill,
        )
        self.discover = to_streamed_response_wrapper(
            agent_connection.discover,
        )
        self.get_by_id = to_streamed_response_wrapper(
            agent_connection.get_by_id,
        )
        self.list_backfills = to_streamed_response_wrapper(
            agent_connection.list_backfills,
        )
        self.list_providers = to_streamed_response_wrapper(
            agent_connection.list_providers,
        )


class AsyncAgentConnectionResourceWithStreamingResponse:
    def __init__(self, agent_connection: AsyncAgentConnectionResource) -> None:
        self._agent_connection = agent_connection

        self.create = async_to_streamed_response_wrapper(
            agent_connection.create,
        )
        self.update = async_to_streamed_response_wrapper(
            agent_connection.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agent_connection.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agent_connection.delete,
        )
        self.cancel_backfill = async_to_streamed_response_wrapper(
            agent_connection.cancel_backfill,
        )
        self.create_backfill = async_to_streamed_response_wrapper(
            agent_connection.create_backfill,
        )
        self.discover = async_to_streamed_response_wrapper(
            agent_connection.discover,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            agent_connection.get_by_id,
        )
        self.list_backfills = async_to_streamed_response_wrapper(
            agent_connection.list_backfills,
        )
        self.list_providers = async_to_streamed_response_wrapper(
            agent_connection.list_providers,
        )
