#!/usr/bin/python


def quick_sort(data):
    left = list()
    stand = list()
    right = list()
    if len(data) <= 1:
        return data
    reference_element = data[len(data)//2]
    for i in data:
        if i < reference_element:
            left.append(i)
        if i == reference_element:
            stand.append(i)
        if i > reference_element:
            right.append(i)
    return quick_sort(left) + stand + quick_sort(right)


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    print(' '.join(map(str, quick_sort(data))))
