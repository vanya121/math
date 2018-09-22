#!/usr/bin/python


def get_nearest_happy_ticket(current_ticket):
    number_1 = int(current_ticket[0])
    number_2 = int(current_ticket[1])
    number_3 = int(current_ticket[2])
    number_4 = int(current_ticket[3])
    number_5 = int(current_ticket[4])
    number_6 = int(current_ticket[5])
    first_sum = number_1 + number_2 + number_3
    second_sum = number_4 + number_5 + number_6
    if first_sum > second_sum:
        delta = first_sum - second_sum
        if delta <= 9 - number_6:
            number_6 = delta + number_6
        else:
            delta = delta - 9 + number_6
            number_6 = 9
            if delta < 9 - number_5:
                number_5 = delta + number_5
            else:
                delta = delta - 9 + number_5
                number_5 = 9
                number_4 = number_4 + delta
    if first_sum < second_sum:
        delta = second_sum - first_sum
        if delta <= number_6:
            number_6 = number_6 - delta
        else:
            delta = delta - number_6
            number_6 = 0
            if delta < number_5:
                number_5 = number_5 - delta
            else:
                delta = delta - number_5
                number_5 = 0
                number_4 = number_4 - delta
    happy_ticket = str()
    happy_ticket = happy_ticket + str(number_1)
    happy_ticket = happy_ticket + str(number_2)
    happy_ticket = happy_ticket + str(number_3)
    happy_ticket = happy_ticket + str(number_4)
    happy_ticket = happy_ticket + str(number_5)
    happy_ticket = happy_ticket + str(number_6)
    return happy_ticket
