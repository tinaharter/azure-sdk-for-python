# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._access_review_instance_my_decisions_operations import (
    build_get_by_id_request,
    build_list_request,
    build_patch_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AccessReviewInstanceMyDecisionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.v2021_07_01_preview.aio.AuthorizationManagementClient`'s
        :attr:`access_review_instance_my_decisions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, schedule_definition_id: str, id: str, filter: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.AccessReviewDecision"]:
        """Get my access review instance decisions.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param filter: The filter to apply on the operation. Other than standard filters, one custom
         filter option is supported : 'assignedToMeToReview()'. When one specified
         $filter=assignedToMeToReview(), only items that are assigned to the calling user to review are
         returned. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AccessReviewDecision or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.authorization.v2021_07_01_preview.models.AccessReviewDecision]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-07-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-07-01-preview")
        )
        cls: ClsType[_models.AccessReviewDecisionListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    schedule_definition_id=schedule_definition_id,
                    id=id,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

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
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AccessReviewDecisionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}/decisions"
    }

    @distributed_trace_async
    async def get_by_id(
        self, schedule_definition_id: str, id: str, decision_id: str, **kwargs: Any
    ) -> _models.AccessReviewDecision:
        """Get my single access review instance decision.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param decision_id: The id of the decision record. Required.
        :type decision_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewDecision or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_07_01_preview.models.AccessReviewDecision
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

        api_version: Literal["2021-07-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-07-01-preview")
        )
        cls: ClsType[_models.AccessReviewDecision] = kwargs.pop("cls", None)

        request = build_get_by_id_request(
            schedule_definition_id=schedule_definition_id,
            id=id,
            decision_id=decision_id,
            api_version=api_version,
            template_url=self.get_by_id.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AccessReviewDecision", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_id.metadata = {
        "url": "/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}/decisions/{decisionId}"
    }

    @overload
    async def patch(
        self,
        schedule_definition_id: str,
        id: str,
        decision_id: str,
        properties: _models.AccessReviewDecisionProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AccessReviewDecision:
        """Record a decision.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param decision_id: The id of the decision record. Required.
        :type decision_id: str
        :param properties: Access review decision properties to patch. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_07_01_preview.models.AccessReviewDecisionProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewDecision or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_07_01_preview.models.AccessReviewDecision
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch(
        self,
        schedule_definition_id: str,
        id: str,
        decision_id: str,
        properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AccessReviewDecision:
        """Record a decision.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param decision_id: The id of the decision record. Required.
        :type decision_id: str
        :param properties: Access review decision properties to patch. Required.
        :type properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewDecision or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_07_01_preview.models.AccessReviewDecision
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def patch(
        self,
        schedule_definition_id: str,
        id: str,
        decision_id: str,
        properties: Union[_models.AccessReviewDecisionProperties, IO],
        **kwargs: Any
    ) -> _models.AccessReviewDecision:
        """Record a decision.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param decision_id: The id of the decision record. Required.
        :type decision_id: str
        :param properties: Access review decision properties to patch. Is either a
         AccessReviewDecisionProperties type or a IO type. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_07_01_preview.models.AccessReviewDecisionProperties or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewDecision or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_07_01_preview.models.AccessReviewDecision
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-07-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-07-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AccessReviewDecision] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IO, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "AccessReviewDecisionProperties")

        request = build_patch_request(
            schedule_definition_id=schedule_definition_id,
            id=id,
            decision_id=decision_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.patch.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AccessReviewDecision", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    patch.metadata = {
        "url": "/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}/decisions/{decisionId}"
    }
