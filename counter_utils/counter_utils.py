#!/usr/bin/ python
import sys


if __name__ == '__main__':
    keys = input().split()
    key = dict()
    m = 0
    le = 0
    L = 0
    w = 0
    for line in sys.stdin:
        le += 1
        m += len(line)
        if L < len(line) - 1:
            L = len(line) - 1
        words = line.split()
        w += len(words)
    for elem in keys:
        if elem == '-m':
            key[elem] = m
        if elem == '-l':
            key[elem] = le
        if elem == '-L':
            key[elem] = L
        if elem == '-w':
            key[elem] = w
    if key.get('-l') is not None:
        print(le, end=' ')
    if key.get('-w') is not None:
        print(w, end=' ')
    if key.get('-m') is not None:
        print(m, end=' ')
    if key.get('-L') is not None:
        print(L)
