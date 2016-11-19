#! /usr/bin/env python
# -*- coding: utf-8 -*-

# import pytest
from uuid import UUID
from functools import reduce

import simulacrum
from simulacrum.dataset import DataSet


def _default_test(listToCheck, typeToWait, length):
    return len(listToCheck) == length\
        and reduce(lambda p, n: p and type(n) == typeToWait, listToCheck, True)


def test_uuid_data():
    uuids_list = DataSet.uuid_data(None, 30)
    assert _default_test(uuids_list, UUID, 30)\
        and len(set(uuids_list)) == len(uuids_list)


def test_faker_data_ipv6():
    ipv6_list = DataSet.faker_data({
        "provider": "ipv6",
        "network": False
    }, 23)
    random_element_list = DataSet.faker_data({
        "provider": "random_element",
        "elements": ('a', 'b', 'c', 'd'),
    }, 13)
    assert _default_test(ipv6_list, str, 23)\
        and _default_test(random_element_list, str, 13)\
        and reduce(lambda p, n: p and n in ['a', 'b', 'c', 'd'], random_element_list, True)
