from unique_elements import uniq


def test_example1():
    assert uniq([1, 2, 2, 3, 3, 3]) == [1]


def test_example2():
    assert uniq([1, 2, 3, 4, 5, 5]) == [1, 2, 3, 4]
