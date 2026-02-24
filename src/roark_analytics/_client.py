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
    from .resources import (
        call,
        agent,
        health,
        metric,
        webhook,
        metric_policy,
        agent_endpoint,
        simulation_job,
        simulation_persona,
        simulation_run_plan,
        simulation_scenario,
        metric_collection_job,
        http_request_definition,
        simulation_run_plan_job,
    )
    from .resources.call import CallResource, AsyncCallResource
    from .resources.agent import AgentResource, AsyncAgentResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.metric import MetricResource, AsyncMetricResource
    from .resources.webhook import WebhookResource, AsyncWebhookResource
    from .resources.metric_policy import MetricPolicyResource, AsyncMetricPolicyResource
    from .resources.agent_endpoint import AgentEndpointResource, AsyncAgentEndpointResource
    from .resources.simulation_job import SimulationJobResource, AsyncSimulationJobResource
    from .resources.simulation_persona import SimulationPersonaResource, AsyncSimulationPersonaResource
    from .resources.simulation_run_plan import SimulationRunPlanResource, AsyncSimulationRunPlanResource
    from .resources.simulation_scenario import SimulationScenarioResource, AsyncSimulationScenarioResource
    from .resources.metric_collection_job import MetricCollectionJobResource, AsyncMetricCollectionJobResource
    from .resources.http_request_definition import HTTPRequestDefinitionResource, AsyncHTTPRequestDefinitionResource
    from .resources.simulation_run_plan_job import SimulationRunPlanJobResource, AsyncSimulationRunPlanJobResource

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
    def call(self) -> CallResource:
        from .resources.call import CallResource

        return CallResource(self)

    @cached_property
    def metric(self) -> MetricResource:
        from .resources.metric import MetricResource

        return MetricResource(self)

    @cached_property
    def metric_policy(self) -> MetricPolicyResource:
        from .resources.metric_policy import MetricPolicyResource

        return MetricPolicyResource(self)

    @cached_property
    def metric_collection_job(self) -> MetricCollectionJobResource:
        from .resources.metric_collection_job import MetricCollectionJobResource

        return MetricCollectionJobResource(self)

    @cached_property
    def simulation_job(self) -> SimulationJobResource:
        from .resources.simulation_job import SimulationJobResource

        return SimulationJobResource(self)

    @cached_property
    def simulation_run_plan(self) -> SimulationRunPlanResource:
        from .resources.simulation_run_plan import SimulationRunPlanResource

        return SimulationRunPlanResource(self)

    @cached_property
    def simulation_run_plan_job(self) -> SimulationRunPlanJobResource:
        from .resources.simulation_run_plan_job import SimulationRunPlanJobResource

        return SimulationRunPlanJobResource(self)

    @cached_property
    def simulation_scenario(self) -> SimulationScenarioResource:
        from .resources.simulation_scenario import SimulationScenarioResource

        return SimulationScenarioResource(self)

    @cached_property
    def simulation_persona(self) -> SimulationPersonaResource:
        from .resources.simulation_persona import SimulationPersonaResource

        return SimulationPersonaResource(self)

    @cached_property
    def agent(self) -> AgentResource:
        from .resources.agent import AgentResource

        return AgentResource(self)

    @cached_property
    def agent_endpoint(self) -> AgentEndpointResource:
        from .resources.agent_endpoint import AgentEndpointResource

        return AgentEndpointResource(self)

    @cached_property
    def http_request_definition(self) -> HTTPRequestDefinitionResource:
        from .resources.http_request_definition import HTTPRequestDefinitionResource

        return HTTPRequestDefinitionResource(self)

    @cached_property
    def webhook(self) -> WebhookResource:
        from .resources.webhook import WebhookResource

        return WebhookResource(self)

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
    def call(self) -> AsyncCallResource:
        from .resources.call import AsyncCallResource

        return AsyncCallResource(self)

    @cached_property
    def metric(self) -> AsyncMetricResource:
        from .resources.metric import AsyncMetricResource

        return AsyncMetricResource(self)

    @cached_property
    def metric_policy(self) -> AsyncMetricPolicyResource:
        from .resources.metric_policy import AsyncMetricPolicyResource

        return AsyncMetricPolicyResource(self)

    @cached_property
    def metric_collection_job(self) -> AsyncMetricCollectionJobResource:
        from .resources.metric_collection_job import AsyncMetricCollectionJobResource

        return AsyncMetricCollectionJobResource(self)

    @cached_property
    def simulation_job(self) -> AsyncSimulationJobResource:
        from .resources.simulation_job import AsyncSimulationJobResource

        return AsyncSimulationJobResource(self)

    @cached_property
    def simulation_run_plan(self) -> AsyncSimulationRunPlanResource:
        from .resources.simulation_run_plan import AsyncSimulationRunPlanResource

        return AsyncSimulationRunPlanResource(self)

    @cached_property
    def simulation_run_plan_job(self) -> AsyncSimulationRunPlanJobResource:
        from .resources.simulation_run_plan_job import AsyncSimulationRunPlanJobResource

        return AsyncSimulationRunPlanJobResource(self)

    @cached_property
    def simulation_scenario(self) -> AsyncSimulationScenarioResource:
        from .resources.simulation_scenario import AsyncSimulationScenarioResource

        return AsyncSimulationScenarioResource(self)

    @cached_property
    def simulation_persona(self) -> AsyncSimulationPersonaResource:
        from .resources.simulation_persona import AsyncSimulationPersonaResource

        return AsyncSimulationPersonaResource(self)

    @cached_property
    def agent(self) -> AsyncAgentResource:
        from .resources.agent import AsyncAgentResource

        return AsyncAgentResource(self)

    @cached_property
    def agent_endpoint(self) -> AsyncAgentEndpointResource:
        from .resources.agent_endpoint import AsyncAgentEndpointResource

        return AsyncAgentEndpointResource(self)

    @cached_property
    def http_request_definition(self) -> AsyncHTTPRequestDefinitionResource:
        from .resources.http_request_definition import AsyncHTTPRequestDefinitionResource

        return AsyncHTTPRequestDefinitionResource(self)

    @cached_property
    def webhook(self) -> AsyncWebhookResource:
        from .resources.webhook import AsyncWebhookResource

        return AsyncWebhookResource(self)

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
    def call(self) -> call.CallResourceWithRawResponse:
        from .resources.call import CallResourceWithRawResponse

        return CallResourceWithRawResponse(self._client.call)

    @cached_property
    def metric(self) -> metric.MetricResourceWithRawResponse:
        from .resources.metric import MetricResourceWithRawResponse

        return MetricResourceWithRawResponse(self._client.metric)

    @cached_property
    def metric_policy(self) -> metric_policy.MetricPolicyResourceWithRawResponse:
        from .resources.metric_policy import MetricPolicyResourceWithRawResponse

        return MetricPolicyResourceWithRawResponse(self._client.metric_policy)

    @cached_property
    def metric_collection_job(self) -> metric_collection_job.MetricCollectionJobResourceWithRawResponse:
        from .resources.metric_collection_job import MetricCollectionJobResourceWithRawResponse

        return MetricCollectionJobResourceWithRawResponse(self._client.metric_collection_job)

    @cached_property
    def simulation_job(self) -> simulation_job.SimulationJobResourceWithRawResponse:
        from .resources.simulation_job import SimulationJobResourceWithRawResponse

        return SimulationJobResourceWithRawResponse(self._client.simulation_job)

    @cached_property
    def simulation_run_plan(self) -> simulation_run_plan.SimulationRunPlanResourceWithRawResponse:
        from .resources.simulation_run_plan import SimulationRunPlanResourceWithRawResponse

        return SimulationRunPlanResourceWithRawResponse(self._client.simulation_run_plan)

    @cached_property
    def simulation_run_plan_job(self) -> simulation_run_plan_job.SimulationRunPlanJobResourceWithRawResponse:
        from .resources.simulation_run_plan_job import SimulationRunPlanJobResourceWithRawResponse

        return SimulationRunPlanJobResourceWithRawResponse(self._client.simulation_run_plan_job)

    @cached_property
    def simulation_scenario(self) -> simulation_scenario.SimulationScenarioResourceWithRawResponse:
        from .resources.simulation_scenario import SimulationScenarioResourceWithRawResponse

        return SimulationScenarioResourceWithRawResponse(self._client.simulation_scenario)

    @cached_property
    def simulation_persona(self) -> simulation_persona.SimulationPersonaResourceWithRawResponse:
        from .resources.simulation_persona import SimulationPersonaResourceWithRawResponse

        return SimulationPersonaResourceWithRawResponse(self._client.simulation_persona)

    @cached_property
    def agent(self) -> agent.AgentResourceWithRawResponse:
        from .resources.agent import AgentResourceWithRawResponse

        return AgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def agent_endpoint(self) -> agent_endpoint.AgentEndpointResourceWithRawResponse:
        from .resources.agent_endpoint import AgentEndpointResourceWithRawResponse

        return AgentEndpointResourceWithRawResponse(self._client.agent_endpoint)

    @cached_property
    def http_request_definition(self) -> http_request_definition.HTTPRequestDefinitionResourceWithRawResponse:
        from .resources.http_request_definition import HTTPRequestDefinitionResourceWithRawResponse

        return HTTPRequestDefinitionResourceWithRawResponse(self._client.http_request_definition)

    @cached_property
    def webhook(self) -> webhook.WebhookResourceWithRawResponse:
        from .resources.webhook import WebhookResourceWithRawResponse

        return WebhookResourceWithRawResponse(self._client.webhook)


