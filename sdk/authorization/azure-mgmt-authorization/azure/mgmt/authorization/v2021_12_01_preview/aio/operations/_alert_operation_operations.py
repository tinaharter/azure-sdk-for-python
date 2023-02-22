# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._alert_operation_operations import build_get_request, build_list_for_scope_request

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AlertOperationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.v2021_12_01_preview.aio.AuthorizationManagementClient`'s
        :attr:`alert_operation` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, scope: str, operation_id: str, **kwargs: Any) -> _models.AlertOperationResult:
        """Get the specified alert operation.

        :param scope: The scope of the alert operation. Required.
        :type scope: str
        :param operation_id: The id of the alert operation. Required.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AlertOperationResult or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AlertOperationResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-08-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2022-08-01-preview")
        )
        cls: ClsType[_models.AlertOperationResult] = kwargs.pop("cls", None)

        request = build_get_request(
            scope=scope,
            operation_id=operation_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AlertOperationResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleManagementAlertOperations/{operationId}"}

    @distributed_trace_async
    async def list_for_scope(self, scope: str, **kwargs: Any) -> _models.AlertOperationListResult:
        """Gets alert operations for a resource scope.

        :param scope: The scope of the alert operation. Required.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AlertOperationListResult or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AlertOperationListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-08-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2022-08-01-preview")
        )
        cls: ClsType[_models.AlertOperationListResult] = kwargs.pop("cls", None)

        request = build_list_for_scope_request(
            scope=scope,
            api_version=api_version,
            template_url=self.list_for_scope.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AlertOperationListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_for_scope.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleManagementAlertOperations"}
