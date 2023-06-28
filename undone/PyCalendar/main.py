class GregorianCalendar(object):

    @staticmethod
    def is_leap(year: int):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(GregorianCalendar.is_leap(1600))
