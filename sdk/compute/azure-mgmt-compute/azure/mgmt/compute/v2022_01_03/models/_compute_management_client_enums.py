# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AggregatedReplicationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This is the aggregated replication status based on all the regional replication status flags.
    """

    UNKNOWN = "Unknown"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"

class Architecture(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The architecture of the image. Applicable to OS disks only.
    """

    X64 = "x64"
    ARM64 = "Arm64"

class ConfidentialVMEncryptionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """confidential VM encryption types
    """

    ENCRYPTED_VM_GUEST_STATE_ONLY_WITH_PMK = "EncryptedVMGuestStateOnlyWithPmk"
    ENCRYPTED_WITH_PMK = "EncryptedWithPmk"
    ENCRYPTED_WITH_CMK = "EncryptedWithCmk"

class ExtendedLocationTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of extendedLocation.
    """

    EDGE_ZONE = "EdgeZone"

class GalleryExpandParams(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    SHARING_PROFILE_GROUPS = "SharingProfile/Groups"

class GalleryExtendedLocationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """It is type of the extended location.
    """

    EDGE_ZONE = "EdgeZone"
    UNKNOWN = "Unknown"

class GalleryProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state, which only appears in the response.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    MIGRATING = "Migrating"

class GallerySharingPermissionTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This property allows you to specify the permission of sharing gallery. :code:`<br>`:code:`<br>`
    Possible values are: :code:`<br>`:code:`<br>` **Private** :code:`<br>`:code:`<br>` **Groups**
    :code:`<br>`:code:`<br>` **Community**
    """

    PRIVATE = "Private"
    GROUPS = "Groups"
    COMMUNITY = "Community"

class HostCaching(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The host caching of the disk. Valid values are 'None', 'ReadOnly', and 'ReadWrite'
    """

    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"

class HyperVGeneration(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    """

    V1 = "V1"
    V2 = "V2"

class OperatingSystemStateTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This property allows the user to specify whether the virtual machines created under this image
    are 'Generalized' or 'Specialized'.
    """

    GENERALIZED = "Generalized"
    SPECIALIZED = "Specialized"

class OperatingSystemTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This property allows you to specify the supported type of the OS that application is built for.
    :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>` **Windows**
    :code:`<br>`:code:`<br>` **Linux**
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class ReplicationMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Optional parameter which specifies the mode to be used for replication. This property is not
    updatable.
    """

    FULL = "Full"
    SHALLOW = "Shallow"

class ReplicationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This is the regional replication state.
    """

    UNKNOWN = "Unknown"
    REPLICATING = "Replicating"
    COMPLETED = "Completed"
    FAILED = "Failed"

class ReplicationStatusTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    REPLICATION_STATUS = "ReplicationStatus"

class SelectPermissions(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    PERMISSIONS = "Permissions"

class SharedGalleryHostCaching(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The host caching of the disk. Valid values are 'None', 'ReadOnly', and 'ReadWrite'
    """

    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"

class SharedToValues(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    TENANT = "tenant"

class SharingProfileGroupTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This property allows you to specify the type of sharing group. :code:`<br>`:code:`<br>`
    Possible values are: :code:`<br>`:code:`<br>` **Subscriptions** :code:`<br>`:code:`<br>`
    **AADTenants**
    """

    SUBSCRIPTIONS = "Subscriptions"
    AAD_TENANTS = "AADTenants"

class SharingState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The sharing state of the gallery, which only appears in the response.
    """

    SUCCEEDED = "Succeeded"
    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    UNKNOWN = "Unknown"

class SharingUpdateOperationTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This property allows you to specify the operation type of gallery sharing update.
    :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>` **Add**
    :code:`<br>`:code:`<br>` **Remove** :code:`<br>`:code:`<br>` **Reset**
    """

    ADD = "Add"
    REMOVE = "Remove"
    RESET = "Reset"
    ENABLE_COMMUNITY = "EnableCommunity"

class StorageAccountType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the storage account type to be used to store the image. This property is not
    updatable.
    """

    STANDARD_LRS = "Standard_LRS"
    STANDARD_ZRS = "Standard_ZRS"
    PREMIUM_LRS = "Premium_LRS"
