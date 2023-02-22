# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import logging
import os
from typing import List, TYPE_CHECKING, Any, cast

from azure.core.credentials import AccessToken
from ..._constants import EnvironmentVariables
from ..._internal import get_default_authority, normalize_authority
from .azure_cli import AzureCliCredential
from .azd_cli import AzureDeveloperCliCredential
from .azure_powershell import AzurePowerShellCredential
from .chained import ChainedTokenCredential
from .environment import EnvironmentCredential
from .managed_identity import ManagedIdentityCredential
from .shared_cache import SharedTokenCacheCredential
from .vscode import VisualStudioCodeCredential
from .workload_identity import WorkloadIdentityCredential

if TYPE_CHECKING:
    from azure.core.credentials_async import AsyncTokenCredential

_LOGGER = logging.getLogger(__name__)


class DefaultAzureCredential(ChainedTokenCredential):
    """A default credential capable of handling most Azure SDK authentication scenarios.

    The identity it uses depends on the environment. When an access token is needed, it requests one using these
    identities in turn, stopping when one provides a token:

    1. A service principal configured by environment variables. See :class:`~azure.identity.aio.EnvironmentCredential`
       for more details.
    2. WorkloadIdentityCredential if environment variable configuration is set by the Azure workload
       identity webhook.
    3. An Azure managed identity. See :class:`~azure.identity.aio.ManagedIdentityCredential` for more details.
    4. The identity currently logged in to the Azure Developer CLI.
    5. On Windows only: a user who has signed in with a Microsoft application, such as Visual Studio. If multiple
       identities are in the cache, then the value of  the environment variable ``AZURE_USERNAME`` is used to select
       which identity to use. See :class:`~azure.identity.aio.SharedTokenCacheCredential` for more details.
    6. The identity currently logged in to the Azure CLI.
    7. The identity currently logged in to Azure PowerShell.

    This default behavior is configurable with keyword arguments.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example 'login.microsoftonline.com',
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds. Managed identities ignore this because they reside in a single cloud.
    :keyword bool exclude_azd_cli_credential: Whether to exclude the Azure Developer CLI
        from the credential. Defaults to **False**.
    :keyword bool exclude_cli_credential: Whether to exclude the Azure CLI from the credential. Defaults to **False**.
    :keyword bool exclude_environment_credential: Whether to exclude a service principal configured by environment
        variables from the credential. Defaults to **False**.
    :keyword bool exclude_powershell_credential: Whether to exclude Azure PowerShell. Defaults to **False**.
    :keyword bool exclude_visual_studio_code_credential: Whether to exclude stored credential from VS Code.
        Defaults to **True**.
    :keyword bool exclude_managed_identity_credential: Whether to exclude managed identity from the credential.
        Defaults to **False**.
    :keyword bool exclude_shared_token_cache_credential: Whether to exclude the shared token cache. Defaults to
        **False**.
    :keyword str managed_identity_client_id: The client ID of a user-assigned managed identity. Defaults to the value
        of the environment variable AZURE_CLIENT_ID, if any. If not specified, a system-assigned identity will be used.
    :keyword str workload_identity_client_id: The client ID of an identity assigned to the pod. Defaults to the value
        of the environment variable AZURE_CLIENT_ID, if any. If not specified, the pod's default identity will be used.
    :keyword str shared_cache_username: Preferred username for :class:`~azure.identity.aio.SharedTokenCacheCredential`.
        Defaults to the value of environment variable AZURE_USERNAME, if any.
    :keyword str shared_cache_tenant_id: Preferred tenant for :class:`~azure.identity.aio.SharedTokenCacheCredential`.
        Defaults to the value of environment variable AZURE_TENANT_ID, if any.
    :keyword str visual_studio_code_tenant_id: Tenant ID to use when authenticating with
        :class:`~azure.identity.aio.VisualStudioCodeCredential`. Defaults to the "Azure: Tenant" setting in VS Code's
        user settings or, when that setting has no value, the "organizations" tenant, which supports only Azure Active
        Directory work or school accounts.
    """

    def __init__(self, **kwargs: Any) -> None:
        if "tenant_id" in kwargs:
            raise TypeError("'tenant_id' is not supported in DefaultAzureCredential.")

        authority = kwargs.pop("authority", None)

        vscode_tenant_id = kwargs.pop(
            "visual_studio_code_tenant_id", os.environ.get(EnvironmentVariables.AZURE_TENANT_ID)
        )
        vscode_args = dict(kwargs)
        if authority:
            vscode_args["authority"] = authority
        if vscode_tenant_id:
            vscode_args["tenant_id"] = vscode_tenant_id

        authority = normalize_authority(authority) if authority else get_default_authority()

        shared_cache_username = kwargs.pop("shared_cache_username", os.environ.get(EnvironmentVariables.AZURE_USERNAME))
        shared_cache_tenant_id = kwargs.pop(
            "shared_cache_tenant_id", os.environ.get(EnvironmentVariables.AZURE_TENANT_ID)
        )

        managed_identity_client_id = kwargs.pop(
            "managed_identity_client_id", os.environ.get(EnvironmentVariables.AZURE_CLIENT_ID)
        )
        workload_identity_client_id = kwargs.pop(
            "workload_identity_client_id", managed_identity_client_id
        )

        vscode_tenant_id = kwargs.pop(
            "visual_studio_code_tenant_id", os.environ.get(EnvironmentVariables.AZURE_TENANT_ID)
        )

        exclude_visual_studio_code_credential = kwargs.pop("exclude_visual_studio_code_credential", True)
        exclude_azd_cli_credential = kwargs.pop("exclude_azd_cli_credential", False)
        exclude_cli_credential = kwargs.pop("exclude_cli_credential", False)
        exclude_environment_credential = kwargs.pop("exclude_environment_credential", False)
        exclude_managed_identity_credential = kwargs.pop("exclude_managed_identity_credential", False)
        exclude_shared_token_cache_credential = kwargs.pop("exclude_shared_token_cache_credential", False)
        exclude_powershell_credential = kwargs.pop("exclude_powershell_credential", False)

        credentials = []  # type: List[AsyncTokenCredential]
        if not exclude_environment_credential:
            credentials.append(EnvironmentCredential(authority=authority, **kwargs))
        if all(os.environ.get(var) for var in EnvironmentVariables.WORKLOAD_IDENTITY_VARS):
            client_id = workload_identity_client_id
            credentials.append(WorkloadIdentityCredential(
                client_id=cast(str, client_id),
                tenant_id=os.environ[EnvironmentVariables.AZURE_TENANT_ID],
                file=os.environ[EnvironmentVariables.AZURE_FEDERATED_TOKEN_FILE],
                **kwargs))
        if not exclude_managed_identity_credential:
            credentials.append(ManagedIdentityCredential(client_id=managed_identity_client_id, **kwargs))
        if not exclude_azd_cli_credential:
            credentials.append(AzureDeveloperCliCredential())
        if not exclude_shared_token_cache_credential and SharedTokenCacheCredential.supported():
            try:
                # username and/or tenant_id are only required when the cache contains tokens for multiple identities
                shared_cache = SharedTokenCacheCredential(
                    username=shared_cache_username, tenant_id=shared_cache_tenant_id, authority=authority, **kwargs
                )
                credentials.append(shared_cache)
            except Exception as ex:  # pylint:disable=broad-except
                _LOGGER.info("Shared token cache is unavailable: '%s'", ex)
        if not exclude_visual_studio_code_credential:
            credentials.append(VisualStudioCodeCredential(**vscode_args))
        if not exclude_cli_credential:
            credentials.append(AzureCliCredential())
        if not exclude_powershell_credential:
            credentials.append(AzurePowerShellCredential())

        super().__init__(*credentials)

    async def get_token(self, *scopes: str, **kwargs: Any) -> AccessToken:
        """Asynchronously request an access token for `scopes`.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str tenant_id: optional tenant to include in the token request.
        :rtype: :class:`azure.core.credentials.AccessToken`
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The exception has a
          `message` attribute listing each authentication attempt and its error message.
        """
        if self._successful_credential:
            return await self._successful_credential.get_token(*scopes, **kwargs)

        return await super().get_token(*scopes, **kwargs)
