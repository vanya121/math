#!/usr/bin/python
import math


def is_perfect(num):
    p = 1
    if num % 2 == 1:
        return "False"
    while (2 ** (p - 1)) * (2 ** p - 1) < num:
        p += 1
    if (2 ** (p - 1)) * (2 ** p - 1) == num:
        b = int(math.sqrt(2 ** p - 1))
        for i in range(2, b):
            if (2 ** p - 1) % i == 0:
                return "False"
        return "True"
    return "False"
