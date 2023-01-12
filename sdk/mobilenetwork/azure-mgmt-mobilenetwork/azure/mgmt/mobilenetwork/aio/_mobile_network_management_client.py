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
from .._serialization import Deserializer, Serializer
from ._configuration import MobileNetworkManagementClientConfiguration
from .operations import (
    AttachedDataNetworksOperations,
    DataNetworksOperations,
    MobileNetworksOperations,
    Operations,
    PacketCoreControlPlaneOperations,
    PacketCoreControlPlaneVersionsOperations,
    PacketCoreControlPlanesOperations,
    PacketCoreDataPlanesOperations,
    ServicesOperations,
    SimGroupsOperations,
    SimOperations,
    SimPoliciesOperations,
    SimsOperations,
    SitesOperations,
    SlicesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class MobileNetworkManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The resources in this API specification will be used to manage attached data network resources
    in mobile network attached to a particular packet core instance.

    :ivar attached_data_networks: AttachedDataNetworksOperations operations
    :vartype attached_data_networks:
     azure.mgmt.mobilenetwork.aio.operations.AttachedDataNetworksOperations
    :ivar data_networks: DataNetworksOperations operations
    :vartype data_networks: azure.mgmt.mobilenetwork.aio.operations.DataNetworksOperations
    :ivar mobile_networks: MobileNetworksOperations operations
    :vartype mobile_networks: azure.mgmt.mobilenetwork.aio.operations.MobileNetworksOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.mobilenetwork.aio.operations.Operations
    :ivar packet_core_control_planes: PacketCoreControlPlanesOperations operations
    :vartype packet_core_control_planes:
     azure.mgmt.mobilenetwork.aio.operations.PacketCoreControlPlanesOperations
    :ivar packet_core_control_plane: PacketCoreControlPlaneOperations operations
    :vartype packet_core_control_plane:
     azure.mgmt.mobilenetwork.aio.operations.PacketCoreControlPlaneOperations
    :ivar packet_core_control_plane_versions: PacketCoreControlPlaneVersionsOperations operations
    :vartype packet_core_control_plane_versions:
     azure.mgmt.mobilenetwork.aio.operations.PacketCoreControlPlaneVersionsOperations
    :ivar packet_core_data_planes: PacketCoreDataPlanesOperations operations
    :vartype packet_core_data_planes:
     azure.mgmt.mobilenetwork.aio.operations.PacketCoreDataPlanesOperations
    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.mobilenetwork.aio.operations.ServicesOperations
    :ivar sims: SimsOperations operations
    :vartype sims: azure.mgmt.mobilenetwork.aio.operations.SimsOperations
    :ivar sim: SimOperations operations
    :vartype sim: azure.mgmt.mobilenetwork.aio.operations.SimOperations
    :ivar sim_groups: SimGroupsOperations operations
    :vartype sim_groups: azure.mgmt.mobilenetwork.aio.operations.SimGroupsOperations
    :ivar sim_policies: SimPoliciesOperations operations
    :vartype sim_policies: azure.mgmt.mobilenetwork.aio.operations.SimPoliciesOperations
    :ivar sites: SitesOperations operations
    :vartype sites: azure.mgmt.mobilenetwork.aio.operations.SitesOperations
    :ivar slices: SlicesOperations operations
    :vartype slices: azure.mgmt.mobilenetwork.aio.operations.SlicesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-11-01". Note that overriding this
     default value may result in unsupported behavior.
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
        self._config = MobileNetworkManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.attached_data_networks = AttachedDataNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_networks = DataNetworksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.mobile_networks = MobileNetworksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.packet_core_control_planes = PacketCoreControlPlanesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.packet_core_control_plane = PacketCoreControlPlaneOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.packet_core_control_plane_versions = PacketCoreControlPlaneVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.packet_core_data_planes = PacketCoreDataPlanesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.services = ServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sims = SimsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sim = SimOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sim_groups = SimGroupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sim_policies = SimPoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sites = SitesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.slices = SlicesOperations(self._client, self._config, self._serialize, self._deserialize)

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

    async def __aenter__(self) -> "MobileNetworkManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
