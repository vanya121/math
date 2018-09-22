#!/usr/bin/python


def reverse_complement(dna):
    dna = dna[::-1]
    ans = str()
    for i in dna:
        if i == 'T':
            ans += 'A'
        if i == 'A':
            ans += 'T'
        if i == 'G':
            ans += 'C'
        if i == 'C':
            ans += 'G'
    return ans


if __name__ == '__main__':
    dnka = input()
    print(reverse_complement(dnka))
