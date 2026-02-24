# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import simulation_persona_list_params, simulation_persona_create_params, simulation_persona_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.simulation_persona_list_response import SimulationPersonaListResponse
from ..types.simulation_persona_create_response import SimulationPersonaCreateResponse
from ..types.simulation_persona_update_response import SimulationPersonaUpdateResponse
from ..types.simulation_persona_get_by_id_response import SimulationPersonaGetByIDResponse

__all__ = ["SimulationPersonaResource", "AsyncSimulationPersonaResource"]


class SimulationPersonaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationPersonaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return SimulationPersonaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationPersonaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return SimulationPersonaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        accent: Literal[
            "US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT", "ID", "TH", "JP"
        ],
        gender: Literal["MALE", "FEMALE"],
        language: Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT", "ID", "TH", "JA"],
        name: str,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        backstory_prompt: Optional[str] | Omit = omit,
        base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"] | Omit = omit,
        confirmation_style: Literal["EXPLICIT", "VAGUE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        has_disfluencies: bool | Omit = omit,
        idle_message_max_spoken_count: int | Omit = omit,
        idle_message_reset_count_on_user_speech_enabled: bool | Omit = omit,
        idle_messages: SequenceNotStr[str] | Omit = omit,
        idle_timeout_seconds: int | Omit = omit,
        intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] | Omit = omit,
        memory_reliability: Literal["HIGH", "LOW"] | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        response_timing: Literal["RELAXED", "NORMAL", "QUICK"] | Omit = omit,
        secondary_language: Optional[Literal["EN"]] | Omit = omit,
        speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] | Omit = omit,
        speech_pace: Literal["SLOW", "NORMAL", "FAST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPersonaCreateResponse:
        """
        Creates a new persona for the authenticated project.

        Args:
          accent: Accent of the persona, defined using ISO 3166-1 alpha-2 country codes with
              optional variants

          gender: Gender of the persona

          language: Primary language ISO 639-1 code for the persona

          name: The name the agent will identify as during conversations

          background_noise: Background noise setting

          backstory_prompt: Background story and behavioral patterns for the persona

          base_emotion: Base emotional state of the persona

          confirmation_style: How the persona confirms information

          description: Human-readable description of the persona

          has_disfluencies: Whether the persona uses filler words like "um" and "uh"

          idle_message_max_spoken_count: Maximum number of idle messages the persona will send before giving up

          idle_message_reset_count_on_user_speech_enabled: Whether the idle message counter resets when the agent speaks

          idle_messages: Messages the persona will say when the agent goes silent during a call

          idle_timeout_seconds: Seconds of silence before the persona sends an idle message

          intent_clarity: How clearly the persona expresses their intentions

          memory_reliability: How reliable the persona's memory is

          properties: Additional custom properties about the persona

          response_timing: Controls how quickly the persona responds to pauses in conversation (QUICK,
              NORMAL, RELAXED)

          secondary_language: Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)

          speech_clarity: Speech clarity of the persona

          speech_pace: Speech pace of the persona

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/persona",
            body=maybe_transform(
                {
                    "accent": accent,
                    "gender": gender,
                    "language": language,
                    "name": name,
                    "background_noise": background_noise,
                    "backstory_prompt": backstory_prompt,
                    "base_emotion": base_emotion,
                    "confirmation_style": confirmation_style,
                    "description": description,
                    "has_disfluencies": has_disfluencies,
                    "idle_message_max_spoken_count": idle_message_max_spoken_count,
                    "idle_message_reset_count_on_user_speech_enabled": idle_message_reset_count_on_user_speech_enabled,
                    "idle_messages": idle_messages,
                    "idle_timeout_seconds": idle_timeout_seconds,
                    "intent_clarity": intent_clarity,
                    "memory_reliability": memory_reliability,
                    "properties": properties,
                    "response_timing": response_timing,
                    "secondary_language": secondary_language,
                    "speech_clarity": speech_clarity,
                    "speech_pace": speech_pace,
                },
                simulation_persona_create_params.SimulationPersonaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationPersonaCreateResponse,
        )

    def update(
        self,
        persona_id: str,
        *,
        accent: Literal[
            "US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT", "ID", "TH", "JP"
        ]
        | Omit = omit,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        backstory_prompt: Optional[str] | Omit = omit,
        base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"] | Omit = omit,
        confirmation_style: Literal["EXPLICIT", "VAGUE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        gender: Literal["MALE", "FEMALE"] | Omit = omit,
        has_disfluencies: bool | Omit = omit,
        idle_message_max_spoken_count: int | Omit = omit,
        idle_message_reset_count_on_user_speech_enabled: bool | Omit = omit,
        idle_messages: SequenceNotStr[str] | Omit = omit,
        idle_timeout_seconds: int | Omit = omit,
        intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] | Omit = omit,
        language: Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT", "ID", "TH", "JA"] | Omit = omit,
        memory_reliability: Literal["HIGH", "LOW"] | Omit = omit,
        name: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        response_timing: Literal["RELAXED", "NORMAL", "QUICK"] | Omit = omit,
        secondary_language: Optional[Literal["EN"]] | Omit = omit,
        speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] | Omit = omit,
        speech_pace: Literal["SLOW", "NORMAL", "FAST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPersonaUpdateResponse:
        """
        Updates an existing persona by its ID.

        Args:
          accent: Accent of the persona, defined using ISO 3166-1 alpha-2 country codes with
              optional variants

          background_noise: Background noise setting

          backstory_prompt: Background story and behavioral patterns for the persona

          base_emotion: Base emotional state of the persona

          confirmation_style: How the persona confirms information

          description: Human-readable description of the persona

          gender: Gender of the persona

          has_disfluencies: Whether the persona uses filler words like "um" and "uh"

          idle_message_max_spoken_count: Maximum number of idle messages the persona will send before giving up

          idle_message_reset_count_on_user_speech_enabled: Whether the idle message counter resets when the agent speaks

          idle_messages: Messages the persona will say when the agent goes silent during a call

          idle_timeout_seconds: Seconds of silence before the persona sends an idle message

          intent_clarity: How clearly the persona expresses their intentions

          language: Primary language ISO 639-1 code for the persona

          memory_reliability: How reliable the persona's memory is

          name: The name the agent will identify as during conversations

          properties: Additional custom properties about the persona

          response_timing: Controls how quickly the persona responds to pauses in conversation (QUICK,
              NORMAL, RELAXED)

          secondary_language: Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)

          speech_clarity: Speech clarity of the persona

          speech_pace: Speech pace of the persona

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not persona_id:
            raise ValueError(f"Expected a non-empty value for `persona_id` but received {persona_id!r}")
        return self._put(
            f"/v1/persona/{persona_id}",
            body=maybe_transform(
                {
                    "accent": accent,
                    "background_noise": background_noise,
                    "backstory_prompt": backstory_prompt,
                    "base_emotion": base_emotion,
                    "confirmation_style": confirmation_style,
                    "description": description,
                    "gender": gender,
                    "has_disfluencies": has_disfluencies,
                    "idle_message_max_spoken_count": idle_message_max_spoken_count,
                    "idle_message_reset_count_on_user_speech_enabled": idle_message_reset_count_on_user_speech_enabled,
                    "idle_messages": idle_messages,
                    "idle_timeout_seconds": idle_timeout_seconds,
                    "intent_clarity": intent_clarity,
                    "language": language,
                    "memory_reliability": memory_reliability,
                    "name": name,
                    "properties": properties,
                    "response_timing": response_timing,
                    "secondary_language": secondary_language,
                    "speech_clarity": speech_clarity,
                    "speech_pace": speech_pace,
                },
                simulation_persona_update_params.SimulationPersonaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationPersonaUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPersonaListResponse:
        """
        Returns a paginated list of personas for the authenticated project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/persona",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "search_text": search_text,
                    },
                    simulation_persona_list_params.SimulationPersonaListParams,
                ),
            ),
            cast_to=SimulationPersonaListResponse,
        )

    def get_by_id(
        self,
        persona_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPersonaGetByIDResponse:
        """
        Returns a specific persona by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not persona_id:
            raise ValueError(f"Expected a non-empty value for `persona_id` but received {persona_id!r}")
        return self._get(
            f"/v1/persona/{persona_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationPersonaGetByIDResponse,
        )


class AsyncSimulationPersonaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationPersonaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationPersonaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationPersonaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncSimulationPersonaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        accent: Literal[
            "US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT", "ID", "TH", "JP"
        ],
        gender: Literal["MALE", "FEMALE"],
        language: Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT", "ID", "TH", "JA"],
        name: str,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        backstory_prompt: Optional[str] | Omit = omit,
        base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"] | Omit = omit,
        confirmation_style: Literal["EXPLICIT", "VAGUE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        has_disfluencies: bool | Omit = omit,
        idle_message_max_spoken_count: int | Omit = omit,
        idle_message_reset_count_on_user_speech_enabled: bool | Omit = omit,
        idle_messages: SequenceNotStr[str] | Omit = omit,
        idle_timeout_seconds: int | Omit = omit,
        intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] | Omit = omit,
        memory_reliability: Literal["HIGH", "LOW"] | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        response_timing: Literal["RELAXED", "NORMAL", "QUICK"] | Omit = omit,
        secondary_language: Optional[Literal["EN"]] | Omit = omit,
        speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] | Omit = omit,
        speech_pace: Literal["SLOW", "NORMAL", "FAST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPersonaCreateResponse:
        """
        Creates a new persona for the authenticated project.

        Args:
          accent: Accent of the persona, defined using ISO 3166-1 alpha-2 country codes with
              optional variants

          gender: Gender of the persona

          language: Primary language ISO 639-1 code for the persona

          name: The name the agent will identify as during conversations

          background_noise: Background noise setting

          backstory_prompt: Background story and behavioral patterns for the persona

          base_emotion: Base emotional state of the persona

          confirmation_style: How the persona confirms information

          description: Human-readable description of the persona

          has_disfluencies: Whether the persona uses filler words like "um" and "uh"

          idle_message_max_spoken_count: Maximum number of idle messages the persona will send before giving up

          idle_message_reset_count_on_user_speech_enabled: Whether the idle message counter resets when the agent speaks

          idle_messages: Messages the persona will say when the agent goes silent during a call

          idle_timeout_seconds: Seconds of silence before the persona sends an idle message

          intent_clarity: How clearly the persona expresses their intentions

          memory_reliability: How reliable the persona's memory is

          properties: Additional custom properties about the persona

          response_timing: Controls how quickly the persona responds to pauses in conversation (QUICK,
              NORMAL, RELAXED)

          secondary_language: Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)

          speech_clarity: Speech clarity of the persona

          speech_pace: Speech pace of the persona

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/persona",
            body=await async_maybe_transform(
                {
                    "accent": accent,
                    "gender": gender,
                    "language": language,
                    "name": name,
                    "background_noise": background_noise,
                    "backstory_prompt": backstory_prompt,
                    "base_emotion": base_emotion,
                    "confirmation_style": confirmation_style,
                    "description": description,
                    "has_disfluencies": has_disfluencies,
                    "idle_message_max_spoken_count": idle_message_max_spoken_count,
                    "idle_message_reset_count_on_user_speech_enabled": idle_message_reset_count_on_user_speech_enabled,
                    "idle_messages": idle_messages,
                    "idle_timeout_seconds": idle_timeout_seconds,
                    "intent_clarity": intent_clarity,
                    "memory_reliability": memory_reliability,
                    "properties": properties,
                    "response_timing": response_timing,
                    "secondary_language": secondary_language,
                    "speech_clarity": speech_clarity,
                    "speech_pace": speech_pace,
                },
                simulation_persona_create_params.SimulationPersonaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationPersonaCreateResponse,
        )

    async def update(
        self,
        persona_id: str,
        *,
        accent: Literal[
            "US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT", "ID", "TH", "JP"
        ]
        | Omit = omit,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        backstory_prompt: Optional[str] | Omit = omit,
        base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"] | Omit = omit,
        confirmation_style: Literal["EXPLICIT", "VAGUE"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        gender: Literal["MALE", "FEMALE"] | Omit = omit,
        has_disfluencies: bool | Omit = omit,
        idle_message_max_spoken_count: int | Omit = omit,
        idle_message_reset_count_on_user_speech_enabled: bool | Omit = omit,
        idle_messages: SequenceNotStr[str] | Omit = omit,
        idle_timeout_seconds: int | Omit = omit,
        intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] | Omit = omit,
        language: Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT", "ID", "TH", "JA"] | Omit = omit,
        memory_reliability: Literal["HIGH", "LOW"] | Omit = omit,
        name: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        response_timing: Literal["RELAXED", "NORMAL", "QUICK"] | Omit = omit,
        secondary_language: Optional[Literal["EN"]] | Omit = omit,
        speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] | Omit = omit,
        speech_pace: Literal["SLOW", "NORMAL", "FAST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPersonaUpdateResponse:
        """
        Updates an existing persona by its ID.

        Args:
          accent: Accent of the persona, defined using ISO 3166-1 alpha-2 country codes with
              optional variants

          background_noise: Background noise setting

          backstory_prompt: Background story and behavioral patterns for the persona

          base_emotion: Base emotional state of the persona

          confirmation_style: How the persona confirms information

          description: Human-readable description of the persona

          gender: Gender of the persona

          has_disfluencies: Whether the persona uses filler words like "um" and "uh"

          idle_message_max_spoken_count: Maximum number of idle messages the persona will send before giving up

          idle_message_reset_count_on_user_speech_enabled: Whether the idle message counter resets when the agent speaks

          idle_messages: Messages the persona will say when the agent goes silent during a call

          idle_timeout_seconds: Seconds of silence before the persona sends an idle message

          intent_clarity: How clearly the persona expresses their intentions

          language: Primary language ISO 639-1 code for the persona

          memory_reliability: How reliable the persona's memory is

          name: The name the agent will identify as during conversations

          properties: Additional custom properties about the persona

          response_timing: Controls how quickly the persona responds to pauses in conversation (QUICK,
              NORMAL, RELAXED)

          secondary_language: Secondary language ISO 639-1 code for code-switching (e.g., Hinglish, Spanglish)

          speech_clarity: Speech clarity of the persona

          speech_pace: Speech pace of the persona

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not persona_id:
            raise ValueError(f"Expected a non-empty value for `persona_id` but received {persona_id!r}")
        return await self._put(
            f"/v1/persona/{persona_id}",
            body=await async_maybe_transform(
                {
                    "accent": accent,
                    "background_noise": background_noise,
                    "backstory_prompt": backstory_prompt,
                    "base_emotion": base_emotion,
                    "confirmation_style": confirmation_style,
                    "description": description,
                    "gender": gender,
                    "has_disfluencies": has_disfluencies,
                    "idle_message_max_spoken_count": idle_message_max_spoken_count,
                    "idle_message_reset_count_on_user_speech_enabled": idle_message_reset_count_on_user_speech_enabled,
                    "idle_messages": idle_messages,
                    "idle_timeout_seconds": idle_timeout_seconds,
                    "intent_clarity": intent_clarity,
                    "language": language,
                    "memory_reliability": memory_reliability,
                    "name": name,
                    "properties": properties,
                    "response_timing": response_timing,
                    "secondary_language": secondary_language,
                    "speech_clarity": speech_clarity,
                    "speech_pace": speech_pace,
                },
                simulation_persona_update_params.SimulationPersonaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationPersonaUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        search_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPersonaListResponse:
        """
        Returns a paginated list of personas for the authenticated project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/persona",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "search_text": search_text,
                    },
                    simulation_persona_list_params.SimulationPersonaListParams,
                ),
            ),
            cast_to=SimulationPersonaListResponse,
        )

    async def get_by_id(
        self,
        persona_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationPersonaGetByIDResponse:
        """
        Returns a specific persona by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not persona_id:
            raise ValueError(f"Expected a non-empty value for `persona_id` but received {persona_id!r}")
        return await self._get(
            f"/v1/persona/{persona_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationPersonaGetByIDResponse,
        )


class SimulationPersonaResourceWithRawResponse:
    def __init__(self, simulation_persona: SimulationPersonaResource) -> None:
        self._simulation_persona = simulation_persona

        self.create = to_raw_response_wrapper(
            simulation_persona.create,
        )
        self.update = to_raw_response_wrapper(
            simulation_persona.update,
        )
        self.list = to_raw_response_wrapper(
            simulation_persona.list,
        )
        self.get_by_id = to_raw_response_wrapper(
            simulation_persona.get_by_id,
        )


class AsyncSimulationPersonaResourceWithRawResponse:
    def __init__(self, simulation_persona: AsyncSimulationPersonaResource) -> None:
        self._simulation_persona = simulation_persona

        self.create = async_to_raw_response_wrapper(
            simulation_persona.create,
        )
        self.update = async_to_raw_response_wrapper(
            simulation_persona.update,
        )
        self.list = async_to_raw_response_wrapper(
            simulation_persona.list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            simulation_persona.get_by_id,
        )


class SimulationPersonaResourceWithStreamingResponse:
    def __init__(self, simulation_persona: SimulationPersonaResource) -> None:
        self._simulation_persona = simulation_persona

        self.create = to_streamed_response_wrapper(
            simulation_persona.create,
        )
        self.update = to_streamed_response_wrapper(
            simulation_persona.update,
        )
        self.list = to_streamed_response_wrapper(
            simulation_persona.list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            simulation_persona.get_by_id,
        )


class AsyncSimulationPersonaResourceWithStreamingResponse:
    def __init__(self, simulation_persona: AsyncSimulationPersonaResource) -> None:
        self._simulation_persona = simulation_persona

        self.create = async_to_streamed_response_wrapper(
            simulation_persona.create,
        )
        self.update = async_to_streamed_response_wrapper(
            simulation_persona.update,
        )
        self.list = async_to_streamed_response_wrapper(
            simulation_persona.list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            simulation_persona.get_by_id,
        )
