# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import persona_create_params, persona_update_params, persona_find_all_params
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
from ..types.persona_create_response import PersonaCreateResponse
from ..types.persona_update_response import PersonaUpdateResponse
from ..types.persona_find_all_response import PersonaFindAllResponse
from ..types.persona_get_by_id_response import PersonaGetByIDResponse

__all__ = ["PersonaResource", "AsyncPersonaResource"]


class PersonaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PersonaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return PersonaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return PersonaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        accent: Literal["US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT"],
        gender: Literal["MALE", "FEMALE", "NEUTRAL"],
        language: Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT"],
        name: str,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        backstory_prompt: Optional[str] | Omit = omit,
        base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"] | Omit = omit,
        confirmation_style: Literal["EXPLICIT", "VAGUE"] | Omit = omit,
        has_disfluencies: bool | Omit = omit,
        intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] | Omit = omit,
        memory_reliability: Literal["HIGH", "LOW"] | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        secondary_language: Optional[Literal["EN"]] | Omit = omit,
        speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] | Omit = omit,
        speech_pace: Literal["SLOW", "NORMAL", "FAST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonaCreateResponse:
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

          has_disfluencies: Whether the persona uses filler words like "um" and "uh"

          intent_clarity: How clearly the persona expresses their intentions

          memory_reliability: How reliable the persona's memory is

          properties: Additional custom properties about the persona

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
                    "has_disfluencies": has_disfluencies,
                    "intent_clarity": intent_clarity,
                    "memory_reliability": memory_reliability,
                    "properties": properties,
                    "secondary_language": secondary_language,
                    "speech_clarity": speech_clarity,
                    "speech_pace": speech_pace,
                },
                persona_create_params.PersonaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonaCreateResponse,
        )

    def update(
        self,
        persona_id: str,
        *,
        accent: Literal["US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT"] | Omit = omit,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        backstory_prompt: Optional[str] | Omit = omit,
        base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"] | Omit = omit,
        confirmation_style: Literal["EXPLICIT", "VAGUE"] | Omit = omit,
        gender: Literal["MALE", "FEMALE", "NEUTRAL"] | Omit = omit,
        has_disfluencies: bool | Omit = omit,
        intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] | Omit = omit,
        language: Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT"] | Omit = omit,
        memory_reliability: Literal["HIGH", "LOW"] | Omit = omit,
        name: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        secondary_language: Optional[Literal["EN"]] | Omit = omit,
        speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] | Omit = omit,
        speech_pace: Literal["SLOW", "NORMAL", "FAST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonaUpdateResponse:
        """
        Updates an existing persona by its ID.

        Args:
          accent: Accent of the persona, defined using ISO 3166-1 alpha-2 country codes with
              optional variants

          background_noise: Background noise setting

          backstory_prompt: Background story and behavioral patterns for the persona

          base_emotion: Base emotional state of the persona

          confirmation_style: How the persona confirms information

          gender: Gender of the persona

          has_disfluencies: Whether the persona uses filler words like "um" and "uh"

          intent_clarity: How clearly the persona expresses their intentions

          language: Primary language ISO 639-1 code for the persona

          memory_reliability: How reliable the persona's memory is

          name: The name the agent will identify as during conversations

          properties: Additional custom properties about the persona

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
                    "gender": gender,
                    "has_disfluencies": has_disfluencies,
                    "intent_clarity": intent_clarity,
                    "language": language,
                    "memory_reliability": memory_reliability,
                    "name": name,
                    "properties": properties,
                    "secondary_language": secondary_language,
                    "speech_clarity": speech_clarity,
                    "speech_pace": speech_pace,
                },
                persona_update_params.PersonaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonaUpdateResponse,
        )

    def find_all(
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
    ) -> PersonaFindAllResponse:
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
                    persona_find_all_params.PersonaFindAllParams,
                ),
            ),
            cast_to=PersonaFindAllResponse,
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
    ) -> PersonaGetByIDResponse:
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
            cast_to=PersonaGetByIDResponse,
        )


class AsyncPersonaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPersonaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPersonaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncPersonaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        accent: Literal["US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT"],
        gender: Literal["MALE", "FEMALE", "NEUTRAL"],
        language: Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT"],
        name: str,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        backstory_prompt: Optional[str] | Omit = omit,
        base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"] | Omit = omit,
        confirmation_style: Literal["EXPLICIT", "VAGUE"] | Omit = omit,
        has_disfluencies: bool | Omit = omit,
        intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] | Omit = omit,
        memory_reliability: Literal["HIGH", "LOW"] | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        secondary_language: Optional[Literal["EN"]] | Omit = omit,
        speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] | Omit = omit,
        speech_pace: Literal["SLOW", "NORMAL", "FAST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonaCreateResponse:
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

          has_disfluencies: Whether the persona uses filler words like "um" and "uh"

          intent_clarity: How clearly the persona expresses their intentions

          memory_reliability: How reliable the persona's memory is

          properties: Additional custom properties about the persona

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
                    "has_disfluencies": has_disfluencies,
                    "intent_clarity": intent_clarity,
                    "memory_reliability": memory_reliability,
                    "properties": properties,
                    "secondary_language": secondary_language,
                    "speech_clarity": speech_clarity,
                    "speech_pace": speech_pace,
                },
                persona_create_params.PersonaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonaCreateResponse,
        )

    async def update(
        self,
        persona_id: str,
        *,
        accent: Literal["US", "US_X_SOUTH", "GB", "ES", "DE", "IN", "FR", "NL", "SA", "GR", "AU", "IT"] | Omit = omit,
        background_noise: Literal[
            "NONE", "AIRPORT", "CHILDREN_PLAYING", "CITY", "COFFEE_SHOP", "DRIVING", "OFFICE", "THUNDERSTORM"
        ]
        | Omit = omit,
        backstory_prompt: Optional[str] | Omit = omit,
        base_emotion: Literal["NEUTRAL", "CHEERFUL", "CONFUSED", "FRUSTRATED", "SKEPTICAL", "RUSHED"] | Omit = omit,
        confirmation_style: Literal["EXPLICIT", "VAGUE"] | Omit = omit,
        gender: Literal["MALE", "FEMALE", "NEUTRAL"] | Omit = omit,
        has_disfluencies: bool | Omit = omit,
        intent_clarity: Literal["CLEAR", "INDIRECT", "VAGUE"] | Omit = omit,
        language: Literal["EN", "ES", "DE", "HI", "FR", "NL", "AR", "EL", "IT"] | Omit = omit,
        memory_reliability: Literal["HIGH", "LOW"] | Omit = omit,
        name: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        secondary_language: Optional[Literal["EN"]] | Omit = omit,
        speech_clarity: Literal["CLEAR", "VAGUE", "RAMBLING"] | Omit = omit,
        speech_pace: Literal["SLOW", "NORMAL", "FAST"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonaUpdateResponse:
        """
        Updates an existing persona by its ID.

        Args:
          accent: Accent of the persona, defined using ISO 3166-1 alpha-2 country codes with
              optional variants

          background_noise: Background noise setting

          backstory_prompt: Background story and behavioral patterns for the persona

          base_emotion: Base emotional state of the persona

          confirmation_style: How the persona confirms information

          gender: Gender of the persona

          has_disfluencies: Whether the persona uses filler words like "um" and "uh"

          intent_clarity: How clearly the persona expresses their intentions

          language: Primary language ISO 639-1 code for the persona

          memory_reliability: How reliable the persona's memory is

          name: The name the agent will identify as during conversations

          properties: Additional custom properties about the persona

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
                    "gender": gender,
                    "has_disfluencies": has_disfluencies,
                    "intent_clarity": intent_clarity,
                    "language": language,
                    "memory_reliability": memory_reliability,
                    "name": name,
                    "properties": properties,
                    "secondary_language": secondary_language,
                    "speech_clarity": speech_clarity,
                    "speech_pace": speech_pace,
                },
                persona_update_params.PersonaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonaUpdateResponse,
        )

    async def find_all(
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
    ) -> PersonaFindAllResponse:
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
                    persona_find_all_params.PersonaFindAllParams,
                ),
            ),
            cast_to=PersonaFindAllResponse,
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
    ) -> PersonaGetByIDResponse:
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
            cast_to=PersonaGetByIDResponse,
        )


