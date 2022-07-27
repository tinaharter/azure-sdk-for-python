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
from ._configuration import AzureReservationAPIConfiguration
from .operations import AzureReservationAPIOperationsMixin, CalculateExchangeOperations, ExchangeOperations, OperationOperations, QuotaOperations, QuotaRequestStatusOperations, ReservationOperations, ReservationOrderOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class AzureReservationAPI(AzureReservationAPIOperationsMixin):    # pylint: disable=too-many-instance-attributes
    """This API describe Azure Reservation.

    :ivar reservation: ReservationOperations operations
    :vartype reservation: azure.mgmt.reservations.operations.ReservationOperations
    :ivar reservation_order: ReservationOrderOperations operations
    :vartype reservation_order: azure.mgmt.reservations.operations.ReservationOrderOperations
    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.reservations.operations.OperationOperations
    :ivar calculate_exchange: CalculateExchangeOperations operations
    :vartype calculate_exchange: azure.mgmt.reservations.operations.CalculateExchangeOperations
    :ivar exchange: ExchangeOperations operations
    :vartype exchange: azure.mgmt.reservations.operations.ExchangeOperations
    :ivar quota: QuotaOperations operations
    :vartype quota: azure.mgmt.reservations.operations.QuotaOperations
    :ivar quota_request_status: QuotaRequestStatusOperations operations
    :vartype quota_request_status: azure.mgmt.reservations.operations.QuotaRequestStatusOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AzureReservationAPIConfiguration(credential=credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.reservation = ReservationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.reservation_order = ReservationOrderOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.calculate_exchange = CalculateExchangeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.exchange = ExchangeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.quota = QuotaOperations(self._client, self._config, self._serialize, self._deserialize)
        self.quota_request_status = QuotaRequestStatusOperations(self._client, self._config, self._serialize, self._deserialize)


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
        # type: () -> AzureReservationAPI
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
