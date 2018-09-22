#!/usr/bin/python


def uniq(elements):
    while len(elements) > 0:
        element = elements[0]
        if elements.count(element) > 1:
            for i in range(elements.count(element)):
                elements.remove(element)
    return elements
