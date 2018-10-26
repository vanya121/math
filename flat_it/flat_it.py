from typing import Iterable
import collections


def flat_it(sequence):
    if isinstance(sequence, str):
        for it in sequence:
            yield it
    else:
        for it in sequence:
            if (isinstance(it, collections.Iterable)):
                yield from flat_it(it)
            else:
                yield it


if __name__ == "__main__":
    print(list(flat_it([[1, [[2, [5, [6, [2, 'test']]]], 3], range(-5, -3, 1)]])))
