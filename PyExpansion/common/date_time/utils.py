from PyExpansion.common.constants import datetime as constants_datetime


def convert_day_to_readable_date(number_of_days):
    left = number_of_days - constants_datetime.s_day_in_a_year
    days = constants_datetime.s_day_in_a_year
    left *= constants_datetime.s_hour_in_a_day
    hours = int(left - (left % 1))
    left = left % 1
    left *= constants_datetime.s_minute_in_a_hour
    minutes = int(left - (left % 1))
    left = left % 1
    left *= constants_datetime.s_second_in_a_minute
    seconds = int(left - (left % 1))
    return days, hours, minutes, seconds


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

