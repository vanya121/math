#!usr/bin/python
import random


def shuffle_text(text, letters_to_shuffle):
    new_text = list(text)
    a = []
    for elem in new_text:
        if elem.isalpha():
            a.append(1)
        else:
            a.append(0)
    k = 0
    b = []
    for elem in a:
        if elem == 0:
            b.append(0)
            k = 0
        if elem == 1:
            if k == 0:
                b.append(0)
                k = 1
            else:
                b.append(1)
    a = b[::-1]
    b = []
    k = 0
    for elem in a:
        if elem == 0:
            b.append(0)
            k = 0
        if elem == 1:
            if k == 0:
                b.append(2)
                k = 1
            else:
                b.append(1)
    a = b[::-1]
    answer = []
    sh = []
    for i in range(len(new_text)):
        if a[i] == 0:
            answer.append(new_text[i])
        if a[i] == 1:
            sh.append(new_text[i])
        if a[i] == 2:
            random.shuffle(sh)
            answer += sh
            sh = []
            answer.append(new_text[i])
    answer = ''.join(answer)
    return answer


if __name__ == "__main__":
    text = 'Ваня просил без обзыва'
    print(shuffle_text(text, 1))
