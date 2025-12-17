# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import RoarkError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import call, health, metric, persona, evaluation, simulation, integrations
    from .resources.call import CallResource, AsyncCallResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.metric import MetricResource, AsyncMetricResource
    from .resources.persona import PersonaResource, AsyncPersonaResource
    from .resources.evaluation import EvaluationResource, AsyncEvaluationResource
    from .resources.simulation import SimulationResource, AsyncSimulationResource
    from .resources.integrations import IntegrationsResource, AsyncIntegrationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Roark", "AsyncRoark", "Client", "AsyncClient"]


class Roark(SyncAPIClient):
    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Roark client instance.

        This automatically infers the `bearer_token` argument from the `ROARK_API_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("ROARK_API_BEARER_TOKEN")
        if bearer_token is None:
            raise RoarkError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the ROARK_API_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("ROARK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.roark.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def evaluation(self) -> EvaluationResource:
        from .resources.evaluation import EvaluationResource

        return EvaluationResource(self)

    @cached_property
    def call(self) -> CallResource:
        from .resources.call import CallResource

        return CallResource(self)

    @cached_property
    def metric(self) -> MetricResource:
        from .resources.metric import MetricResource

        return MetricResource(self)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        from .resources.integrations import IntegrationsResource

        return IntegrationsResource(self)

    @cached_property
    def simulation(self) -> SimulationResource:
        from .resources.simulation import SimulationResource

        return SimulationResource(self)

    @cached_property
    def persona(self) -> PersonaResource:
        from .resources.persona import PersonaResource

        return PersonaResource(self)

    @cached_property
    def with_raw_response(self) -> RoarkWithRawResponse:
        return RoarkWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoarkWithStreamedResponse:
        return RoarkWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncRoark(AsyncAPIClient):
    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncRoark client instance.

        This automatically infers the `bearer_token` argument from the `ROARK_API_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("ROARK_API_BEARER_TOKEN")
        if bearer_token is None:
            raise RoarkError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the ROARK_API_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("ROARK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.roark.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def evaluation(self) -> AsyncEvaluationResource:
        from .resources.evaluation import AsyncEvaluationResource

        return AsyncEvaluationResource(self)

    @cached_property
    def call(self) -> AsyncCallResource:
        from .resources.call import AsyncCallResource

        return AsyncCallResource(self)

    @cached_property
    def metric(self) -> AsyncMetricResource:
        from .resources.metric import AsyncMetricResource

        return AsyncMetricResource(self)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        from .resources.integrations import AsyncIntegrationsResource

        return AsyncIntegrationsResource(self)

    @cached_property
    def simulation(self) -> AsyncSimulationResource:
        from .resources.simulation import AsyncSimulationResource

        return AsyncSimulationResource(self)

    @cached_property
    def persona(self) -> AsyncPersonaResource:
        from .resources.persona import AsyncPersonaResource

        return AsyncPersonaResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncRoarkWithRawResponse:
        return AsyncRoarkWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoarkWithStreamedResponse:
        return AsyncRoarkWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class RoarkWithRawResponse:
    _client: Roark

    def __init__(self, client: Roark) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def evaluation(self) -> evaluation.EvaluationResourceWithRawResponse:
        from .resources.evaluation import EvaluationResourceWithRawResponse

        return EvaluationResourceWithRawResponse(self._client.evaluation)

    @cached_property
    def call(self) -> call.CallResourceWithRawResponse:
        from .resources.call import CallResourceWithRawResponse

        return CallResourceWithRawResponse(self._client.call)

    @cached_property
    def metric(self) -> metric.MetricResourceWithRawResponse:
        from .resources.metric import MetricResourceWithRawResponse

        return MetricResourceWithRawResponse(self._client.metric)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithRawResponse:
        from .resources.integrations import IntegrationsResourceWithRawResponse

        return IntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def simulation(self) -> simulation.SimulationResourceWithRawResponse:
        from .resources.simulation import SimulationResourceWithRawResponse

        return SimulationResourceWithRawResponse(self._client.simulation)

    @cached_property
    def persona(self) -> persona.PersonaResourceWithRawResponse:
        from .resources.persona import PersonaResourceWithRawResponse

        return PersonaResourceWithRawResponse(self._client.persona)


class AsyncRoarkWithRawResponse:
    _client: AsyncRoark

    def __init__(self, client: AsyncRoark) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def evaluation(self) -> evaluation.AsyncEvaluationResourceWithRawResponse:
        from .resources.evaluation import AsyncEvaluationResourceWithRawResponse

        return AsyncEvaluationResourceWithRawResponse(self._client.evaluation)

    @cached_property
    def call(self) -> call.AsyncCallResourceWithRawResponse:
        from .resources.call import AsyncCallResourceWithRawResponse

        return AsyncCallResourceWithRawResponse(self._client.call)

    @cached_property
    def metric(self) -> metric.AsyncMetricResourceWithRawResponse:
        from .resources.metric import AsyncMetricResourceWithRawResponse

        return AsyncMetricResourceWithRawResponse(self._client.metric)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithRawResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithRawResponse

        return AsyncIntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def simulation(self) -> simulation.AsyncSimulationResourceWithRawResponse:
        from .resources.simulation import AsyncSimulationResourceWithRawResponse

        return AsyncSimulationResourceWithRawResponse(self._client.simulation)

    @cached_property
    def persona(self) -> persona.AsyncPersonaResourceWithRawResponse:
        from .resources.persona import AsyncPersonaResourceWithRawResponse

        return AsyncPersonaResourceWithRawResponse(self._client.persona)


class RoarkWithStreamedResponse:
    _client: Roark

    def __init__(self, client: Roark) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def evaluation(self) -> evaluation.EvaluationResourceWithStreamingResponse:
        from .resources.evaluation import EvaluationResourceWithStreamingResponse

        return EvaluationResourceWithStreamingResponse(self._client.evaluation)

    @cached_property
    def call(self) -> call.CallResourceWithStreamingResponse:
        from .resources.call import CallResourceWithStreamingResponse

        return CallResourceWithStreamingResponse(self._client.call)

    @cached_property
    def metric(self) -> metric.MetricResourceWithStreamingResponse:
        from .resources.metric import MetricResourceWithStreamingResponse

        return MetricResourceWithStreamingResponse(self._client.metric)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithStreamingResponse:
        from .resources.integrations import IntegrationsResourceWithStreamingResponse

        return IntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def simulation(self) -> simulation.SimulationResourceWithStreamingResponse:
        from .resources.simulation import SimulationResourceWithStreamingResponse

        return SimulationResourceWithStreamingResponse(self._client.simulation)

    @cached_property
    def persona(self) -> persona.PersonaResourceWithStreamingResponse:
        from .resources.persona import PersonaResourceWithStreamingResponse

        return PersonaResourceWithStreamingResponse(self._client.persona)


class AsyncRoarkWithStreamedResponse:
    _client: AsyncRoark

    def __init__(self, client: AsyncRoark) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def evaluation(self) -> evaluation.AsyncEvaluationResourceWithStreamingResponse:
        from .resources.evaluation import AsyncEvaluationResourceWithStreamingResponse

        return AsyncEvaluationResourceWithStreamingResponse(self._client.evaluation)

    @cached_property
    def call(self) -> call.AsyncCallResourceWithStreamingResponse:
        from .resources.call import AsyncCallResourceWithStreamingResponse

        return AsyncCallResourceWithStreamingResponse(self._client.call)

    @cached_property
    def metric(self) -> metric.AsyncMetricResourceWithStreamingResponse:
        from .resources.metric import AsyncMetricResourceWithStreamingResponse

        return AsyncMetricResourceWithStreamingResponse(self._client.metric)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithStreamingResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithStreamingResponse

        return AsyncIntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def simulation(self) -> simulation.AsyncSimulationResourceWithStreamingResponse:
        from .resources.simulation import AsyncSimulationResourceWithStreamingResponse

        return AsyncSimulationResourceWithStreamingResponse(self._client.simulation)

    @cached_property
    def persona(self) -> persona.AsyncPersonaResourceWithStreamingResponse:
        from .resources.persona import AsyncPersonaResourceWithStreamingResponse

        return AsyncPersonaResourceWithStreamingResponse(self._client.persona)


Client = Roark

AsyncClient = AsyncRoark