class AsyncRoarkWithRawResponse:
    _client: AsyncRoark

    def __init__(self, client: AsyncRoark) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def call(self) -> call.AsyncCallResourceWithRawResponse:
        from .resources.call import AsyncCallResourceWithRawResponse

        return AsyncCallResourceWithRawResponse(self._client.call)

    @cached_property
    def metric(self) -> metric.AsyncMetricResourceWithRawResponse:
        from .resources.metric import AsyncMetricResourceWithRawResponse

        return AsyncMetricResourceWithRawResponse(self._client.metric)

    @cached_property
    def metric_policy(self) -> metric_policy.AsyncMetricPolicyResourceWithRawResponse:
        from .resources.metric_policy import AsyncMetricPolicyResourceWithRawResponse

        return AsyncMetricPolicyResourceWithRawResponse(self._client.metric_policy)

    @cached_property
    def metric_collection_job(self) -> metric_collection_job.AsyncMetricCollectionJobResourceWithRawResponse:
        from .resources.metric_collection_job import AsyncMetricCollectionJobResourceWithRawResponse

        return AsyncMetricCollectionJobResourceWithRawResponse(self._client.metric_collection_job)

    @cached_property
    def simulation_job(self) -> simulation_job.AsyncSimulationJobResourceWithRawResponse:
        from .resources.simulation_job import AsyncSimulationJobResourceWithRawResponse

        return AsyncSimulationJobResourceWithRawResponse(self._client.simulation_job)

    @cached_property
    def simulation_run_plan(self) -> simulation_run_plan.AsyncSimulationRunPlanResourceWithRawResponse:
        from .resources.simulation_run_plan import AsyncSimulationRunPlanResourceWithRawResponse

        return AsyncSimulationRunPlanResourceWithRawResponse(self._client.simulation_run_plan)

    @cached_property
    def simulation_run_plan_job(self) -> simulation_run_plan_job.AsyncSimulationRunPlanJobResourceWithRawResponse:
        from .resources.simulation_run_plan_job import AsyncSimulationRunPlanJobResourceWithRawResponse

        return AsyncSimulationRunPlanJobResourceWithRawResponse(self._client.simulation_run_plan_job)

    @cached_property
    def simulation_scenario(self) -> simulation_scenario.AsyncSimulationScenarioResourceWithRawResponse:
        from .resources.simulation_scenario import AsyncSimulationScenarioResourceWithRawResponse

        return AsyncSimulationScenarioResourceWithRawResponse(self._client.simulation_scenario)

    @cached_property
    def simulation_persona(self) -> simulation_persona.AsyncSimulationPersonaResourceWithRawResponse:
        from .resources.simulation_persona import AsyncSimulationPersonaResourceWithRawResponse

        return AsyncSimulationPersonaResourceWithRawResponse(self._client.simulation_persona)

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithRawResponse:
        from .resources.agent import AsyncAgentResourceWithRawResponse

        return AsyncAgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def agent_endpoint(self) -> agent_endpoint.AsyncAgentEndpointResourceWithRawResponse:
        from .resources.agent_endpoint import AsyncAgentEndpointResourceWithRawResponse

        return AsyncAgentEndpointResourceWithRawResponse(self._client.agent_endpoint)

    @cached_property
    def http_request_definition(self) -> http_request_definition.AsyncHTTPRequestDefinitionResourceWithRawResponse:
        from .resources.http_request_definition import AsyncHTTPRequestDefinitionResourceWithRawResponse

        return AsyncHTTPRequestDefinitionResourceWithRawResponse(self._client.http_request_definition)

    @cached_property
    def webhook(self) -> webhook.AsyncWebhookResourceWithRawResponse:
        from .resources.webhook import AsyncWebhookResourceWithRawResponse

        return AsyncWebhookResourceWithRawResponse(self._client.webhook)


