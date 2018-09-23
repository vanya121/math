import pytest
from collections import OrderedDict

from .seconds_diff import get_seconds_diff


class Case(object):
    def __init__(self, params, expected):
        self.params = params
        self.expected = expected


TEST_CASES = OrderedDict([
    ("simple_case", Case(params=(1, 1, 1, 2, 2, 2), expected=3661))
])


@pytest.mark.parametrize("test_case", TEST_CASES.values(),
                         ids=list(TEST_CASES.keys()))
def test_get_seconds_diff(test_case):
    assert get_seconds_diff(*test_case.params) == test_case.expected
