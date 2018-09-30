#!/usr/bin/python
import itertools


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
    password.sort()
    return password


if __name__ == '__main__':
    words = input().strip().split()
    for pswd in generate_passwords(words):
        print(pswd)