class RoarkWithStreamedResponse:
    _client: Roark

    def __init__(self, client: Roark) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def call(self) -> call.CallResourceWithStreamingResponse:
        from .resources.call import CallResourceWithStreamingResponse

        return CallResourceWithStreamingResponse(self._client.call)

    @cached_property
    def metric(self) -> metric.MetricResourceWithStreamingResponse:
        from .resources.metric import MetricResourceWithStreamingResponse

        return MetricResourceWithStreamingResponse(self._client.metric)

    @cached_property
    def metric_policy(self) -> metric_policy.MetricPolicyResourceWithStreamingResponse:
        from .resources.metric_policy import MetricPolicyResourceWithStreamingResponse

        return MetricPolicyResourceWithStreamingResponse(self._client.metric_policy)

    @cached_property
    def metric_collection_job(self) -> metric_collection_job.MetricCollectionJobResourceWithStreamingResponse:
        from .resources.metric_collection_job import MetricCollectionJobResourceWithStreamingResponse

        return MetricCollectionJobResourceWithStreamingResponse(self._client.metric_collection_job)

    @cached_property
    def simulation_job(self) -> simulation_job.SimulationJobResourceWithStreamingResponse:
        from .resources.simulation_job import SimulationJobResourceWithStreamingResponse

        return SimulationJobResourceWithStreamingResponse(self._client.simulation_job)

    @cached_property
    def simulation_run_plan(self) -> simulation_run_plan.SimulationRunPlanResourceWithStreamingResponse:
        from .resources.simulation_run_plan import SimulationRunPlanResourceWithStreamingResponse

        return SimulationRunPlanResourceWithStreamingResponse(self._client.simulation_run_plan)

    @cached_property
    def simulation_run_plan_job(self) -> simulation_run_plan_job.SimulationRunPlanJobResourceWithStreamingResponse:
        from .resources.simulation_run_plan_job import SimulationRunPlanJobResourceWithStreamingResponse

        return SimulationRunPlanJobResourceWithStreamingResponse(self._client.simulation_run_plan_job)

    @cached_property
    def simulation_scenario(self) -> simulation_scenario.SimulationScenarioResourceWithStreamingResponse:
        from .resources.simulation_scenario import SimulationScenarioResourceWithStreamingResponse

        return SimulationScenarioResourceWithStreamingResponse(self._client.simulation_scenario)

    @cached_property
    def simulation_persona(self) -> simulation_persona.SimulationPersonaResourceWithStreamingResponse:
        from .resources.simulation_persona import SimulationPersonaResourceWithStreamingResponse

        return SimulationPersonaResourceWithStreamingResponse(self._client.simulation_persona)

    @cached_property
    def agent(self) -> agent.AgentResourceWithStreamingResponse:
        from .resources.agent import AgentResourceWithStreamingResponse

        return AgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def agent_endpoint(self) -> agent_endpoint.AgentEndpointResourceWithStreamingResponse:
        from .resources.agent_endpoint import AgentEndpointResourceWithStreamingResponse

        return AgentEndpointResourceWithStreamingResponse(self._client.agent_endpoint)

    @cached_property
    def http_request_definition(self) -> http_request_definition.HTTPRequestDefinitionResourceWithStreamingResponse:
        from .resources.http_request_definition import HTTPRequestDefinitionResourceWithStreamingResponse

        return HTTPRequestDefinitionResourceWithStreamingResponse(self._client.http_request_definition)

    @cached_property
    def webhook(self) -> webhook.WebhookResourceWithStreamingResponse:
        from .resources.webhook import WebhookResourceWithStreamingResponse

        return WebhookResourceWithStreamingResponse(self._client.webhook)


