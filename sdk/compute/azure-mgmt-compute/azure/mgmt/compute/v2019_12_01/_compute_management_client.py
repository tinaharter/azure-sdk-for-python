# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models
from ._configuration import ComputeManagementClientConfiguration
from .operations import AvailabilitySetsOperations, DedicatedHostGroupsOperations, DedicatedHostsOperations, GalleriesOperations, GalleryApplicationVersionsOperations, GalleryApplicationsOperations, GalleryImageVersionsOperations, GalleryImagesOperations, ImagesOperations, LogAnalyticsOperations, Operations, ProximityPlacementGroupsOperations, SshPublicKeysOperations, UsageOperations, VirtualMachineExtensionImagesOperations, VirtualMachineExtensionsOperations, VirtualMachineImagesOperations, VirtualMachineRunCommandsOperations, VirtualMachineScaleSetExtensionsOperations, VirtualMachineScaleSetRollingUpgradesOperations, VirtualMachineScaleSetVMExtensionsOperations, VirtualMachineScaleSetVMsOperations, VirtualMachineScaleSetsOperations, VirtualMachineSizesOperations, VirtualMachinesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class ComputeManagementClient:    # pylint: disable=too-many-instance-attributes
    """Compute Client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.compute.v2019_12_01.operations.Operations
    :ivar availability_sets: AvailabilitySetsOperations operations
    :vartype availability_sets:
     azure.mgmt.compute.v2019_12_01.operations.AvailabilitySetsOperations
    :ivar proximity_placement_groups: ProximityPlacementGroupsOperations operations
    :vartype proximity_placement_groups:
     azure.mgmt.compute.v2019_12_01.operations.ProximityPlacementGroupsOperations
    :ivar dedicated_host_groups: DedicatedHostGroupsOperations operations
    :vartype dedicated_host_groups:
     azure.mgmt.compute.v2019_12_01.operations.DedicatedHostGroupsOperations
    :ivar dedicated_hosts: DedicatedHostsOperations operations
    :vartype dedicated_hosts: azure.mgmt.compute.v2019_12_01.operations.DedicatedHostsOperations
    :ivar ssh_public_keys: SshPublicKeysOperations operations
    :vartype ssh_public_keys: azure.mgmt.compute.v2019_12_01.operations.SshPublicKeysOperations
    :ivar virtual_machine_extension_images: VirtualMachineExtensionImagesOperations operations
    :vartype virtual_machine_extension_images:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineExtensionImagesOperations
    :ivar virtual_machine_extensions: VirtualMachineExtensionsOperations operations
    :vartype virtual_machine_extensions:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineExtensionsOperations
    :ivar virtual_machine_images: VirtualMachineImagesOperations operations
    :vartype virtual_machine_images:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineImagesOperations
    :ivar usage: UsageOperations operations
    :vartype usage: azure.mgmt.compute.v2019_12_01.operations.UsageOperations
    :ivar virtual_machines: VirtualMachinesOperations operations
    :vartype virtual_machines: azure.mgmt.compute.v2019_12_01.operations.VirtualMachinesOperations
    :ivar virtual_machine_sizes: VirtualMachineSizesOperations operations
    :vartype virtual_machine_sizes:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineSizesOperations
    :ivar images: ImagesOperations operations
    :vartype images: azure.mgmt.compute.v2019_12_01.operations.ImagesOperations
    :ivar virtual_machine_scale_sets: VirtualMachineScaleSetsOperations operations
    :vartype virtual_machine_scale_sets:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineScaleSetsOperations
    :ivar virtual_machine_scale_set_extensions: VirtualMachineScaleSetExtensionsOperations
     operations
    :vartype virtual_machine_scale_set_extensions:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineScaleSetExtensionsOperations
    :ivar virtual_machine_scale_set_rolling_upgrades:
     VirtualMachineScaleSetRollingUpgradesOperations operations
    :vartype virtual_machine_scale_set_rolling_upgrades:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineScaleSetRollingUpgradesOperations
    :ivar virtual_machine_scale_set_vm_extensions: VirtualMachineScaleSetVMExtensionsOperations
     operations
    :vartype virtual_machine_scale_set_vm_extensions:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineScaleSetVMExtensionsOperations
    :ivar virtual_machine_scale_set_vms: VirtualMachineScaleSetVMsOperations operations
    :vartype virtual_machine_scale_set_vms:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineScaleSetVMsOperations
    :ivar log_analytics: LogAnalyticsOperations operations
    :vartype log_analytics: azure.mgmt.compute.v2019_12_01.operations.LogAnalyticsOperations
    :ivar virtual_machine_run_commands: VirtualMachineRunCommandsOperations operations
    :vartype virtual_machine_run_commands:
     azure.mgmt.compute.v2019_12_01.operations.VirtualMachineRunCommandsOperations
    :ivar galleries: GalleriesOperations operations
    :vartype galleries: azure.mgmt.compute.v2019_12_01.operations.GalleriesOperations
    :ivar gallery_images: GalleryImagesOperations operations
    :vartype gallery_images: azure.mgmt.compute.v2019_12_01.operations.GalleryImagesOperations
    :ivar gallery_image_versions: GalleryImageVersionsOperations operations
    :vartype gallery_image_versions:
     azure.mgmt.compute.v2019_12_01.operations.GalleryImageVersionsOperations
    :ivar gallery_applications: GalleryApplicationsOperations operations
    :vartype gallery_applications:
     azure.mgmt.compute.v2019_12_01.operations.GalleryApplicationsOperations
    :ivar gallery_application_versions: GalleryApplicationVersionsOperations operations
    :vartype gallery_application_versions:
     azure.mgmt.compute.v2019_12_01.operations.GalleryApplicationVersionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2019-12-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ComputeManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.availability_sets = AvailabilitySetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.proximity_placement_groups = ProximityPlacementGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dedicated_host_groups = DedicatedHostGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dedicated_hosts = DedicatedHostsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.ssh_public_keys = SshPublicKeysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_extension_images = VirtualMachineExtensionImagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_extensions = VirtualMachineExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_images = VirtualMachineImagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.usage = UsageOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machines = VirtualMachinesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.images = ImagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_scale_sets = VirtualMachineScaleSetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_scale_set_extensions = VirtualMachineScaleSetExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_scale_set_rolling_upgrades = VirtualMachineScaleSetRollingUpgradesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_scale_set_vm_extensions = VirtualMachineScaleSetVMExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_scale_set_vms = VirtualMachineScaleSetVMsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.log_analytics = LogAnalyticsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_run_commands = VirtualMachineRunCommandsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.galleries = GalleriesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.gallery_images = GalleryImagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.gallery_image_versions = GalleryImageVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.gallery_applications = GalleryApplicationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.gallery_application_versions = GalleryApplicationVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ComputeManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
