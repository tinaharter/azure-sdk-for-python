# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import base64
from json import JSONEncoder
import types
from typing import TYPE_CHECKING

from .utils._utils import _FixedOffset

if TYPE_CHECKING:
    from typing import List, Dict, Optional
    from datetime import timedelta

try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

from collections import OrderedDict, namedtuple

__all__ = ["NULL", "AzureJSONEncoder"]



class _Null(object):
    """To create a Falsy object"""

    def __bool__(self):
        return False

    __nonzero__ = __bool__  # Python2 compatibility


NULL = _Null()
"""
A falsy sentinel object which is supposed to be used to specify attributes
with no data. This gets serialized to `null` on the wire.
"""


def _timedelta_as_isostr(value):
    # type: (timedelta) -> str
    """Converts a datetime.timedelta object into an ISO 8601 formatted string, e.g. 'P4DT12H30M05S'

    Function adapted from the Tin Can Python project: https://github.com/RusticiSoftware/TinCanPython
    """

    # Split seconds to larger units
    seconds = value.total_seconds()
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    days, hours, minutes = list(map(int, (days, hours, minutes)))
    seconds = round(seconds, 6)

    # Build date
    date = ""
    if days:
        date = "%sD" % days

    # Build time
    time = "T"

    # Hours
    bigger_exists = date or hours
    if bigger_exists:
        time += "{:02}H".format(hours)

    # Minutes
    bigger_exists = bigger_exists or minutes
    if bigger_exists:
        time += "{:02}M".format(minutes)

    # Seconds
    try:
        if seconds.is_integer():
            seconds_string = "{:02}".format(int(seconds))
        else:
            # 9 chars long w/ leading 0, 6 digits after decimal
            seconds_string = "%09.6f" % seconds
            # Remove trailing zeros
            seconds_string = seconds_string.rstrip("0")
    except AttributeError:  # int.is_integer() raises
        seconds_string = "{:02}".format(seconds)

    time += "{}S".format(seconds_string)

    return "P" + date + time


try:
    from datetime import timezone

    TZ_UTC = timezone.utc  # type: ignore
except ImportError:
    TZ_UTC = _FixedOffset(0)  # type: ignore


class AzureJSONEncoder(JSONEncoder):
    """A JSON encoder that's capable of serializing datetime objects and bytes."""

    def default(self, o):  # pylint: disable=too-many-return-statements
        try:
            return super(AzureJSONEncoder, self).default(o)
        except TypeError:
            if isinstance(o, (bytes, bytearray)):
                return base64.b64encode(o).decode()
            try:
                # First try datetime.datetime
                if hasattr(o, "year") and hasattr(o, "hour"):
                    # astimezone() fails for naive times in Python 2.7, so make make sure o is aware (tzinfo is set)
                    if not o.tzinfo:
                        iso_formatted = o.replace(tzinfo=TZ_UTC).isoformat()
                    else:
                        iso_formatted = o.astimezone(TZ_UTC).isoformat()
                    # Replace the trailing "+00:00" UTC offset with "Z" (RFC 3339: https://www.ietf.org/rfc/rfc3339.txt)
                    return iso_formatted.replace("+00:00", "Z")
                # Next try datetime.date or datetime.time
                return o.isoformat()
            except AttributeError:
                pass
            # Last, try datetime.timedelta
            try:
                return _timedelta_as_isostr(o)
            except AttributeError:
                # This will be raised when it hits value.total_seconds in the method above
                pass
            return super(AzureJSONEncoder, self).default(o)


def _deserialize(item):
    return item

_PropertyValue = namedtuple("PropertyValue", ["original", "deserialized"])


class Metaclass(type):

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        obj.__init__(*args, **{
            obj._get_property_name(kwarg) or kwarg: value
            for kwarg, value in kwargs.items()
        })
        return obj



class Model(MutableMapping):
    _attribute_map = NotImplementedError()  # type: Dict[str, Dict[str, str]]

    def __init__(self, **kwargs):
        self._dict = OrderedDict()
        self.update(self._dict, **kwargs)

    def __setitem__(self, key, item):
        # if the key is for an attr that we know of
        # we deserialize it. Then, we keep it as a tuple of
        # (passed value, deserialized value).
        # Otherwise, it's just a single value
        """
        _attribute_map = {
            "array": {"key": "array", "type": "str"},
        }
        """
        deserialized = _deserialize(item) if key in self._attribute_map else item
        self._dict[key] = _PropertyValue(item, deserialized)

    def __getitem__(self, key):
        # return non-deserialized
        return self._dict[key].original

    def __delitem__(self, key):
        self._dict[key] = None

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return (key for key in self._dict)

    def __len__(self):
        return len(self._dict)

    def __eq__(self, other):
        """Compare objects by comparing all attributes."""
        if isinstance(other, self.__class__):
            return self._dict == other._dict
        return False

    def __str__(self):
        return str({k: v.original for k, v in self._dict.items() if not k.startswith("_")})

    def has_key(self, k):
        return k in self._dict

    def keys(self):
        return [k for k in self._dict if not k.startswith("_")]

    def values(self):
        return [v.original for k, v in self._dict.items() if not k.startswith("_")]

    def items(self):
        return [(k, v.original) for k, v in self._dict.items() if not k.startswith("_")]

    def get(self, key, default=None):
        if key in self._dict:
            return self._dict[key]
        return default

    @classmethod
    def _get_dict_name(cls, property_name):
        # type: (str) -> Optional[str]
        return cls._attribute_map.get(property_name, {"key": None})["key"]

    @classmethod
    def _get_property_name(cls, dict_name):
        # type: (str) -> Optional[str]
        try:
            return next(
                k for k, v in cls._attribute_map.items()
                if v["key"] == dict_name
            )
        except StopIteration:
            return None

    def __getattr__(self, attr):
        if not self.__hasattr__(attr):
            raise AttributeError(
                "{} instance has no attribute '{}'".format(
                    type(self).__name__,
                    attr
                )
            )

        return self._dict[self._get_dict_name(attr)].deserialized

    def __setattr__(self, name, value):
        # the properties on the base class
        my_model_properties = [
            "_dict",
            "_property_to_dict_name",
        ]
        if name in my_model_properties:
            super(Model, self).__setattr__(name, value)
        else:
            self.__setitem__(self._get_dict_name(name), value)

    def __delattr__(self, name):
        return self.__delitem__(self._get_dict_name(name))

    def __hasattr__(self, attr):
        return self._get_dict_name(attr) in self._dict

    def copy(self):
        return Model(**self._dict)
