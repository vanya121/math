import pytest
from .biletik import get_nearest_happy_ticket


class Case(object):
    def __init__(self, current_ticket, expected):
        self.current_ticket = current_ticket
        self.expected = expected

    def __str__(self):
        return "test_{}".format(self.current_ticket)


TEST_CASES = [
    Case(current_ticket="228419", expected="228417")
]


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_nearest_happy_ticket(test_case):
    nearest_happy_ticket = get_nearest_happy_ticket(test_case.current_ticket)
    assert nearest_happy_ticket == test_case.expected
