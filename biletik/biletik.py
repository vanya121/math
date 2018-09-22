#!/usr/bin/python


def is_happy_ticket(current_ticket):
    current_ticket = str(current_ticket)
    number_1 = int(current_ticket[0])
    number_2 = int(current_ticket[1])
    number_3 = int(current_ticket[2])
    number_4 = int(current_ticket[3])
    number_5 = int(current_ticket[4])
    number_6 = int(current_ticket[5])
    if number_1 + number_2 + number_3 == number_4 + number_5 + number_6:
        return True
    return False


def get_nearest_happy_ticket(current_ticket):
    ticket = int(current_ticket)
    cnt = 0
    while True:
        if is_happy_ticket(ticket + cnt) is True:
            happy_ticket = str(ticket + cnt)
            return happy_ticket
        if is_happy_ticket(ticket - cnt) is True:
            happy_ticket = str(ticket - cnt)
            return happy_ticket
        cnt += 1


if __name__ == '__main__':
    current_ticket = input()
    print(get_nearest_happy_ticket(current_ticket))
