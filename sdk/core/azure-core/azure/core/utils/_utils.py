# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime
from typing import (
    Any,
    Dict,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    Optional,
    Tuple,
    Union,
)
from datetime import timezone

TZ_UTC = timezone.utc  # type: ignore


class _FixedOffset(datetime.tzinfo):
    """Fixed offset in minutes east from UTC.

    Copy/pasted from Python doc

    :param int offset: offset in minutes
    """

    def __init__(self, offset):
        self.__offset = datetime.timedelta(minutes=offset)

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return str(self.__offset.total_seconds() / 3600)

    def __repr__(self):
        return "<FixedOffset {}>".format(self.tzname(None))

    def dst(self, dt):
        return datetime.timedelta(0)


def _convert_to_isoformat(date_time):
    """Deserialize a date in RFC 3339 format to datetime object.
    Check https://tools.ietf.org/html/rfc3339#section-5.8 for examples.
    """
    if not date_time:
        return None
    if date_time[-1] == "Z":
        delta = 0
        timestamp = date_time[:-1]
    else:
        timestamp = date_time[:-6]
        sign, offset = date_time[-6], date_time[-5:]
        delta = int(sign + offset[:1]) * 60 + int(sign + offset[-2:])

    check_decimal = timestamp.split(".")
    if len(check_decimal) > 1:
        decimal_str = ""
        for digit in check_decimal[1]:
            if digit.isdigit():
                decimal_str += digit
            else:
                break
        if len(decimal_str) > 6:
            timestamp = timestamp.replace(decimal_str, decimal_str[0:6])

    if delta == 0:
        tzinfo = TZ_UTC
    else:
        tzinfo = timezone(datetime.timedelta(minutes=delta))

    try:
        deserialized = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        deserialized = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

    deserialized = deserialized.replace(tzinfo=tzinfo)
    return deserialized


def case_insensitive_dict(*args: Any, **kwargs: Any) -> MutableMapping:
    """Return a case-insensitive mutable mapping from an inputted mapping structure.

    :return: A case-insensitive mutable mapping object.
    :rtype: ~collections.abc.MutableMapping
    """
    return CaseInsensitiveDict(*args, **kwargs)


class CaseInsensitiveDict(MutableMapping[str, Any]):
    """
    NOTE: This implementation is heavily inspired from the case insensitive dictionary from the requests library.
    Thank you !!
    Case insensitive dictionary implementation.
    The keys are expected to be strings and will be stored in lower case.
    case_insensitive_dict = CaseInsensitiveDict()
    case_insensitive_dict['Key'] = 'some_value'
    case_insensitive_dict['key'] == 'some_value' #True
    """

    def __init__(
        self,
        data: Optional[Union[Mapping[str, Any], Iterable[Tuple[str, Any]]]] = None,
        **kwargs: Any
    ) -> None:
        self._store: Dict[str, Any] = {}
        if data is None:
            data = {}

        self.update(data, **kwargs)

    def copy(self) -> "CaseInsensitiveDict":
        return CaseInsensitiveDict(self._store.values())

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the `key` to `value`. The original key will be stored with the value
        """
        self._store[key.lower()] = (key, value)

    def __getitem__(self, key: str) -> Any:
        return self._store[key.lower()][1]

    def __delitem__(self, key: str) -> None:
        del self._store[key.lower()]

    def __iter__(self) -> Iterator[str]:
        return (key for key, _ in self._store.values())

    def __len__(self) -> int:
        return len(self._store)

    def lowerkey_items(self):
        return (
            (lower_case_key, pair[1]) for lower_case_key, pair in self._store.items()
        )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Mapping):
            other = CaseInsensitiveDict(other)
        else:
            return False

        return dict(self.lowerkey_items()) == dict(other.lowerkey_items())

    def __repr__(self) -> str:
        return str(dict(self.items()))
