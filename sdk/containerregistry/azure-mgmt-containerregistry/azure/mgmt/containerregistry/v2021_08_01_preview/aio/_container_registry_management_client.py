# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from ..._serialization import Deserializer, Serializer
from ._configuration import ContainerRegistryManagementClientConfiguration
from .operations import (
    ConnectedRegistriesOperations,
    ExportPipelinesOperations,
    ImportPipelinesOperations,
    Operations,
    PipelineRunsOperations,
    PrivateEndpointConnectionsOperations,
    RegistriesOperations,
    ReplicationsOperations,
    ScopeMapsOperations,
    TokensOperations,
    WebhooksOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class ContainerRegistryManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """ContainerRegistryManagementClient.

    :ivar connected_registries: ConnectedRegistriesOperations operations
    :vartype connected_registries:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.ConnectedRegistriesOperations
    :ivar export_pipelines: ExportPipelinesOperations operations
    :vartype export_pipelines:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.ExportPipelinesOperations
    :ivar registries: RegistriesOperations operations
    :vartype registries:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.RegistriesOperations
    :ivar import_pipelines: ImportPipelinesOperations operations
    :vartype import_pipelines:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.ImportPipelinesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.Operations
    :ivar pipeline_runs: PipelineRunsOperations operations
    :vartype pipeline_runs:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.PipelineRunsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.PrivateEndpointConnectionsOperations
    :ivar replications: ReplicationsOperations operations
    :vartype replications:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.ReplicationsOperations
    :ivar scope_maps: ScopeMapsOperations operations
    :vartype scope_maps:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.ScopeMapsOperations
    :ivar tokens: TokensOperations operations
    :vartype tokens:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.TokensOperations
    :ivar webhooks: WebhooksOperations operations
    :vartype webhooks:
     azure.mgmt.containerregistry.v2021_08_01_preview.aio.operations.WebhooksOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The Microsoft Azure subscription ID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2021-08-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ContainerRegistryManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.connected_registries = ConnectedRegistriesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.export_pipelines = ExportPipelinesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registries = RegistriesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.import_pipelines = ImportPipelinesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_runs = PipelineRunsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replications = ReplicationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.scope_maps = ScopeMapsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.tokens = TokensOperations(self._client, self._config, self._serialize, self._deserialize)
        self.webhooks = WebhooksOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ContainerRegistryManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
