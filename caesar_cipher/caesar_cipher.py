#!/usr/bin/python


def caesar_encrypt(st, n):
    encrypt = str()
    for elem in st:
        if ord(elem) <= ord('z') and ord(elem) >= ord('a'):
            sym = chr((ord(elem) - ord('a') + n) % 26 + ord('a'))
        elif ord(elem) <= ord('Z') and ord(elem) >= ord('A'):
            sym = chr((ord(elem) - ord('A') + n) % 26 + ord('A'))
        elif elem == ' ':
            sym = ' '
        else:
            sym = chr(ord(elem) + n)
        encrypt += sym
    return encrypt


if __name__ == "__main__":
    stroka = input()
    n = int(input())
    print(caesar_encrypt(stroka, n))