class PersonaResourceWithRawResponse:
    def __init__(self, persona: PersonaResource) -> None:
        self._persona = persona

        self.create = to_raw_response_wrapper(
            persona.create,
        )
        self.update = to_raw_response_wrapper(
            persona.update,
        )
        self.find_all = to_raw_response_wrapper(
            persona.find_all,
        )
        self.get_by_id = to_raw_response_wrapper(
            persona.get_by_id,
        )


class AsyncPersonaResourceWithRawResponse:
    def __init__(self, persona: AsyncPersonaResource) -> None:
        self._persona = persona

        self.create = async_to_raw_response_wrapper(
            persona.create,
        )
        self.update = async_to_raw_response_wrapper(
            persona.update,
        )
        self.find_all = async_to_raw_response_wrapper(
            persona.find_all,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            persona.get_by_id,
        )


class PersonaResourceWithStreamingResponse:
    def __init__(self, persona: PersonaResource) -> None:
        self._persona = persona

        self.create = to_streamed_response_wrapper(
            persona.create,
        )
        self.update = to_streamed_response_wrapper(
            persona.update,
        )
        self.find_all = to_streamed_response_wrapper(
            persona.find_all,
        )
        self.get_by_id = to_streamed_response_wrapper(
            persona.get_by_id,
        )


class AsyncPersonaResourceWithStreamingResponse:
    def __init__(self, persona: AsyncPersonaResource) -> None:
        self._persona = persona

        self.create = async_to_streamed_response_wrapper(
            persona.create,
        )
        self.update = async_to_streamed_response_wrapper(
            persona.update,
        )
        self.find_all = async_to_streamed_response_wrapper(
            persona.find_all,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            persona.get_by_id,
        )
