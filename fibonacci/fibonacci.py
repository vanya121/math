#!/usr/bin/python


def get_fibonacci_value(first, second, position_value):
    """
    :param position:  Position in fibonacci sequence
    :param first_value: First value of fibonacci sequence
    :param second_value: Second value of fibonacci sequence
    :return: value of fibonacci sequence on given position
    """
    cnt = 0
    value = first + second
    while cnt < position_value:
        first = second
        second = value
        value = first + second
        cnt += 1
    return value


if __name__ == "__main__":
    first, second, position_value = int(input()), int(input()), int(input())
    print(get_fibonacci_value(first, second, position_value))
