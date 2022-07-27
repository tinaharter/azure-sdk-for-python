# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_list_file_systems_request(
    url,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    resource = kwargs.pop('resource', _params.pop('resource', "account"))  # type: str
    version = kwargs.pop('version', _headers.pop('x-ms-version', "2021-06-08"))  # type: str
    prefix = kwargs.pop('prefix', _params.pop('prefix', None))  # type: Optional[str]
    continuation = kwargs.pop('continuation', _params.pop('continuation', None))  # type: Optional[str]
    max_results = kwargs.pop('max_results', _params.pop('maxResults', None))  # type: Optional[int]
    request_id_parameter = kwargs.pop('request_id_parameter', _headers.pop('x-ms-client-request-id', None))  # type: Optional[str]
    timeout = kwargs.pop('timeout', _params.pop('timeout', None))  # type: Optional[int]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['resource'] = _SERIALIZER.query("resource", resource, 'str')
    if prefix is not None:
        _params['prefix'] = _SERIALIZER.query("prefix", prefix, 'str')
    if continuation is not None:
        _params['continuation'] = _SERIALIZER.query("continuation", continuation, 'str')
    if max_results is not None:
        _params['maxResults'] = _SERIALIZER.query("max_results", max_results, 'int', minimum=1)
    if timeout is not None:
        _params['timeout'] = _SERIALIZER.query("timeout", timeout, 'int', minimum=0)

    # Construct headers
    if request_id_parameter is not None:
        _headers['x-ms-client-request-id'] = _SERIALIZER.header("request_id_parameter", request_id_parameter, 'str')
    _headers['x-ms-version'] = _SERIALIZER.header("version", version, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

# fmt: on
class ServiceOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.filedatalake.AzureDataLakeStorageRESTAPI`'s
        :attr:`service` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list_file_systems(
        self,
        prefix=None,  # type: Optional[str]
        continuation=None,  # type: Optional[str]
        max_results=None,  # type: Optional[int]
        request_id_parameter=None,  # type: Optional[str]
        timeout=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable[_models.FileSystemList]
        """List FileSystems.

        List filesystems and their properties in given account.

        :param prefix: Filters results to filesystems within the specified prefix. Default value is
         None.
        :type prefix: str
        :param continuation: Optional.  When deleting a directory, the number of paths that are deleted
         with each invocation is limited.  If the number of paths to be deleted exceeds this limit, a
         continuation token is returned in this response header.  When a continuation token is returned
         in the response, it must be specified in a subsequent invocation of the delete operation to
         continue deleting the directory. Default value is None.
        :type continuation: str
        :param max_results: An optional value that specifies the maximum number of items to return. If
         omitted or greater than 5,000, the response will include up to 5,000 items. Default value is
         None.
        :type max_results: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword resource: The value must be "account" for all account operations. Default value is
         "account". Note that overriding this default value may result in unsupported behavior.
        :paramtype resource: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FileSystemList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.storage.filedatalake.models.FileSystemList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        resource = kwargs.pop('resource', _params.pop('resource', "account"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FileSystemList]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_file_systems_request(
                    url=self._config.url,
                    resource=resource,
                    version=self._config.version,
                    prefix=prefix,
                    continuation=continuation,
                    max_results=max_results,
                    request_id_parameter=request_id_parameter,
                    timeout=timeout,
                    template_url=self.list_file_systems.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_file_systems_request(
                    url=self._config.url,
                    resource=resource,
                    version=self._config.version,
                    prefix=prefix,
                    continuation=continuation,
                    max_results=max_results,
                    request_id_parameter=request_id_parameter,
                    timeout=timeout,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("FileSystemList", pipeline_response)
            list_of_elem = deserialized.filesystems
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

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
                error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_file_systems.metadata = {'url': "{url}"}  # type: ignore
