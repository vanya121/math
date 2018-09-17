#!/usr/bin/python

from typing import List, TypeVar

FizzBuzzType = TypeVar('FizzBuzzType', int, str)


def get_fizz_buzz(n):
    """
    :param n: size of sequence
    :return: list of values. If value divided by 3 - "Fizz",
    if value divided by 5 - "Buzz", if value divided by 15 -
            "Fizz Buzz", else - value.
    """
    myList = list(range(1, n + 1))
    for i in range(3, n + 1, 3):
        myList[i - 1] = 'Fizz'
    for i in range(5, n + 1, 5):
        myList[i - 1] = 'Buzz'
    for i in range(15, n + 1, 15):
        myList[i - 1] = 'Fizz Buzz'
    return myList


if __name__ == "__main__":
    n = int(input())
    print(get_fizz_buzz(n))
