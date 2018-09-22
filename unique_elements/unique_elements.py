#!/usr/bin/python


def uniq(elements):
    ans = list()
    while len(elements) > 0:
        element = elements[0]
        if elements.count(element) == 1:
            ans.append(element)
        for i in range(elements.count(element)):
            elements.remove(element)
    return ans
