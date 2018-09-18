#!/usr/bin/python


def get_fibonacci_value(position_value, first, second):
    """
    :param position:  Position in fibonacci sequence
    :param first_value: First value of fibonacci sequence
    :param second_value: Second value of fibonacci sequence
    :return: value of fibonacci sequence on given position
    """
    if position_value == 0:
        return first
    if position_value == 1:
        return second
    cnt = 2
    value = first + second
    while cnt < position_value:
        first = second
        second = value
        value = first + second
        cnt += 1
    return value


if __name__ == "__main__":
    position_value, first, second = int(input()), int(input()), int(input())
    print(get_fibonacci_value(position_value, first, second))
