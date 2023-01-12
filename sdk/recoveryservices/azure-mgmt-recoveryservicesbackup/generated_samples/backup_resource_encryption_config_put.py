# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.recoveryservicesbackup import RecoveryServicesBackupClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-recoveryservicesbackup
# USAGE
    python backup_resource_encryption_config_put.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = RecoveryServicesBackupClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.backup_resource_encryption_configs.update(
        vault_name="source-rsv",
        resource_group_name="test-rg",
        parameters={
            "properties": {
                "encryptionAtRestType": "CustomerManaged",
                "infrastructureEncryptionState": "true",
                "keyUri": "https://gktestkv1.vault.azure.net/keys/Test1/ed2e8cdc7f86477ebf0c6462b504a9ed",
                "subscriptionId": "1a2311d9-66f5-47d3-a9fb-7a37da63934b",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/preview/2022-09-01-preview/examples/BackupResourceEncryptionConfig_Put.json
if __name__ == "__main__":
    main()
