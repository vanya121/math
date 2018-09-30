#!/usr/bin/python


def password_strength(password):
    if len(password) < 8:
        return 'weak'
    if password.islower() == 1:
        return 'weak'
    if password.isupper() == 1:
        return 'weak'
    if any(map(str.isdigit, password)) == 0:
        return 'weak'
    if any(map(str.isalpha, password)) == 0:
        return 'weak'
    password = password.lower()
    if password.find('anna') != -1:
        return 'weak'
    summ = 0
    for elem in password:
        summ += password.count(elem)
    if summ > 21*len(password)//8:
        return 'weak'
    return 'strong'


if __name__ == '__main__':
    s = input()
    print(password_strength(s))
