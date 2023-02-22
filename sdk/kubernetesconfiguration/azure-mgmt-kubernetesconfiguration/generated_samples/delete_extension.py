# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.kubernetesconfiguration import SourceControlConfigurationClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-kubernetesconfiguration
# USAGE
    python delete_extension.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SourceControlConfigurationClient(
        credential=DefaultAzureCredential(),
        subscription_id="subId1",
    )

    response = client.extensions.begin_delete(
        resource_group_name="rg1",
        cluster_rp="Microsoft.Kubernetes",
        cluster_resource_name="connectedClusters",
        cluster_name="clusterName1",
        extension_name="ClusterMonitor",
    ).result()
    print(response)


# x-ms-original-file: specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/stable/2022-11-01/examples/DeleteExtension.json
if __name__ == "__main__":
    main()
