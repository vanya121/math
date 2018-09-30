#!/usr/bin.python


def is_Palindrome(stroka):
    first = stroka[0:len(stroka) // 2]
    second = stroka[len(stroka) - len(stroka) // 2:]
    second = second[::-1]
    if first == second:
        return True
    return False


def add(stroka, cnt):
    addd = stroka[0:cnt]
    addd = addd[::-1]
    return stroka + addd


def addition_upto_palindrome(line):
    cnt = 1
    reverse_line = line[::-1]
    if is_Palindrome(line) == 1:
        return 0
    for cnt in range(1, len(line)):
        if is_Palindrome(add(line, cnt)) == 1:
            return cnt
        if is_Palindrome(add(reverse_line, cnt)) == 1:
            return cnt


if __name__ == "__main__":
    line = input()
    print(addition_upto_palindrome(line))
