# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import Addon
from ._models_py3 import AddonArcProperties
from ._models_py3 import AddonHcxProperties
from ._models_py3 import AddonList
from ._models_py3 import AddonProperties
from ._models_py3 import AddonSrmProperties
from ._models_py3 import AddonVrProperties
from ._models_py3 import AdminCredentials
from ._models_py3 import AvailabilityProperties
from ._models_py3 import Circuit
from ._models_py3 import CloudLink
from ._models_py3 import CloudLinkList
from ._models_py3 import Cluster
from ._models_py3 import ClusterList
from ._models_py3 import ClusterProperties
from ._models_py3 import ClusterUpdate
from ._models_py3 import ClusterZone
from ._models_py3 import ClusterZoneList
from ._models_py3 import CommonClusterProperties
from ._models_py3 import Datastore
from ._models_py3 import DatastoreList
from ._models_py3 import DiskPoolVolume
from ._models_py3 import Encryption
from ._models_py3 import EncryptionKeyVaultProperties
from ._models_py3 import Endpoints
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorResponse
from ._models_py3 import ExpressRouteAuthorization
from ._models_py3 import ExpressRouteAuthorizationList
from ._models_py3 import GlobalReachConnection
from ._models_py3 import GlobalReachConnectionList
from ._models_py3 import HcxEnterpriseSite
from ._models_py3 import HcxEnterpriseSiteList
from ._models_py3 import IdentitySource
from ._models_py3 import LogSpecification
from ._models_py3 import ManagementCluster
from ._models_py3 import MetricDimension
from ._models_py3 import MetricSpecification
from ._models_py3 import NetAppVolume
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationList
from ._models_py3 import OperationProperties
from ._models_py3 import PSCredentialExecutionParameter
from ._models_py3 import PlacementPoliciesList
from ._models_py3 import PlacementPolicy
from ._models_py3 import PlacementPolicyProperties
from ._models_py3 import PlacementPolicyUpdate
from ._models_py3 import PrivateCloud
from ._models_py3 import PrivateCloudIdentity
from ._models_py3 import PrivateCloudList
from ._models_py3 import PrivateCloudProperties
from ._models_py3 import PrivateCloudUpdate
from ._models_py3 import PrivateCloudUpdateProperties
from ._models_py3 import ProxyResource
from ._models_py3 import Quota
from ._models_py3 import Resource
from ._models_py3 import ScriptCmdlet
from ._models_py3 import ScriptCmdletsList
from ._models_py3 import ScriptExecution
from ._models_py3 import ScriptExecutionParameter
from ._models_py3 import ScriptExecutionsList
from ._models_py3 import ScriptPackage
from ._models_py3 import ScriptPackagesList
from ._models_py3 import ScriptParameter
from ._models_py3 import ScriptSecureStringExecutionParameter
from ._models_py3 import ScriptStringExecutionParameter
from ._models_py3 import ServiceSpecification
from ._models_py3 import Sku
from ._models_py3 import TrackedResource
from ._models_py3 import Trial
from ._models_py3 import VirtualMachine
from ._models_py3 import VirtualMachineRestrictMovement
from ._models_py3 import VirtualMachinesList
from ._models_py3 import VmHostPlacementPolicyProperties
from ._models_py3 import VmPlacementPolicyProperties
from ._models_py3 import WorkloadNetwork
from ._models_py3 import WorkloadNetworkDhcp
from ._models_py3 import WorkloadNetworkDhcpEntity
from ._models_py3 import WorkloadNetworkDhcpList
from ._models_py3 import WorkloadNetworkDhcpRelay
from ._models_py3 import WorkloadNetworkDhcpServer
from ._models_py3 import WorkloadNetworkDnsService
from ._models_py3 import WorkloadNetworkDnsServicesList
from ._models_py3 import WorkloadNetworkDnsZone
from ._models_py3 import WorkloadNetworkDnsZonesList
from ._models_py3 import WorkloadNetworkGateway
from ._models_py3 import WorkloadNetworkGatewayList
from ._models_py3 import WorkloadNetworkList
from ._models_py3 import WorkloadNetworkPortMirroring
from ._models_py3 import WorkloadNetworkPortMirroringList
from ._models_py3 import WorkloadNetworkPublicIP
from ._models_py3 import WorkloadNetworkPublicIPsList
from ._models_py3 import WorkloadNetworkSegment
from ._models_py3 import WorkloadNetworkSegmentPortVif
from ._models_py3 import WorkloadNetworkSegmentSubnet
from ._models_py3 import WorkloadNetworkSegmentsList
from ._models_py3 import WorkloadNetworkVMGroup
from ._models_py3 import WorkloadNetworkVMGroupsList
from ._models_py3 import WorkloadNetworkVirtualMachine
from ._models_py3 import WorkloadNetworkVirtualMachinesList

