#!/usr/bin/python
from typing import List
import itertools


def uniq(elements):
    ans = list()
    while len(elements) > 0:
        element = elements[0]
        ans.append(element)
        for i in range(elements.count(element)):
            elements.remove(element)
    return ans


def generate_permnutations(words):
    answer = list()
    ans = list(itertools.permutations(words))
    for i in range(len(ans)):
        answer.append(''.join(ans[i]))
    return answer


def generate_passwords(words):
    password = list()
    for i in range(1, 2 ** len(words)):
        subset = list()
        k = i
        cnt = 0
        while k > 0:
            if k % 2 == 1:
                subset.append(words[cnt])
            cnt += 1
            k = k // 2
        password += generate_permnutations(subset)
#    password = uniq(password)
#    password.sort()
    return password
