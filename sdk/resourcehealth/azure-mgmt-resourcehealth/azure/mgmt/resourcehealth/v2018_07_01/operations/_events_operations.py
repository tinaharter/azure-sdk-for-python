# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_subscription_id_request(
    subscription_id: str,
    *,
    filter: Optional[str] = None,
    query_start_time: Optional[str] = None,
    view: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01"))  # type: Literal["2018-07-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/events")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if query_start_time is not None:
        _params["queryStartTime"] = _SERIALIZER.query("query_start_time", query_start_time, "str")
    if view is not None:
        _params["view"] = _SERIALIZER.query("view", view, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_single_resource_request(
    resource_uri: str, *, filter: Optional[str] = None, view: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01"))  # type: Literal["2018-07-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{resourceUri}/providers/Microsoft.ResourceHealth/events")
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if view is not None:
        _params["view"] = _SERIALIZER.query("view", view, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class EventsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.resourcehealth.v2018_07_01.MicrosoftResourceHealth`'s
        :attr:`events` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_subscription_id(
        self,
        filter: Optional[str] = None,
        query_start_time: Optional[str] = None,
        view: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.Event"]:
        """Lists current service health events in the subscription.

        :param filter: A valid odata query to limit the events returned. The logical operators and, or,
         equal, not equal, and top are supported. For example, $filter=Properties/EventType eq
         'ServiceIssue' or Properties/EventType eq 'PlannedMaintenance' OR
         %24filter=Properties%2FEventType%20eq%20%27ServiceIssue%27%20or%20Properties%2FEventType%20eq%20%27PlannedMaintenance%27.
         Default value is None.
        :type filter: str
        :param query_start_time: Specifies from when to return events, based on the lastUpdateTime
         property. For example, queryStartTime = 7/24/2020 OR queryStartTime=7%2F24%2F2020. Default
         value is None.
        :type query_start_time: str
        :param view: setting view=full expands the article parameters. Default value is None.
        :type view: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Event or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.resourcehealth.v2018_07_01.models.Event]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01"))  # type: Literal["2018-07-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Events]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_subscription_id_request(
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    query_start_time=query_start_time,
                    view=view,
                    api_version=api_version,
                    template_url=self.list_by_subscription_id.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("Events", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_subscription_id.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/events"}  # type: ignore

    @distributed_trace
    def list_by_single_resource(
        self, resource_uri: str, filter: Optional[str] = None, view: Optional[str] = None, **kwargs: Any
    ) -> Iterable["_models.Event"]:
        """Lists current service health events for given resource.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Currently the API support not nested and one nesting level resource types :
         /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name}
         and
         /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}.
         Required.
        :type resource_uri: str
        :param filter: A valid odata query to limit the events returned. The logical operators and, or,
         equal, not equal, and top are supported. For example, $filter=Properties/EventType eq
         'ServiceIssue' or Properties/EventType eq 'PlannedMaintenance' OR
         %24filter=Properties%2FEventType%20eq%20%27ServiceIssue%27%20or%20Properties%2FEventType%20eq%20%27PlannedMaintenance%27.
         Default value is None.
        :type filter: str
        :param view: setting view=full expands the article parameters. Default value is None.
        :type view: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Event or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.resourcehealth.v2018_07_01.models.Event]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01"))  # type: Literal["2018-07-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Events]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_single_resource_request(
                    resource_uri=resource_uri,
                    filter=filter,
                    view=view,
                    api_version=api_version,
                    template_url=self.list_by_single_resource.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("Events", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_single_resource.metadata = {"url": "/{resourceUri}/providers/Microsoft.ResourceHealth/events"}  # type: ignore