from typing import List
from typing import Iterator
from typing import TypeVar
from typing import Dict

T = TypeVar('T')


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def uniq(sequence):
    a = {}
    for item in sequence:
        if a.get(item) is None:
            a[item] = 1
            yield item


def dict_merge(*dicts: Dict) -> Dict:
    q = {}
    for item in dicts:
        q.update(item)
    return q


def product(lhs: List[int], rhs: List[int]):
    return sum(list(a * b for (a, b) in zip(lhs, rhs)))


if __name__ == "__main__":
    a = [[1, 2], [3, 4], [5, 6]]
    print(transpose(a))
    b = [1, 2, 3, 3, 1, 7]
    print(list(uniq(b)))
    c = [{1: 2}, {2: 2}, {1: 1}]
    print(dict_merge(c))
    lft = [1, 2, 3]
    rgt = [4, 5, 6]
    print(product(lft, rgt))
