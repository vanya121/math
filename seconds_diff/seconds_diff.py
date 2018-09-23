#!/isr/bin/python


def get_seconds_diff(hours_1, minutes_1, seconds_1,
                     hours_2, minutes_2, seconds_2):
    total_seconds_1 = seconds_1 + (minutes_1 * 60) + (hours_1 * 3600)
    total_seconds_2 = seconds_2 + (minutes_2 * 60) + (hours_2 * 3600)
    return total_seconds_2 - total_seconds_1