from ._avs_client_enums import AddonProvisioningState
from ._avs_client_enums import AddonType
from ._avs_client_enums import AffinityStrength
from ._avs_client_enums import AffinityType
from ._avs_client_enums import AvailabilityStrategy
from ._avs_client_enums import AzureHybridBenefitType
from ._avs_client_enums import CloudLinkStatus
from ._avs_client_enums import ClusterProvisioningState
from ._avs_client_enums import DatastoreProvisioningState
from ._avs_client_enums import DatastoreStatus
from ._avs_client_enums import DhcpTypeEnum
from ._avs_client_enums import DnsServiceLogLevelEnum
from ._avs_client_enums import DnsServiceStatusEnum
from ._avs_client_enums import EncryptionKeyStatus
from ._avs_client_enums import EncryptionState
from ._avs_client_enums import EncryptionVersionType
from ._avs_client_enums import ExpressRouteAuthorizationProvisioningState
from ._avs_client_enums import GlobalReachConnectionProvisioningState
from ._avs_client_enums import GlobalReachConnectionStatus
from ._avs_client_enums import HcxEnterpriseSiteStatus
from ._avs_client_enums import InternetEnum
from ._avs_client_enums import MountOptionEnum
from ._avs_client_enums import NsxPublicIpQuotaRaisedEnum
from ._avs_client_enums import OptionalParamEnum
from ._avs_client_enums import PlacementPolicyProvisioningState
from ._avs_client_enums import PlacementPolicyState
from ._avs_client_enums import PlacementPolicyType
from ._avs_client_enums import PortMirroringDirectionEnum
from ._avs_client_enums import PortMirroringStatusEnum
from ._avs_client_enums import PrivateCloudProvisioningState
from ._avs_client_enums import QuotaEnabled
from ._avs_client_enums import ResourceIdentityType
from ._avs_client_enums import ScriptExecutionParameterType
from ._avs_client_enums import ScriptExecutionProvisioningState
from ._avs_client_enums import ScriptOutputStreamType
from ._avs_client_enums import ScriptParameterTypes
from ._avs_client_enums import SegmentStatusEnum
from ._avs_client_enums import SslEnum
from ._avs_client_enums import TrialStatus
from ._avs_client_enums import VMGroupStatusEnum
from ._avs_client_enums import VMTypeEnum
from ._avs_client_enums import VirtualMachineRestrictMovementState
from ._avs_client_enums import VisibilityParameterEnum
from ._avs_client_enums import WorkloadNetworkDhcpProvisioningState
from ._avs_client_enums import WorkloadNetworkDnsServiceProvisioningState
from ._avs_client_enums import WorkloadNetworkDnsZoneProvisioningState
from ._avs_client_enums import WorkloadNetworkName
from ._avs_client_enums import WorkloadNetworkPortMirroringProvisioningState
from ._avs_client_enums import WorkloadNetworkPublicIPProvisioningState
from ._avs_client_enums import WorkloadNetworkSegmentProvisioningState
from ._avs_client_enums import WorkloadNetworkVMGroupProvisioningState
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Addon",
    "AddonArcProperties",
    "AddonHcxProperties",
    "AddonList",
    "AddonProperties",
    "AddonSrmProperties",
    "AddonVrProperties",
    "AdminCredentials",
    "AvailabilityProperties",
    "Circuit",
    "CloudLink",
    "CloudLinkList",
    "Cluster",
    "ClusterList",
    "ClusterProperties",
    "ClusterUpdate",
    "ClusterZone",
    "ClusterZoneList",
    "CommonClusterProperties",
    "Datastore",
    "DatastoreList",
    "DiskPoolVolume",
    "Encryption",
    "EncryptionKeyVaultProperties",
    "Endpoints",
    "ErrorAdditionalInfo",
    "ErrorResponse",
    "ExpressRouteAuthorization",
    "ExpressRouteAuthorizationList",
    "GlobalReachConnection",
    "GlobalReachConnectionList",
    "HcxEnterpriseSite",
    "HcxEnterpriseSiteList",
    "IdentitySource",
    "LogSpecification",
    "ManagementCluster",
    "MetricDimension",
    "MetricSpecification",
    "NetAppVolume",
    "Operation",
    "OperationDisplay",
    "OperationList",
    "OperationProperties",
    "PSCredentialExecutionParameter",
    "PlacementPoliciesList",
    "PlacementPolicy",
    "PlacementPolicyProperties",
    "PlacementPolicyUpdate",
    "PrivateCloud",
    "PrivateCloudIdentity",
    "PrivateCloudList",
    "PrivateCloudProperties",
    "PrivateCloudUpdate",
    "PrivateCloudUpdateProperties",
    "ProxyResource",
    "Quota",
    "Resource",
    "ScriptCmdlet",
    "ScriptCmdletsList",
    "ScriptExecution",
    "ScriptExecutionParameter",
    "ScriptExecutionsList",
    "ScriptPackage",
    "ScriptPackagesList",
    "ScriptParameter",
    "ScriptSecureStringExecutionParameter",
    "ScriptStringExecutionParameter",
    "ServiceSpecification",
    "Sku",
    "TrackedResource",
    "Trial",
    "VirtualMachine",
    "VirtualMachineRestrictMovement",
    "VirtualMachinesList",
    "VmHostPlacementPolicyProperties",
    "VmPlacementPolicyProperties",
    "WorkloadNetwork",
    "WorkloadNetworkDhcp",
    "WorkloadNetworkDhcpEntity",
    "WorkloadNetworkDhcpList",
    "WorkloadNetworkDhcpRelay",
    "WorkloadNetworkDhcpServer",
    "WorkloadNetworkDnsService",
    "WorkloadNetworkDnsServicesList",
    "WorkloadNetworkDnsZone",
    "WorkloadNetworkDnsZonesList",
    "WorkloadNetworkGateway",
    "WorkloadNetworkGatewayList",
    "WorkloadNetworkList",
    "WorkloadNetworkPortMirroring",
    "WorkloadNetworkPortMirroringList",
    "WorkloadNetworkPublicIP",
    "WorkloadNetworkPublicIPsList",
    "WorkloadNetworkSegment",
    "WorkloadNetworkSegmentPortVif",
    "WorkloadNetworkSegmentSubnet",
    "WorkloadNetworkSegmentsList",
    "WorkloadNetworkVMGroup",
    "WorkloadNetworkVMGroupsList",
    "WorkloadNetworkVirtualMachine",
    "WorkloadNetworkVirtualMachinesList",
    "AddonProvisioningState",
    "AddonType",
    "AffinityStrength",
    "AffinityType",
    "AvailabilityStrategy",
    "AzureHybridBenefitType",
    "CloudLinkStatus",
    "ClusterProvisioningState",
    "DatastoreProvisioningState",
    "DatastoreStatus",
    "DhcpTypeEnum",
    "DnsServiceLogLevelEnum",
    "DnsServiceStatusEnum",
    "EncryptionKeyStatus",
    "EncryptionState",
    "EncryptionVersionType",
    "ExpressRouteAuthorizationProvisioningState",
    "GlobalReachConnectionProvisioningState",
    "GlobalReachConnectionStatus",
    "HcxEnterpriseSiteStatus",
    "InternetEnum",
    "MountOptionEnum",
    "NsxPublicIpQuotaRaisedEnum",
    "OptionalParamEnum",
    "PlacementPolicyProvisioningState",
    "PlacementPolicyState",
    "PlacementPolicyType",
    "PortMirroringDirectionEnum",
    "PortMirroringStatusEnum",
    "PrivateCloudProvisioningState",
    "QuotaEnabled",
    "ResourceIdentityType",
    "ScriptExecutionParameterType",
    "ScriptExecutionProvisioningState",
    "ScriptOutputStreamType",
    "ScriptParameterTypes",
    "SegmentStatusEnum",
    "SslEnum",
    "TrialStatus",
    "VMGroupStatusEnum",
    "VMTypeEnum",
    "VirtualMachineRestrictMovementState",
    "VisibilityParameterEnum",
    "WorkloadNetworkDhcpProvisioningState",
    "WorkloadNetworkDnsServiceProvisioningState",
    "WorkloadNetworkDnsZoneProvisioningState",
    "WorkloadNetworkName",
    "WorkloadNetworkPortMirroringProvisioningState",
    "WorkloadNetworkPublicIPProvisioningState",
    "WorkloadNetworkSegmentProvisioningState",
    "WorkloadNetworkVMGroupProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
