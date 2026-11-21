# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import customer_flow_folder_create_params
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
from ..types.customer_flow_folder_list_response import CustomerFlowFolderListResponse
from ..types.customer_flow_folder_create_response import CustomerFlowFolderCreateResponse
from ..types.customer_flow_folder_delete_response import CustomerFlowFolderDeleteResponse

__all__ = ["CustomerFlowFolderResource", "AsyncCustomerFlowFolderResource"]


class CustomerFlowFolderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomerFlowFolderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return CustomerFlowFolderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerFlowFolderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return CustomerFlowFolderResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        color: Literal[
            "GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"
        ]
        | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowFolderCreateResponse:
        """Creates a folder to group customer flows.

        File a flow into it by sending its
        `folderId` when you create or update the flow. Names are unique within a
        project, ignoring case. Customer flows were previously called scenarios.

        Args:
          name: The folder name. Must be unique in the project.

          color: The color the folder is shown with in the app. Folders share the palette labels
              use. Defaults to GREY.

          description: What belongs in this folder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/customer-flow/folder",
            body=maybe_transform(
                {
                    "name": name,
                    "color": color,
                    "description": description,
                },
                customer_flow_folder_create_params.CustomerFlowFolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowFolderCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowFolderListResponse:
        """
        Returns every folder the project groups its customer flows into, with how many
        flows each holds, in the order the app shows them. Filter the flow list to one
        folder with `GET /v1/customer-flow?folderId=`. Customer flows were previously
        called scenarios.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/customer-flow/folder",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowFolderListResponse,
        )

    def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowFolderDeleteResponse:
        """Deletes a folder.

        The flows in it are kept and no longer sit in any folder.
        Built-in folders cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._delete(
            f"/v1/customer-flow/folder/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowFolderDeleteResponse,
        )


class AsyncCustomerFlowFolderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomerFlowFolderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerFlowFolderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerFlowFolderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/roarkhq/sdk-roark-analytics-python#with_streaming_response
        """
        return AsyncCustomerFlowFolderResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        color: Literal[
            "GREEN", "RED", "ORANGE", "PURPLE", "GREY", "BLUE", "PEACH", "TEAL", "INDIGO", "AMBER", "ROSE", "CYAN"
        ]
        | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowFolderCreateResponse:
        """Creates a folder to group customer flows.

        File a flow into it by sending its
        `folderId` when you create or update the flow. Names are unique within a
        project, ignoring case. Customer flows were previously called scenarios.

        Args:
          name: The folder name. Must be unique in the project.

          color: The color the folder is shown with in the app. Folders share the palette labels
              use. Defaults to GREY.

          description: What belongs in this folder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/customer-flow/folder",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "color": color,
                    "description": description,
                },
                customer_flow_folder_create_params.CustomerFlowFolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowFolderCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowFolderListResponse:
        """
        Returns every folder the project groups its customer flows into, with how many
        flows each holds, in the order the app shows them. Filter the flow list to one
        folder with `GET /v1/customer-flow?folderId=`. Customer flows were previously
        called scenarios.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/customer-flow/folder",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowFolderListResponse,
        )

    async def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerFlowFolderDeleteResponse:
        """Deletes a folder.

        The flows in it are kept and no longer sit in any folder.
        Built-in folders cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._delete(
            f"/v1/customer-flow/folder/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerFlowFolderDeleteResponse,
        )


class CustomerFlowFolderResourceWithRawResponse:
    def __init__(self, customer_flow_folder: CustomerFlowFolderResource) -> None:
        self._customer_flow_folder = customer_flow_folder

        self.create = to_raw_response_wrapper(
            customer_flow_folder.create,
        )
        self.list = to_raw_response_wrapper(
            customer_flow_folder.list,
        )
        self.delete = to_raw_response_wrapper(
            customer_flow_folder.delete,
        )


class AsyncCustomerFlowFolderResourceWithRawResponse:
    def __init__(self, customer_flow_folder: AsyncCustomerFlowFolderResource) -> None:
        self._customer_flow_folder = customer_flow_folder

        self.create = async_to_raw_response_wrapper(
            customer_flow_folder.create,
        )
        self.list = async_to_raw_response_wrapper(
            customer_flow_folder.list,
        )
        self.delete = async_to_raw_response_wrapper(
            customer_flow_folder.delete,
        )


class CustomerFlowFolderResourceWithStreamingResponse:
    def __init__(self, customer_flow_folder: CustomerFlowFolderResource) -> None:
        self._customer_flow_folder = customer_flow_folder

        self.create = to_streamed_response_wrapper(
            customer_flow_folder.create,
        )
        self.list = to_streamed_response_wrapper(
            customer_flow_folder.list,
        )
        self.delete = to_streamed_response_wrapper(
            customer_flow_folder.delete,
        )


class AsyncCustomerFlowFolderResourceWithStreamingResponse:
    def __init__(self, customer_flow_folder: AsyncCustomerFlowFolderResource) -> None:
        self._customer_flow_folder = customer_flow_folder

        self.create = async_to_streamed_response_wrapper(
            customer_flow_folder.create,
        )
        self.list = async_to_streamed_response_wrapper(
            customer_flow_folder.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            customer_flow_folder.delete,
        )
