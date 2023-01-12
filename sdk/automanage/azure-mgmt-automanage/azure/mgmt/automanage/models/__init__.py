# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AssignmentReportProperties
from ._models_py3 import BestPractice
from ._models_py3 import BestPracticeList
from ._models_py3 import ConfigurationProfile
from ._models_py3 import ConfigurationProfileAssignment
from ._models_py3 import ConfigurationProfileAssignmentList
from ._models_py3 import ConfigurationProfileAssignmentProperties
from ._models_py3 import ConfigurationProfileList
from ._models_py3 import ConfigurationProfileProperties
from ._models_py3 import ConfigurationProfileUpdate
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import ProxyResource
from ._models_py3 import Report
from ._models_py3 import ReportList
from ._models_py3 import ReportResource
from ._models_py3 import Resource
from ._models_py3 import ServicePrincipal
from ._models_py3 import ServicePrincipalListResult
from ._models_py3 import ServicePrincipalProperties
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UpdateResource

from ._automanage_client_enums import ActionType
from ._automanage_client_enums import CreatedByType
from ._automanage_client_enums import Origin
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AssignmentReportProperties",
    "BestPractice",
    "BestPracticeList",
    "ConfigurationProfile",
    "ConfigurationProfileAssignment",
    "ConfigurationProfileAssignmentList",
    "ConfigurationProfileAssignmentProperties",
    "ConfigurationProfileList",
    "ConfigurationProfileProperties",
    "ConfigurationProfileUpdate",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "ProxyResource",
    "Report",
    "ReportList",
    "ReportResource",
    "Resource",
    "ServicePrincipal",
    "ServicePrincipalListResult",
    "ServicePrincipalProperties",
    "SystemData",
    "TrackedResource",
    "UpdateResource",
    "ActionType",
    "CreatedByType",
    "Origin",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
