# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_by_namespace_request(
    resource_group_name: str,
    namespace_name: str,
    subscription_id: str,
    *,
    skip: Optional[int] = None,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/schemagroups")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if skip is not None:
        _query_parameters['$skip'] = _SERIALIZER.query("skip", skip, 'int', maximum=1000, minimum=0)
    if top is not None:
        _query_parameters['$top'] = _SERIALIZER.query("top", top, 'int', maximum=1000, minimum=1)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_create_or_update_request(
    resource_group_name: str,
    namespace_name: str,
    schema_group_name: str,
    subscription_id: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/schemagroups/{schemaGroupName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
        "schemaGroupName": _SERIALIZER.url("schema_group_name", schema_group_name, 'str', max_length=256, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request(
    resource_group_name: str,
    namespace_name: str,
    schema_group_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/schemagroups/{schemaGroupName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
        "schemaGroupName": _SERIALIZER.url("schema_group_name", schema_group_name, 'str', max_length=256, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_request(
    resource_group_name: str,
    namespace_name: str,
    schema_group_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/schemagroups/{schemaGroupName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
        "schemaGroupName": _SERIALIZER.url("schema_group_name", schema_group_name, 'str', max_length=256, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

class SchemaRegistryOperations(object):
    """SchemaRegistryOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.eventhub.v2022_01_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_by_namespace(
        self,
        resource_group_name: str,
        namespace_name: str,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.SchemaGroupListResult"]:
        """Gets all the Schema Groups in a Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param skip: Skip is only used if a previous operation returned a partial result. If a previous
         response contains a nextLink element, the value of the nextLink element will include a skip
         parameter that specifies a starting point to use for subsequent calls. Default value is None.
        :type skip: int
        :param top: May be used to limit the number of results to the most recent N usageDetails.
         Default value is None.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SchemaGroupListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.eventhub.v2022_01_01_preview.models.SchemaGroupListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SchemaGroupListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_namespace_request(
                    resource_group_name=resource_group_name,
                    namespace_name=namespace_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    skip=skip,
                    top=top,
                    template_url=self.list_by_namespace.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_namespace_request(
                    resource_group_name=resource_group_name,
                    namespace_name=namespace_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    skip=skip,
                    top=top,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("SchemaGroupListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_namespace.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/schemagroups"}  # type: ignore

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        schema_group_name: str,
        parameters: "_models.SchemaGroup",
        **kwargs: Any
    ) -> "_models.SchemaGroup":
        """create_or_update.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param schema_group_name: The Schema Group name.
        :type schema_group_name: str
        :param parameters: Parameters supplied to create an Event Hub resource.
        :type parameters: ~azure.mgmt.eventhub.v2022_01_01_preview.models.SchemaGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SchemaGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2022_01_01_preview.models.SchemaGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SchemaGroup"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'SchemaGroup')

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            schema_group_name=schema_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SchemaGroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/schemagroups/{schemaGroupName}"}  # type: ignore


    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        namespace_name: str,
        schema_group_name: str,
        **kwargs: Any
    ) -> None:
        """delete.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param schema_group_name: The Schema Group name.
        :type schema_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            schema_group_name=schema_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/schemagroups/{schemaGroupName}"}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        namespace_name: str,
        schema_group_name: str,
        **kwargs: Any
    ) -> "_models.SchemaGroup":
        """get.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param schema_group_name: The Schema Group name.
        :type schema_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SchemaGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2022_01_01_preview.models.SchemaGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SchemaGroup"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            schema_group_name=schema_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SchemaGroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/schemagroups/{schemaGroupName}"}  # type: ignore

