#!/usr/bin/python


def quick_sort(data):
    left = list()
    stand = list()
    right = list()
    if len(data) <= 1:
        return data
    for i in data:
        if i < data[0]:
            left.append(i)
        if i == data[0]:
            stand.append(i)
        if i > data[0]:
            right.append(i)
    return quick_sort(left) + stand + quick_sort(right)


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    print(' '.join(map(str, quick_sort(data))))
