#!/usr/bin/python


def uniq(elements):
    ans = list()
    while len(elements) > 0:
        element = elements[0]
        ans.append(element)
        for i in range(elements.count(element)):
            elements.remove(element)
    return ans


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
        return 'weak5'
    password = password.lower()
    if password.find('anna') != -1:
        return 'weak'
    password_list = list(password)
    if len(uniq(password_list)) < 4:
        return 'weak'
    return 'strong'


if __name__ == '__main__':
    s = input()
    print(password_strength(s))
