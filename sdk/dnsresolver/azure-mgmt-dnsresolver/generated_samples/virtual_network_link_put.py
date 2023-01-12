# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.dnsresolver import DnsResolverManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-dnsresolver
# USAGE
    python virtual_network_link_put.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DnsResolverManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="abdd4249-9f34-4cc6-8e42-c2e32110603e",
    )

    response = client.virtual_network_links.begin_create_or_update(
        resource_group_name="sampleResourceGroup",
        dns_forwarding_ruleset_name="sampleDnsForwardingRuleset",
        virtual_network_link_name="sampleVirtualNetworkLink",
        parameters={
            "properties": {
                "metadata": {"additionalProp1": "value1"},
                "virtualNetwork": {
                    "id": "/subscriptions/0403cfa9-9659-4f33-9f30-1f191c51d111/resourceGroups/sampleVnetResourceGroupName/providers/Microsoft.Network/virtualNetworks/sampleVirtualNetwork"
                },
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/dnsresolver/resource-manager/Microsoft.Network/stable/2022-07-01/examples/VirtualNetworkLink_Put.json
if __name__ == "__main__":
    main()
