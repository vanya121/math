#!/usr/bin/python


def get_value(value, repeats):
    """
    :param value: value to repeat
    :param repeats: number of repeats
    :return: square of repeated value
    """
    if value == 0:
        return value
    value = str(value)
    value = value*repeats
    value = int(value)
    return value*value


if __name__ == '__main__':
    value = int(input())
    repeats = int(input())
    print(get_value(value, repeats))