class AsyncRoarkWithStreamedResponse:
    _client: AsyncRoark

    def __init__(self, client: AsyncRoark) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def call(self) -> call.AsyncCallResourceWithStreamingResponse:
        from .resources.call import AsyncCallResourceWithStreamingResponse

        return AsyncCallResourceWithStreamingResponse(self._client.call)

    @cached_property
    def metric(self) -> metric.AsyncMetricResourceWithStreamingResponse:
        from .resources.metric import AsyncMetricResourceWithStreamingResponse

        return AsyncMetricResourceWithStreamingResponse(self._client.metric)

    @cached_property
    def metric_policy(self) -> metric_policy.AsyncMetricPolicyResourceWithStreamingResponse:
        from .resources.metric_policy import AsyncMetricPolicyResourceWithStreamingResponse

        return AsyncMetricPolicyResourceWithStreamingResponse(self._client.metric_policy)

    @cached_property
    def metric_collection_job(self) -> metric_collection_job.AsyncMetricCollectionJobResourceWithStreamingResponse:
        from .resources.metric_collection_job import AsyncMetricCollectionJobResourceWithStreamingResponse

        return AsyncMetricCollectionJobResourceWithStreamingResponse(self._client.metric_collection_job)

    @cached_property
    def simulation_job(self) -> simulation_job.AsyncSimulationJobResourceWithStreamingResponse:
        from .resources.simulation_job import AsyncSimulationJobResourceWithStreamingResponse

        return AsyncSimulationJobResourceWithStreamingResponse(self._client.simulation_job)

    @cached_property
    def simulation_run_plan(self) -> simulation_run_plan.AsyncSimulationRunPlanResourceWithStreamingResponse:
        from .resources.simulation_run_plan import AsyncSimulationRunPlanResourceWithStreamingResponse

        return AsyncSimulationRunPlanResourceWithStreamingResponse(self._client.simulation_run_plan)

    @cached_property
    def simulation_run_plan_job(self) -> simulation_run_plan_job.AsyncSimulationRunPlanJobResourceWithStreamingResponse:
        from .resources.simulation_run_plan_job import AsyncSimulationRunPlanJobResourceWithStreamingResponse

        return AsyncSimulationRunPlanJobResourceWithStreamingResponse(self._client.simulation_run_plan_job)

    @cached_property
    def simulation_scenario(self) -> simulation_scenario.AsyncSimulationScenarioResourceWithStreamingResponse:
        from .resources.simulation_scenario import AsyncSimulationScenarioResourceWithStreamingResponse

        return AsyncSimulationScenarioResourceWithStreamingResponse(self._client.simulation_scenario)

    @cached_property
    def simulation_persona(self) -> simulation_persona.AsyncSimulationPersonaResourceWithStreamingResponse:
        from .resources.simulation_persona import AsyncSimulationPersonaResourceWithStreamingResponse

        return AsyncSimulationPersonaResourceWithStreamingResponse(self._client.simulation_persona)

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithStreamingResponse:
        from .resources.agent import AsyncAgentResourceWithStreamingResponse

        return AsyncAgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def agent_endpoint(self) -> agent_endpoint.AsyncAgentEndpointResourceWithStreamingResponse:
        from .resources.agent_endpoint import AsyncAgentEndpointResourceWithStreamingResponse

        return AsyncAgentEndpointResourceWithStreamingResponse(self._client.agent_endpoint)

    @cached_property
    def http_request_definition(
        self,
    ) -> http_request_definition.AsyncHTTPRequestDefinitionResourceWithStreamingResponse:
        from .resources.http_request_definition import AsyncHTTPRequestDefinitionResourceWithStreamingResponse

        return AsyncHTTPRequestDefinitionResourceWithStreamingResponse(self._client.http_request_definition)

    @cached_property
    def webhook(self) -> webhook.AsyncWebhookResourceWithStreamingResponse:
        from .resources.webhook import AsyncWebhookResourceWithStreamingResponse

        return AsyncWebhookResourceWithStreamingResponse(self._client.webhook)


Client = Roark

AsyncClient = AsyncRoark
